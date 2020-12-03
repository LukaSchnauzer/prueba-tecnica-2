from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from db.mockInitialDB import courses, users
from Lessons import getLessonByID

courses_put_args = reqparse.RequestParser()
courses_put_args.add_argument("name",type=str,required=True,help="Course must have a name")
courses_put_args.add_argument("previous_courses",type=int, action='append')
courses_put_args.add_argument("lessons",type=int, action='append',required=True,help="Course must have lessons")
courses_put_args.add_argument("session-user-id",type=int,required=True,help="Session Closed")

courses_update_args = reqparse.RequestParser()
courses_update_args.add_argument("name",type=str)
courses_update_args.add_argument("previous_courses",type=int, action='append')
courses_update_args.add_argument("lessons",type=int, action='append')
courses_update_args.add_argument("session-user-id",type=int,required=True,help="Session Closed")

courses_delete_args = reqparse.RequestParser()
courses_delete_args.add_argument("session-user-id",type=int,required=True,help="Session Closed")

def abort_if_course_id_not_found(course_id):
    if course_id not in courses:
        abort(404, message="Course ID "+str(course_id)+" Not Found")

def abort_if_course_id_exists(course_id):
    if course_id in courses:
        abort(404, message="Course ID "+str(course_id)+" Already Taken")

def abort_if_not_allowed(user_id):
    if user_id in users:
        rol = users[user_id]["role"]
        if rol != "P":
            abort(401, message="Only professors can modify data")
    else:
        abort(404, message="Invalid: User not found")

def format(course_data):
    return {
            "name" : course_data["name"],
            "previous_courses" : course_data["previous_courses"],
            "lessons" : [lesson[0] for lesson in list(map(getLessonByID,course_data["lessons"]))]
           }

def getCourseByID(course_id):
    abort_if_course_id_not_found(course_id)
    return format(courses[course_id]), 200

def addCourse(course_id, args):
    abort_if_not_allowed(args["session-user-id"])
    abort_if_course_id_exists(course_id)
    courses[course_id] = args
    return courses[course_id], 201

def deleteCourseByID(course_id,args):
    abort_if_not_allowed(args["session-user-id"])
    abort_if_course_id_not_found(course_id)
    del courses[course_id]
    return '', 204

def updateCourseById(course_id, args):
    abort_if_not_allowed(args["session-user-id"])
    abort_if_course_id_not_found(course_id)
    if args["name"]:
        courses[course_id]["name"] = args["name"]
    if args["previous_courses"]:
        courses[course_id]["previous_courses"] = args["previous_courses"]
    if args["lessons"]:
        courses[course_id]["lessons"] = args["lessons"] 
    return courses[course_id], 200

class Course(Resource):
    def get(self, course_id):
        return getCourseByID(course_id)

    def put(self, course_id):
        args = courses_put_args.parse_args()
        return addCourse(course_id,args)

    def delete(self, course_id):
        args = courses_delete_args.parse_args()
        return deleteCourseByID(course_id,args)
    
    def patch(self, course_id):
        args = courses_update_args.parse_args()
        return updateCourseById(course_id,args)

        
