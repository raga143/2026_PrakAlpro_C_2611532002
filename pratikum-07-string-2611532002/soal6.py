# Name: <Raga Mohammad Aidil Fitra>
# NIM: <2611532002>
# Question 6

full_name = "Raga Mohammad Aidil Fitra"
nim = "2611532002"

print("Full Name:", full_name.strip())
print("NIM:", nim)

clean_full_name = full_name.strip()
space = clean_full_name.find(" ")
if space != -1:
    first_name = clean_full_name[:space]
else:
    first_name = clean_full_name

username = first_name.lower() + nim[-3:]
print("Username:", username)
