import random

print("Welcome to the Star Generator!")
print("----------------")

def generate_question():
    num_1 = random.randint(0,20)
    num_2 = random.randint(0,20)
    num_3 = random.randint(0,20)
    num_4 = random.randint(0,20)
    num_5 = random.randint(0,20)
    print("What is",num_1,"x",num_2,"-",num_3,"+",num_4,"-",num_5,"?")
    num_array = [num_1,num_2,num_3,num_4,num_5]
    return num_array

def check(num_1,num_2,num_3,num_4,num_5):
    ans_user = int(input("Answer: "))
    print("")
    ans_comp = num_1 * num_2 - num_3 + num_4 - num_5

    if ans_user == ans_comp:
        status = "Correct"
    else:
        status = "Wrong"
    return status

def main():
    points = 0
    for i in range(0,10):
        print("Question",i + 1)
        num_array = generate_question()
        status = check(num_array[0], num_array[1], num_array[2], num_array[3], num_array[4])
        if status == "Correct":
            points = points + 1
    print("You got",points,"questions correct")
    print("------------------")

    if points == 10:
        print("Great job! You earned THREE stars :D")
    elif points >= 7 and points <= 9:
        print("Good job! You earned TWO stars :)")
    elif points >= 5 and points <= 6:
        print("Not bad! You earned ONE star :]")
    else:
        print("Better luck next time! You get no stars :(")


main()
