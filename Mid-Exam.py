class Star_Cinema:
    __hall_list =[]

    def entry_hall(self, hall):
        self.__hall_list.append(hall)

    @classmethod
    def hall_list_show(clas):
        return clas.__hall_list

class hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().entry_hall(self)
    
    def  entry_show(self, show_id, movie_name, time):
        showInfo = (show_id, movie_name, time)
        self.__show_list.append(showInfo)

        seatManagement = [['0' for i in range(self.__rows)]
                      for i in range(self.__cols)]
        self.__seats[show_id] = seatManagement
    
    def book_seats(self, show_id, seat_bookList):
        for i, j in seat_bookList: #i row || j col
            if i >= self.__rows or j >= self.__cols or i < 0 or j < 0:
                print(f"Error: Seat at {i}{j} is invalid.")
                continue
            if self.__seats[show_id][i][j] == '0':#Free
                self.__seats[show_id][i][j] = '1' #Booked
                print('Your Seat booked')
            else:
                print(f'This {i, j} seat is already booked')

    def view_show_list(self):
        for show_id, movie_name, time in self.__show_list:
            print(f'Show ID is: {show_id}, Movie Name is: {movie_name}, Time: {time}')

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            return

        print(f"Available seats View:")
        for i, row in enumerate(self.__seats[show_id]):
            for j, element in enumerate(row):
                if self.__seats[show_id][i][j] == '1':
                    element = '1'
                    print(element, end=" ")
                else:
                    print(element, end=" ")
            print()
    
    def checkID(self, id):
        if id not in self.__seats:
            print(f'This {id} is not found.')
            return False
        return True

    @property
    def hall_no(self):
        return self.__hall_no

Bashundhara = Star_Cinema()
hall1 = hall(5, 6, 'Hall 1')


hall1.entry_show('S1', 'Rupkotha', '12:00 PM')
hall1.entry_show('S2', 'Rajkonna', '04:00 PM')

while True:
    print("1. View all shows today")
    print("2. View available seats in show")
    print("3. Book tickets")
    print("4. Exit")
    Option = input("Enter Option: ")

    if Option == '1':
        for i in Star_Cinema.hall_list_show():
            print(f"Hall No: {i.hall_no}")
            i.view_show_list()
    
    elif Option == '2':
        showID = input("Enter show ID: ")
        hall1.view_available_seats(showID)
    
    elif Option == '3':
        showID = input("Enter show ID: ")
        val = hall1.checkID(showID)
        seats_to_book = []
        if val == False:
            continue
        N = int(input('Enter the number of seat that you want to book: '))
        while N:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            seats_to_book.append((row, col))
            N -= 1
        hall1.book_seats(showID, seats_to_book)
    
    elif Option == '4':
        break
    
    else:
        print("Invalid Option. Please try again.")
