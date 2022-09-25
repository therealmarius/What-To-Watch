import random
from os.path import exists
import sys

print("Hi, Welcome to WhatToWatch!")
print("Please select one of the options above:")
print("1: Add a film")
print("2: Choose a film for me")
main = input("So! What do you want to do?\n")
while True:
    if main == "1":
        film_title = input("Ok! What is the title of the film you want to add?\n")
        verification = input("Do you want to add {} to your films list?\n".format(film_title)).lower()
        while True:
            if verification == "yes":
                print("Ok! Adding {} to your films list.".format(film_title))
                with open("filmslist.txt", "a+") as file:
                    file.write("{}\n".format(film_title))
                    file.close()
                break
            elif verification == "no":
                film_title = input("Ok! What is the title of the film you want to add?\n")
                verification = input("Do you want to add {} to your films list?\n".format(film_title)).lower()
                continue

            else:
                print("Please awnser by Yes or No.")
                verification = input("Do you want to add {} to your films list?\n".format(film_title)).lower()
                continue
        break
    
    elif main == "2":
        print("Ok! Let's choose what to watch now")
        file_exists = exists("filmslist.txt")
        while True:
            if file_exists == False:
                print("Please add before films in your list.")
                sys.exit()
            else:
                break
        films_list = []
        with open("filmslist.txt", "r") as file:
            for lines in file:
                line = lines.strip()
                films_list.append(line)
            file.close()
        print(films_list)
        print(random.choice(films_list))
        break
    else:
        print("Sorry, I don't understand. Please awnser with the numbers only.")
        main = input("So! What do you want to do?\n")
        continue