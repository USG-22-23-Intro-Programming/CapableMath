def main():
    #Currency Converter
    cur = int(input("Please enter which type of currency you have. Choose from the list: 1. United States Dollar 2. European Euro 3. Chinese Yuan 4. Turkish Lira"))
    currency = {1 :  1, 2 : 0.99, 3 : 7.29, 4 : 18.62}
    curr = float(currency.get(cur))
    amount = float(input("Please enter how much money you have."))
    total = amount / curr
    con = int(input("Please enter which type of currency you would like to convert to. Choose from the list: 1. United States Dollar 2. European Euro 3. Chinese Yuan 4. Turkish Lira"))
    conv = float(currency.get(con))
    total2 = conv * total
    print(total2)

    #Grocery List
    grocerylist = {"apple" : 1.50, "orange" : 1.00, "banana" : 1.00, "bagel" : 1.25,"cabbage" : 1.50,"spinach" : 4.25,"milk" : 2.75,"eggs" : 3.25,"cake" : 8.00,"pasta" : 3.50}
    x = [str(item) for item in input("You Have Purchased: ").split(',')]
    res = 0
    for i in x:
       res = res + (grocerylist.get(i))
    print(res)


   



if __name__ == "__main__":
    main()
