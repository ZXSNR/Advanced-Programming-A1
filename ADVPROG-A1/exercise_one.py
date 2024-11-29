import random

def displayMenu():
    print("DIFFICULTY")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")
    choice = input("Choose your difficulty level (1-3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid input. Please choose between 1, 2, or 3.")
        choice = input("Choose your difficulty level (1-3): ")
    return int(choice)

def randomInt(level):
    if level == 1:
        return random.randint(1, 9)  
    elif level == 2:
        return random.randint(10, 99)  
    elif level == 3:
        return random.randint(1000, 9999)  

def decideOperation():
    return '+' if random.choice([True, False]) else '-'

def displayProblem(num1, num2, operation):
    print(f"{num1} {operation} {num2} = ", end='')
    try:
        answer = int(input())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    return answer

def isCorrect(num1, num2, operation, answer):
    correct_answer = num1 + num2 if operation == '+' else num1 - num2
    return answer == correct_answer

def displayResults(score):
    print("\nYour final score:", score)
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    print(f"Your grade: {grade}")

def playQuiz():
    level = displayMenu()
    score = 0
    for i in range(10):
        num1 = randomInt(level)
        num2 = randomInt(level)
        operation = decideOperation()
        
        answer = displayProblem(num1, num2, operation)
        if answer is None:
            continue 

        if isCorrect(num1, num2, operation, answer):
            print("Correct!")
            score += 10
        else:
            print("Incorrect. Try again.")
            
            answer = displayProblem(num1, num2, operation)
            if answer is None:
                continue
            
            if isCorrect(num1, num2, operation, answer):
                print("Correct!")
                score += 5
            else:
                print("Incorrect again. Next question.")
    
    displayResults(score)
    return input("Play again? (yes/no): ").lower() == 'yes'

def main():
    while playQuiz():
        print("\nStarting a new quiz...\n")
    print("Hope you had fun, see you again!")

if __name__ == "__main__":
    main()
