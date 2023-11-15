mackerel_price_kg = float(input())
sprat_price_kg = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = float(input())

bonito_price_kg = mackerel_price_kg + mackerel_price_kg * 0.60
safrid_price_kg = sprat_price_kg + sprat_price_kg * 0.80

price_mussels = mussels_kg * 7.50
price_bonito = bonito_price_kg * bonito_kg
price_safrid = safrid_price_kg * safrid_kg

total_cost = price_safrid + price_bonito + price_mussels
print(f"{total_cost:.2f}")