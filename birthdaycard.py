print("Good day! What's your name?")

name = input("Tell me your name: ")

print(f"Hello hello hello {name}, are you curious about whom you interact with? Give me a name!")

senders_name = input("I guess it's: ")
print(f"Bingo! You're right. I'm {senders_name}, nice meeting you!")

print("Alright, what year were you born in?")
year = int(input("I was born in: "))
year_sum= 2023 - year

print("Grand! We're going to make a birthday card. So tell me, what would you say to future you for the very special day?")
personalized_content = input("Let's started, contents will be added onto the card:  ")


print(f"Hey {name}, let's celebrate your {year_sum} years of awareness!")
print(f"Wishing you a day filled with joy and laughter as you turn {year_sum}!")
print(f"{personalized_content}")
# grinning squinting face
print("\U0001F606")

print(f"With love and best wishes,")
print(f"{senders_name}")