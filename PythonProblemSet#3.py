def main():
    #Currency Converter
    #to make sure the user inputs are accessed as integers and therefore can be accessed as a type of currency.
    cur = int(input("Please enter which type of currency you have. Choose from the list: 1. United States Dollar 2. European Euro 3. Chinese Yuan 4. Turkish Lira"))
    #in order to access the currency for usd to any other currency, use a dictionary to define the currencies.
    currency = {1 :  1, 2 : 0.99, 3 : 7.29, 4 : 18.62}
    #then define a new variable as whatever the user inputed, then get the corresponding currency in the dictionary.
    curr = float(currency.get(cur))
    #next, the user inputs how much money they have and it has to be defined as a float because they can answer a decimal.
    amount = float(input("Please enter how much money you have."))
    #then get the total amount through dividing.
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
