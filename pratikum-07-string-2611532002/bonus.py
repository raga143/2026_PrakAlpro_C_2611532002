# Name: <Raga Mohammad Aidil Fitra>
# NIM: <2611532002>
# Question bonus

sentence = input("Sentence: ")
s = sentence.replace(" ", "").lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")