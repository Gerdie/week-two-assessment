"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   >> Abstraction: You don't have to know how the code works in order to use it. 
   As an example, we were able to draw a picture using the oo-drawing module without
   knowing how their Circle, Point or Polygon classes were constructed.

   >> Encapsulation: All the code relating to a certain "thing" is stored within that
   thing. If we constructed a Cat() class, all our Cat attributes and methods would be
   stored inside that class. So we don't have to look through a bunch of different files
   and libraries to find all the scattered codebits that relate to the object we're
   working with.

   >> Polymorphism: Components are interchangeable. We can access methods and attributes
   in a standardized, predictable way across different instances of a class (and
   that class's children, parents, relatives).


2. What is a class?

    >> A class is a datatype that contains specialized variables (attributes) and
    functions (methods) for its own particular use.

3. What is an instance attribute?

    >> An instance attribute is an attribute that is unique to that instance. Many
    are set in the __init__ function as parameters.

4. What is a method?

    >> A method is a special function that is defined inside a class, and used by
    instances of that class. It takes "self" as its first parameter, and is called
    on an instance using dot notation.

5. What is an instance in object orientation?

>> An instance is an object of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

>> A class attribute is (unless otherwise specified) shared by all members of that
class. An instance attribute is unique to that instance. If we were working with a
HackbrightStudents class, coolness = True might be a class attribute
and name might be an instance attribute, because all hackbright students are cool
and all hackbright students (in Ada at least) have differently spelled names.


"""


# Parts 2 through 5:
# Create your classes and class methods

"""Create a Student class with below info
{'first_name': 'Jasmine',
 'last_name': 'Debugger',
 'address': '0101 Computer Street'}
"""


class Student(object):
    """A student"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


"""Questions are a question ans a correct answer as below
{'question': 'What is the capital of Alberta?',
 'correct_answer': 'Edmonton'}

{'question': 'Who is the author of Python?',
 'correct_answer': 'Guido Van Rossum'}
"""


class Question(object):
    """A question/answer pair"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = raw_input("{} > ".format(self.question))
        return answer == self.correct_answer


"""Exams
{'name':'Midterm',
 'questions': [] }
"""


class Exam(object):
    """An exam, using Questions"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        results = []
        for question in self.questions:
            result = question.ask_and_evaluate()
            results.append(result)
        return results.count(True) / float(len(results))


class Quiz(Exam):
    """Pass if at least 50 percent correct"""

    def administer(self):
        return super(Quiz, self).administer >= .5


def take_test(exam, student):
    """Assigns test to student; records student's score"""

    score = exam.administer()

    student.score = score


def example():
    """Creates exam, Adds questions to exam, Creates student, Administers test"""

    exam = Exam("Example exam")
    print exam

    exam.add_question("1 + 1 = ", "2")
    print exam.questions
    exam.add_question("1 x 1 = ", "1")
    print exam.questions[0].question

    student = Student("Maria", "Moy", "1600 Pennsylvania Ave")
    print student
    take_test(exam, student)
    print student.score
