import unittest
from esnu_grade_calculations import *

lga_q_4 = {"programming": [Score.S] * 5,
           "analysis": [Score.S] * 4 + [Score.N],
           "midterm": Score.N,
           "final": Score.S}

lga_q_5 = {"programming": [Score.S] * 4 + [Score.U],
           "analysis": [Score.E] * 2 + [Score.S] * 2 + [Score.U],
           "midterm": Score.N,  # doesn't matter
           "final": Score.S}


class TestProgrammingCalculation(unittest.TestCase):
    def test_lga_q_4(self):
        self.assertEqual(Score.E, compute_programming_score(
            lga_q_4["programming"]))

    def test_lga_q_5(self):
        self.assertEqual(Score.S, compute_programming_score(
            lga_q_5["programming"]))

    def test_all_possible_E(self):
        self.assertEqual(Score.E, compute_programming_score([Score.S] * 5))

    def test_all_possible_S(self):
        self.assertEqual(Score.S, compute_programming_score(
            [Score.S] * 4 + [Score.N]))
        self.assertEqual(Score.S, compute_programming_score(
            [Score.S] * 4 + [Score.U]))

    def test_all_possible_N(self):
        self.assertEqual(Score.N, compute_programming_score(
            [Score.S] * 3 + [Score.N] * 2))
        self.assertEqual(Score.N, compute_programming_score(
            [Score.S] * 2 + [Score.N] * 3))
        self.assertEqual(Score.N, compute_programming_score(
            [Score.S] * 3 + [Score.U] * 2))
        self.assertEqual(Score.N, compute_programming_score(
            [Score.S] * 2 + [Score.U] * 3))

    def test_all_possible_U(self):
        self.assertEqual(Score.U, compute_programming_score(
            [Score.S] + [Score.N] * 4))
        self.assertEqual(Score.U, compute_programming_score([Score.N] * 5))
        self.assertEqual(Score.U, compute_programming_score(
            [Score.S] + [Score.U] * 4))
        self.assertEqual(Score.U, compute_programming_score([Score.U] * 5))


class TestAnalysisCalculation(unittest.TestCase):
    def test_lga_q_4(self):
        self.assertEqual(Score.S, compute_analysis_score(lga_q_4["analysis"]))

    def test_lga_q_5(self):
        self.assertEqual(Score.E, compute_analysis_score(lga_q_5["analysis"]))

    def test_many_E(self):
        self.assertEqual(Score.E, compute_analysis_score(
            [Score.E, Score.E, Score.S, Score.S, Score.S]))
        self.assertEqual(Score.E, compute_analysis_score(
            [Score.E, Score.E, Score.E, Score.S, Score.S]))
        self.assertEqual(Score.E, compute_analysis_score(
            [Score.E, Score.E, Score.E, Score.E, Score.S]))
        self.assertEqual(Score.E, compute_analysis_score(
            [Score.E, Score.E, Score.E, Score.E, Score.E]))
        self.assertEqual(Score.E, compute_analysis_score(
            [Score.E, Score.E, Score.S, Score.S, Score.N]))
        self.assertEqual(Score.E, compute_analysis_score(
            [Score.E, Score.E, Score.E, Score.S, Score.N]))
        self.assertEqual(Score.E, compute_analysis_score(
            [Score.E, Score.E, Score.S, Score.S, Score.U]))
        self.assertEqual(Score.E, compute_analysis_score(
            [Score.E, Score.E, Score.E, Score.S, Score.U]))
        self.assertEqual(Score.E, compute_analysis_score(
            [Score.E, Score.E, Score.E, Score.E, Score.N]))
        self.assertEqual(Score.E, compute_analysis_score(
            [Score.E, Score.E, Score.E, Score.E, Score.U]))

    def test_many_S(self):
        self.assertEqual(Score.S, compute_analysis_score(
            [Score.E, Score.S, Score.S, Score.S, Score.S]))
        self.assertEqual(Score.S, compute_analysis_score(
            [Score.S, Score.S, Score.S, Score.S, Score.S]))
        self.assertEqual(Score.S, compute_analysis_score(
            [Score.E, Score.S, Score.S, Score.S, Score.N]))
        self.assertEqual(Score.S, compute_analysis_score(
            [Score.S, Score.S, Score.S, Score.S, Score.N]))
        self.assertEqual(Score.S, compute_analysis_score(
            [Score.E, Score.S, Score.S, Score.S, Score.U]))
        self.assertEqual(Score.S, compute_analysis_score(
            [Score.S, Score.S, Score.S, Score.S, Score.U]))

    def test_many_N(self):
        self.assertEqual(Score.N, compute_analysis_score(
            [Score.E, Score.N, Score.N, Score.N, Score.N]))
        self.assertEqual(Score.N, compute_analysis_score(
            [Score.S, Score.N, Score.N, Score.N, Score.N]))
        self.assertEqual(Score.N, compute_analysis_score(
            [Score.S, Score.S, Score.N, Score.N, Score.N]))
        self.assertEqual(Score.N, compute_analysis_score(
            [Score.S, Score.S, Score.S, Score.N, Score.N]))
        self.assertEqual(Score.N, compute_analysis_score(
            [Score.E, Score.S, Score.S, Score.N, Score.N]))
        self.assertEqual(Score.N, compute_analysis_score(
            [Score.E, Score.E, Score.S, Score.N, Score.N]))
        self.assertEqual(Score.N, compute_analysis_score(
            [Score.E, Score.E, Score.E, Score.N, Score.N]))
        self.assertEqual(Score.N, compute_analysis_score(
            [Score.E, Score.E, Score.E, Score.N, Score.U]))
        self.assertEqual(Score.N, compute_analysis_score(
            [Score.S, Score.S, Score.S, Score.N, Score.U]))

    def test_many_U(self):
        self.assertEqual(Score.U, compute_analysis_score(
            [Score.U, Score.U, Score.U, Score.U, Score.U]))
        self.assertEqual(Score.U, compute_analysis_score(
            [Score.N, Score.U, Score.U, Score.U, Score.U]))
        self.assertEqual(Score.U, compute_analysis_score(
            [Score.N, Score.N, Score.U, Score.U, Score.U]))
        self.assertEqual(Score.U, compute_analysis_score(
            [Score.N, Score.N, Score.N, Score.U, Score.U]))
        self.assertEqual(Score.U, compute_analysis_score(
            [Score.E, Score.E, Score.E, Score.U, Score.U]))
        self.assertEqual(Score.U, compute_analysis_score(
            [Score.E, Score.S, Score.N, Score.U, Score.U]))
        self.assertEqual(Score.U, compute_analysis_score(
            [Score.S, Score.N, Score.N, Score.U, Score.U]))


class TestComprehensionCalculation(unittest.TestCase):
    def test_lga_q_4(self):
        self.assertEqual(Score.S, compute_comprehension_score(
            lga_q_4["final"], lga_q_4["midterm"]))

    def test_lga_q_5(self):
        self.assertEqual(Score.S, compute_comprehension_score(
            lga_q_5["final"], lga_q_5["midterm"]))

    def test_all_possible_E(self):
        # midterm doesn't matter
        self.assertEqual(
            Score.E, compute_comprehension_score(Score.E, Score.E))
        self.assertEqual(
            Score.E, compute_comprehension_score(Score.E, Score.S))
        self.assertEqual(
            Score.E, compute_comprehension_score(Score.E, Score.N))
        self.assertEqual(
            Score.E, compute_comprehension_score(Score.E, Score.U))

    def test_all_possible_S(self):
        # first case (final = S): midterm doesn't matter
        self.assertEqual(
            Score.S, compute_comprehension_score(Score.S, Score.E))
        self.assertEqual(
            Score.S, compute_comprehension_score(Score.S, Score.S))
        self.assertEqual(
            Score.S, compute_comprehension_score(Score.S, Score.N))
        self.assertEqual(
            Score.S, compute_comprehension_score(Score.S, Score.U))
        # second case (final = N, midterm = E)
        self.assertEqual(
            Score.S, compute_comprehension_score(Score.N, Score.E))

    def test_all_possible_N(self):
        self.assertEqual(
            Score.N, compute_comprehension_score(Score.N, Score.S))
        self.assertEqual(
            Score.N, compute_comprehension_score(Score.N, Score.N))
        self.assertEqual(
            Score.N, compute_comprehension_score(Score.N, Score.U))
        self.assertEqual(
            Score.N, compute_comprehension_score(Score.U, Score.E))
        self.assertEqual(
            Score.N, compute_comprehension_score(Score.U, Score.S))

    def test_all_possible_U(self):
        self.assertEqual(
            Score.U, compute_comprehension_score(Score.U, Score.N))
        self.assertEqual(
            Score.U, compute_comprehension_score(Score.U, Score.U))


class TestFinalGradeCalculation(unittest.TestCase):
    def test_lga_q_4(self):
        self.assertEqual('B', calculate_grade(
            lga_q_4["programming"], lga_q_4["analysis"], lga_q_4["midterm"], lga_q_4["final"]))

    def test_lga_q_5(self):
        self.assertEqual('B', calculate_grade(
            lga_q_5["programming"], lga_q_5["analysis"], lga_q_5["midterm"], lga_q_5["final"]))

    def test_all_possible_A(self):
        self.assertEqual('A', compute_final_grade([Score.E, Score.E, Score.E]))
        self.assertEqual('A', compute_final_grade([Score.E, Score.E, Score.S]))

    def test_all_possible_B(self):
        self.assertEqual('B', compute_final_grade([Score.E, Score.S, Score.S]))

    def test_all_possible_C(self):
        self.assertEqual('C', compute_final_grade([Score.S, Score.S, Score.S]))

    def test_all_possible_D(self):
        self.assertEqual('D', compute_final_grade([Score.S, Score.S, Score.N]))
        self.assertEqual('D', compute_final_grade([Score.E, Score.S, Score.N]))

    def test_all_possible_F(self):
        self.assertEqual('F', compute_final_grade([Score.S, Score.N, Score.N]))
        self.assertEqual('F', compute_final_grade([Score.S, Score.N, Score.U]))
        self.assertEqual('F', compute_final_grade([Score.N, Score.N, Score.N]))
        self.assertEqual('F', compute_final_grade([Score.U, Score.U, Score.N]))
        self.assertEqual('F', compute_final_grade([Score.U, Score.E, Score.E]))
        self.assertEqual('F', compute_final_grade([Score.U, Score.S, Score.S]))
        self.assertEqual('F', compute_final_grade([Score.U, Score.U, Score.S]))
        self.assertEqual('F', compute_final_grade([Score.U, Score.U, Score.U]))


if __name__ == '__main__':
    unittest.main()
