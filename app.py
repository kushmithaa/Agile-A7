# Student Management and Academic Performance System

students = [
    {
        "id": 101,
        "name": "Arun",
        "marks": [85, 90, 78]
    },
    {
        "id": 102,
        "name": "Priya",
        "marks": [92, 88, 95]
    },
    {
        "id": 103,
        "name": "Rahul",
        "marks": [76, 81, 79]
    }
]


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"


print("Student Management and Academic Performance System")
print("==================================================")

for student in students:
    average = calculate_average(student["marks"])
    grade = calculate_grade(average)

    print("Student ID:", student["id"])
    print("Student Name:", student["name"])
    print("Marks:", student["marks"])
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("-----------------------------------")
