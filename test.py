import requests
import json

BASE = "http://127.0.0.1:5000/"

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ START SIMPLE API REST TEST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~ Get All Courses ~~~~~~~~~~~~~~")
# Get all available courses and their status
response = requests.post(BASE + "/courses/all", {"session-user-id":2})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

print("~~~~~~~~~~~~~~ Get All Lessons from Course 1 ~~~~~~~~~~~~~~")
# Get all available courses and their status
response = requests.post(BASE + "/lessons/all", {"course_id":1,"session-user-id":2})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

answers = [{"question_id":1,"given_answer":["True"]},{"question_id":2,"given_answer":["Option b"]}]
print("~~~~~~~~~~~~~~ Sending Answers for Questions in Lesson 1 ~~~~~~~~~~~~~~")
response = requests.post(BASE + "/lessons/answer", json = {"lesson_id":1, "session-user-id":2 , "answers": answers} )
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

print("Verify if Lesson 1 is now approved...")
print("~~~~~~~~~~~~~~ Get All Lessons from Course 1 ~~~~~~~~~~~~~~")
response = requests.post(BASE + "/lessons/all", {"course_id":1,"session-user-id":2})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
print("If this is the first execution of this script: Lesson 1 should be approved and Lesson 2 should not")
input()

answers = [{"question_id":3,"given_answer":["Option b"]},{"question_id":4,"given_answer":["Option b","Option c"]}]
print("~~~~~~~~~~~~~~ Sending Answers for Questions in Lesson 2 ~~~~~~~~~~~~~~")
response = requests.post(BASE + "/lessons/answer", json = {"lesson_id":2, "session-user-id":2 , "answers": answers} )
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

print("Verify if Lesson 2 is now approved...")
print("~~~~~~~~~~~~~~ Get All Lessons from Course 1 ~~~~~~~~~~~~~~")
response = requests.post(BASE + "/lessons/all", {"course_id":1,"session-user-id":2})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
print("Lesson 1 and Lesson 2 should both be approved. Which means Course 1 should now be approved too")
input()

print("Verifying if Course 1 is approved...")
print("~~~~~~~~~~~~~~ Get All Courses ~~~~~~~~~~~~~~")
# Get all available courses and their status
response = requests.post(BASE + "/courses/all", {"session-user-id":2})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

print("~~~~~~~~~~~~~~ Start Course CRUD TEST ~~~~~~~~~~~~~~")
# Get an existing course
print("~~~~~~~~~~~~~~ Trying to get Course 3 (Full Output) ~~~~~~~~~~~~~~")
response = requests.get(BASE + "course/3")
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Try to get a non existing course
print("~~~~~~~~~~~~~~ Trying to get Course 5 (Doesn't Exists) ~~~~~~~~~~~~~~")
response = requests.get(BASE + "course/5")
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Put a course
print("~~~~~~~~~~~~~~ Trying to put Course 5 ~~~~~~~~~~~~~~")
response = requests.put(BASE + "course/5", {"name": "Course 5", "previous_courses":[1], "lessons" : [1,2,3], "session-user-id":1})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Updating a course
print("~~~~~~~~~~~~~~ Trying to update Course 5 ~~~~~~~~~~~~~~")
response = requests.patch(BASE + "course/5", {"name": "New name for Course 5", "session-user-id":1})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Try to update a non existing course
print("~~~~~~~~~~~~~~ Trying to update Course 99 (Doesn't Exists) ~~~~~~~~~~~~~~")
response = requests.patch(BASE + "course/99", {"name": "New name for Course 5", "session-user-id":1})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

#Deleting course
print("~~~~~~~~~~~~~~ Trying to delete Course 5 ~~~~~~~~~~~~~~")
response = requests.delete(BASE + "course/5", data={"session-user-id":1})
print("Delete operation finished... verifying Course 5 no longer exists:")
response = requests.get(BASE + "course/5")
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

print("~~~~~~~~~~~~~~ Start Lesson CRUD TEST ~~~~~~~~~~~~~~")
# Get an existing lesson
print("~~~~~~~~~~~~~~ Trying to get Lesson 3 (Full Output) ~~~~~~~~~~~~~~")
response = requests.get(BASE + "lesson/3")
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Try to get a non existing lesson
print("~~~~~~~~~~~~~~ Trying to get Lesson 11 (Doesn't Exists) ~~~~~~~~~~~~~~")
response = requests.get(BASE + "lesson/11")
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Put a lesson
print("~~~~~~~~~~~~~~ Trying to put Leson 11 ~~~~~~~~~~~~~~")
response = requests.put(BASE + "lesson/11", {"name": "lesson 11", "previous_lessons":[10], "questions" : [1,2,3], "minimum_score":10, "session-user-id":1})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Updating a lesson
print("~~~~~~~~~~~~~~ Trying to update Lesson 11 ~~~~~~~~~~~~~~")
response = requests.patch(BASE + "lesson/11", {"name": "New name for lesson 11", "session-user-id":1})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Try to update a non existing lesson
print("~~~~~~~~~~~~~~ Trying to get Lesson 99 (Doesn't Exists) ~~~~~~~~~~~~~~")
response = requests.patch(BASE + "lesson/99", {"name": "New name for lesson 11", "session-user-id":1})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

#Deleting lesson
print("~~~~~~~~~~~~~~ Trying to delete Lesson 11 ~~~~~~~~~~~~~~")
response = requests.delete(BASE + "lesson/11", data = {"session-user-id":1})
print("Delete operation finished... verifying Lesson 11 no longer exists:")
response = requests.get(BASE + "lesson/11")
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

print("~~~~~~~~~~~~~~ Start Question CRUD TEST ~~~~~~~~~~~~~~")
# Get an existing question
print("~~~~~~~~~~~~~~ Trying to get Question 3 (Full Output) ~~~~~~~~~~~~~~")
response = requests.get(BASE + "question/3")
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Try to get a non existing question
print("~~~~~~~~~~~~~~ Trying to get Question 11 (Doesn't Exists) ~~~~~~~~~~~~~~")
response = requests.get(BASE + "question/11")
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Put a question
print("~~~~~~~~~~~~~~ Trying to put Question 11 ~~~~~~~~~~~~~~")
response = requests.put(BASE + "question/11", 
                            {"question": "What's the capital of Mexico?", "score":10, "allCorrectRequired" : True,
                             "aswers":["CDMX","Xalapa","Cancun"], "correct_answers" : ["CDMX"], "session-user-id":1})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Updating a question
print("~~~~~~~~~~~~~~ Trying to update Question 11 ~~~~~~~~~~~~~~")
response = requests.patch(BASE + "question/11", {"question": "Correction for question 11", "session-user-id":1})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

# Try to update a non existing question
print("~~~~~~~~~~~~~~ Trying to update Question 99 (Doesn't Exists) ~~~~~~~~~~~~~~")
response = requests.patch(BASE + "question/99", {"question": "New name for question 99", "session-user-id":1})
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)
input()

#Deleting question
print("~~~~~~~~~~~~~~ Trying to delete Question 11 ~~~~~~~~~~~~~~")
response = requests.delete(BASE + "question/11", data={"session-user-id":1})
print("Delete operation finished... verifying Question 11 no longer exists:")
response = requests.get(BASE + "question/11")
json_formatted_str = json.dumps(response.json(), indent=1)
print(json_formatted_str)