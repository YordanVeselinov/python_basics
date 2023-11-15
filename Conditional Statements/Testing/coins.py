bitcoin = float(input())
yuan = float(input())
commission = float(input()) / 100
bitcoin_to_eur = (bitcoin * 1168) / 1.95
yuan_to_eur = yuan * 0.15 * 1.76 / 1.95


total_eur = bitcoin_to_eur + yuan_to_eur
minus_commission = total_eur * commission
real_money = total_eur - minus_commission


print("%.2f"%real_money)


