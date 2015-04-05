import random
userChoice = raw_input("is rock, paper or a scissors? ")
choices = ["rock", "paper", "scissors"]
computerChoice = random.choice(choices)
if computerChoice == userChoice:
     print "Computer choice was " + computerChoice
     print "Your choice was " + userChoice
     print "The result is a tie"
elif computerChoice == "rock":
     if userChoice == "paper":
         print "Computer choice was " + computerChoice
         print "Your choice was " + userChoice
         print "You win, computer lost"
     else:
         print "Computer choice was " + computerChoice
         print "Your choice was " + userChoice
         print "Computer wins, you lost"
elif computerChoice == "scissors":
     if userChoice == "paper":
         print "Computer choice was " + computerChoice
         print "Your choice was " + userChoice
         print "Computer wins, you lost"
     else:
         print "Computer choice was " + computerChoice
         print "Your choice was " + userChoice
         print "You win, computer lost"
elif computerChoice == "paper":
    if userChoice == "rock":
         print "Computer choice was " + computerChoice
         print "Your choice was " + userChoice
         print "Computer wins, you lost"
    else:
         print "The computer choice was " + computerChoice
         print "Your choice was " + userChoice
         print "You wins, Computer lost"
