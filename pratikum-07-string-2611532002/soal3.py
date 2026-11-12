# Name: <Raga Mohammad Aidil Fitra>
# NIM: <2611532002>
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])



text = "Raga Mohammad Aidil Fitra"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)
