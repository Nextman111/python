import argparse
import logging
from student_ex import NameError, ValueReadError, IncorrectValueError
from student import Student


def main():
    logging.basicConfig(filename='student.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

    parser = argparse.ArgumentParser(description='Student base.')
    parser.add_argument('name', help='Student name')
    parser.add_argument('filename', help='Filename')
    parser.add_argument('subject ', help='Subject ')
    parser.add_argument('score ', help='Score ')
    args = parser.parse_args()

    try:
        student = Student(args.name, args.filename)
        student.add_score(args.subject, args.score)
    except NameError as e:
        logging.error(f'Student Name Error. {e.message}')
    except ValueReadError as e:
        logging.error(f'Error reading item from file: {e.subject}')
    except IncorrectValueError as e:
        logging.error(f'Incorrect Value Score: {e.score}')


if __name__ == '__main__':
    main()