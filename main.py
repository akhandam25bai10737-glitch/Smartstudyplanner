print("Welcome to Smart Study Planner")

subjects = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    name = input(f"Enter subject {i+1} name: ")
    difficulty = int(input("Enter difficulty (1-5): "))
    days_left = int(input("Days left for exam: "))

    subject = {
        "name": name,
        "difficulty": difficulty,
        "days_left": days_left
    }

    subjects.append(subject)

print(subjects)






















































