#
# ESNU Grading Calculations Helper Functions
# author: Joey Lovato
# last updated: 11/13/22
#

from enum import Enum


class Score(Enum):
    E = 4
    S = 3
    N = 2
    U = 1
    X = 0

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value


def convert_to_score(s: str):
    if s == "E":
        return Score.E
    elif s == "S":
        return Score.S
    elif s == "N":
        return Score.N
    elif s == "U":
        return Score.U
    else:
        return Score.X


def score_to_string(score):
    if score == Score.E:
        return "E"
    elif score == Score.S:
        return "S"
    elif score == Score.N:
        return "N"
    elif score == Score.U:
        return "U"
    else:
        raise RuntimeError("Cannot convert score: " + score)


def count_at_least(scores: list, minimum: Score):
    """returns the number of scores greater than
    or equal the provided minimum
    """
    return [x.value >= minimum.value for x in scores].count(True)


def compute_comprehension_score(final, midterm):
    """Computes the ESNU comprehensions component score given the final and midterm scores"""
    if final == Score.E:
        return Score.E
    elif final == Score.S or (midterm == Score.E and final == Score.N):
        return Score.S
    elif final >= Score.N or midterm >= Score.S:
        return Score.N
    elif final == Score.U and (midterm == Score.N or midterm == Score.U):
        return Score.U
    else:
        return Score.X


def compute_programming_score(scores: list):
    """Computes the ESNU programming component score given a list of programming scores"""
    if scores.count(Score.S) == 5:
        return Score.E
    elif scores.count(Score.S) == 4:
        return Score.S
    elif scores.count(Score.S) == 2 or scores.count(Score.S) == 3:
        return Score.N
    elif scores.count(Score.S) <= 1:
        return Score.U
    else:
        return Score.X


def compute_analysis_score(scores: list):
    """Computes the ESNU analysis component score given a list of analysis scores"""
    if count_at_least(scores, Score.S) >= 4 and scores.count(Score.E) >= 2:
        return Score.E
    elif count_at_least(scores, Score.S) >= 4:
        return Score.S
    elif count_at_least(scores, Score.N) >= 4:
        return Score.N
    elif count_at_least(scores, Score.N) < 4:
        return Score.U
    else:
        return Score.X


def compute_final_score(component_scores: list):
    """Computes final A-F grade given a list of three component scores
    """
    if component_scores.count(Score.E) == 3 or (component_scores.count(Score.E) >= 2 and count_at_least([s for s in component_scores if s != Score.E], Score.S) >= 1):
        return 'A'
    elif component_scores.count(Score.E) == 1 and [s for s in component_scores if s != Score.E].count(Score.S) == 2:
        return 'B'
    elif count_at_least(component_scores, Score.S) == 3:
        return 'C'
    elif count_at_least(component_scores, Score.S) == 2 and count_at_least([s for s in component_scores if s.value < Score.S.value], Score.N) == 1:
        return 'D'
    elif component_scores.count(Score.S) <= 1 or component_scores.count(Score.U) > 0:
        return 'F'


def calculate_grade(programming_scores, analysis_scores, midterm_score, final_score):
    return compute_final_score([compute_programming_score(programming_scores),
                                compute_analysis_score(analysis_scores),
                                compute_comprehension_score(final_score, midterm_score)])
