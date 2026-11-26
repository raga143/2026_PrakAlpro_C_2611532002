schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

busiest = ""
most = 0
for day, courses in schedule.items():
    if len(courses) > most:
        busiest = day
        most = len(courses)
print(f"Busiest day: {busiest} ({most} courses)")

course = input("Course: ")
count = 0
for day, courses in schedule.items():
    if course in courses:
        count += 1
print(f"{course}: {count} days")