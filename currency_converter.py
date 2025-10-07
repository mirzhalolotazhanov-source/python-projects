def currency_converter():
    while True:
        print("\n--- Currency Converter ---")
        print("1) USD -> UZS")
        print("2) UZS -> USD")
        print("3) EUR -> USD")
        print("4) USD -> EUR")
        print("5) Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            usd = float(input("Enter amount in USD: "))
            uzs = usd * 12600
            print(f"{usd} USD = {uzs} UZS")
        elif choice == "2":
            uzs = float(input("Enter amount in UZS: "))
            usd = uzs / 12600
            print(f"{uzs} UZS = {usd} USD")
        elif choice == "3":
            eur = float(input("Enter amount in EUR: "))
            usd = eur * 1.1
            print(f"{eur} EUR = {usd} USD")
        elif choice == "4":
            usd = float(input("Enter amount in USD: "))
            eur = usd / 1.1
            print(f"{usd} USD = {eur} EUR")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

        again = input("Do you want to continue? (y/n): ")
        if again.lower() != "y":
            print("Goodbye!")
            break


currency_converter()