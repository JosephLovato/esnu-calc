from canvasapi import Canvas
from student import student
import csv

# Canvas API URL
API_URL = "https://elearning.mines.edu"
# Canvas API key (generate from https://elearning.mines.edu/profile/settings > + New Access Token)
API_KEY = "9802~GdDE4yv0soEtR9NuvEUSstoWFXbZb7sugttdFKKrsnUh7ruC9ycqhAR8mqr2zpwT"
# Course to work on (get id from canvas URL)
COURSE = "42642"
# assignment IDs
ANALYSIS = ["304181", "307097", "308081", "311687", "312462"]
PROGRAMMING = ["302406", "306104", "307705", "309508", "311736"]
MIDTERM = "310726"
FINAL = "316389"

canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE)

analysis_assignments = []
for a in ANALYSIS:
    analysis_assignments.append(course.get_assignment(a))

programming_assignments = []
for p in PROGRAMMING:
    programming_assignments.append(course.get_assignment(p))

midterm_assignment = course.get_assignment(MIDTERM)
final_assignment = course.get_assignment(FINAL)

outfile = open("gradebook.csv", 'w')
csvwriter = csv.writer(outfile, delimiter=",")
csvwriter.writerow(["last_name", "first_name",
                   "analysis_1", "analysis_2", "analysis_3", "analysis_4", "analysis_5",
                    "programming_1", "programming_2", "programming_3", "programming_4", "programming_5",
                    "midterm", "final"])

roster = open("roster.csv", "r")
lines = roster.readlines()
students = []
for line in lines:
    data = line.split(',')
    students.append(student(data[1], data[0], data[2][:-1]))

for s in students:
    print(s.last_name)
    analysis_grades = []
    for a in analysis_assignments:
        analysis_grades.append(a.get_submission(s.id).grade)
    programming_grades = []
    for p in programming_assignments:
        programming_grades.append(p.get_submission(s.id).grade)
    midterm_grade = midterm_assignment.get_submission(s.id).grade
    final_grade = final_assignment.get_submission(s.id).grade
    csvwriter.writerow([s.last_name, s.first_name] +
                       analysis_grades + programming_grades + [midterm_grade, final_grade])

outfile.close()
print("...done")
