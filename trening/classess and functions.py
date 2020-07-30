# def recursion(a):
#     if (a==0):
#         return 1
#     return a*recursion(a-1)


# print(recursion(4))

orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

sort_orders = dict(sorted(orders.items(), key=lambda x: x[1], reverse=True))

print(sort_orders)