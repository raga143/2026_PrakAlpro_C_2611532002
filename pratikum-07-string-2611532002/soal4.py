# Name: <Raga Mohammad Aidil Fitra>
# NIM: <2611532002>
# Question 4

phone = "082611532002"

first_part = phone[:4]
last_part = phone[-3:]
hidden_count = len(phone) - len(first_part) - len(last_part)

masked = first_part + "*" * hidden_count + last_part
print(masked)
