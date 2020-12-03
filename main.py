from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from db.mockInitialDB import courses, lessons, questions, users
from Courses import Course
from Lessons import Lesson
from Questions import Question
from GetCourses import GetCourses
from GetLessons import GetLessons
from AnswerLesson import AnswerLesson

app = Flask(__name__)
api = Api(app)

api.add_resource(Course,"/course/<int:course_id>")
api.add_resource(Lesson,"/lesson/<int:lesson_id>")
api.add_resource(Question,"/question/<int:question_id>")
api.add_resource(GetCourses,"/courses/all")
api.add_resource(GetLessons,"/lessons/all")
api.add_resource(AnswerLesson,"/lessons/answer")

if __name__ == "__main__":
    app.run(debug=True)