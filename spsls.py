import random

def number_to_name(number):
    #
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return None
    
        
    
    
    
def name_to_number(name):
    
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name =="lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return None
    
def rpsls(name):
    
    computer = random.randrange(0,4)
    player = name_to_number(name)
    computer_rpsls = number_to_name(computer)
    print "computer's rpsls = %s" % computer_rpsls
    print "player's rpsls = %s" % name
    score = computer - player
    if score == 1 or score == 2:
        print "computer win \n "
    elif score == 0:
        print "All win"
    else:
        print "player win \n"
 
    return 0

rpsls("spock")
rpsls("rock")
#print number_to_name(0)


