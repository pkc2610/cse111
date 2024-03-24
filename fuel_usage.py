def main():
    odo1=float(input("Enter the first odometer reading (in miles): "))

    odo2=float(input("Enter the second odometer reading (in miles): "))

    fuelamt=float(input("Enter the fuel amount (in gallons):"))

    mpg = miles_per_gallon(odo1, odo2, fuelamt)

    lp100k = lp100k_from_mpg(mpg)

    print(f"{mpg:.1f} miles per gallon")
    
    print(f"{lp100k:.2f} liters per 100 kilometers")

def miles_per_gallon(odo1, odo2, fuelamt):
    mpg = abs(odo2 - odo1) / fuelamt
    return mpg
    print(f"Your car gets {mpg} miles per gallon.")

def lp100k_from_mpg(mpg):
     lpk = (mpg * 1.609344) / 3.785
     lp100k = lpk * 100
     return lp100k
     print(f"Your car gets {lp100k} liters per 100 kilometers.")


main()