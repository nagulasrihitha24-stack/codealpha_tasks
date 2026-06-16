stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}
portfolio = {}
total_investment = 0
print("=== Stock Investment Tracker ===")
print("Available Stocks and Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
num_stocks = int(input("\nHow many different stocks do you want to buy? "))
for i in range(num_stocks):
    stock_name = input("\nEnter stock symbol: ").upper()
    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        portfolio[stock_name] = quantity
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
    else:
        print("Stock not found in price list!")
print("\n=== Investment Summary ===")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    print(f"{stock} -> Quantity: {quantity}, "
          f"Price: ${price}, "
          f"Investment: ${investment}")
print(f"\nTotal Investment Value: ${total_investment}")
save_option = input("\nDo you want to save the result? (yes/no): ").lower()
if save_option == "yes":
    file_type = input("Save as TXT or CSV? ").lower()
    if file_type == "txt":
        with open("investment_report.txt", "w") as file:
            file.write("=== Investment Report ===\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity
                file.write(
                    f"{stock} -> Quantity: {quantity}, "
                    f"Price: ${price}, "
                    f"Investment: ${investment}\n"
                )
            file.write(f"\nTotal Investment Value: ${total_investment}")
        print("Report saved as investment_report.txt")
    elif file_type == "csv":
        with open("investment_report.csv", "w") as file:
            file.write("Stock,Quantity,Price,Investment\n")
            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity
                file.write(
                    f"{stock},{quantity},{price},{investment}\n"
                )
            file.write(f"\nTotal Investment Value,,,{total_investment}")
        print("Report saved as investment_report.csv")
    else:
        print("Invalid file type selected!")
else:
    print("Result not saved.")