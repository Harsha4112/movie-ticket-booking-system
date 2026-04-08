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

# simple terminal QR style pattern
def generate_sample_qr(amount):
    print("\n----- PAYMENT QR -----")
    print("Scan to pay ₹", amount)
    print()

    qr_pattern = [
        "████████████████████████",
        "██ ▄▄▄▄▄ ██ ▀ ▄ ▄▄▄▄▄ ██",
        "██ █   █ ██▄▀█ █   █ ██",
        "██ █▄▄▄█ ██ ▄ █ █▄▄▄█ ██",
        "██▄▄▄▄▄▄▄██▄█▄██▄▄▄▄▄██",
        "██ ▀▀▄ ▄▄ ▄█ ▀▄ ▄▄▀▀ ██",
        "██ █ ▄ ▄▀ ▀▄▀▄ ▀▄ ▄ ██",
        "██ ▄▄▄▄▄ ██▀▄ ▀ █▄ ██",
        "██ █   █ ██ ▄▀ ▄▄█ ██",
        "██ █▄▄▄█ ██▀ ▄ ▄▀ ██",
        "██▄▄▄▄▄▄▄██▄▄██▄▄██"
    ]

    for line in qr_pattern:
        print(line)

    print("\nUPI ID: movie@upi")
    print("Amount: ₹", amount)
    print("----------------------")

print("\nWelcome to Movie Ticket Booking\n")

# show movies
print("Available Movies:")
for m in movies:
    print(m, "-", movies[m]["name"])

# movie selection
while True:
    try:
        movie_choice = int(input("\nSelect movie number: "))
        if movie_choice in movies:
            break
        else:
            print("Invalid movie number. Try again.")
    except:
        print("Enter a valid number.")

print("\nShow Timings:")
shows = movies[movie_choice]["shows"]

for i in range(len(shows)):
    print(i+1, "-", shows[i])

# show selection
while True:
    try:
        show_choice = int(input("Select show number: "))
        if 1 <= show_choice <= len(shows):
            break
        else:
            print("Invalid show number.")
    except:
        print("Enter a valid number.")

display_seats()

# ticket count
while True:
    try:
        tickets = int(input("\nHow many tickets: "))
        if tickets > 0:
            break
        else:
            print("Enter a positive number.")
    except:
        print("Enter a valid number.")

selected = []

for i in range(tickets):

    seat = input("Enter seat (Example A1): ").upper()

    if len(seat) != 2 or not seat[0].isalpha() or not seat[1].isdigit():
        print("Invalid seat format.")
        continue

    row = ord(seat[0]) - 65
    col = int(seat[1]) - 1

    if row < 0 or row >= rows or col < 0 or col >= cols:
        print("Seat does not exist.")
        continue

    if book_seat(row, col):
        selected.append(seat)

total = ticket_price * len(selected)

print("\n----- Booking Summary -----")
print("Movie:", movies[movie_choice]["name"])
print("Show:", shows[show_choice-1])
print("Seats:", selected)
print("Total Price: ₹", total)

pay = input("\nProceed to payment? (yes/no): ").lower()

if pay == "yes":
    generate_sample_qr(total)

    confirm = input("\nAfter payment type 'done': ")

    if confirm.lower() == "done":
        print("\nPayment Successful!")
        print("Booking Confirmed")
    else:
        print("\nPayment not confirmed.")
else:
    print("\nBooking Cancelled")
