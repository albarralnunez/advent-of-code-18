import argparse

from src.day1.day1 import Day1Problem1, Day1Problem2
from src.day2.day2 import Day2Problem1
from src.libs.problem import ProblemRunner

PROBLEMS = {
    1: {1: Day1Problem1, 2: Day1Problem2},
    2: {1: Day2Problem1, },
}


def get_problem(day, number):
    return PROBLEMS[day][number]()


def main(day, number, send):
    problem = get_problem(day, number)
    problem_runner = ProblemRunner(problem)
    result = problem_runner.solve()
    print(result)
    if send:
        problem_runner.send()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--day', type=int, help='day to solve')
    parser.add_argument('--number', type=int, help='Problem to solve')
    parser.add_argument('--send', action='store_true')
    args = parser.parse_args()
    main(args.day, args.number, args.send)
