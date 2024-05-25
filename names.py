import csv_runner

# name = input("Whats your name ? ")
#
# with open("names.txt", "a") as file:
#         file.write(f"{name}\n")
#
# with open("names.txt","r") as file:
#         for line in sorted(file):
#             print("Hey,", line.rstrip())

students = []

with open("students.csv") as file:
    reader = csv_runner.DictReader(file)
    for row in reader:
        students.append({"name":row["Name"],"house":row["House"]})

for student in sorted(students,key=lambda student:student["name"]):
    print(f"{student['name']} is from {student['house']}")
