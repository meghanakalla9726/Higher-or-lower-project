#display art
from art import logo,vs
from game_data import data
import random
def format_data(account):
    """user take account data and format into printable form"""
    account_name=account['name']
    account_descr=account['description']
    account_country=account['country']
    return (f"{account_name}, a {account_descr}, from {account_country}")

def check_ans(user_guess,a_followers,b_followers):
    if a_followers>b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"
print(logo)
score=0
account_b = random.choice(data)
game_should_continue=True
# make the game repeatable
while game_should_continue:
    # making the ac at positon B to postion A on next step
    account_a=account_b
    account_b=random.choice(data)

    # generate a random account from game data
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Compare B:{format_data(account_b)}")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B':").lower()
    #clear screen
    print("\n"*20)
    # check if the user is correct
    ##get follower count of each ac
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    ##use if statement to check the user is correct
    is_correct=check_ans(guess,a_followers,b_followers)

    # give user feedback on their guess
    if is_correct:
        # score keeping
        score+=1
        print(f"you are right!, your current score is {score}")
    else:
        print(f"you are wrong!, your final score is {score}")
        game_should_continue=False

