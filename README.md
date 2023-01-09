# CSCI220 Fall 2022: Scripts for Calculating Final Grades

This repo contains Python scripts to calculate the component ESNU scores and the final A-F grade for CSCI220 (CS@Mines) Fall 2022

## Files

- `esnu_grade_calculations.py`: source for calculations and `Score` enum type
- `scrape_gradebook.py`: used last minute to scrape relevant scores from canvas because the csv export tool didn't output the ESNU grading scheme (maybe post idea to Instructure community site)
- `final.py`: outputs a final grades csv from a gradebook csv 
- `student.py`: small student class to make CanvasAPI easier to use
- `sample_gradebook`: small sample input gradebook

## Unit Tests

To run the unit tests:

`python3 unit_tests.py -v`


