from random import seed,random,randint,randrange,sample
LotteryTickets=10000
nummberOfLotteries=1
LotterTicketsPicked=10
LotterDraws=100000

def randomGenerator2(rangeNumbers, returnNumbers):
     return [randrange(1, rangeNumbers, 1) for i in range(returnNumbers)]

def draw(lotteryDaw,MyLottery):
	#print ("The lottery draw : " +  str(lotteryDaw))
	#print ("Your lottery is   : " +  str(MyLottery))
	if MyLottery[nummberOfLotteries-1] in lotteryDaw:
		print (True)
	else:
		print (False)
 
for draws in range(1,LotterDraws,1):
	print ("Draw number %d" %draws)
	draw(randomGenerator2(LotteryTickets, LotterTicketsPicked),randomGenerator2(LotteryTickets, nummberOfLotteries))