daily_sales = [4, 5, 10, 15, 12, 6, 7]

total_sales_above_5 = sum(sale for sale in daily_sales if sale > 5)
print(total_sales_above_5)