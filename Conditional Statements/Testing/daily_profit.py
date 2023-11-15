working_days = int(input())
money_per_day = float(input())
exchange_rate_dollar_bgn = float(input())
tax = 25 / 100
month_income = working_days * money_per_day
year_income = (month_income * 12) + (month_income * 2.5)
year_income_bgn = year_income * exchange_rate_dollar_bgn
lose_after_tax_bgn = year_income * tax * exchange_rate_dollar_bgn
net_year_income = year_income_bgn - lose_after_tax_bgn
average_money_per_day = net_year_income / 365
print("%.2f"% average_money_per_day)
