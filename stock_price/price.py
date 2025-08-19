# Hardcoded dictionary for stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3500,
    "MSFT": 300,
    "TCS":3750.25,    
    "INFY":1510.75,    
    "RELI":2815.50,    
    "HDFC":1723.40,     
    "ITC":451.60,      
    "SBIN":637.80,      
    "WIPRO":432.90,   
    "HCLT":1215.00,    
    "BAJAJ":7199.95, 
    "MARUTI":11025.00

}

portfolio = {}
total_investment = 0

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        continue

    investment = stock_prices[stock] * quantity
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    total_investment += investment

    print(f"Added {quantity} shares of {stock}. Total so far: ₹{total_investment}")

# Display summary
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    print(f"{stock} - Qty: {qty}, Price: ₹{price}, Subtotal: ₹{price * qty}")

print(f"\nTotal Investment: ₹{total_investment}")

# Option to save file
save = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()
if save == "yes":
    file_format = input("Choose file format - txt or csv: ").lower()

    if file_format == "txt":
        with open("portfolio.txt", "w") as f:
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                f.write(f"{stock} - Qty: {qty}, Price: ₹{price}, Subtotal: ₹{price * qty}\n")
            f.write(f"\nTotal Investment: ₹{total_investment}")
        print("Saved to portfolio.txt")

    elif file_format == "csv":
        import csv
        with open("portfolio.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Stock", "Quantity", "Price", "Subtotal"])
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                writer.writerow([stock, qty, price, price * qty])
            writer.writerow(["Total", "", "", total_investment])
        print("Saved to portfolio.csv")

    else:
        print("Invalid file format. File not saved.")
