def main():


    '''
    Task 1 Data Acquisition and Task 2 Data storage
    '''
    import yfinance as yf

    # Acquisite the raw data for the stock ZM using yfinance provided by Yahoo Finance
    data = yf.download('ZM','2017-04-30','2022-04-30')
    # save the data to local disk as csv file
    data.to_csv("ZoomStockPriceDaily_Raw.csv")
    
    # also save the data to MongoDB
    # the MongoDB account name is shentong987, password is ST19950412
    import pymongo
    client = pymongo.MongoClient("mongodb+srv://shentong987:ST19950412@cluster0.dklnsc7.mongodb.net/?retryWrites=true&w=majority")


    # Acquisite the raw data for the Covid cases from WHO official website
    import pandas as pd
    df = pd.read_csv("https://covid19.who.int/WHO-COVID-19-global-data.csv")

    # Save it into local disk
    df.to_csv("CovidCasesDaily_Raw.csv", index=False)

    # Raw data is too complicated, do an initial data preprocessing to save the data only related to the US
    usa = df['Country'] == 'United States of America'
    filtered_data = df[usa]
    filtered_data.to_csv("CovidCasesDailyUSA.csv", index=False)
    df = pd.read_csv("CovidCasesDailyUSA.csv")

    '''
    Task 3 Data Preprocessing (Cleaning, Visualization, Transformation)
    '''
    '''
    # Normalize the close price of the ZM
    from sklearn.preprocessing import MinMaxScaler
    df = pd.read_csv("ZoomStockPriceDaily_Raw.csv")
    scaler = MinMaxScaler()
    StockPrice_normalized = df['Adj Close'].values.reshape(-1, 1)
    scaled_data = scaler.fit_transform(StockPrice_normalized)
    df['Adj Close'] = scaled_data
    '''
    # Data Visualization
    # Import the plotting library
    import matplotlib.pyplot as plt


    # Plot the close price of the ZM
    plt.figure(figsize=(8,4))
    data['Adj Close'].plot()
    plt.xlabel("Date")
    plt.ylabel("Daily Stock Price")
    plt.savefig('ZoomStockPriceDaily.png')

    # Plot the Daily Covid Cases in the US
    plt.figure(figsize=(8,4))
    plt.plot(df['Date_reported'],df['New_cases'])
    plt.tight_layout
    plt.xlabel("Date")
    plt.ylabel("Daily New Cases")
    plt.savefig('CovidCasesDaily.png')

    '''
    Task 4 Exploratory Data Analysis
    '''
    # hypothesis - the daily stock price of Zoom has a positive correlation with the daily Covid Cases in the US
    # Choose the same period from 2020-01-02 to 2022-04-30
    df = pd.read_csv("ZoomStockPriceDaily_Raw.csv")
    zoomstockprice_subset = df['Adj Close'][181:766]

    df = pd.read_csv("CovidCasesDailyUSA.csv")
    covidcasesdailyUSA_subset = df['New_cases'][181:765]

    
    plt.figure(figsize=(8,4))
    plt.scatter(covidcasesdailyUSA_subset, zoomstockprice_subset)
    plt.xlabel('Daily Covid Cases')
    plt.ylabel('Daily Stock Prices')
    plt.savefig('EDA Scatter.png')

    plt.close()


if __name__ == "__main__":
    main()
