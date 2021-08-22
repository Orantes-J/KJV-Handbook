# imports
import csv 

# inputs for client side
chapter_question = "Which book would you like to read from?: "
verse_question = "Which verse would you like me to pick from?In roman numerals please: "


# creating csv for bible verses
header = ['chapter', 'verse', 'scripture']
rows = [
    {
        'chapter':'genesis',
        'verse': 1.5,
        'scripture':'And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.'
    },
    {
        'chapter':'genesis',
        'verse': 1.6,
        'scripture':'And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.'
    },
    {
        'chapter':'genesis',
        'verse':1.7,
        'scripture':'And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so.'
    },
    {
        'chapter':'genesis',
        'verse':1.8,
        'scripture':'And God called the firmament Heaven. And the evening and the morning were the second day.'
    }
]

with open('bible_verses.csv', "a", newline='') as b:
    script = csv.DictWriter(b, fieldnames=header)
    script.writeheader()
    script.writerows(rows)


# with open("bible_verses" "r") as i:
    
# book_input = input(chapter_question).lower()
# verse_input = input(verse_question).upper()

# print(user_input)
# print("\n")
# print("*"*50)
# bible_verse = {
#     'joab': {1:"get blessed", 2:"stay lifted"}
# }

# print(bible_verse['joab'][2])
# print("*" * 50)
# print("\n")

# if user_input == "joab":
#     print("Here you go ")