print ("Fibonacci sequence:")
# first two terms
n1, n2 = 0, 1
nth=0
stopCondition=1000
#Perform a while true loop until my main variable n1 becomes 
# greater than the stopCondition and print the last Fibonacci number and 
while True:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    #Break id n1 is bigger than stopCondition and print the last nunmber
    if n1>stopCondition:
       print(n1)
       break