from random import randrange
#The range of the ticket number [0,LotteryTicketRange] i.e the lottery will 
# provide 10 (LotteryTicketsPicked) lotteries in the range of [0,10] 
LotteryTicketRange=100
#Number of my tickets i.e how many Lottery ticket(s) I buy
NumberOfLotteries=1
#Number of  winning tickets (exercices says 10)
LotteryTicketsPicked=10
#Number of lotter draws, ie how many times I draw the lottery and I pick 
# the LotteryTicketsPicked in the range of LotteryTicketRange
LotteryDraws=100
#Number of wins
wins=0
#Whether we wish to keep the same lottery number or not to each draw
SameLottery=True

#A random regerator returning  a pseudorandom set of numbers within a specific range  
# ie. a. We call this to generate a lottery ticket that is the one we buy by calling this -(Line 26) 
# randomGenerator(LotteryTicketRange, NumberOfLotteries)))) were LotteryTicketRange=10 and NumberOfLotteries=1
#  b.We call this with function (line 27) randomGenerator(LotteryTicketRange, LotteryTicketsPicked) with the same LotteryTicketRange=10
#   to get the winning tickets 10 (LotteryTicketsPicked)
def randomGenerator(rangeNumbers, returnNumbers):
     return [randrange(1, rangeNumbers, 1) for i in range(returnNumbers)]

#Select my lottery number
myLottery=randomGenerator(LotteryTicketRange, NumberOfLotteries)

# Having selected my ticket, draw the winning lotteries for "LotterDraws" times and 
# compare the results
for draws in range(1,LotteryDraws,1):
	#If I need a new lottery number on each draw I can set SameLottery=False above
	#We assume the same lottery for each draw
	if (SameLottery!=True):
		myLottery=randomGenerator(LotteryTicketRange, NumberOfLotteries)
	winningLotteries=randomGenerator(LotteryTicketRange, LotteryTicketsPicked)
	print ("The lottery draw : " +  str(myLottery))
	print ("Your lottery is  : " +  str(winningLotteries))
	#Compare my ticket with the drawn winning lotteries
	if myLottery[NumberOfLotteries-1] in winningLotteries:
		wins+= 1
		print ("------------You win-------------")
	print("Number of wins : "+str(wins) +" from "+str(LotteryDraws)+ " draws")
