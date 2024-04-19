import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime
import yfinance as yf

print('Note: This is just a project to analyse some of the blue chip stocks.')
print('Buying and selling of stocks should be done solely on the advice of SEBI registered advisors')
print('-------------------------------------------------------------------------------------')
print('This project focuses on the following factors for analysing a stock:')
print('1.Market Cap')
print('2.EPS (Earnings per share)')
print('3.ROE (Return On Equity)')
print('4.ROCE (Return on Capital Equity)')
print('5.PE (Price to Earning)')
print('6.Dividend per share')
print('7.Debt on Company')

start_date = datetime.now() - pd.DateOffset(months=3)
end_date = datetime.now()
shares = ['LT.BO', 'TCS.BO', 'HDFCBANK.NS', 'INFY.NS']
df_list = []

for share in shares:
    data = yf.download(share, start=start_date, end=end_date)
    df_list.append(data)

df = pd.concat(df_list, keys=shares, names=['Share', 'Date'])
df = df.reset_index()
print(df.head())

chart = px.area(df, x='Date', y='Close', color='Share', facet_col='Share',
                labels={'Date': 'Date', 'Close': 'Closing Price', 'Share': 'Company'},
                title='Stock prices for L&T, TCS, Hdfc Bank, Infosys')

chart.show()

print("MARKET CAP : Also called market capitalisation measures the value of a company based on the number of stock "
      "shares it has issued and the price at which investors are willing to buy them.")
print("It is generally broken down as micro-cap, small-cap, mid-cap, large-cap and ultra or mega-cap")
print("L&T, TCS, Hdfc Bank, Infosys form large cap companies.")
Company = ['L&T', 'TCS', 'Hdfc Bank', 'Infosys']
market_cap = [5.28, 14.12, 11.14, 6.22]
colors = ['lightcoral', 'c', 'blue', 'k']
explode = (0, 0.1, 0, 0)

plt.pie(market_cap, labels=Company, explode=explode, colors=colors, startangle=90, shadow=True)


plt.axis('equal')
plt.legend(title="Four Bluechip Stocks:")
plt.title("Market cap in LCr")
plt.savefig('market_cap_plot.png')
plt.show()
print("**************************************************************************")
print(
    "ROE - Return on Equity is an essential parameter that helps potential investors analyse a company's profitability. ")
print("It indicates how well a company has utilised its shareholders' money. One can calculate a")
print(
    "company's ROE by dividing the net income of the company by total shareholder equity and is denoted in percentages.")
Period = ['Mar-23', 'Mar-22', 'Mar-21', 'Mar-20', 'Mar-19']
ROE = [11.72, 10.49, 15.04, 14.02, 13.28]
plt.xlabel("Period")
plt.ylabel("ROE(%)")
plt.title("ROE OF L&T Ltd. in last 5 years")
plt.bar(Period, ROE, color='lightcoral')
for i, value in enumerate(ROE):
    plt.text(i,value+0.5,str(value), ha='center', va='bottom')
plt.savefig('ROE_plot_L&T.png')
plt.show()

Period = ['Mar-23', 'Mar-22', 'Mar-21', 'Mar-20', 'Mar-19']
ROE = [46.61, 43.00, 37.52, 38.44, 35.19]
plt.xlabel("Period")
plt.ylabel("ROE(%)")
plt.title("ROE OF TCS in last 5 years")
plt.bar(Period, ROE, color='c')
for i, value in enumerate(ROE):
    plt.text(i,value+0.5,str(value), ha='center', va='bottom')
plt.savefig('ROE_plot_tcs.png')
plt.show()

Period = ['Mar-23', 'Mar-22', 'Mar-21', 'Mar-20', 'Mar-19']
ROE = [31.95, 29.34, 25.34, 25.35, 23.72]
plt.xlabel("Period")
plt.ylabel("ROE(%)")
plt.title("ROE OF Hdfc Bank in last 5 years")
plt.bar(Period, ROE, color='black')
for i, value in enumerate(ROE):
    plt.text(i,value+0.5,str(value), ha='center', va='bottom')
plt.savefig('ROE_plot_hdfc.png')
plt.show()

Share = ['L&T', 'TCS', 'Hdfc Bank', 'Infosys']
Avg_ROE = [12.91, 40.152,15.328, 27.14]
plt.xlabel("Period")
plt.ylabel("AVERAGE ROE(%)")
plt.title("Average ROE OF Stocks in last 5 years")
plt.bar(Share, Avg_ROE, color='pink')
for i, value in enumerate(Avg_ROE):
    plt.text(i, value+0.5, str(value), ha='center', va='bottom')

plt.savefig('ROE_plot_avgroe.png')
plt.show()
print("*******************************************************************************************************")
print("Return On Capital Employed (ROCE) - is a long-term profitability ratio that measures how efficiently a company is employing its capital to generate profit.")
print("It is calculated by dividing the EBIT (Earnings before Interest and Taxes) by total assets minus total current liabilities.")
time_period =('Mar-23','Mar-22','Mar-21','Mar-20','Mar-19')
TCS=[57.48,52.91,45.96,46.01,44.97]
LarsenTubro =[1.43,10.52,12.35,10.44,10.91]
Hdfc_bank =[3.36,4.76,5.29,5.92,6.17]
Infosys=[44.58,39.96,37.83,34.01,32.40]
plt.subplot(2,1,1)
plt.ylabel("ROCE(%)")
plt.title("TCS")
plt.grid(True)
plt.plot(time_period,TCS,'g')
plt.subplots_adjust(hspace=0.4,wspace=0.4)

plt.subplot(2,1,2)
plt.ylabel("ROCE(%)")
plt.title("L&T")
plt.grid(True)
plt.plot(time_period,LarsenTubro,'k')
plt.subplots_adjust(hspace=0.4,wspace=0.4)
plt.show()
plt.savefig('roce of tcs and larsen and tubro.png')

plt.subplot(2,1,1)
plt.ylabel("ROCE(%)")
plt.title("HDFC Bank")
plt.grid(True)
plt.plot(time_period,Hdfc_bank,'c')
plt.subplots_adjust(hspace=0.4,wspace=0.4)

plt.subplot(2,1,2)
plt.ylabel("ROCE(%)")
plt.title("Infosys")
plt.grid(True)
plt.plot(time_period,Infosys,'m')
plt.subplots_adjust(hspace=0.4,wspace=0.4)
plt.show()
plt.savefig('ROCE of hdfc and infosys.png')
print("*******************************************************************************************************")

print("The PE Ratio - measures the relationship between the company's current stock price and EPS (Earnings Per Share)")
print(" A PE Ratio indicates how many times investors pay money to get 1 rupee of return.")
print("A PE Ratio indicates how many times investors pay money to get 1 rupee of return.")
print("It is one of the important parameters to evaluate whether a company's stock price is overvalued or undervalued.")

print("The PE ratio is the most popular and well-known valuation metric used by many investors to analyze whether a stock is overvalued or undervalued. ")
print("It indicates how much investors are willing to pay for a stock's current price to earn one rupee.")

shares= ['TCS', 'L&T', 'HDFC Bank', 'Infosys']
Avg_PE=[29.172,21.70,19.57,25.70]
plt.barh(shares, Avg_PE, align='center',color='c')
plt.xlabel("Average P/E ratio")
plt.ylabel("Share")
plt.show()
print("*********************************************************************************")

shares= ['TCS', 'L&T', 'HDFC Bank', 'Infosys']
Total_liabilities=[142859,329722,2530432,124596]
plt.xlabel("Stock")
plt.ylabel("Total liabilities")
plt.title("Total liabilities of stock in Rs Cr")
plt.bar(shares,Total_liabilities, color='green')
for i, value in enumerate(Total_liabilities):
    plt.text(i, value+0.5, str(value), ha='center', va='bottom')
plt.show()
plt.savefig('total_liabilities.png')


stock= ['TCS', 'L&T', 'HDFC Bank', 'Infosys']
DY=[1.24,0.68,1.27,2.40]
plt.xlabel("Stock")
plt.ylabel("Dividend Yield")
plt.title("Dividend Yield in %")
colors = ['lightcoral', 'g', 'c', 'pink']
plt.pie(DY, labels=stock,  colors=colors, startangle=90, shadow=True,autopct='%1.1f%%')
plt.axis('equal')
plt.show()
plt.savefig('dividend yield.png')











