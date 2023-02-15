import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bidders = {}
print(logo)
print("\nWelcome to the secret auctioning program\n")

while True:
    name = input("Name of bidder: ")
    bid = int(input("Your bid is : $"))
    bidders[name] = bid

    more_bidders = input("Anyone else bidding? (yes/no) ")
    os.system('cls')
    if more_bidders == "no":
        break

max = 0
winner = 0

for bidder in bidders:
    if bidders[bidder] > max:
        max = bidders[bidder]
        winner = bidder


print(f"The winner is {winner} with ${max}")