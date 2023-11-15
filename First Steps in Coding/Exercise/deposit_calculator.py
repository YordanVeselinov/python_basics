amount = float(input())
months = int(input())
year_tax_procent = float(input())

tax = amount * (year_tax_procent / 100 )
month_tax = tax / 12
full_amounth = amount + (month_tax * months)

print(full_amounth)
