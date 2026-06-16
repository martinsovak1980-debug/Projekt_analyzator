#promenne
texts = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
"bob":"123",
"ann":"pass123",
"mike":"password123",
"liz":"pass12"
}
gap = "-"*48

attempt =0
while  attempt<3:
    username = input("Username: ")
    password = input("Password: ")
    print(gap)

    if username in users and users[username] == password:
        print("Welcome to the app, "+username.upper()+"\nWe have "+str(len(texts))+" texts to be anylyzed.")
        print(gap)
        break
    else:
       
        attempt += 1
        if attempt < 3:
            print("Try again. You have "+str(3-attempt)+" attempts left.")
        else:  
            print("Unregistered user, terminating the program..") 
            quit()  

chosen_text = input ("Enter a number btw. 1 and "+str(len(texts))+" to select stored text or 0 to input own text: ")

#not numeric sign
if not chosen_text.isnumeric():  
    print("It is not a number.")
    quit()

#invalid selection
if  1 < int(chosen_text) > len(texts):
    print("Invalid selection")  
    quit()

if int(chosen_text) == 0:   
    own_text = input("Enter your own text: ")
    texts.append(own_text)
    chosen_text = len(texts)
    print("Your text has been added to the list of texts to be analyzed."+"\nWe have "+str(chosen_text)+" texts to be anylyzed.")

# Word count
word_count = len((texts[int(chosen_text)-1]).split())
print("There are "+str(word_count)+" words in the selected text.")

# Titlecase words
word_count_upper = 0
for word in (texts[int(chosen_text)-1]).split():
    if word.istitle():
        word_count_upper += 1
print("There are "+str(word_count_upper)+" titlecase words.")
# word_count_upper = sum (1 for slovo in (texts[chosen_text-1]).split() if slovo[0].isupper())

#Uppercase words
uppercase_words = 0
for word in (texts[int(chosen_text)-1]).split():
    if word.isupper():
        uppercase_words += 1
print("There are "+str(uppercase_words)+" uppercase words.")

# Lowercase words
lowercase_words = 0
for word in (texts[int(chosen_text)-1]).split():
    if word.islower():
        lowercase_words += 1
print("There are "+str(lowercase_words)+" lowercase words.")

# Numeric words
numeric_words = 0
for word in (texts[int(chosen_text)-1]).split():
    if word.isnumeric():
        numeric_words += 1
print("There are "+str(numeric_words)+" numeric strings.")

# sum of numbers
sum_numbers = 0
for word in (texts[int(chosen_text)-1]).split():
    if word.isnumeric():
        sum_numbers += int(word)
print("The sum of all numbers " + str(sum_numbers))

#graf
print (gap)
print ("LEN|    OCCURRENCES      |NR.")
print (gap)

progress_bar_sign = "*"
words = (texts[int(chosen_text)-1]).split()
words_length = [len(word) for word in words]
max_lenght = max(words_length) if words_length else 0

for delka in range(1, max_lenght + 1):
    pocet = words_length.count(delka)
    if pocet > 0:
        graf = progress_bar_sign * pocet
        print(f"{delka:2}|{graf:<30}        |{pocet}")