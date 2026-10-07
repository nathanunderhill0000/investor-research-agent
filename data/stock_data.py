import yfinance as yf

def get_stock_data(ticker):

    stock = yf.Ticker(ticker)
    info = stock.info

    stock_data = {
         "company_name": info.get("longName"),
         "ticker": ticker,
         "current_price": info.get("currentPrice"),
         "market_cap": info.get("marketCap"),
         "revenue": info.get("totalRevenue"),
         "net_income": info.get("netIncomeToCommon"),
         "eps": info.get("trailingEps"),
         "pe_ratio": info.get("trailingPE"),
         "cash": info.get("totalCash"),
         "total_debt": info.get("totalDebt"),
    }

    return stock_data
