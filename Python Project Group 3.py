
# 1.	Displays a list of snacks and drinks with item numbers and prices.

items= {
   1: ('chips', 1),
   2: ('pepsi', 1.5),
   3: ('donut', 2),
   4: ('coca-cola', 1.3),
   5: ('popcorn', 2.5)
}
selected_items =[]
total_price =0
print('print snacks in list =>', items)

#ii.	Ask the user to choose items by number in a loop.
for item_no, (name, price) in items. items():
    print(f'{item_no}. {name} ${price}')



print()
while True:
    user_choice= input('enter item number or done :')
    if user_choice.lower()=='done':
        break
    items_no= int(user_choice)
    
    if items_no in items:
        name, price = items[items_no]
        selected_items.append((name,price))
        total_price = total_price + price
        print(f' added {name}, -->${price}')
    else:
        print('invalid item number')

print('total_price',' =', '$',total_price)

print()
print('=='*10)
print(     'Receipt')
print('=='*10)
for name, price in selected_items:
    print(name, price)
print('=='*10)
print(f'Total_costs:   ${total_price}')
print('=='*10)



# 2)	Write a program that:
# •	Has a predefined dictionary of groceries with prices.
# •	Lets the user "add" items by typing their names.
# •	For each valid item, asks for the quantity.
# •	Keeps adding to the cart until the user types "checkout".
# •	Displays a final bill: each item, quantity, subtotal, and total.


groceries = {
     "milk":3.5,
     "eggs":6,
     "bread":7,
     "butter":10,
     "apple":8,
     "tomato":6

}

total=0
#item_total = 0

for key,value in groceries.items():
       print(f"{key}:${value}")

while True:
   grocery = (input("enter items you want to buy(checkout to quit):"))
   
   if grocery == "checkout":
        break
   
   if grocery in groceries:   
        quantity = int(input("how many:"))   
        price=groceries.get(grocery)
        item_total=price*quantity
        total += item_total
        print(f"you selected {quantity} {grocery}")
   else:
        print("you entered invalid item")
print()
print(f"your total is {total}$")



4.Movie Ticket Booking Simulation
a. Simulate a movie theater booking system that:

b. Shows a list of available movie titles, showtimes, and seat prices.

c. Asks the user to choose a movie and number of tickets.

d. Confirms total price and asks if they want to book another movie.

e. Ends when they say "no" and displays total bookings and cost.

movies = {
    1: {"title": "David", "showtime": "11:00 AM", "price": 10},
    2: {"title": "Mario Brothers", "showtime": "2:00 PM", "price": 15},
    3: {"title": "Spiderman", "showtime": "5:00 PM", "price": 12},
    4: {"title": "Utopia", "showtime": "8:00 PM", "price": 10}
}

total_cost = 0
total_tickets = 0

booked_movies = []
counts = []
costs = []

print("Welcome to the Movie Theater")

while True:
    print("\nAvailable Movies:")
    for key, movie in movies.items():
        print(f"{key}. {movie['title']} | Showtime: {movie['showtime']} | Price: ${movie['price']}")
    while True:
        choice = input("\nEnter movie number: ").strip()

        if not choice.isdigit():
          print("Please enter a valid number.")
          continue

          num = int(choice)

          if 1 <= num <= len(movies):
            movie = movies[num]

        tickets = int(input("Enter number of tickets: "))

        booking_cost = tickets * movie["price"]

        print(f"Total price: ${booking_cost}")

        booked_movies.append(movie)
        counts.append(tickets)
        costs.append(booking_cost)

        total_cost += booking_cost
        total_tickets += tickets

    else:
        print("Invalid movie selection!")
        continue

    another = input("\nDo you want to book another movie? (yes/no): ").lower()

    if another == "yes":
        continue
    elif another == "no":
        break
    else:
        print("Invalid entry. Exiting.")
        break

print("\nBooking Summary")
for i in range(len(booked_movies)):
    print(f"\nMovie: {booked_movies[i]['title']}")
    print(f"Showtime: {booked_movies[i]['showtime']}")
    print(f"Tickets: {counts[i]}")
    print(f"Cost: ${costs[i]}")

print("\n-- Booking Completed --")
print(f"Total Tickets Booked: {total_tickets}")
print(f"Total Cost: ${total_cost}")
print("Thank you for booking with us!")

#question 5
# Create a basic quiz game that:
# •	Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
# •	Ask the user each question and records their answers.
# •	At the end, displays:
# o	 The user's score (e.g., 7/10)
# o	Correct answers for any questions they got wrong


correct_answer={}
score=0
questions=[
    {"question":"what is the capital city of ethiopia", "answer":"addis ababa"},
    {"question":"what is the capital city of turkey", "answer":"ankara"},
    {"question":"what is the capital city of eriteria", "answer":"asmara"},
    {"question":"what is the capital city of kenya", "answer":"nairobi"},
    {"question":"what is the capital city of Gana", "answer":"akra"},
]

for i in questions:
    user_answer = input(i["question"])
    if user_answer==i["answer"]:
        print("correct")
        score=score+1

    else:
        print("wrong")
        correct_answer=i["answer"]
        print(f" the correct answer for this question is {correct_answer}")
y=(len(questions))
print(f"your score is {score}/{y}")

6.You receive log records: logs = [ {"user": "alice", "action": "login"}, {"user": "bob", "action": "login"}, {"user": "alice", "action": "purchase"}, {"user": "", "action": "login"}, {"user": "charlie", "action": None}, {"user": "bob", "action": "logout"} ]
Build a program that: • Remove invalid records where: o user is empty OR o action is missing (None) o Count actions per user (dictionary) o Count frequency of each action (dictionary) o Cleaned record count o User activity summary o Most common action

Expected Output Cleaned Records: 4

User Activity: { "alice": 2, "bob": 2, "charlie": 0 }

Action Counts:

logs = [
    {"user": "alice", "action": "login"},
    {"user": "bob", "action": "login"},
    {"user": "alice", "action": "purchase"},
    {"user": "", "action": "login"},
    {"user": "charlie", "action": None},
    {"user": "bob", "action": "logout"}
]


user_activity={}  #stores number of action per users 
cleaning_logs=[]   #record only valid records
action_counts={}   #stores frequency of each action   

    
for log in logs:
    user=log['user']
    action =log['action']

    if user != '' and user not in user_activity:
        user_activity[user]=0
    
    if user == '' or action is None:
        continue
 
    cleaning_logs.append(log)   #only take the valid records
   
    if user in user_activity:
        user_activity[user]= user_activity[user] +1
    else:
        user_activity[user]=1


    if action in action_counts:                     #counting the each action
         action_counts[action] = action_counts[action]+1
    else:
        action_counts[action]=1

Most_common_action= max(action_counts, key=action_counts.get)

print('user_activity :', user_activity)


print('cleaning_records:', len(cleaning_logs))
#print(cleaning_logs)


print('number of action records: ', action_counts)

print('most common action: ', Most_common_action)
user_activity : {'alice': 2, 'bob': 2, 'charlie': 0}
cleaning_records: 4
number of action records:  {'login': 2, 'purchase': 1, 'logout': 1}
most common action:  login