import json


class Deque:
    def __init__(self, size):
        self.rear = 0
        self.front = -1
        self.size = size
        self.items = [None] * self.size

    def isFull(self):
        if ((self.front == 0 and self.rear == self.size - 1) or self.front == self.rear + 1):
            self.items *= 2

    def addFirst(self, key):
        self.isFull()
        if (self.front == -1):
            self.front = 0
            self.rear = 0
        elif (self.front == 0):
            self.front = self.size - 1
        else:
            self.front = self.front - 1

        self.items[self.front] = key

    def addLast(self, key):
        self.isFull()
        if (self.front == -1):
            self.front = 0
            self.rear = 0
        elif (self.rear == self.size - 1):
            self.rear = 0
        else:
            self.rear = self.rear + 1

        self.items[self.rear] = key

    def removeFirst(self):
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            if (self.front == self.size - 1):
                self.front = 0
            else:
                self.front = self.front + 1

    def removeLast(self):
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        elif (self.rear == 0):
            self.rear = self.size - 1
        else:
            self.rear = self.rear - 1

    def first(self):
        return self.items[self.front]

    def last(self):
        return self.items[self.rear]

    def printDeq(self):
        for favMov in self.items:
            if (favMov != None):
                print(favMov)


class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class HashSet():
    def __init__(self, capacity):
        self._hashtable = [None] * capacity
        self._capacity = capacity
        self._size = 0

    def _hash(self, element):

        # return hash(element) % self._capacity
        return ord(element[0]) % self._capacity

    def add(self, element):
        index = self._hash(element)

        if (self._hashtable[index] == None):
            self._hashtable[index] = Node(element)
        else:
            n = Node(element, self._hashtable[index])
            self._hashtable[index] = n
        self._size += 1

    def contains(self, element):
        index = self._hash(element)

        n = self._hashtable[index]
        while (n != None):
            if (n.data == element):
                return True
            n = n.next
        return False

    def remove(self, element):
        index = self._hash(element)

        n = self._hashtable[index]
        p = None
        while (n != None):
            if (n.data == element):
                if (p == None):
                    self._hashtable[index] = n.next
                else:
                    p.next = n.next
                n.next = None
                self._size -= 1
                return n
            p = n
            n = n.next
        return None

    def size(self):
        return self._size

    def print(self):
        print("printing hashset elements")

        for e in self._hashtable:
            while (e != None):
                print(e.data)
                e = e.next

    def __iter__(self):
        for e in self._hashtable:
            if (e != None):
                self._elem = e;

            break
        return self

    def __next__(self):
        if self._elem == None:
            raise StopIteration

        tmp = self._elem
        if (self._elem.next != None):
            self._elem = self._elem.next
        else:
            index = self._hash(self._elem.data)
        self._elem = None
        for i in range(index + 1, len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._elem = self._hashtable[i]
                break
        return tmp.data





# Creating HashSet
movieSet = HashSet(100)

# Creating the list that will have all movies
with open('movieList.json')as data_file:
    movieList = json.load(data_file)

# Adding movies to HashSet
for movie in movieList:
    movieSet.add(movie)

favouriteTen = Deque(10)


# welcome message
def welcoming():
    print("           Welcome to our MovieHub")
    print("       Please write the name of the movie you want to find")


# providing message of choices
def askingToChoose(desiredMovie):
    print("   We have found something for you")
    print("  What do you want to know about " + desiredMovie + "?")
    print("1. Director")
    print("2. Year of premiere")
    print("3. Short description of movie")
    print("4. Genres")
    print("0. To skip")


# Determining the choice of the user
def determineTheChoice(desiredMovie):
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
def addingToFavTen(desiredMovie):
    print('   Do you wanna add this movie to your top 10 movies list?')

    answer = input()

    if (answer == 'Yes'):
        favouriteTen.addLast(desiredMovie)


# Printing user's favourite movies
def printingFavMovies():
    print('   Here are your favourite movies!!!')
    favouriteTen.printDeq()


def menu():
    welcoming()
    desiredMovie = input()
    while desiredMovie != 'add it':
        if movieSet.contains(desiredMovie):

            askingToChoose(desiredMovie)

            determineTheChoice(desiredMovie)

            addingToFavTen(desiredMovie)

        else:
            print("Sorry, we could not find it")

        desiredMovie = input()

    printingFavMovies()


menu()