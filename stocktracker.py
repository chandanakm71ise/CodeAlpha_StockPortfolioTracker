# CodeAlpha Task 2: Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 180,
    "MSFT": 420
}

total_investment = 0

print("----- Stock Portfolio Tracker -----")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(stock, "investment =", investment)
    else:
        print("Stock not available.")

print("-----------------------------------")
print("Total Investment Value =", total_investment)
print("-----------------------------------")