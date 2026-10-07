from data.stock_data import get_stock_data







def main():
    ticker = input("Enter ticker: ").strip().upper()

    print("\n--- Investment Research Agent ---")
    print(f"Analyzing: {ticker}")

    stock_data = get_stock_data(ticker)

    print(f"Company: {stock_data['company_name']}")
    print(f"Ticker: {stock_data['ticker']}")
    print(f"Price: ${stock_data['current_price']}")
    print(f"Market Cap: {format_large_number(stock_data['market_cap'])}")
    print(f"Revenue: {format_large_number(stock_data['revenue'])}")
    print(f"Net Income: {format_large_number(stock_data['net_income'])}")
    print(f"EPS: ${stock_data['eps']}")
    print(f"P/E Ratio: {stock_data['pe_ratio']:.2f}")
    print(f"Cash: {format_large_number(stock_data['cash'])}")
    print(f"Total Debt: {format_large_number(stock_data['total_debt'])}")

def format_large_number(value):
    if value is None:
        return "N/A"
    if value >= 1000000000000:
        return f"${value / 1000000000000:.2f}T"
    if value >= 1000000000:
        return f"${value / 1000000000:.2f}B"
    if value >= 1000000:
        return f"${value / 1000000:.2f}M"

if __name__ == "__main__":
    main()

