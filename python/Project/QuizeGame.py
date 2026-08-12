questions = [
    "What is the capital city of Brazil?",
    "Which of the following processes is an example of a chemical change?",
    "What is the longest river in the world?",
    "Which planet in our Solar System is the largest and is classified as a gas giant?",
    "Who was the first human to travel into space?",
    "What type of bond is formed when electrons are shared between two atoms?",
    "Who was the mastermind behind the Kot Massacre and the founder of the 104-year-long autocratic Rana regime?",
    "How many days does Earth take to orbit the Sun?",
    "What is the smallest ocean in the world",
    "In what year was the first iPhone released?"
]

options = [
    ["a) Kathmandu", "b) Rio de Janeiro", "c) London", "d) Kyiv"],
    ["a) Melting Ice", "b) Boiling Water", "c) Burning Wood", "d) Breaking a glass"],
    ["a) Nile River", "b) The Amazon River", "c) The Yangtze River", "d) Mississippi-Missouri River system"],
    ["a) Earth", "b) Saturn", "c) Neptune", "d) Jupiter"],
    ["a) Albert Einstein", "b) Yuri Gagarin", "c) Neil Armstrong", "d) Alan Shepard"],
    ["a) Iconic bond", "b) Metallic bond", "c) Covalent bond", "d) Hydrogen bond"], 
    ["a) Mathabar Singh Thapa", "b) Junga Bahadur Rana", "c) Bhimsen Thapa", "d) Chandra Shamsher"], 
    ["a) 366", "b) 465", "c) 365", "d) 145"], 
    ["a) Pacifi Ocean", "b) Arctic Ocean", "c) Atlantic Ocean", "d) Indian Ocean"], 
    ["a) 2003", "b) 2007", "c) 2000", "d) 1995"]
]

answers = answers = ["b", "c", "a", "d", "b", "c", "b", "c", "b", "b"]

score = 0

for i, question in enumerate(questions):
    print("\n" + question)

    for option in options[i]:
        print(option)

    answer = input("Your answer: ").lower()

    if answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz Finished.")
print("Your Score:", score, "/", len(questions))