from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from db.mockInitialDB import lessons, users
from Questions import getQuestionByID

lessons_put_args = reqparse.RequestParser()
lessons_put_args.add_argument("name",type=str,required=True,help="Lesson must have a name")
lessons_put_args.add_argument("previous_lessons",type=int, action='append')
lessons_put_args.add_argument("questions",type=int, action='append',required=True,help="Lesson must have questions")
lessons_put_args.add_argument("minimum_score",type=int,required=True,help="Lesson must have a minimun score")
lessons_put_args.add_argument("session-user-id",type=int,required=True,help="Session Closed")

lessons_update_args = reqparse.RequestParser()
lessons_update_args.add_argument("name",type=str)
lessons_update_args.add_argument("previous_lessons",type=int, action='append')
lessons_update_args.add_argument("questions",type=int, action='append')
lessons_update_args.add_argument("minimum_score",type=int)
lessons_update_args.add_argument("session-user-id",type=int,required=True,help="Session Closed")

lessons_delete_args = reqparse.RequestParser()
lessons_delete_args.add_argument("session-user-id",type=int,required=True,help="Session Closed")

def abort_if_lesson_id_not_found(lesson_id):
    if lesson_id not in lessons:
        abort(404, message="Lesson ID "+str(lesson_id)+" Not Found")

def abort_if_lesson_id_exists(lesson_id):
    if lesson_id in lessons:
        abort(404, message="Lesson ID "+str(lesson_id)+" Already Taken")

def abort_if_not_allowed(user_id):
    if user_id in users:
        rol = users[user_id]["role"]
        if rol != "P":
            abort(401, message="Only professors can modify data")
    else:
        abort(404, message="Invalid: User not found")

def format(lesson_data):
    return {
            "name" : lesson_data["name"],
            "previous_lessons" : lesson_data["previous_lessons"],
            "questions" : [qustion[0] for qustion in list(map(getQuestionByID,lesson_data["questions"]))],
            "minimum_score" : lesson_data["minimum_score"]
           }

def getLessonByID(lesson_id):
    abort_if_lesson_id_not_found(lesson_id)
    return format(lessons[lesson_id]), 200

def addLesson(lesson_id, args):
    abort_if_not_allowed(args["session-user-id"])
    abort_if_lesson_id_exists(lesson_id)
    lessons[lesson_id] = args
    return lessons[lesson_id], 201

def deleteLessonByID(lesson_id,args):
    abort_if_not_allowed(args["session-user-id"])
    abort_if_lesson_id_not_found(lesson_id)
    del lessons[lesson_id]
    return '', 204

def updateLessonById(lesson_id, args):
    abort_if_not_allowed(args["session-user-id"])
    abort_if_lesson_id_not_found(lesson_id)
    if args["name"]:
        lessons[lesson_id]["name"] = args["name"]
    if args["previous_lessons"]:
        lessons[lesson_id]["previous_lessons"] = args["previous_lessons"]
    if args["questions"]:
        lessons[lesson_id]["questions"] = args["questions"]
    if args["minimum_score"]:
        lessons[lesson_id]["minimum_score"] = args["minimum_score"]
    return lessons[lesson_id], 200

class Lesson(Resource):
    def get(self, lesson_id):
        return getLessonByID(lesson_id)

    def put(self, lesson_id):
        args = lessons_put_args.parse_args()
        return addLesson(lesson_id,args)

    def delete(self, lesson_id):
        args = lessons_delete_args.parse_args()
        return deleteLessonByID(lesson_id,args)
    
    def patch(self, lesson_id):
        args = lessons_update_args.parse_args()
        return updateLessonById(lesson_id,args)

        
