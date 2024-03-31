import csv

product_dictionary = {}

with open("products.csv", "request.csv") as infile:
    
    will_read = csv.reader(infile)

    next(will_read)

    for row in will_read:
        code = row(0)
        product = row(1)
        price = row(2)