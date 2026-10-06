'''
import random
player1 = input("enter your choice: rock , Paper, Scissors").lower()
computer = random.choice(['rock', 'paper', 'scissors']).lower()
print(computer)
if player1=='rock'and computer=='scissors':
    print("player1 wins")
elif player1=='scissors' and computer=='paper':
    print("player1 wins")
elif player1=='paper' and computer=='rock':
    print("player1 wins")
elif player1==computer:
    print("tie")
else:
    print("computer wins")'''

import pyqrcode
import png

link="https://www.linkedin.com/in/ch-sanjay-kumar-b13b51376/"
#now we will create a qr code for this link
qr_code=pyqrcode.create(link)
print(qr_code)
#now we need  to create image for our qr code
qr_code.png("qr_code.png", scale=10)#scale defines the size of the image

#your task is make your virtual assistant
#play RPS game
#play number guessing game
#create a qr code
#open your desired file in your system
