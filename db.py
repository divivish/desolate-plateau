import validations

class Student:
	"""Student class"""
	@staticmethod
	def new_student(students, branches):
		roll = raw_input("Enter roll no.: ")

		name = raw_input("Enter name: ")
		while not validations.name(name):
			name = raw_input("Enter name: ")

		sex = raw_input("Enter sex: ")
		while not validations.sex(sex):
			sex = raw_input("Enter sex: ")

		dob = raw_input("Enter dob (YYYY-MM-DD): ")
		while not validations.date(dob):
			dob = raw_input("Enter dob (YYYY-MM-DD): ")

		ph = raw_input("Enter phone number: ")
		while not validations.phno(ph):
			ph = raw_input("Enter phone number: ")

		addr = raw_input("Enter Address: ")
		br = raw_input("Enter branch: ")
		b_id = -1
		for key in branches:
			if branches[key]["name"] == br:
				b_id = key
				break
		if b_id == -1:
			print "\n\nERROR! No such branch exists!\n\n"
			return
		stu = Student(roll, name, sex, dob, ph, addr, b_id)
		if roll in students:
			print "\n\nERROR! Student already registered!\n\n"
			return
		students[roll] = {
			"name": name,
			"dob": dob,
			"sex": sex.upper(),
			"addr": addr,
			"ph_no": ph,
			"b_id": b_id
		}

	def __init__(self, rollno, name, sex, dob, ph_no, addr, b_id):
		self.rollno = rollno
		self.name = name
		self.sex = sex
		self.dob = dob
		self.ph_no = ph_no
		self.addr = addr
		self.b_id = b_id


class Course:
	"""Course class"""
	@staticmethod
	def new_course(courses, branches):
		c_id = len(courses)
		c_type = raw_input("Enter course type: ")
		while not validations.c_type(c_type):
			c_type = raw_input("Enter course type: ")
		#name= raw_input("Enter course name: ")
		#while not validations.name(name):
		#	name= raw_input("Enter course name: ")
		cred= raw_input("Enter credits: ")
		while not validations.cred(cred):
			cred= raw_input("Enter credits: ")
		sem= raw_input("Enter sem: ")
		while not validations.sem(sem,c_type):
			sem= raw_input("Enter sem: ")
		br = raw_input("Enter branch: ")
		b_id = -1
		for key in branches:
			if branches[key]["name"] == br:
				b_id = key
				break
		if b_id == -1:
			print "\n\nERROR! No such branch exists!\n\n"
		else:
			print "yo\n"
			cou = Course(c_id, c_type, name, b_id, cred, sem)
			courses[c_id] = {
			"c_type": c_type,
			"name": name,
			"b_id": b_id,
			"cred": cred,
			"sem": sem
			}

	def __init__(self, c_id, c_type, name, b_id, cred, sem):
		self.c_id = c_id
		self.c_type = c_type
		self.name = name
		self.b_id=b_id
		self.credits = cred
		self.sem = sem

class Enrollment:
	"""Enrollment class"""
	def __init__(self, c_id, rollno, doe):
		self.c_id = c_id
		self.rollno = rollno
		self.doe = doe

class Branch:
	"""Branch class"""
	def __init__(self, b_id, name):
		self.b_id = b_id
		self.name = name
