from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from db.mockInitialDB import lessons, questions, users

form = reqparse.RequestParser()
form.add_argument("lesson_id",type=int, required = True, help = "No Lesson Selected")
form.add_argument("answers",type=dict,action="append",required=True,help="Invalid Answer Object")
form.add_argument("session-user-id",type=int,required=True,help="Session Closed")

def abort_if_not_allowed(user_id):
    if user_id not in users:
        abort(404, message="Invalid: User not found")

def abort_if_answers_invalid(args):
    try:
        for answer in args["answers"]:
            if not answer["question_id"] or not isinstance(answer["question_id"],int) :
                abort(400, message="Invalid Answer (NO QUESTION ID)")
            if not answer["given_answer"] or not isinstance(answer["given_answer"],list):
                abort(400, message="Invalid Answer (NO ANSWER GIVEN)")
            for a in answer["given_answer"]:
                if not isinstance(a, str):
                    abort(400, message="Invalid Answer (SELECTED ANDSWERS MUST BE STRING)")
    except KeyError:
        abort(400, message="Invalid Answer")
    

def abort_if_lesson_not_found(args):
    if args["lesson_id"] not in lessons:
        abort(404, message="Lesson ID "+str(args["lesson_id"])+" Not Found")

def abort_if_answers_dont_corespond_to_lesson(questions_of_lesson,answers):
    for answer in answers:
        if answer["question_id"] not in questions_of_lesson:
            #One of the given answers doesn't correspond to a question of this lesson
            abort(400, message = "The Question with ID "+str(answer["question_id"])+" is not a part of this lesson")

def validateGivenAnswers(correct_answers,given_answer,allCorrectRequired):
    if(allCorrectRequired):
        for ca in correct_answers:
            #Each correct answer must be on the given answers
            if(ca not in given_answer):
                #One of the correct answers is not given, the answer is wrong
                return False
        return True
    else:
        value = False
        for ga in given_answer:
            #If a single given answer is on the correct_aswers list, then it is correct
            #However if the answer also includes a wrong answer, then the answer is wrong
            if(ga in correct_answers):
                #A Correct answer was given, so for now we set True, while we validate the rest of the answers
                value = True
            else:
                #A wrong answer was given
                return False
        return value

def addAprovedLesson(lesson_id, user_id):
    user = users[user_id]
    if(user["approved_lessons"] is None):
        user["approved_lessons"] = []
    if(lesson_id not in user["approved_lessons"]):
        user["approved_lessons"].append(lesson_id)

def validateAnswer(args):
    lesson =  lessons[args["lesson_id"]]
    minimunScore = lesson["minimum_score"]
    curent_score = 0
    questions_of_lesson = lesson["questions"]
    answers = args["answers"]
    abort_if_answers_dont_corespond_to_lesson(questions_of_lesson,answers)
    for answer in answers:
        question_id = answer["question_id"]
        if(question_id not in questions):
            abort(404, message="Question ID "+str(question_id)+" Not Found")
        question = questions[question_id]
        correct_answers = question["correct_answers"]
        allCorrectRequired = question["allCorrectRequired"]
        if(validateGivenAnswers(correct_answers,answer["given_answer"],allCorrectRequired)):
            curent_score += question["score"]
    if curent_score >= minimunScore:
        addAprovedLesson(args["lesson_id"],args["session-user-id"])
        return {"result" : "Lesson Approved!!","score" : curent_score}, 200
    return {"result" : "Lesson failed","score" : curent_score}, 200

class AnswerLesson(Resource):
    def post(self):
        args = form.parse_args()
        abort_if_not_allowed(args["session-user-id"])
        abort_if_answers_invalid(args)
        abort_if_lesson_not_found(args)
        return validateAnswer(args)
