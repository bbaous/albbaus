from random import seed,random,randint,randrange,sample
#The range of the ticket number [0,LotteryTicketRange] i.e the lottery will 
# provide 10 (LotteryTicketsPicked) lotteries in the range of [0,10] 
LotteryTicketRange=10
#Number of my tickets i.e how many Lottery ticket(s) I buy
NumberOfLotteries=1
#Number of  winning tickets (exercices says 10)
LotteryTicketsPicked=10
#Number of lotter draws, ie how many times I draw the lottery and I pick 
# the LotteryTicketsPicked in the range of LotteryTicketRange
LotteryDraws=100
#Number of wins
wins=0
#A random regerator returning  a pseudorandom set of numbers within a specific range  
# ie. a. We call this to generate a lottery ticket that is the one we buy by calling this -(Line 30) 
# randomGenerator(LotteryTicketRange, NumberOfLotteries)))) were LotteryTicketRange=10 and NumberOfLotteries=1
#  b.We call this with fuinction (line 29) randomGenerator(LotteryTicketRange, LotteryTicketsPicked) with the same LotteryTicketRange=10
#   to get the winning tickets 10 (LotteryTicketsPicked)
def randomGenerator(rangeNumbers, returnNumbers):
     return [randrange(1, rangeNumbers, 1) for i in range(returnNumbers)]

#Compare my ticket with the drawn winning lotteries
#This function takes as arguments  two lists (my lottert and the winning lotteries) and checks if my lottery is 
# is "in" the winning lotteries list (line 26)
def draw(lotteryDaw,MyLottery):
	print ("The lottery draw : " +  str(lotteryDaw))
	print ("Your lottery is   : " +  str(MyLottery))
	if MyLottery[NumberOfLotteries-1] in lotteryDaw:
		return True
	return False
#Select my random ticket, draw the winning lotteries for "LotterDraws" times and compare
#the results
for draws in range(0,LotteryDraws,1):
	myLottery=randomGenerator(LotteryTicketRange, NumberOfLotteries)
	print ("Draw number %d and result is %s " \
		%((draws+1),draw(randomGenerator(LotteryTicketRange, LotteryTicketsPicked),	randomGenerator(LotteryTicketRange, NumberOfLotteries))))