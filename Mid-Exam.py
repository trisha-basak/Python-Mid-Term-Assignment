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
        if show_id not in self.__seats:
            print(f'This {show_id} is not found.')
            return
        
        for i, j in seat_bookList: #i row || j col
            if i >= self.__rows or j >= self.__cols or i < 0 or j < 0:
                print(f"Error: Seat at {i}{j} is invalid.")
                continue
            if self.__seats[show_id][i][j] == '0':#Free
                self.__seats[show_id][i][j] = '1' #Booked
            else:
                print(f'This {i, j} seat is already booked')

    def view_show_list(self):
        # if not self.__show_list:
        #     print("No shows available.")
        #     return
        for show_id, movie_name, time in self.__show_list:
            print(f'Show ID is: {show_id}, Movie Name is: {movie_name}, Time: {time}')

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            return
        
        print(f"Available seats for show ID {show_id}:")
        for i, row in enumerate(self.__seats[show_id]):
            for j, seat in enumerate(row):
                # if seat == '0':
                print(f"Seat ({i},{j})", end='\n')
            print()

        for row in self.__seats[show_id]:
            for element in row:
                if self.__seats[show_id][i][j] == '1':
                    element = '1'
                    print(element, end=" ")
                else:
                    print(element, end=" ")
            print()

    @property
    def hall_no(self):
        return self.__hall_no

Bashundhara = Star_Cinema()
hall1 = hall(5, 6, 'Hall 1')


hall1.entry_show('S1', 'Rupkotha', '12:00 PM')
hall1.entry_show('S2', 'Rajkonna', '04:00 PM')

# print(Star_Cinema.hall_list)
# print(hall1.view_available_seats(11))
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
        # hall2.view_available_seats(showID)
    
    elif Option == '3':
        showID = input("Enter show ID: ")

        seats_to_book = []
        while True:
            row = int(input("Enter row: "))
            if row == -1:
                print('Your Seat booked')
                break
            col = int(input("Enter col: "))
            seats_to_book.append((row, col))
        hall1.book_seats(showID, seats_to_book)
        # hall2.book_seats(showID, seats_to_book)
    
    elif Option == '4':
        break
    
    else:
        print("Invalid Option. Please try again.")