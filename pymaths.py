import random
import datetime

def main():

    MULTIPLICATION = "multiplication"
    DIVISION = "division"

    print("Welcome to the Maths Test!")
    name = input("What is your name? ")

    types = {MULTIPLICATION : "x", DIVISION: "/"}
    try:
        type = pick("test type", list(types.keys()))
    except Exception as e:
        print(e)
        return

    options = []
    RANDOM = "Random Test"
    options.append(RANDOM)
    options += (list(range(2,13)))

    try:
        number = pick("test", options)
    except Exception as e:
        print(e)
        return

    if number == RANDOM:
        test_type = "random test"
    else:
        test_type = "{0} {1} test".format(number, type)

    input("OK {0} - press Enter to start the {1}.\n".format(name, test_type))

    score = 0
    questions = 5

    passed = []
    failed = []
    start_time = datetime.time()
    #print("You started the test at {0}".format(datetime.strftime("%H:%M:%S", start_time)))

    for i in range(1,questions + 1):

        loop = True

        while loop is True:

            if type == RANDOM:
                a = random.randint(1,12)
            else:
                a = number

            b = random.randint(1,12)

            # If we have not already passed this combination the we are good to ask this question
            if (a,b) not in passed:
                loop = False

        question = (a,b)

        # For multiplication randomly reverse the questions
        if type == MULTIPLICATION and random.randint(0,10) > 5:
            a,b = b,a

        # For divide need to make b the answer to the question
        if type == DIVISION:
            a_temp = a
            a = a * b
            b = a_temp

        print("Question {0}: What is {1} {2} {3}?".format(i,a,types[type],b))

        good = False
        while good is False:
            answer = input("Answer=")
            answer = is_numeric(answer)
            if answer is not None:
                good = True
            else:
                print("Not a number, try again.")

        if type == (MULTIPLICATION and answer == (a*b)) or (type == DIVISION and answer == (a/b)):
            print("*** Correct ***")
            score += 1
            passed.append(question)
        else:
            if type == MULTIPLICATION:
                correct_answer = a*b
            else:
                correct_answer = a/b

            print("Wrong !!!  The correct answer is {0} {1} {2} = {3:0.0f}".format(a,types[type],b,correct_answer))
            failed.append(question)

        end_time = datetime.time()

        input()

    #print("You finished the test at {0}.".format(datetime.strftime("%H:%M:%S", end_time)), end="")
    #elapsed = end_time-start_time
    #print("That took you {0}".format(time.strftime("%M:%S", end_time-start_time)))


    print("\nEnd of the Maths Test\n{0}, you scored {1} out of {2} in the {3}.".format(name, score, questions, test_type))
    print("Correct answers:")

    if len(passed) > 0:
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

__author__ = 'user'

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