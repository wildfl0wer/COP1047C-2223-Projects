# Trivia Challenge
# Trivia game that reads a plain text file

import sys
# contains chdir
import os

# ensures local file is read
#os.chdir("C:/Users/maide/Desktop/Trivia")

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file) 

    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome the player and get their name."""
    print("\n\t\t****************************")
    print("\n\t\tWelcome to Trivia Challenge!\n")
    print("\t\t      ", title)
    print("\t\t****************************\n")
 
def main():
    trivia_file = open_file("name_trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    questions = 0

    # get first block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
        print("\t", category)
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")
        # ensure answer is valid
        isValid = False
        while (isValid == False):
            if (answer == "1"):
                isValid = True
                break
            elif (answer == "2"):
                isValid = True
                break
            elif (answer == "3"):
                isValid = True
                break
            elif (answer == "4"):
                isValid = True
                break
            else:
                print("\nPlease enter 1, 2, 3, or 4.")
                answer = input("What's your answer?: ")


        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += 1
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score)
        input("\n\nPress enter to continue.")

        # increments question count
        questions += 1

        # get next block
        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    # calculates score percentage
    score_float = float(score)
    questions_float = float(questions)
    score_percentage = (score_float / questions_float) * 100

    print("\n\n\tThat was the last question!\n")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("\tYou're final score is", score)
    if (score == questions):
        print("\tPerfect score! Great job!")
    elif (score_percentage >= 80):
        print("\tGood job! You know your stuff!")
    elif (score_percentage >= 60):
        print("\tNot bad! Brush up on your trivia.")
    elif (score_percentage > 0):
        print("\tOuch! Better luck next time!")
        print(score, questions, (score // questions) * 100 )
    elif (score == 0):
        print("You didn't answer any questions correctly.")
        print("Well, that's statistically unlikely.")
        print("Congratulations on beating the odds...")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
 
main()  
input("\n\nPress the enter key to exit.")
