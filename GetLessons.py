from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from db.mockInitialDB import courses, lessons, users

form = reqparse.RequestParser()
form.add_argument("course_id",type=int,required=True,help="No course selected")
form.add_argument("session-user-id",type=int,required=True,help="Session Closed")

def abort_if_not_allowed(user_id):
    if user_id not in users:
        abort(404, message="Invalid: User not found")

def verifyApprovedLesson(lesson_id,user):
    if user["approved_lessons"]:
        return lesson_id in user["approved_lessons"]
    return False

def canDoThisLesson(lesson_id,user):
    lesson = lessons[lesson_id]
    if lesson["previous_lessons"]:
        if user["approved_lessons"] :
            for required_lesson in lesson["previous_lessons"]:
                if required_lesson not in user["approved_lessons"]:
                    return False
            return True
        return False
    return True
    
class GetLessons(Resource):
    def post(self):
        #Get all available lesons for the given course
        args = form.parse_args()
        abort_if_not_allowed(args["session-user-id"])
        course = courses[args["course_id"]]
        user = users[args["session-user-id"]]
        availableLessons = []
        for lesson_id in course["lessons"]:
            if(lesson_id not in lessons):
                abort(404, message = "Lesson Not Found")
            entry = {int(lesson_id) : lessons[lesson_id], "aproved" : verifyApprovedLesson(lesson_id,user), "canAccess" : canDoThisLesson(lesson_id,user)}
            availableLessons.append(entry)
        return {"lessons":availableLessons}, 200