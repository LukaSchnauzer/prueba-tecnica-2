from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from db.mockInitialDB import questions, users

questions_put_args = reqparse.RequestParser()
questions_put_args.add_argument("question",type=str,required=True,help="Question must have a question")
questions_put_args.add_argument("score",type=int,required=True,help="Question must have a score")
questions_put_args.add_argument("allCorrectRequired",type=bool,required=True,help="allCorrectRequired is required for Question")
questions_put_args.add_argument("aswers",type=str, action='append',required=True,help="Question must have answers")
questions_put_args.add_argument("correct_answers",type=str, action='append',required=True,help="Question must have correct answers")
questions_put_args.add_argument("session-user-id",type=int,required=True,help="Session Closed")

questions_update_args = reqparse.RequestParser()
questions_update_args.add_argument("question",type=str)
questions_update_args.add_argument("score",type=int)
questions_update_args.add_argument("allCorrectRequired",type=bool)
questions_update_args.add_argument("aswers",type=str, action='append')
questions_update_args.add_argument("correct_answers",type=str, action='append')
questions_update_args.add_argument("session-user-id",type=int,required=True,help="Session Closed")

questions_delete_args = reqparse.RequestParser()
questions_delete_args.add_argument("session-user-id",type=int,required=True,help="Session Closed")

def abort_if_question_id_not_found(question_id):
    if question_id not in questions:
        abort(404, message="Question ID "+str(question_id)+" Not Found")

def abort_if_question_id_exists(question_id):
    if question_id in questions:
        abort(404, message="Question ID "+str(question_id)+" Already Taken")

def abort_if_not_allowed(user_id):
    if user_id in users:
        rol = users[user_id]["role"]
        if rol != "P":
            abort(401, message="Only professors can modify data")
    else:
        abort(404, message="Invalid: User not found")

def getQuestionByID(question_id):
    abort_if_question_id_not_found(question_id)
    return questions[question_id], 200

def addQuestion(question_id, args):
    abort_if_not_allowed(args["session-user-id"])
    abort_if_question_id_exists(question_id)
    questions[question_id] = args
    return questions[question_id], 201

def deleteQuestionByID(question_id,args):
    abort_if_not_allowed(args["session-user-id"])
    abort_if_question_id_not_found(question_id)
    del questions[question_id]
    return '', 204

def updateQuestionById(question_id, args):
    abort_if_not_allowed(args["session-user-id"])
    abort_if_question_id_not_found(question_id)
    if args["question"]:
        questions[question_id]["question"] = args["question"]
    if args["score"]:
        questions[question_id]["score"] = args["score"]
    if args["allCorrectRequired"]:
        questions[question_id]["allCorrectRequired"] = args["allCorrectRequired"]
    if args["aswers"]:
        questions[question_id]["aswers"] = args["aswers"]
    if args["correct_answers"]:
        questions[question_id]["correct_answers"] = args["correct_answers"]
    return questions[question_id], 200

class Question(Resource):
    def get(self, question_id):
        return getQuestionByID(question_id)

    def put(self, question_id):
        args = questions_put_args.parse_args()
        return addQuestion(question_id,args)

    def delete(self, question_id):
        args = questions_delete_args.parse_args()
        return deleteQuestionByID(question_id,args)
    
    def patch(self, question_id):
        args = questions_update_args.parse_args()
        return updateQuestionById(question_id,args)

        
