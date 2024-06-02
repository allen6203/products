products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price)
	# 7~9, p = [name, price]
	products.append(p)
	# 7~11, products.append([name, price])
print(products)

products[0][0]
