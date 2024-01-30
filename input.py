# Prompt user for words
place = input("Enter a place: ")
person = input("Enter a person's name: ")
action = input("Enter an action: ")                        emotion = input("Enter an emotion: ")
time_period = input("Enter a time period: ")

# my additional words for the story
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")                        verb1 = input("Enter a verb: ")
exclamation = input("Enter an exclamation: ").capitalize()
verb2 = input("Enter another verb: ")                      
# Display the  story with user's words                     story = f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. \"{exclamation}\" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {action} right in front of my family."
print("\nYour Extended Story:")
print(story)
