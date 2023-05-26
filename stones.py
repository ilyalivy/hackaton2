import random
import api
import db


p1 = 10
p2 = 10

print("HELLO! THIS IS ---- SOUPER SECRET GAME ----")
print("\nYou are a Chef's Intern in one of the best 2 Michelin Stars Paris restaurant.\nYou decide to play a game with a Chef. And if he loses, he provides you with one\nof his best secret recipes! So, go ahead and start collect your first book of great recipes!")
print("\nEach player has 10 stones. Both players take several stones in their hand, squeeze\nit, and then stretch it forward. The player who owns the right to move must guess the number\nof stones in the second player’s hand - 1 or 2. If he guesses correctly, he takes as many\nstones from the second player as he himself holds. And vice versa - if he does not guess, he\ngives as many stones as he has in his hand. The winner is the one who ends up with 20 stones.")

while p1 > 0 and p2 > 0:
    print(f"\nYou have {p2} stone(s) and Chef has {p1} stone(s)\n")
    print("Chef's turn...")
    print("Chef has made a bet.")
    bet1 = random.randint(1, min(p1, p2))

    while True:
        try:
            choice2 = int(input("How many stone(s) do you put in your hand? 1 or 2: "))
            if choice2 != 1 and choice2 != 2:
                raise ValueError
            break
        except ValueError:
            print("Invalid input.")

    turn1 = random.randint(0, 1)
    if turn1 == 0:
        print("Chef says that you have 2 stones in your hand.")
    else:
        print("Chef says that you have 1 stone in your hand.")

    if choice2 % 2 == turn1:
        print("Chef won!")
        p2 -= bet1
        p1 += bet1
    else:
        print("You won!")
        p2 += bet1
        p1 -= bet1

    print(f"Chef's bet was {bet1} stone(s)\n")

    if p1 > 0 and p2 > 0:
        print(f"You have {p2} stone(s) and Chef has {p1} stone(s)\n")
        print("Your turn...")

        while True:
            try:
                bet2 = int(input("Make your bet: "))
                if bet2 < 1 or bet2 > p2 or bet2 > p1:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. You can enter number from range of stones you have and not more than Chef has.")

        while True:
            try:
                turn2_num = int(input("How many stones does Chef have in his hand - 1 or 2?: "))
                if turn2_num != 1 and turn2_num != 2:
                    raise ValueError
                break
            except ValueError:
                print("Invalid Input.")


        choice1 = random.randint(1, 2)
        turn2 = -1
        if turn2_num == 1:
            turn2 = 0
        elif turn2_num == 2:
            turn2 = 1

        print(f"Chef has {choice1} stone(s) in his hand")

        if choice1 % 2 == turn2:
            print("Chef won!")
            p2 -= bet2
            p1 += bet2
        else:
            print("You won!")
            p2 += bet2
            p1 -= bet2

if p1 <= 0:
    print("Congratulations! You won the game!")
    print("Here's your recipe!")
    print(f"It's a wonderful {api.recipe[0]}, that you can cook like a professional chef. Enjoy - {api.recipe[1]}")

    save_to_table = f"""
        INSERT INTO my_recipes (date_added, name, url)
        VALUES (now(), '{api.recipe[0]}','{api.recipe[1]}')
        """
    db.cursor.execute(save_to_table)

    db.connection.commit()
    db.cursor.close()
    db.connection.close()
    print(f"The {api.recipe[0]} was successufully added to your book of great recipes!")

else:
    print("Sorry, You lost the game")