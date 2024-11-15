# Joshua Phillips
# 11/15/24
# Making a function for asking single questions
import time

def ask_question(question, answer):
    user_answer = input(question + ' ')
    if user_answer.lower() == answer.lower():
        return True
    else:
        return False
    
# Function to run quiz

def run_quiz():
    questions = [
        ("What is the capital of North Korea?", "Payongyang"),
        ("What is roughly four times the size of our Earth?", "Uranus"),
        ("What is the decible level of a quit room?", "Thirty"),
        ("How many rodent hairs are in the average peanut butter jar?", "Ten")
    ]

# Loop through questions
    score = 0
    for q in questions:
        if ask_question(q[0], q[1]):
            print('Correct')
            score += 1
        else:
            print('Incorrect answer!')


# Claculatew THe score average
    print(f'\nYour final score is: {score}/{len(questions)}')
    percentage = (score / len(questions)) * 100
    print(f'You scored: {percentage:.1f}%')
    time.sleep(2)
    print('Goodbye!')

    # Main funtion to start the game
def main():
        print('Welcome to my Python Quiz Game!')
        run_quiz()

    # Start the game
if __name__ == '__main__':
    main()