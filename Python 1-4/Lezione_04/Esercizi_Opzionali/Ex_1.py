'''1. School Grading System:
    ∙ Create a function that takes a student's name and their scores in different subjects as input.
    ∙ The function calculates the average score and prints the student's name, average, and a message indicating
      whether the student passed the exam (average >= 60) or failed.
    ∙ Create a for loop to iterate over a list of students and scores, calling the function for each student.
'''

def average_score(name: str, scores: dict[str, int]):
    result = 0
    for grade in scores.values():
        result += grade
    
    result /= len(scores.values())
    
    print(f"{name} averaged {result}.", end = " ")
    if result >= 60:
        print(f"{name} has passed the exam =D")
    else:
        print(f"Sadly {name} could not pass the exam :(")

students: dict[str, dict[str, int]] = {}

students["Mark"] = {
    "Math" : 90,
    "History" : 69,
    "Informatics" : 100,
    "Litterature" : 62
    }

students["Lisa"] = {
    "Math" : 38,
    "History" : 83,
    "Informatics" : 62,
    "Litterature" : 79
}

students["Alex"] = {
    "Math" : 77,
    "History" : 84,
    "Informatics" : 96,
    "Litterature" : 74
    }

students["Sharon"] = {
    "Math" : 34,
    "History" : 61,
    "Informatics" : 54,
    "Litterature" : 72
}

for k, v in students.items():
    average_score(k, v)
    print("\n")