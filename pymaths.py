__author__ = 'user'

import random
import datetime

passed = []
failed = []

def main():

    MULTIPLICATION = "multiplication"
    DIVISION = "division"
    HALVING = "halving"

    print("Welcome to the Maths Test!")
    name = input("What is your name? ")

    types = {MULTIPLICATION : "x", DIVISION: "/", HALVING : "halved"}
    try:
        type = pick("test type", sorted(list(types.keys())))
    except Exception as e:
        print(e)
        return

    # If you picked the halving test...
    if type == HALVING:

        # ...then this is a divide by 2 test with 20 questions and max numerator of 100
        questions = 20
        score = division_test(2, max_numerator=100, questions = questions)

    else:

        questions = 5
        options = []

        # Now pick the multiplier or divisor that you want to be tested on from 2-12 or random
        RANDOM = "Random Test"
        options.append(RANDOM)
        options += (list(range(2,13)))

        try:
            number = pick("test", options)
        except Exception as e:
            print(e)
            return

        if type == DIVISION:
            if number == RANDOM:
                number = 0
            score = division_test(number, max_numerator=number * 12, questions = questions)

        elif type == MULTIPLICATION:
            if number == RANDOM:
                number = 0
            score = multiplication_test(number, questions = questions)

    print("\n{0}, you scored {1} out of {2}.".format(name, score, questions))

    # Print out the detailed results...
    if len(passed) > 0:
        print("Correct answers:")
        for a,b in passed:
            if type == MULTIPLICATION:
                answer = a*b
            else:
                # For divide need to make b the answer to the question
                answer = b
                a = a * b
                b = int(a / answer)

            print("{0} {1} {2} = {3:0.0f}".format(a,types[type],b, answer))

    if len(failed) > 0:
        print("Wrong answers:")
        for a,b in failed:
            if type == MULTIPLICATION:
                answer = a*b
            else:
                # For divide need to make b the answer to the question
                answer = b
                a = a * b
                b = int(a / answer)

            print("{0} {1} {2} = {3:0.0f}".format(a,types[type],b, answer))

    return


def multiplication_test(multiplier : int, questions : int = 10):
    # Run a multiplication based Maths Test
    # multiplier = specific times table that you want to test
    # multiplier = 0 is a random times table test between 2 and 12.

    # Cap the number of questions to be 11
    questions = min(questions, 11)

    global passed
    global failed

    score = 0

    print("Starting the multiply by {0} test with {1} questions...".format(multiplier, questions))
    input()

    # Loop asking the set number of questions in the test
    for i in range(1,questions + 1):

        loop = True

        # Select a question that has not yet been passed
        while loop is True:

            if multiplier == 0:
                a = random.randint(2,12)
            else:
                a = multiplier

            b = random.randint(2,12)

            # If we have not already passed this combination the we are good to ask this question
            if (a,b) not in passed:
                loop = False

        question = (a,b)

        # Randomly reverse the questions to make it harder
        if random.randint(0,10) > 5:
            a,b = b,a

        print("Question {0}: What is {1} x {2}?".format(i,a,b))

        # Get the user to enter a valid number
        good = False
        while good is False:
            answer = input("Answer=")
            answer = is_numeric(answer)
            if answer is not None:
                good = True
            else:
                print("Not a number, try again.")

        # Now see if they were correct
        correct_answer = a*b

        if answer == correct_answer:
            print("*** Correct ***")
            score += 1
            passed.append(question)
        else:
            print("Wrong !!!  The correct answer is {0} x {1} = {2}".format(a,b,correct_answer))
            failed.append(question)

        input()

    return score

def division_test(divisor : int, max_numerator : int = 144, questions : int = 10, ):
    # Run a division based maths test
    # divisor = 0 means random test with a random divisor between 2 and 12
    # max_numerator - the biggest number that you want to test as the numerator
    # questions - how many questions do you want to set

    global passed
    global failed

    score = 0

    if divisor != 0 :
        # Cap the number of questions tha we can test
        questions = min(questions, max_numerator // divisor - 1)
        print("Starting the divide by {0} division test with {1} questions...".format(divisor, questions))
    else:
        print("Starting the random division test with {0} questions...".format(questions))

    passed = []
    failed = []
    b = divisor

    # Loop asking the set number of questions in the test
    for i in range(1, questions + 1):

        loop = True
        if max_numerator == 0:
            max_numerator = 144

        while loop is True:

            # Pick a random divisor (b)
            if divisor == 0:
                b = random.randint(2,12)

            # Pick a random numerator (a)  based on divisor and max numerator
            max_answer = max_numerator // b
            a = random.randint(2, max_answer) * b

            # If we have not already passed this combination the we are good to ask this question
            if (a, b) not in passed:
                loop = False

        question = (a, b)

        print("\nQuestion {0}: What is {1} / {2}?".format(i, a, b))

        # Loop until we get a valid numerical answer from the user
        good = False
        while good is False:
            answer = input("Answer = ")
            answer = is_numeric(answer)
            if answer is not None:
                good = True
            else:
                print("Not a number, try again.")

        # See if the user got the answer correct...
        correct_answer = a / b

        if answer == correct_answer:
            print("*** Correct ***")
            score += 1
            passed.append(question)
        else:
            print("Wrong !!!  The correct answer is {0} / {1} = {2:.0f}".format(a, b, correct_answer))
            failed.append(question)


        input()

    return score

import logging, sys, time


def confirm(question : str):
    '''confirm() - Function to ask the user a simple Yes/No confirmation and return a boolean'''

    choices = ["Yes", "No"]

    while True:
        print(question)
        for i in range(0, len(choices)):
            print("%i. %s" % (i+1, choices[i]))
        choice = input("Choice?")
        if is_numeric(choice) and int(choice) > 0 and int(choice) <= (len(choices)):
            break
        else:
            print("Invalid choice.  Try again!")

    return (int(choice) == 1)


def pick(object_type: str, objects: list, auto_pick: bool=False):
    '''pick() -  Function to present a menu to pick an object from a list of objects
    auto_pick means if the list has only one item then automatically pick that item'''

    selected_object = None
    choices = len(objects)
    vowels ="AEIOU"
    if object_type[0].upper() in vowels:
        a_or_an = "an"
    else:
        a_or_an = "a"

    # If the list of objects is no good the raise an exception
    if objects is None or choices == 0:
        raise(Exception("No %s to pick from." % object_type))

    # If you selected auto pick and there is only one object in the list then pick it
    if auto_pick is True and choices == 1:
        selected_object = objects[0]

    # While an object has not yet been picked...
    while selected_object == None:

        # Print the menu of available objects to select
        print("Select %s %s:-" % (a_or_an, object_type))

        for i in range(0, choices):
            print("\t%i) %s" % (i + 1, str(objects[i])))

        # Along with an extra option to cancel selection
        print("\t%i) Cancel" % (choices + 1))

        # Get the user's selection and validate it
        choice = input("%s?" % object_type)
        if is_numeric(choice) is not None:
            choice = int(choice)

            if 0 < choice <= choices:
                selected_object = objects[choice -1]
                logging.info("pick(): You chose %s %s." % (object_type, str(selected_object)))
            elif choice == (choices + 1):
                raise (Exception("You cancelled. No %s selected" % object_type))
            else:
                print("Invalid choice '%i' - try again." % choice)
        else:
            print("You choice '%s' is not a number - try again." % choice)

    return selected_object


def is_numeric(s):

    try:
        x = int(s)
    except:
        try:
            x = float(s)
        except:
            x = None
    return x

if __name__ == "__main__":
    main()