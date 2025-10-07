# live_currency_converter.py
import requests

API_BASE = "https://api.exchangerate-api.com/v4/latest"


PAIRS = {
    "1": ("USD", "UZS"),
    "2": ("UZS", "USD"),
    "3": ("EUR", "USD"),
    "4": ("USD", "EUR"),
    "5": ("EUR", "UZS"),
    "6": ("UZS", "EUR"),
    "7": ("EXIT", "EXIT")
}

def get_rate(src: str, dst: str) -> float:
    url = f"{API_BASE}/{src.upper()}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()
    if "rates" not in data or dst.upper() not in data["rates"]:
        raise ValueError("Rate not found for given currency pair.")
    return data["rates"][dst.upper()]

def main():
    while True:
        print("\n--- Live Currency Converter ---")
        print("1) USD -> UZS")
        print("2) UZS -> USD")
        print("3) EUR -> USD")
        print("4) USD -> EUR")
        print("5) EUR -> UZS")
        print("6) UZS -> EUR")
        print("7) Exit")

        choice = input("Enter option (1-7): ")

        if choice not in PAIRS:
            print("Invalid choice, try again.")
            continue

        if choice == "7":
            print("Goodbye!")
            break

        src, dst = PAIRS[choice]

        try:
            amt = float(input(f"Enter amount in {src}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        try:
            rate = get_rate(src, dst)
            result = amt * rate
            print(f"{amt} {src} = {result:.2f} {dst}")
        except Exception as e:
            print(f"Failed to fetch live rate: {e}")

        again = input("Do you want to convert again? (y/n): ")
        if again.lower() != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":main()