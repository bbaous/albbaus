from random import seed,random,randint,randrange,sample
LotteryTickets=10
numberOfLotteries=1
LotterTicketsPicked=10
LotterDraws=10

def randomGenerator2(rangeNumbers, returnNumbers):
     return [randrange(1, rangeNumbers, 1) for i in range(returnNumbers)]

def draw(lotteryDaw,MyLottery):
	#print ("The lottery draw : " +  str(lotteryDaw))
	#print ("Your lottery is   : " +  str(MyLottery))
	if MyLottery[numberOfLotteries-1] in lotteryDaw:
		print (True)
	else:
		print (False)
 
for draws in range(1,LotterDraws,1):
	print ("Draw number %d" %(draws+1))
	draw(randomGenerator2(LotteryTickets, LotterTicketsPicked),randomGenerator2(LotteryTickets, numberOfLotteries))