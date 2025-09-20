import pandas as pd

# --- 1. Stock Market Master Data ---
stocks = pd.DataFrame({
    "Ticker": ["ABC", "XYZ", "MNO", "HDP"],
    "Company": ["Alpha Inc", "Xyza Corp", "Mono Labs", "HeadPro"],
    "Price": [150, 120, 80, 50]  # Current market price
})
print("Welcome to Mini Stock Market!\nAvailable Stocks:")
print(stocks, "\n")

# --- 2. Ask user how many stocks to view ---
num_stocks = int(input("How many stocks do you want to view? "))
print("\nHere are the first", num_stocks, "stocks:")
print(stocks.head(num_stocks), "\n")

# --- 3. Simulate Buy/Sell ---
trades = []
while True:
    action = input("Do you want to BUY or SELL a stock? (type 'exit' to quit): ").upper()
    if action == "EXIT":
        break
    ticker = input("Enter Ticker: ").upper()
    qty = int(input("Enter Quantity: "))
    
    # Get current price
    price = stocks.loc[stocks["Ticker"] == ticker, "Price"].values[0]
    
    # Store trade
    trades.append({"Ticker": ticker, "Action": action, "Quantity": qty, "Price": price})
    print(f"{action} order recorded: {qty} shares of {ticker} at {price}\n")

# --- 4. Convert trades to DataFrame ---
trades_df = pd.DataFrame(trades)
print("\nAll Trades:")
print(trades_df)

# --- 5. Calculate Profit/Loss (simple) ---
# For SELL trades, assume profit = (Sell price - Buy price) * qty
# For demo, we assume all previous BUY trades were at initial market price
profit_loss = []
for index, row in trades_df.iterrows():
    buy_price = stocks.loc[stocks["Ticker"] == row["Ticker"], "Price"].values[0]
    if row["Action"] == "SELL":
        pl = (row["Price"] - buy_price) * row["Quantity"]
    else:
        pl = 0
    profit_loss.append(pl)

trades_df["Profit/Loss"] = profit_loss
print("\nTrades with Profit/Loss:")
print(trades_df)

# --- 6. Summary per Stock ---
summary = trades_df.groupby("Ticker").agg({
    "Quantity":"sum",
    "Profit/Loss":"sum"
}).reset_index()
print("\nSummary by Stock:")
print(summary)
