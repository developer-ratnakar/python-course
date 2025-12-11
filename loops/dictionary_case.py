users = [
    {"id": 1, "total": 100, "coupon": "P10"},
    {"id": 2, "total": 150, "coupon": "F20"},
    {"id": 3, "total": 200, "coupon": "A50"}
]

discounts = {
    "P10": (0.2, 0),
    "F20": (0.5, 0),
    "A50": (0, 10),
}

for user in users:
    percent, fixed = discounts[user.get("coupon", (0, 0))]
    discount = user["total"] * percent + fixed
    print(f"User {user['id']} shopped rs {user['total']} and got discount of rs {discount} with coupon {user['coupon']} on next time visit.") 