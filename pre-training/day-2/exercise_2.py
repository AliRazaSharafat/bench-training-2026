school_students = [
    {
        "name": "John Doe",
        "scores": [30, 40, 50, 60, 33],
        "subject": "Maths"
    },
    {
        "name": "John Wick",
        "scores": [44, 95, 39, 88, 99],
        "subject": "Maths"
    },
    {
        "name": "John Carter",
        "scores": [66, 77, 49, 54, 67],
        "subject": "Maths"
    },
    {
        "name": "John Cena",
        "scores": [76, 33, 29, 49, 58],
        "subject": "Maths"
    },
    {
        "name": "John David",
        "scores": [64, 77, 39, 89, 59],
        "subject": "Maths"
    }
]


def calculate_average(scores):
    return sum(scores) / len(scores)


def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def class_topper(students):
    topper = students[0]
    for student in students:
        if calculate_average(student["scores"]) > calculate_average(topper["scores"]):
            topper = student
    return topper


topper_student = class_topper(school_students)

sorted_students = sorted(school_students, key=lambda s: calculate_average(s["scores"]), reverse=True)

for student in sorted_students:
    average_score = calculate_average(student["scores"])
    topper_label=""
    if topper_student["name"] == student["name"]:
        topper_label = "*** TOP ***"
    print(f' {student["name"]} | {average_score} | {get_grade(average_score)}  {topper_label} ')
