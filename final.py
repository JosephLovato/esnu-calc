import pandas as pd
import csv

from esnu_grade_calculations import *


# import gradebook csv into a pandas data frame
df = pd.read_csv("sample_gradebook")

# setup output csv
outfile = open("sample_output", 'w')
csvwriter = csv.writer(outfile, delimiter=",")
csvwriter.writerow(["last_name", "first_name", "Analysis",
                   "Programming", "Comprehension", "Final"])

# gradebook csv column names
analysis_names = ["analysis_1", "analysis_2",
                  "analysis_3", "analysis_4", "analysis_5"]
programming_names = ["programming_1", "programming_2",
                     "programming_3", "programming_4", "programming_5"]
midterm_name = "midterm"
final_name = "final"
first_name = "first_name"
last_name = "last_name"

# each row in the data frame is a student
for index, student in df.iterrows():
    print(student)

    # get analysis scores from student series
    analysis_scores = []
    for a in analysis_names:
        analysis_scores.append(convert_to_score(student[a]))

    # get programming scores from student series
    programming_scores = []
    for p in programming_names:
        programming_scores.append(convert_to_score(student[p]))

    # get exam scores from student series
    midterm_score = convert_to_score(student[midterm_name])
    final_score = convert_to_score(student[final_name])

    # compute scores and final grade
    analysis = compute_analysis_score(analysis_scores)
    programming = compute_programming_score(programming_scores)
    comprehension = compute_comprehension_score(final_score, midterm_score)
    final = compute_final_grade([analysis, programming, comprehension])

    # write to output csv
    last = student[last_name]
    first = student[first_name]
    csvwriter.writerow([last, first, analysis,
                       programming, comprehension, final])
