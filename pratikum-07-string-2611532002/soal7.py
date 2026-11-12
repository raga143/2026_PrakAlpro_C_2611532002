# Name: <Raga Mohammad Aidil Fitra>
# NIM: <2611532002>
# Question 7

name = "raga mohammad aidil fitra"
nim = "2611532002"

clean = name.strip()
space = clean.find(" ")
if space == -1:
    first = clean
else:
    first = clean[:space]
username = first.lower() + nim[-3:]

line = "=" * 30
print(line)
print(f"{'STUDENT CARD':^30}")
print(line)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: 20{nim[:2]}")
print(line)