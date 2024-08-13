from wheel import Wheel

startingMoney = 100000000
numberOfGames = 100000

money = startingMoney
wheel = Wheel()
biggestFail = 0
currentFail = 0

def main(): 
    global money, currentFail, numberOfGames

    counter = 0
    
    while counter < numberOfGames and money > 0: 
        currentFail = 0
        martinGale(1)
        counter += 1 


    calculateFacts(counter, 2, 2*6*60)  




def calculateFacts(numberOfGames: int, gamePerMinute: int, gameTimePerDay: int): 
    global money, startingMoney

    minutesPlayed = numberOfGames / gamePerMinute
    days = minutesPlayed / gameTimePerDay
    hours = minutesPlayed / 60
    wage = (money - startingMoney) / hours

    print("Biggest loss streak:", biggestFail)
    print("This means playing for", days, "days")
    print("Your hourly wage was:", wage, "euros per hour")



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

