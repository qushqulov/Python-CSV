f = open("students.csv", "r")
lines = f.readlines()
f.close()

lines = lines[1:]

students = []

for line in lines:
    line = line.strip()
    name, score = line.split(",")
    students.append({
        "name": name,
        "score": int(score)
    })

for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i]["score"] < students[j]["score"]:
            students[i], students[j] = students[j], students[i]

f = open("rating.csv", "w")
f.write("rank,name,score\n")

rank = 1
for student in students:
    f.write(f"{rank},{student['name']},{student['score']}\n")
    rank += 1

f.close()
