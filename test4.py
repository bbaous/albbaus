from random import seed,random,randint,randrange,sample
#Total number of tickets to be drawn
LotteryTickets=10
#Number of my tickets
numberOfLotteries=1
#Number of  winning tickets
LotterTicketsPicked=10
#Number of lotter draws
LotterDraws=100
#A random regerator returning  pseudorandom set numbers within a specific range  
def randomGenerator(rangeNumbers, returnNumbers):
     return [randrange(1, rangeNumbers, 1) for i in range(returnNumbers)]

def draw(lotteryDaw,MyLottery):
	print ("The lottery draw : " +  str(lotteryDaw))
	print ("Your lottery is   : " +  str(MyLottery))
	if MyLottery[numberOfLotteries-1] in lotteryDaw:
		return True
	return False
 
for draws in range(0,LotterDraws,1):
	print ("Draw number %d and result is %s " %((draws+1),draw(randomGenerator(LotteryTickets, LotterTicketsPicked),randomGenerator(LotteryTickets, numberOfLotteries))))