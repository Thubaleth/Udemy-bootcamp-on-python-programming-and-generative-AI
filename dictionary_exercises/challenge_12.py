"""Consider the dictionary from the previous challenge.

Create a new dictionary called profit, where the profit is 25% of sales.

Use dictionary comprehension if possible."""


profit = {}
years = [2015, 2016, 2017, 2018, 2019, 2020]

sales = [350000, 400000, 410000, 439000, 500000, 290000]

years_and_sales = {}
cnt = 0
for year in years:
    
    profit[year] = sales[cnt] * 0.25
    cnt+=1

print(profit)
