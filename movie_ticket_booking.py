# Movie Ticket Booking System

movies = {
    1: {"name": "Avengers", "shows": ["10:00 AM", "2:00 PM", "6:00 PM"]},
    2: {"name": "Inception", "shows": ["11:00 AM", "3:00 PM", "8:00 PM"]},
    3: {"name": "Interstellar", "shows": ["9:00 AM", "1:00 PM", "7:00 PM"]}
}

ticket_price = 150

rows = 3
cols = 4

# create seat layout
seats = [["O" for i in range(cols)] for j in range(rows)]

def display_seats():
    print("\nSeat Layout")
    print("   1 2 3 4")
    for i in range(rows):
        print(chr(65+i), end=" ")
        for j in range(cols):
            print(seats[i][j], end=" ")
        print()

def book_seat(row, col):
    if seats[row][col] == "X":
        print("Seat already booked!")
        return False
    else:
        seats[row][col] = "X"
        return True

print("\n🎬 Welcome to Movie Ticket Booking\n")

# show movies
print("Available Movies:")
for m in movies:
    print(m, "-", movies[m]["name"])

movie_choice = int(input("\nSelect movie number: "))

if movie_choice not in movies:
    print("Invalid movie")
    exit()

print("\nShow Timings:")
shows = movies[movie_choice]["shows"]

for i in range(len(shows)):
    print(i+1, "-", shows[i])

show_choice = int(input("Select show number: "))

if show_choice < 1 or show_choice > len(shows):
    print("Invalid show")
    exit()

display_seats()

tickets = int(input("\nHow many tickets: "))

selected = []

for i in range(tickets):

    seat = input("Enter seat (Example A1): ")

    row = ord(seat[0].upper()) - 65
    col = int(seat[1]) - 1

    if row < 0 or row >= rows or col < 0 or col >= cols:
        print("Invalid seat")
        continue

    if book_seat(row, col):
        selected.append(seat.upper())

total = ticket_price * len(selected)

print("\n----- Booking Summary -----")
print("Movie:", movies[movie_choice]["name"])
print("Show:", shows[show_choice-1])
print("Seats:", selected)
print("Total Price: ₹", total)

pay = input("\nProceed to payment? (yes/no): ")

if pay.lower() == "yes":
    print("\nPayment Successful!")
    print("🎟️ Booking Confirmed")
else:
    print("\nBooking Cancelled")
