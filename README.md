# Flask Simple API
This simple API REST was made using **Python 3.9** and the **Flask** framework due to its simplicity and fast setup
## Instalation
The required python modules are all specified in the *requirements.txt* file. For a quick installation of the various modules just run:
  

      pip install -r requirements.txt

## Using the API
To start the API, run the main script

    python ./main.py

This will  start the service locally on the URL **http://127.0.0.1:5000/** 
Now you can use the API. Here I included a script that I used to test the diferent processes, this script requires the python modules **requests** and **json**.
To run the test script run:

    python ./test.py

You can add more tests to this script as you see fit.
However, you should be able to access the different endpoints any other way you want.
## Endpoints
The enpoints exposed are as following:

 - **/course/<int:course_id>**
CRUD for Courses, depending on the request (GET to read the Course with id *course_id*, PUT to create a Course with the given id, PATCH to update and DELETE to delete). When data is needed (for PUT, PATCH and DELETE), it's passed as a form in the request.
When working with python a dictionary can be used, here's an example of the form for Course as a python dict:

> {"name": "Course 5", "previous_courses":[1], "lessons" : [1,2,3], "session-user-id":1}

The request is not processed if the form is incorrect.

 - **/lesson/<int:lesson_id>**
CRUD for Lessons, similar to the last endpoint it uses the request to decide wheter to create, update, read or delete.
Here's an example of the correct request form as a python dict:

> {"name": "lesson 11", "previous_lessons":[10], "questions" : [1,2,3], "minimum_score":10, "session-user-id":1}

 

 - **/question/<int:question_id>**

 CRUD for Questions, similiar to the first two endpoints.
 Request form as python dict:
 
> {"question": "What's the capital of Mexico?", "score":10, "allCorrectRequired" : True, "aswers":["CDMX","Xalapa","Cancun"], "correct_answers" : ["CDMX"], "session-user-id":1}

Here the value *allCorrectRequired* is used to diferenciate between the different types of questions available:

 1. Boolean question: is just a multiple choice question with only two possible answers and only one correct
 2. Multiple choice where only one answer is correct: can be achieved with *allCorrectRequired* set to True, and just entering a single *correct_answer*. So it's necesary to answer every correct answer but there's only one.
 3.  Multiple choice where more than one answer is correct: just setting *allCorrectRequired* to False.
 4. Multiple choice where more than one answer is correct and all of them must be answered correctly: setting *allCorrectRequired* to True

The 3 first enpoints always return either an error report like

> { message:"error message"}

or they return a JSON-like response similar to the form of the corresponding object type.

 - **/courses/all**
Used to obtain every course available and whether it can be done by the user in session based on the requiered previous courses. This one only requieres the *session-user-id* in the form

> {"session-user-id":id}

Example of response:

 

	       {
		     "courses": [
		      {
		       "1": {
				        "name": "Course 1",
				        "previous_courses": null,
				        "lessons": [1, 2]
					},
		       "aproved": false, #based on whether all the lessons for the course are approved
		       "canAccess": true #based on the attribute previous_courses
		      },
		    ...
		   ] }

 - **/lessons/all**
 Used to obtain every lesson in the selected course and whether they can be done by the current user, based on the previous lessons. The selected course's id is given via the form of the request:
 

> {"course_id":id,"session-user-id":user_id}

Response Example:

	{
	 "lessons": [
	  {
	   "1": {
	    "name": "Lesson 1",
	    "previous_lessons": null,
	    "questions": [1,2],
	    "minimum_score": 6
	   },
	   "aproved": false,
	   "canAccess": true
	  },...
	 ]
	}

 - **/lessons/answer**
Used to send the answer for all questions in a lesson. This time the data for the request is sent as a JSON like this one:

	    {"lesson_id":1, "session-user-id":2 , "answers": [{"question_id":1,"given_answer":["True"]},{"question_id":2,"given_answer":["Option b"]}]}

the list *answers* is used to validate if the question was answered correctly. At the end of the call the response is like this:

	{
	 "result": "Lesson Approved!!", #Can also be "Lesson failed"
	 "score": 6
	}
If the lesson was approved, this is stored at the user data, so they can access the rest of lessons and courses.

## Mock Database
This project has a mock database included in the file *db\mockInitialDB.py*. This is just a set of python dictionaries. The data sotored here persists while the API is running. When it stops and is started again, all data is reverted to that of the file.
 