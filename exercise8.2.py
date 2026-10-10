prices = {"ლეპტოპი": 2500, "მაუსი": 40, "კლავიატურა": 120, "მონიტორი": 650}
stock = {"ლეპტოპი": 2, "მაუსი": 10, "კლავიატურა": 1, "მონიტორი": 3}

orders = [
    ("ნინო", "ლეპტოპი", 1),
    ("გიორგი", "მაუსი", 3),
    ("ანა", "კლავიატურა", 1),
    ("ნინო", "მაუსი", 2),
    ("გიორგი", "კლავიატურა", 1),
    ("ანა", "ტელეფონი", 1),
    ("ლუკა", "ლეპტოპი", 1),
    ("ლუკა", "მონიტორი", 5),
]

spent = {}
failed_users = set()
for user, product, amount in orders:
    if product not in prices:
        print(f"❌{user}: {product} არ იყიდება")
        failed_users.add(user)
    elif stock[product] < amount:
        print(f"⚠️ {user}: {product} — მარაგში მხოლოდ  {stock[product]} ცალია")
        failed_users.add(user)
    else :
        stock[product] -= amount
        total = prices[product] * amount
        spent[user] = spent.get(user, 0) + total
        print(f"✅ {user}: {product} x{amount} = {total} ლარი")

print("---ანგარიში ---")

income = 0
for user, money in spent.items():
    print(f"{user}: {money} ლარი")
    income += money

print(f"შემოსავალი: {income} ლარი")

out_of_stock = []
for product, quantity in stock.items():
    if quantity == 0:
        out_of_stock.append(product)

out_of_stock.sort()
print(f"ამოიწურა: {out_of_stock}")

failed_list = sorted(failed_users)
print(f"წარუმატებელი შეკვეთა ჰქონდათ: {failed_list}")