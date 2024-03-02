import math
from datetime import datetime

w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = (math.pi * (w**2) * a * ((w*a) + (2540 * d))) / 10000000000

print(f"The approximate volume is {v:.2f} liters")

with open("volumes.txt", "at") as f:
    now_date = datetime.now(tz=None)
    print(f"{now_date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}", file=f)