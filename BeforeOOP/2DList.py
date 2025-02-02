# fruits = ['apple','banana','orange']
# vegetables = ['banana','orange']
# meats = ["chicken", "fish", "turkey"]
#
# groceries = [fruits,vegetables,meats]
#
# print(groceries[2][2])
#
# for collection in groceries:
#     print(collection)
#
#
# num_pad = ((1,2,3),
#            (4,5,6),
#            (7,8,9),
#            ("*",0,"#"))
#
# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()



######PYTHON QUIZZ GAME#########

questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

# for question, answer, guess in zip(questions, answers, guesses):
#     print(question)

for question in questions:
    print(f"Q{question_num+1}. {question}")
    for option in options[question_num]:
        print(option)
    guesses.append(input("Choose your option: ").upper())
    if guesses[question_num] == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer is: {answers[question_num]} ")
    question_num += 1
    print("--------------------------------------------------------------")


print("answers: ", end="")
for answer in answers:
    print(answer,end=" ")
print()

print(f"guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()



print(f"Your score is {int((score/ len(answers))*100)}%")
