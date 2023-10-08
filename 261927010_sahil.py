FLIGHTS_FILE = "flightdetails.txt" 

#--------------------------------------  BOOKING  -------------------------------------------
def load_flights():

  flights = []
  with open(FLIGHTS_FILE, "r") as f:
    for line in f:
      airline = line.split(",")[0]  
      seats = line[1:].replace(" '", "").replace("'", "").split(",", 1)[1]
      seats = seats.strip()[1:-1].split("],")
      seats = [s.replace('[', '').strip() for s in seats]
      seats = [s.split(",") for s in seats]
      flights.append([airline, seats])

  return flights
#---------------------------------------------------------------------------------------------
def save_flights(flights):
  
  with open(FLIGHTS_FILE, "w") as f:  
    for flight in flights:
      airline = flight[0]
      seats = str(flight[1])
      f.write(f"{airline},{seats}\n")

#----------------------------------------------------------------------------------------------
def display_flights():
  
  flights = load_flights()

  print("AVAILABLE FLIGHTS:")
  for i, flight in enumerate(flights):
    print(f"\t{i+1}. {flight[0]}")

#-----------------------------------------------------------------------------------------------
def book_flight():

  flights = load_flights()
  
  print("Available flights:")

  for i, flight in enumerate(flights):
    print(f"{i+1}. {flight[0]}")

  choice = int(input("Enter flight number to book: "))
  chosen_flight = flights[choice-1]

  name = input("Enter passenger name: ")

  if has_availability(chosen_flight):
    row = get_available_row(chosen_flight)
    col = get_available_col(chosen_flight)  
    book_seat(chosen_flight, row, col, name)


    print(f"Booking seat {row},{col} for {name}")
    book_seat(chosen_flight, row, col, name)

    print("Flight booked!")
  else:
    print("Sorry, flight is full!")

  save_flights(flights)

#..................................................
def has_availability(flight):
  seats = flight[1]

  for row in seats:
    for seat in row:
      if seat == "*":
        return True
  
  return False

#..................................................
def get_available_row(flight):

  seats = flight[1]

  for i, row in enumerate(seats):
    for seat in row:
      if seat == "*":
        if i < len(seats):
          return i
  
  print("Error: No available rows")
  return None

#..................................................
def get_available_col(flight):

  seats = flight[1] 
  row = get_available_row(flight)

  for i, seat in enumerate(seats[row]):
    if seat == "*":
      return i
  
  return None
#..................................................
def book_seat(flight, row, col,name):

  seats = flight[1]

  # Validate row and column
  if 0 <= row < len(seats):
    if 0 <= col < len(seats[row]):

      # Update seat to X  
      seats[row][col] = "X"

      print(f"Seat ({row}, {col}) booked for {name}!")
      print(f"Booking: {name}, {flight[0]}, {row}, {col}")

    else:
      print(f"Invalid column {col} for row {row}")
  else:
    print(f"Invalid row {row}")


#----------------------------------   CANCEL  ---------------------------------------------
def cancel_booking():

  flights = load_flights()

  print("Enter booking to cancel:")
  name = input("Passenger name: ")
  flight_number = int(input("Flight number: "))
  row = int(input("Row number: "))
  col = int(input("Column number: "))

  flight = flights[flight_number-1]
  seats = flight[1]

  if 0 <= row < len(seats) and 0 <= col < len(seats[row]):
    seat = seats[row][col]
    if seat == "X":
      seats[row][col] = "*"
      print("Booking canceled successfully!")
      save_flights(flights)
    else:
      print("Invalid booking details!")
  else:
    print("Invalid row or column!")

###########################################  ADMIN  ###########################################
def aHomescreen():
  print()
  print("Welcome to ADMIN MENU")
  print("1. Add flight")
  print("2. Modify flight") 
  print("3. Remove flight")
  print("4. Exit")
  
  choice = int(input("Enter choice: "))

  if choice == 1:
    add_flight()
  elif choice == 2:
    modify_flight()
  elif choice == 3: 
    remove_flight()
  elif choice == 4:
    pass
  else:
    print("Invalid choice")

#--------------------------- ADD ----------------------
def add_flight():

  flights = load_flights()

  airline = input("Enter airline name: ")
  rows = int(input("Enter number of rows: "))
  cols = int(input("Enter number of columns: "))

  # Create new flightseats matrix
  seats = []
  for r in range(rows):
    row = []
    for c in range(cols):
      row.append("*")
    seats.append(row)

  # Add new flight to list
  new_flight = [airline, seats]
  flights.append(new_flight)

  # Save updated flights
  save_flights(flights)

  print("New flight added successfully!")

#------------------------- MODIFY -----------------------------------
def modify_flight():
  
  flights = load_flights()

  print("AVAILABLE FLIGHTS")
  display_flights()

  flight_number = int(input("Enter flight number to modify: "))

  if flight_number > 0 and flight_number <= len(flights):

    flight = flights[flight_number-1]

    print("1. Modify airline")
    print("2. Modify seats")
    choice = int(input("Enter choice: "))

    if choice == 1:
      new_airline = input("Enter new airline name: ")
      flight[0] = new_airline
    elif choice == 2:
      rows = int(input("Enter number of rows: "))
      cols = int(input("Enter number of columns: "))

      # Create new seats matrix
      seats = []
      for r in range(rows):
        row = []
        for c in range(cols):
          if r < len(flight[1]) and c < len(flight[1][0]):
            row.append(flight[1][r][c])
          else:
            row.append("*")
        seats.append(row)

      flight[1] = seats
    
    print("Flight modified successfully!")
    save_flights(flights)

  else:
    print("Invalid flight number!") 

#-------------------------- REMOVE ----------------------------------
def remove_flight():

  flights = load_flights()

  print("AVAILABLE FLIGHTS") 
  display_flights()

  flight_number = int(input("Enter flight number to remove: "))

  if flight_number > 0 and flight_number <= len(flights):
    
    confirmation = input("Are you sure you want to remove this flight (y/n)? ")
    
    if confirmation.lower() == 'y':
      flight = flights.pop(flight_number-1)
      print(f"Flight {flight_number} removed")
      save_flights(flights)

  else:
    print("Invalid flight number!")

###########################################  USER  ###########################################
def uHomescreen():
    file1 = open('flightdetails.txt', 'a')
    file1.close()
    file2 = open("flightdetails.txt", 'r')
    readData = file2.readlines()
    file2.close()
    if readData == []:
        save_flights([["a", [["row1", "*", "*", "*", "*", "*"], ["row2", "*", "*", "*", "*", "*"], ["row3", "*", "*", "*", "*", "*"]]],["b", [["row1", "*", "*", "*", "*", "*"], ["row2", "*", "*", "*", "*", "*"]]]])

    print("WELCOME USER:")
    print("\t1. Book a Ticket")
    print("\t2. Cancel a Booking")
    print("\t3. Show Flights")
    userchoice = int(input("ENTER THE CORRESPONDING NUMBER: "))
    if userchoice == 1:
      book_flight()
    elif userchoice == 2:
      cancel_booking()
    elif userchoice == 3:
      display_flights()
    else:
      print("Invalid Entery!")
#################################### LOGIN #####################################
username = 'user'
password = '123'

ADMIN_USER = "admin"  
ADMIN_PASS = "456"

while True:
    userinp = input("USERNAME: ")
    userpass = input("PASSWORD: ")
    if userinp == username and userpass == password:
        print("Admin Login successful!")
        uHomescreen()
        break
    elif userinp == ADMIN_USER and userpass == ADMIN_PASS:
      print("Admiin Login successful!")
      aHomescreen()
      break
    else:
        print("INVALID CREDENTIALS!\nTRY AGAIN!\n")
