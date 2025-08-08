# Hardcoded stock prices!!!!!!

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list.")
        continue
    qty = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty
    total_investment += stock_prices[stock] * qty

print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares at ${stock_prices[stock]} each")

print("Total Investment Value: $", total_investment)

# Optional: Save to file
save = input("Save to file? (y/n): ").lower()
if save == "y":
    with open("portfolio.txt", "w") as f:
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares at ${stock_prices[stock]} each\n")
        f.write(f"Total Investment Value: ${total_investment}\n")
    print("Portfolio saved to portfolio.txt")
