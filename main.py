import random
from os.path import exists
import sys

def writefilm(title):
    print("Ok! Adding {} to your films list.".format(title))
    with open("filmslist.txt", "a+") as file:
        file.write("{}\n".format(title))
        file.close()

def writeseries(title):
    print("Ok! Adding {} to your series list.".format(title))
    with open("serieslist.txt", "a+") as file:
        file.write("{}\n".format(title))
        file.close()

def addfilms():
    film_title = input("Ok! What is the title of the film you want to add?\n")
    verification = input("Do you want to add {} to your films list?\n".format(film_title)).lower()
    while True:
        if verification == "yes":
            writefilm(film_title)
            more = input("Do you want to add another film?\n").lower()
            while True:    
                if more == "yes":
                    addfilms()
                    break
                elif more == "no":
                    sys.exit()
                else:
                    print("Please awnser by Yes or No.")
                    more = input("Do you want to add another film?\n").lower()
                    continue
            break
        
        elif verification == "no":
            film_title = input("Ok! What is the title of the film you want to add?\n")
            verification = input("Do you want to add {} to your films list?\n".format(film_title)).lower()
            continue

        else:
            print("Please awnser by Yes or No.")
            verification = input("Do you want to add {} to your films list?\n".format(film_title)).lower()
            continue

def addseries():
    series_title = input("Ok! What is the title of the series you want to add?\n")
    verification = input("Do you want to add {} to your series list?\n".format(series_title)).lower()
    while True:
        if verification == "yes":
            writeseries(series_title)
            more = input("Do you want to add another series?\n").lower()
            while True:
                if more == "yes":
                    addfilms()
                    break
                elif more == "no":
                    sys.exit()
                else:
                    print("Please awnser by Yes or No.")
                    more = input("Do you want to add another series?\n").lower()
                    continue
            break

        elif verification == "no":
            series_title = input("Ok! What is the title of the series you want to add?\n")
            verification = input("Do you want to add {} to your series list?\n".format(series_title)).lower()
            continue

        else:
            print("Please awnser by Yes or No.")
            verification = input("Do you want to add {} to your series list?\n".format(series_title)).lower()
            continue

def whattowatch(what):
    while True:
        if what == "1":
            file_exists = exists("filmslist.txt")
            while True:
                if file_exists == False:
                    print("Please add before films in your list.")
                    break
                else:
                    break
            films_list = []
            with open("filmslist.txt", "r") as file:
                for lines in file:
                    line = lines.strip()
                    films_list.append(line)
                file.close()
            #DEBUG:
            #print(films_list)
            print(random.choice(films_list))
            break

        elif what == "2":
            file_exists = exists("serieslist.txt")
            while True:
                if file_exists == False:
                    print("Please add before series in your list.")
                    break
                else:
                    break
            series_list = []
            with open("serieslist.txt", "r") as file:
                for lines in file:
                    line = lines.strip()
                    series_list.append(line)
                file.close()
            #DEBUG:
            #print(series_list)
            print(random.choice(series_list))
            break
        
        elif what == "3":
            file_exists = exists("filmslist.txt")
            while True:
                if file_exists == False:
                    print("Please add before films AND series in your list.")
                    break
                else:
                    break
            file_exists = exists("serieslist.txt")
            while True:
                if file_exists == False:
                    print("Please add before films AND series in your list.")
                    break
                else:
                    break
            films_and_series_list = []
            with open("filmslist.txt", "r") as file:
                for lines in file:
                    line = lines.strip()
                    films_and_series_list.append(line)
                file.close()
            with open("serieslist.txt", "r") as file:
                for lines in file:
                    line = lines.strip()
                    films_and_series_list.append(line)
                file.close()
            #DEBUG:
            #print(films_and_series_list)
            print(random.choice(films_and_series_list))
            break

        else:
            print("Sorry, I don't understand. Please awnser with the numbers only.")
            global choosing_what
            choosing_what = input("\nSo? what do you want?\n")
            continue

print("\nHi, Welcome to WhatToWatch! developed by therealmarius")
print("Please select one of the options above:")
print("\n1: Add a film")
print("2: Add a series")
print("3: Choose a film/series for me")
print("4: Open my GitHub")
print("5: That's it for today. Goodbye!")

main = input("\nSo! What do you want to do?\n")

while True:
    if main == "1":
        addfilms()
        continue
    
    elif main == "2":
        addseries()
        continue
    
    elif main == "3":
        print("Ok! Let's choose What to Watch now")
        print("Do you want:\n")
        print("1: Films")
        print("2: Series")
        print("3: Both")
        choosing_what = input("\nSo? what do you want?\n")
        whattowatch(choosing_what)
        break
    
    elif main == "4":
        print("Find my GitHub at the address: https://github.com/therealmarius")
        break
    
    elif main == "5":
        sys.exit()

    else:
        print("Sorry, I don't understand. Please awnser with the numbers only.")
        main = input("\nSo! What do you want to do?\n")
        continue

    #WhatToWatch developed by therealmarius
    #Under MIT License
    #Check the GitHub Page projetc
    #https://github.com/therealmarius/What-To-Watch