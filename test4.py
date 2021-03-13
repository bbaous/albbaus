from random import seed,random,randint,randrange,sample
#Total number of tickets to be drawn
LotteryTickets=10
#Number of my tickets
NumberOfLotteries=1
#Number of  winning tickets
LotteryTicketsPicked=10
#Number of lotter draws
LotteryDraws=100
#A random regerator returning  pseudorandom set numbers within a specific range  
def randomGenerator(rangeNumbers, returnNumbers):
     return [randrange(1, rangeNumbers, 1) for i in range(returnNumbers)]
#Compare my ticket with the drawn winning lotteries
def draw(lotteryDaw,MyLottery):
	print ("The lottery draw : " +  str(lotteryDaw))
	print ("Your lottery is   : " +  str(MyLottery))
	if MyLottery[NumberOfLotteries-1] in lotteryDaw:
		return True
	return False
#Select my random ticket, draw the winning lotteries for "LotterDraws" times and compare
#the results
for draws in range(0,LotteryDraws,1):
	print ("Draw number %d and result is %s " \
		%((draws+1),draw(randomGenerator(LotteryTickets, LotteryTicketsPicked),\
			randomGenerator(LotteryTickets, NumberOfLotteries))))