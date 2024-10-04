name = input("Type your name:")
print("Hello", name, "welcome to this adventure!")

answer = input("You are on a dirt road it has come to an end, you can go either left or right. Which way whould you like to go? Type left or right: ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around or swim to swim accross: ")

    if answer == "swim":
        print("You swam accross and were eaten by a shark.")

    elif answer == "walk":
        print("You walked for many miles and lost the game.")

    else:
        print("Not a valid option. You loose. ")


elif answer == "right":
    answer = input("You come to a clif, you can try to corss a wobbly brigde or climb down. Type cross to cross the bridge or climb to climb down")

    if answer == "cross":
        print("You tried to cross the bridge but the bridge was old and broke. You loose.")

    elif answer =="climb":
        print("You safely climb down. Congraz you won!")

    else:
        print("Not a valid option. You loose. ")
    
else:
    print("Not a valid option. You loose. ")

print("Thank you for trying", name,)

    
    