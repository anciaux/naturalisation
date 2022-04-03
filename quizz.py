#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
from IPython.display import clear_output
################################################################


def try_answer(answers, res):
    try:
        return answers[res][1]
    except Exception:
        return False

################################################################


def quizz(questions):
    random.shuffle(questions)
    N = len(questions)
    points = 0

    for i, q in enumerate(questions):
        clear_output()
        print("question " + str(i) + "/" + str(N) + " : points: " +
              str(points) + "/" + str(N))
        print("Question: {0}".format(q['question']))
        random.shuffle(q['answers'])
        answers = [(b, a) for a, b in q['answers']]
        correct = [b for i, (a, b) in enumerate(q['answers']) if a]
        print("")
        for i, (a, b) in enumerate(answers):
            print('{0}: {1}'.format(i, a))
        res = int(input('\nta réponse: '))
        first_shot = 0
        while not try_answer(answers, res):
            print("\nnon!\n")
            first_shot += 1
            if first_shot == 2:
                print('solution: ' + str(correct[0]))
                break
            res = int(input('\nta réponse: '))

        if first_shot == 0:
            print("\nbravo!!!\n")
            time.sleep(1)
        if first_shot == 0:
            points += 1

    print('\n'*2 + '*'*20)
    print('Points: ' + str(points) + '/' + str(N))
    print('Ta note: ' + str(int(points/N*12)/2))

    input('*'*10 + "\n")

################################################################
