import cmath, math;

def InputData ():
    valueA = float(input("What is the value of 'a'? "))
    valueB = float(input("What is the value of 'b'? "))
    valueC = float(input("What is the value of 'c'? "))
    PrintRoots(valueA, valueB, valueC)

def delta (valueA, valueB, valueC):
    return ((valueB**2) - (4*valueA*valueC))

def PrintRoots(valueA, valueB, valueC):
    resultDelta = delta(valueA, valueB, valueC)
    if (resultDelta == 0):
        x1 = int((-valueB + math.sqrt(resultDelta)) / (2*valueA))
        print(f"Δ = {int(resultDelta)} \nWith the only real root being: {x1}")
    else:
        if (resultDelta < 0): 
            x1 = (-valueB + cmath.sqrt(resultDelta)) / (2*valueA)
            x2 = (-valueB - cmath.sqrt(resultDelta)) / (2*valueA)
            print(f"Δ = {int(resultDelta)} \nWith the roots being: {x1} e {x2} \n(Δ < 0 there are no real roots)")
        else:
            x1 = int((-valueB + math.sqrt(resultDelta)) / (2*valueA))
            x2 = int((-valueB - math.sqrt(resultDelta)) / (2*valueA))
            print(f"Δ = {int(resultDelta)} \nWith the roots being: {x1} e {x2}")



#    <-!->  Algorithm activation  <-!->
InputData()
