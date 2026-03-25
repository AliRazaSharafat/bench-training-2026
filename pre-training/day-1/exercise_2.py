def grade_classifier(score):
    if score >= 90:
        return 'Distinction'
    elif 60 <= score < 90:
        return 'Pass'
    else:
        return 'Fail'


scores = [45, 72, 91, 60, 38, 85]

for score in scores:
    print(f"Score: {score}, Grade: {grade_classifier(score)}")