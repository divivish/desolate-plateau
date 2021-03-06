from flask import render_template, session, flash, request
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Regexp, NumberRange

import json
from operator import itemgetter
import datetime

from main import app

class AddEnrollmentForm(Form):
    roll = SelectField('Roll No.:', validators=[DataRequired()])
    c_id = SelectField('Semester:', validators=[DataRequired()])
    submit =  SubmitField('Add!')

    def validate(self):
        if not Form.validate(self):
            return False
        
        _roll = self.roll.data
        _c_id = self.c_id.data

        rv = True

        students = {}
        with open("files/students.json", "r") as f:
            students = json.load(f)
        courses = {}
        with open("files/courses.json", "r") as f:
            courses = json.load(f)
        enrollments = {}
        with open("files/enrollments.json", "r") as f:
            enrollments = json.load(f)
        branches = {}
        with open("files/branches.json", "r") as f:
            branches = json.load(f)

        limit = {"UG": 8, "PG": 4}
        _c_type = students[_roll]["c_type"]
        lim = limit[_c_type]
        if int(_c_id) not in xrange(1, lim+1):
            self.c_id.errors.append(
                "Incorrect sem. Should be between 1-" + str(lim) + " for " + _c_type
                )
            rv = False

        # print _c_id
        for c_id in courses:
            key = str(_roll) + "##@@##" + str(c_id)
            if int(_c_id) == int(courses[c_id]["sem"]) and students[_roll]["c_type"] == courses[c_id]["c_type"] and key in enrollments:
                self.c_id.errors.append(
                    "Student already registered for this semester's courses."
                    )
                print str(c_id)
                rv = False
                break

        f = 0
        print f
        for c_id in courses:
            if int(_c_id) == int(courses[c_id]["sem"]) and students[_roll]["c_type"] == courses[c_id]["c_type"] and students[_roll]["b_id"] == courses[c_id]["b_id"]:
                print c_id
                print _c_id
                print courses[c_id]["sem"]
                print students[_roll]["c_type"]
                print courses[c_id]["c_type"]
                f = 1
                break
        print f
        if f == 0:
            rv = False
            self.c_id.errors.append(
                "No courses were found for this semester."
                )

        # if students[_roll]["c_type"] != courses[_c_id]["c_type"]:
        #     self.c_id.errors.append(
        #         "Course not available for this student. Student is of " + students[_roll]["c_type"] +
        #         ". Whereas the course is for " + courses[_c_id]["c_type"] + "."
        #         )
        #     rv = False

        # if students[_roll]["b_id"] != courses[_c_id]["b_id"]:
        #     self.c_id.errors.append(
        #         "Cannot enroll student in other branch's couse. Student is of " + 
        #         branches[students[_roll]["b_id"]]["name"] + ". Whereas the course is for " +
        #         branches[courses[_c_id]["b_id"]]["name"] + "."
        #         )
        #     rv = False

        # key = _roll + "##@@##" + _c_id
        # if key in enrollments:
        #     self.c_id.errors.append(
        #         "Student already registered for this course."
        #         )
        #     rv = False
        
        return rv

@app.route('/add-enrollment/', methods =["GET", "POST"])
def add_enrollment():
    obj = "Enrollment"

    form = AddEnrollmentForm()
    students = {}
    with open("files/students.json", "r") as f:
        students = json.load(f)
    form.roll.choices = [(roll, str(roll) + " - " + students[roll]["name"]) for roll in sorted(students)]
    # courses = {}
    # with open("files/courses.json", "r") as f:
    #     courses = json.load(f)
    # form.c_id.choices = [(c_id, str(c_id) + " - " + courses[c_id]["name"]) for c_id in sorted(courses)]

    form.c_id.choices = [(str(x), x) for x in xrange(1, 9)]


    if form.validate_on_submit():
        students = {}
        with open("files/students.json", "r") as f:
            students = json.load(f)
        courses = {}
        with open("files/courses.json", "r") as f:
            courses = json.load(f)
        enrollments = {}
        with open("files/enrollments.json", "r") as f:
            enrollments = json.load(f)

        enroll_courses = []
        sem = form.c_id.data
        # sem = courses[form.c_id.data]["sem"]
        b_id = students[form.roll.data]["b_id"]
        c_type = students[form.roll.data]["c_type"]
        for c_id in courses:
            if int(sem) == int(courses[c_id]["sem"]) and b_id == courses[c_id]["b_id"] and c_type == courses[c_id]["c_type"]:
                key = form.roll.data + "##@@##" + c_id
                if key not in enrollments:
                    enroll_courses.append( [c_id, courses[c_id]["name"]])
                    enrollments[key] = {"doe": str(datetime.date.today())}

        with open("files/enrollments.json", "w") as f:
            json.dump(enrollments, f)
        
        flash("Enrollments added successfully.", "success")
        enroll_courses.sort(key=lambda x: x[0])
        cols = [("numeric", "Course ID"), ("input-text", "Course Name")]
        return render_template("add_data.html", form = form, obj = obj,
         rows = enroll_courses, cols = cols
         )
    elif request.method == "POST":
        flash("There seem to be some errors in the form", "danger")
    flash("Student will be enrolled for all the courses of this sem.", "info")
    return render_template("add_data.html", form = form, obj = obj)