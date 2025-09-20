# grade_evaluator.py

def grade_evaluator():
    # Ask the user for input
    name = input("Enter your name: ")
    score = float(input("Enter your score (0-100): "))

    # Assign grades
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    # Print the result
    print(f"Student: {name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    grade_evaluator()
