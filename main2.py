import json
import datetime
from db import Student, Course, Enrollment, Branch


students = {}
courses = {}
enrollments = {}
branches = {}
archived_enrolls = {}

def init():
	global students
	global courses
	global enrollments
	global branches
	global archived_enrolls
	with open("files/branches.json", "r") as f:
		branches = json.load(f)
	with open("files/students.json", "r") as f:
		students = json.load(f)
	with open("files/courses.json", "r") as f:
		courses = json.load(f)
	with open("files/enrollments.json", "r") as f:
		enrollments = json.load(f)
	with open("files/archived_enrolls.json", "r") as f:
		archived_enrolls = json.load(f)

def save():
	with open("files/branches.json", "w") as f:
		json.dump(branches, f)
	with open("files/students.json", "w") as f:
		json.dump(students, f)
	with open("files/courses.json", "w") as f:
		json.dump(courses, f)
	with open("files/enrollments.json", "w") as f:
		json.dump(enrollments, f)
	with open("files/archived_enrolls.json", "w") as f:
		json.dump(archived_enrolls, f)


def menu():
	print "Welcome!"
	while 1:
		print "1. Add a student"
		print "2. Delete student data"
		print "3. Modify student details"
		print "4. List all students"
		print "5. Add a course"
		print "6. Delete course data"
		print "7. Modify course details"
		print "8. List all courses"
		print "9. Enroll student in course"
		print "10. Show enrollments of a student"
		print "11. Show enrollments of a course"
		print "12. Archive old enrollments"
		print "13. Exit"
		ch = raw_input("What would you like to do? ")
		if ch == "1":
			Student.new_student(students, branches)
		elif ch == "2":
			Student.delete_student(students, enrollments)
		elif ch == "3":
			Student.modify_student(students)
		elif ch == "4":
			Student.list_students(students, branches)
		elif ch == "5":
			Course.new_course(courses, branches)
		elif ch == "6":
			Course.delete_course(courses, enrollments)
		elif ch == "7":
			Course.modify_course(courses)
		elif ch == "8":
			Course.list_courses(courses, branches)
		elif ch == "9":
			Enrollment.new_enrollment(enrollments, students, courses)
		elif ch == "10":
			Enrollment.list_enrollments_stu(enrollments, archived_enrolls, students, courses)
		elif ch == "11":
			Enrollment.list_enrollments_cou(enrollments, archived_enrolls, students, courses)
		elif ch == "12":
			Enrollment.archive_enrollments(enrollments, archived_enrolls)
		elif ch == "13":
			print "\nBye!\n"
			break
		else:
			print "\nNot Valid Choice! Try again!\n"
		save()

if __name__ == "__main__":
	init()
	menu()
