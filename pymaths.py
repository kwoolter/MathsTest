import random

def main():
    print("Welcome to the Maths Test!")
    name = input("What is you name?")
    input("OK {0} - press Enter to start the test.".format(name))

    score = 0
    questions = 10
    passed = []
    failed = []

    for i in range(1,questions + 1):

        loop = True

        while loop is True:

            a = random.randint(2,12)
            b = random.randint(2,12)

            if (a,b) not in passed and (b,a) not in passed:
                loop = False

        print("Question {0}: What is {1} x {2}?".format(i,a,b))

        good = False
        while good is False:
            answer = input("Answer=")
            answer = is_numeric(answer)
            if answer is not None:
                good = True
            else:
                print("Not a number, try again.")

        if answer == (a*b):
            print("*** Correct ***")
            score += 1
            passed.append((a,b))
        else:
            print("Wrong !!!  The correct answer is {0} x {1} = {2}".format(a,b,a*b))
            failed.append((a,b))

        input()


    print("\nEnd of the Maths Test\n{0}, you scored {1} out of {2}".format(name, score, questions))
    print("Correct answers:")
    for a,b in passed:
        print("{0} x {1} = {2}".format(a,b, a*b))

    print("Wrong answers:")
    for a,b in failed:
        print("{0} x {1} = {2}".format(a,b, a*b))



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