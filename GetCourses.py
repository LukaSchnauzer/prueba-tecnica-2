from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from db.mockInitialDB import courses, users

form = reqparse.RequestParser()
form.add_argument("session-user-id",type=int,required=True,help="Session Closed")

def abort_if_not_allowed(user_id):
    if user_id not in users:
        abort(404, message="Invalid: User not found")

def verifyApprovedLessons(course,user):
    if user["approved_lessons"]:
        for lesson in course["lessons"]:
            if lesson not in user["approved_lessons"]:
                return False
        return True
    return False

def canDoThisCourse(course,user):
    if course["previous_courses"]:
        if user["approved_lessons"] :
            for required_course_id in course["previous_courses"]:
                if not verifyApprovedLessons(courses[required_course_id],user):
                    return False
            return True
        return False
    return True

class GetCourses(Resource):
    def post(self):
        #Get all available courses
        args = form.parse_args()
        abort_if_not_allowed(args["session-user-id"])
        user = users[args["session-user-id"]]
        availableCourses = []
        for course_id in courses:
            entry = {int(course_id) : courses[course_id], "aproved" : verifyApprovedLessons(courses[course_id],user), "canAccess" : canDoThisCourse(courses[course_id],user)}
            availableCourses.append(entry)
        return {"courses":availableCourses}, 200