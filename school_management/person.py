from school import School
from class_room import ClassRoom
import random


class Person:
	def __init__(self, name):
		self.name = name




class Student(Person):
	def __init__(self, name, classroom):
		super().__init__(name)
		self.classroom = classroom
		self.__id = None
		self.subject_marks = {}
		self.subject_grade = {}
		self.grade = None


	def calculate_final_grade(self):
		sum = 0
		for grade in self.subject_grade.values():
			point = School.grade_to_value(grade)
			sum += point

		if sum == 0:
			gpa = 0.00
			self.grade = "F"
			return f"{self.name}'s' Final grade: {self.grade} with GPA = {gpa}"
		else:
			rounded_gpa = sum / len(self.subject_grade)
			gpa = round(rounded_gpa, 2)
			self.grade = School.value_to_grade(gpa)
			return f"{self.name}'s' Final grade: {self.grade} with GPA = {gpa}"


	@property
	def id(self):
		return self.__id


	@id.setter
	def id(self, value):
		self.__id = value



class Teacher(Person):
	def __init__(self, name):
		super().__init__(name)


	def evaluate_exam(self):
		return random.randint(50, 100)