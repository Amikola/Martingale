from wheel import Wheel

startingMoney = 10000000
numberOfGames = 100000
bet = 1

money = startingMoney
wheel = Wheel()
biggestFail = 0
currentFail = 0

def main(): 
    global money, currentFail, numberOfGames, bet

    counter = 0
    
    while counter < numberOfGames and money > 0: 
        currentFail = 0
        martinGale(bet)
        counter += 1 


    calculateFacts(counter, 2, 6)  




def calculateFacts(numberOfGames: int, gamePerMinute: int, hoursPerDay: int ): 

    global money, startingMoney, bet

    minutesPlayed = numberOfGames / gamePerMinute
    days = minutesPlayed / (gamePerMinute*60*hoursPerDay)
    hours = minutesPlayed / 60
    wage = (money - startingMoney) / hours
    bankRoll = 0

    for i in range(0, biggestFail + 1): 
        bankRoll += pow(2, i)
    

    print("\n Welcome to Amikola's Martingale simulator \n")
    print("This means playing for", days, "days")
    print("Your hourly wage was:", wage, "€/h")
    print("Biggest loss streak:", biggestFail)
    print("Largets bet: ", pow(2, biggestFail), "€" )
    print("Needing bankroll: ",bankRoll, "€" )
    print("Assumptions: ")
    print("Starting bet: ", bet, "€")
    print("Hours per day played: ", hoursPerDay)
    print ("Games per minute: ", gamePerMinute)
    print("\n")



def martinGale(currentBet: int): 
    global money, biggestFail, currentFail

    if money < currentBet:  
        return

    money -= currentBet
    wheel.spinWheel()

    if wheel.winnerColor() == "RED": 
        money += currentBet * 2
    else:
        currentFail += 1
        biggestFail = max(biggestFail, currentFail)
        if money - currentBet * 2 >= 0:  
            martinGale(currentBet * 2)

main()

