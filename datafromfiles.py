
q_file = open("questions.txt", "r")
q = [line.strip() for line in q_file.readlines()]
q_file.close()
n = 0
for i in q:
    q1, a1 = i.split("=")
    a = input(f"{q1}=")
    if a == a1:
        n += 1
m = len(q)
print(f"Your final score is {n}/{m}")
