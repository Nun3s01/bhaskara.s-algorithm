#   Quadratic algorithm
import cmath, math;

valueA = float(input("What is the value of 'a'? "))
valueB = float(input("What is the value of 'b'? "))
valueC = float(input("What is the value of 'c'? "))

delta = (valueB**2) - (4*valueA*valueC)

if (delta == 0):
    x1 = int((-valueB + math.sqrt(delta)) / (2*valueA))
    print(f"Δ = {int(delta)} \nWith the only real root being: {x1}")
else:
    if (delta < 0):
        delta = (valueB**2) - (4*valueA*valueC)
        x1 = (-valueB + cmath.sqrt(delta)) / (2*valueA)
        x2 = (-valueB - cmath.sqrt(delta)) / (2*valueA)
        print(f"Δ = {int(delta)} \nWith the roots being: {x1} e {x2} \n(Δ < 0 there are no real roots)")
    else:
        x1 = int((-valueB + math.sqrt(delta)) / (2*valueA))
        x2 = int((-valueB - math.sqrt(delta)) / (2*valueA))
        print(f"Δ = {int(delta)} \nWith the roots being: {x1} e {x2}")
        
