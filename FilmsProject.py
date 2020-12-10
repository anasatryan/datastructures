import json
from Deque import Deque
from HashSet import HashSet


#welcome message
def welcoming():
    print("           Welcome to our MovieHub")
    print("       Please write the name of the movie you want to find")

#providing message of choices
def askingToChoose(desiredMovie):
    print("   We have found something for you")
    print("  What do you want to know about " + desiredMovie + "?")
    print("1. Director")
    print("2. Year of premiere")
    print("3. Short description of movie")
    print("4. Genres")
    print("0. To skip")

# Determining the choice of the user
def determineTheChoice(desiredMovie,movieList):
    choice = input()
    while choice != "0":

        if (choice == "1"):
            print(movieList[desiredMovie]["director"])
        if (choice == "2"):
            print(movieList[desiredMovie]["year"])
        if (choice == "3"):
            print(movieList[desiredMovie]["description"])
        if (choice == "4"):
            print(movieList[desiredMovie]["genre"])

        choice = input()

# Determining whether to add movie in favourite list or not
def addingToFavTen(desiredMovie,favouriteTen):
    print('   Do you wanna add this movie to your top 10 movies list?')

    answer = input()

    if (answer == 'Yes'):
        favouriteTen.addLast(desiredMovie)

# Printing user's favourite movies
def printingFavMovies(favouriteTen):
    print('   Here are your favourite movies!!!')
    favouriteTen.printDeq()


def menu(movieSet,movieList,favouriteTen):
    welcoming()
    desiredMovie=input()
    while desiredMovie!='Please add it':
        if movieSet.contains(desiredMovie):

            askingToChoose(desiredMovie)

            determineTheChoice(desiredMovie,movieList)

            addingToFavTen(desiredMovie,favouriteTen)

        else:
            print ("Sorry, we could not find it")

        desiredMovie=input()

    printingFavMovies(favouriteTen)

def main():
    # Creating HashSet
    movieSet=HashSet(100)

    # Creating the list that will have all movies
    with open('movieList.json')as data_file:
        movieList = json.load(data_file)

    # Adding movies to HashSet
    for movie in movieList:
        movieSet.add(movie)

    favouriteTen=Deque(10)
    menu(movieSet,movieList,favouriteTen)

main()
