def currency_converter():
    
    rates = {
       "BDT" : {"USD" : 0.0082,"EURO": 0.0071, "GBP" : 0.0061, "JPY" : 1., "BDT":1},
        "USD" : {"BDT" : 121.65, "EURO" : 0.87, "GBP": 0.74, "JPY": 144.14, "USD":1},
        "EURO": {"BDT" : 140.59, "USD" : 1.6, "GBP": 0.85, "JPY": 166.48, "EURO":1},
        "GBP" : {"BDT" : 165.02, "EURO" : 1.17, "USD": 1.36, "JPY": 196.77, "GBP":1 },
        "JPY" : {"BDT" : 0.84, "EURO" : 0.0060, "GBP": 0.0051, "USD": 0.0069, "JPY":1}
    }

    while True:
        print("\nCurrency Converter (type 'quit' to exit)")
        print("Currencies:BDT, USD, EURO, GBP, JPY")

      
        amount = input("Enter amount: ")
        if amount.lower() == 'quit':
            print("Goodbye!")
            break
        try:
            amount = float(amount)
        except ValueError:
            print("Please enter a number.")
            continue

        
        from_currency = input("From (BDT,USD, EURO, GBP, JPY): ").upper()
        if from_currency == 'QUIT':
            print("Goodbye!")
            break
       
        if from_currency not in rates:
            print("Invalid currency. Use BDT, USD, EURO, GBP, JPY.")
            continue

       
        to_currency = input("To (BDT,USD, EURO, GBP,JPY): ").upper()
        if to_currency == 'QUIT':
            print("Goodbye!")
            break
        if to_currency not in rates:
            print("Invalid currency. Use BDT, USD, EURO, GBP, JPY.")
            continue

       
        converted = amount * rates[from_currency][to_currency]
        print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
        print("!!!THANK YOU!!!")
print("===WELCOME===")
currency_converter()