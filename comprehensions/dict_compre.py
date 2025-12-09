chai_prices_inr = {
    "Masala Chai": 40,
    "Ginger Tea": 80,
    "Lemon Tea": 200
}

chai_price_usd = {chai:price / 80 for chai, price in chai_prices_inr.items()}
print(chai_price_usd)