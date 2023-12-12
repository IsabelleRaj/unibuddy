"""
This is a Python program designed to act as a personalised ChatBot called 
'UniBuddy' to help first-year students transition smoother into University.
Unibuddy offers personalised responses and aims to answer frequently asked 
questions (FAQ).
"""

# Initialise message for first time starters
print('''
Welcome to UniBuddy! I hope I make your first-year journey a bit easier to navigate! :)
      
> Please enter your credentials to get started!:  
''')

# Request and store user inputs
# Create personalised responses based on inputs
name = input("> May I have the pleasure of knowing your name?: ").capitalize()
print(f"Hi {name}!")

while True:
    try:
        age = int(input("> What is your age?: "))
    except ValueError:
        print("That's not a number :/")
    else:
        break

if age < 18:
    print(f"Oh wow! {age} is such a young age to be starting university! :O")
elif 25 < age <= 35:
    print(f"Oh, {age} is a little older than I expected. :O")
elif age > 35:
    print("Nice, it's never too old to go to university!")
else:
    print(f"{age} is a nice age to be going to university!")

# Responses based on their favourite colour
fav_colour = (input("> Okay, one last question. Favourite colour!? GO!: ")).upper()

if fav_colour == 'BLUE':
    print("""Omg! Blue is my favourite colour too! What a coincidence! :D
\nHere's a few society and club suggestions based on your choice:
1. Swimming club
2. Stargazing society
3. Bird watching society
""")

elif fav_colour == 'RED':
    print("""Red! That's a nice colour.
\nHere's a few society and club suggestions based on your choice:
1. Vampire club
2. Anatomy practice club
3. Crime show society
""")

elif fav_colour == 'YELLOW':
    print("""I like yellow too. Though, blue is my favourite :)
\nHere's a few society and club suggestions based on your choice:
1. Baking club
2. Beach volleyball club
3. Pikachu appreciation society
""")

elif fav_colour == 'GREEN':
    print("""I like green too. Though, blue is my favourite :)
\nHere's a few society and club suggestions based on your choice:
1. Gardening club
2. Shrek appreciation society
3. Golf club
""")

elif fav_colour == 'PURPLE':
    print("""Oh purple. Not bad.
\nHere's a few society and club suggestions based on your choice:
1. Roller skating club
2. Ube cooking society
3. Purple hiking club
""")

else:
    print(f"{fav_colour}, i'm not sure that was a colour you have entered, please try again.")

# Responses based on their age
if age < 18:
    print("""Here are some fresher events you might be interested in that are under 18s friendly:
1. Board game cafe session
2. Wing hopping (instead of pub/bar hopping :D)
3. Movie night
4. BBQ night
""")

else:
    print("""Here are some fresher events you might be interested in:
1. Pub hopping
2. Themed nightclubs
3. Board game cafe session
""")

# Add the FAQ questions and answers stored in text files to a list

faq_questions = []
faq_answers = []

with open("Portfolio/unibuddy_faq.txt","r", encoding="utf-8") as file_in:
    for lines in file_in:
        lines = lines.strip('\n').split()
        lines = " ".join(lines)
        faq_questions.append(lines)

with open("Portfolio/unibuddy_faq_answers.txt","r", encoding="utf-8") as file_in:
    for lines in file_in:
        lines = lines.strip('\n').split()
        lines = " ".join(lines)
        faq_answers.append(lines)

# Display FAQ questions and request user input
print("Welcome to the frequently asked questions (FAQ) section!\nHere is the list of questions: \n")
for index, question in enumerate(faq_questions, start = 1):
    print(f"{index}. {question}")

while True:
    user_input = input("\nChoose the number of the question (enter 'q' to quit): ").lower()

    if user_input == 'q':
        print("Thank you for using Unibuddy! See you later! :)")
        break

    if not user_input.isdigit():
        print("Error: You did not enter a number or 'q' to quit. Please try again.")

    else:
        user_choice = int(user_input)

        if user_choice not in range(1, len(faq_questions) + 1):
            print("Error: You did not enter a valid number. Please try again.")
        else:
            print(f"You chose question {user_choice}. Here is your answer: {faq_answers[user_choice-1]}")
