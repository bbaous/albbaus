#Your task is to use the random library to help simulate a lottery competition.
#In this competition there are 10,000 tickets, each with a unique ID number. Every week there is one 
#draw, and there are 10 winners (ie. 10 winning numbers are picked).
#Each ticket is identified by a unique integer number between 1 and 10,000. In this lottery, a ticket 
#CAN win twice (unusually!), i.e. we replace a ticket back in the draw after it has been pulled out.

#a) Write a function which takes as a parameter a ticket ID number, and simulates a lottery 
#draw by picking 10 random winners, and returns True if the specified ticket is a winner, 
#and False otherwise (True and False are Boolean datatypes in Python)
#b) Use this function to simulate a million (ie. 1,000,000) lottery draws. Assume each time 
#a different ticket is purchased. How many times did you win in this simulation?
#c) Discuss the following two points:
#i. Do you think it makes a difference if the person buys a different ticket 
#number each week, or if they keep the same number for the million draws?
#(use your simulation to provide evidence to your answer if you can)
#ii. How could you improve your answer to part (b) to give you more 
#confidence in the amount of wins you would expect after a million draws?
	
# seed the pseudorandom number generator
from random import seed,random,randint,randrange

def matching(rangeNumbers, returnNumbers, matchingLottery):
	randomGenerator(1000, 10,)
	return 

def randomGenerator(rangeNumbers, returnNumbers):
    seed(1)
    for lottery in range(returnNumbers):
	    #value = randrange(10000)
	    #print(value)
	    #value = randint(0, rangeNumbers)
	    print('The winning lottery %d is %d' %(lottery+1, randint(0, rangeNumbers)))
		returnValues=['']
		returnValues.append(randint(0, rangeNumbers)) 
	    print(returnValues)
    return 0



randomGenerator(1000, 10,)