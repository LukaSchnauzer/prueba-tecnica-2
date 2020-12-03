courses = {
            1 : {   
                    "name" : "Course 1",
                    "previous_courses" : None,
                    "lessons" : [1,2]
                },
            2 : {   
                    "name" : "Course 2",
                    "previous_courses" : None,
                    "lessons" : [4,5,6]
                },
            3 : {   
                    "name" : "Course 3",
                    "previous_courses" : [1,2],
                    "lessons" : [7,8]
                },
            4 : {   
                    "name" : "Course 4",
                    "previous_courses" : [3],
                    "lessons" : [9,10]
                }
          }

lessons = {
            1 : {   
                    "name" : "Lesson 1",
                    "previous_lessons" : None,
                    "questions" : [1,2],
                    "minimum_score": 6
                },
            2 : {   
                    "name" : "Lesson 2",
                    "previous_lessons" : [1],
                    "questions" : [3,4],
                    "minimum_score": 8
                },
            3 : {   
                    "name" : "Lesson 3",
                    "previous_lessons" : [2],
                    "questions" : [1,2],
                    "minimum_score": 6
                },
            4 : {   
                    "name" : "Lesson 4",
                    "previous_lessons" : None,
                    "questions" : [3,4],
                    "minimum_score": 6
                },
            5 : {   
                    "name" : "Lesson 5",
                    "previous_lessons" : None,
                    "questions" : [1,2],
                    "minimum_score": 6
                },
            6 : {   
                    "name" : "Lesson 6",
                    "previous_lessons" : [4,5],
                    "questions" : [1,2],
                    "minimum_score": 6
                },
            7 : {   
                    "name" : "Lesson 7",
                    "previous_lessons" : None,
                    "questions" : [3,4],
                    "minimum_score": 6
                },
            8 : {   
                    "name" : "Lesson 8",
                    "previous_lessons" : [7],
                    "questions" : [1,2],
                    "minimum_score": 6
                },
            9 : {   
                    "name" : "Lesson 9",
                    "previous_lessons" : None,
                    "questions" : [3,4],
                    "minimum_score": 8
                },
            10 : {   
                    "name" : "Lesson 10",
                    "previous_lessons" : [9],
                    "questions" : [1,2],
                    "minimum_score": 6
                }
          }

questions = {
                1 : {
                        "question" : "Question 1?",
                        "score" : 4,
                        "allCorrectRequired" : True,
                        "aswers" : ["True", "False"],
                        "correct_answers" : ["True"]
                    },
                2 : {
                        "question" : "Question 2?",
                        "score" : 2,
                        "allCorrectRequired" : True,
                        "aswers" : ["Option a", "Option b", "Option c"],
                        "correct_answers" : ["Option b"]
                    },
                3 : {
                        "question" : "Question 3?",
                        "score" : 4,
                        "allCorrectRequired" : False,
                        "aswers" : ["Option a", "Option b", "Option c"],
                        "correct_answers" : ["Option b","Option c"]
                    },
                4 : {
                        "question" : "Question 4?",
                        "score" : 4,
                        "allCorrectRequired" : True,
                        "aswers" : ["Option a", "Option b", "Option c"],
                        "correct_answers" : ["Option b","Option c"]
                    }
            }

users = {
            1 : {
                    "name" : "Juan",
                    "role" : "P", # Proffesor
                    "approved_lessons" : None
                  },
            2 : {
                    "name" : "Carlos",
                    "role" : "S", #Student
                    "approved_lessons" : []
                  }
        }