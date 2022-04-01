print("Welcome to the Love Calculator!")
name1 = input("What is your full name?\n")
name2 = input("What is their full name?\n")
combine_names = name1 + name2
lower_case_str = combine_names.lower()
t = lower_case_str.count("t")
r = lower_case_str.count("r")
u = lower_case_str.count("u")
e = lower_case_str.count("e")
true = t + r + u + e
l = lower_case_str.count("l")
o = lower_case_str.count("o")
v = lower_case_str.count("v")
e = lower_case_str.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))

if love_score > 90 or love_score < 10:
    print(f"Your score is {love_score}, you go together like coke and mentos!")
if love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together!")
else:
    print(f"Your score is {love_score}!")



    