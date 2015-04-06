import random
userChoice = raw_input("is rock, paper or a scissors? ")
choices = ["rock", "paper", "scissors"]
computerChoice = random.choice(choices)
if computerChoice == userChoice:
     print "Computer choice was " + computerChoice +"\n"\
     + "Your choice was " + userChoice + "\n" + "The result is a tie"
elif computerChoice == "rock":
     if userChoice == "paper":
         print "Computer choice was " + computerChoice + "\n"\
          + "Your choice was " + userChoice + "\n" + "You win, computer lost"
     else:
         print "Computer choice was " + computerChoice + "\n"\
          + "Your choice was " + userChoice + "\n" + "Computer wins, you lost"
elif computerChoice == "scissors":
     if userChoice == "paper":
        print "Computer choice was " + computerChoice + "\n"\
          + "Your choice was " + userChoice + "\n" + "Computer wins, you lost"
     else:
          print "Computer choice was " + computerChoice + "\n"\
          + "Your choice was " + userChoice + "\n" + "You win, computer lost"
elif computerChoice == "paper":
    if userChoice == "rock":
         print "Computer choice was " + computerChoice + "\n"\
         + "Your choice was " + userChoice + "\n" + "Computer wins, you lost"
    else:
          print "The computer choice was " + computerChoice + "\n"\
         + "Your choice was " + userChoice + "\n" + "You wins, Computer lost"
