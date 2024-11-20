'''
Script for practicing on manipulatig lists as queues.

This scripts simulates a service desk queue, but instead of
tech questions, the user will demand you to answer math questions.

The queue begins with a certain amount of users between 0 and 3,
and the queue increases by one user within a random interneval
of time.

You must answer each question the faster you can, for the 
queue will keep up increasing. No time limit is given to 
you to answer each question, but do not take too much of
your time, or the queue will reach it's peak, and you will
be fired! LoL.

'''

import random
import time
import inputimeout
import requests
from collections import deque
from os import system
from inputimeout import inputimeout


'''
Defining datasets to increase the fun.
'''
# List of math questions
questions = {
    "What is 2 + 2?": "4",
    "What is 5 - 3?": "2",
    "What is 4 * 3?": "12",
    "What is 10 / 2?": "5",
    "What is 7 + 8?": "15",
    "What is 12 - 5?": "7",
    "What is 6 * 7?": "42",
    "What is 24 / 4?": "6",
    "What is 9 + 11?": "20",
    "What is 15 - 8?": "7",
    "What is 3 * 9?": "27",
    "What is 35 / 5?": "7",
    "What is 12 + 13?": "25",
    "What is 20 - 9?": "11",
    "What is 8 * 5?": "40",
    "What is 48 / 6?": "8",
    "What is 16 + 7?": "23",
    "What is 25 - 12?": "13",
    "What is 4 * 11?": "44",
    "What is 63 / 7?": "9",
    "What is 19 + 14?": "33",
    "What is 30 - 16?": "14",
    "What is 9 * 6?": "54",
    "What is 72 / 8?": "9",
    "What is 23 + 18?": "41",
    "What is 38 - 15?": "23",
    "What is 7 * 10?": "70",
    "What is 56 / 7?": "8",
    "What is 28 + 29?": "57",
    "What is 45 - 22?": "23",
    "What is 12 * 4?": "48",
    "What is 80 / 10?": "8",
    "What is 37 + 16?": "53",
    "What is 50 - 28?": "22",
    "What is 6 * 9?": "54",
    "What is 90 / 9?": "10",
    "What is 42 + 19?": "61",
    "What is 65 - 37?": "28",
    "What is 11 * 7?": "77",
    "What is 105 / 15?": "7",
    "What is 51 + 26?": "77",
    "What is 72 - 48?": "24",
    "What is 8 * 9?": "72",
    "What is 112 / 14?": "8",
    "What is 64 + 32?": "96",
    "What is 85 - 57?": "28",
    "What is 10 * 6?": "60",
    "What is 120 / 12?": "10",
    "What is 73 + 24?": "97",
    "What is 98 - 69?": "29",
    "What is 13 * 5?": "65",
    "What is 130 / 10?": "13",
    "What is 87 + 11?": "98",
    "What is 100 - 33?": "67",
    "What is 9 * 12?": "108",
    "What is 144 / 12?": "12",
    "What is 99 + 1?": "100",
    "What is 110 - 45?": "65",
    "What is 15 * 4?": "60",
    "What is 120 / 8?": "15",
    "What is 102 + 3?": "105",
    "What is 125 - 55?": "70",
    "What is 16 * 3?": "48",
    "What is 100 / 4?": "25",
    "What is 107 + 12?": "119",
    "What is 130 - 65?": "65",
    "What is 11 * 11?": "121",
    "What is 144 / 9?": "16",
    "What is 115 + 17?": "132",
    "What is 140 - 70?": "70",
    "What is 12 * 10?": "120",
    "What is 150 / 10?": "15"
}

# List of people in the queue
def get_random_user():
    num_names = 1
    response = requests.get(f"https://randomuser.me/api/?results={num_names}")
    if response.status_code == 200:
        data = response.json()
        names = [person["name"]["first"] for person in data["results"]]
        return names
    else:
        return []


# Creates a queue of users with questions and answers
def make_queue(num_users):
  queue = deque([])
  for _ in range(num_users):
      names = get_random_user()
      if names:
          name = names[0]
          question = random.choice(list(questions.keys()))
          answer = questions[question]
          queue.append({"name": name, "question": question, "answer": answer})

  return queue

# Adds a new user to the queue
def add_user_to_queue(queue):
  names = get_random_user()
  if names:
      name = names[0]
      question = random.choice(list(questions.keys()))
      answer = questions[question]
      queue.append({"name": name, "question": question, "answer": answer})

  return queue

def pick_user(queue):
    return queue.popleft()


'''

---
 User name 1
 User name 2
 ...
 User name 10
---

Max limit of 10 users in queue. When it reaches 10, the game will be over.
The queue will be shown in a 12x3 matrix filled by spaces, except
for que dashes on top and bottom to mark the limits of the queue.

Each time a user arrives in the queue the console will be cleared
and the exhibition will be refreshed, showing another user name
in the queue matrix.
'''
def show_queue(queue, message='\0'):
    system("clear")
    print("-" * 12)
    matrix = [[" " for _ in range(3)] for _ in range(12)]
    i = 11
    for user in queue:
        matrix[i][0] = user["name"]
        i -= 1
    for row in matrix:
        print(" ".join(row))
    print("-" * 12)
    print(message)

def main():

    # Choose the initial number of users in the queue
    initial_users = random.randint(0, 3)
    # Create the queue
    queue = make_queue(initial_users)
    # Show the initial queue
    show_queue(queue)
    # Keep track of whether the game is over
    game_over = False
    # Keep track of the number of users in the queue
    num_users = initial_users
    while not game_over:

        # Controls the flow of users pickups
        answered = False
        # Wait for a random amount of time
        time.sleep(random.uniform(1, 5))
        # Add a new user to the queue
        queue = add_user_to_queue(queue)
        # Update the number of users
        num_users += 1
        # Show the updated queue
        show_queue(queue)
        # Check if the game is over
        if num_users >= 10:
            game_over = True
            system('clear')
            print("Game Over! You're fired.")
        else:

            # Pick a user from the queue
            user = pick_user(queue)
            user_name = user['name']
            user_question = user['question']

            while not answered:

                # Show the updated queue
                show_queue(queue)

                # Ask the user the question
                print(f"Question for {user_name}: {user_question}")

                try:
                    # Get the answer from the user
                    answer = inputimeout(prompt="Your answer: ", timeout=random.uniform(1, 5))

                    # Check if the answer is correct
                    if answer == user['answer']:
                        print("Correct!")
                        answered = True
                        time.sleep(2)
                    else:
                        print("Incorrect!")
                        time.slepp(2)

                except Exception:
                    # Add a new user to the queue
                    queue = add_user_to_queue(queue)
                    num_users += 1



if __name__ == "__main__":
    main()