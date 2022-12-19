import pandas as pd

from esnu_grade_calculations import *
import csv


df = pd.read_csv("gradebook.csv")
outfile = open("final_grades.csv", 'w')
csvwriter = csv.writer(outfile, delimiter=",")
csvwriter.writerow(["last_name", "first_name", "Analysis",
                   "Programming", "Comprehension", "Final"])

# canvas gradebook csv column names
analysis_names = ["analysis_1", "analysis_2",
                  "analysis_3", "analysis_4", "analysis_5"]
programming_names = ["programming_1", "programming_2",
                     "programming_3", "programming_4", "programming_5"]
midterm_name = "midterm"
final_name = "final"
first_name = "first_name"
last_name = "last_name"
for index, student in df.iterrows():
    print(student)

    analysis_scores = []
    for a in analysis_names:
        analysis_scores.append(convert_to_score(student[a]))

    programming_scores = []
    for p in programming_names:
        programming_scores.append(convert_to_score(student[p]))

    midterm_score = convert_to_score(student[midterm_name])
    final_score = convert_to_score(student[final_name])

    analysis = compute_analysis_score(analysis_scores)
    programming = compute_programming_score(programming_scores)
    comprehension = compute_comprehension_score(final_score, midterm_score)
    final = compute_final_score([analysis, programming, comprehension])
    last = student[last_name]
    first = student[first_name]
    csvwriter.writerow([last, first, analysis,
                       programming, comprehension, final])
