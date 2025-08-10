def grade_in_words(grade: float) -> str:
    return "Fail" if grade < 3 else "Poor" if grade < 3.5 else "Good" if grade < 4.5 else "Very Good"if grade < 5.5 else "Excellent"


grade = float(input())

print(grade_in_words(grade=grade))
