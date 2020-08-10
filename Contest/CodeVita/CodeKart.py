class Cart:
	def __init__(self):
		self.cartItems = {}

	def addItem(self, itemName, quantity):
		if (validateItem(itemName) and quantity < 0):
			return -1
		self.cartItems[itemName] = quantity
		return cartItems[quantity]

	def removeItem(self, itemName):
		if (validateItem(itemName)):
			return -1
		del self.cartItems[itemName]
		return 1

	def validateItem(self, itemName):
		CartItem = CartItem()
		CartItem =  self.cartItems[itemName]
		if CartItem == None:
			return True
		return False

	def increment(self, itemName, quantity):
		if (validateItem(itemName) and quantity < 0): 
			return -1
		self.cartItems[itemName] += quantity
		return self.cartItems[quantity]

	def decrement(self, itemName, quantity):
		if (validateItem(itemName) and quantity < 0): 
			return -1
		self.cartItems[itemName] -= quantity
		return self.cartItems[quantity]

	def getOrderAmount(self):
		total = 0.0
		# for (Map.Entry<String, CartItem> entry : cartItems.entrySet()) {
		# 	total += entry.getValue().getPrice() * entry.getValue().getQuantity()
		return total


class CartItem:
	def __init__(self):
		self.item = Item()
		self.quantity = None

	def getQuantity(self):
		return self.quantity

	def setQuantity(self, quantity):
		self.quantity = quantity

	def CartItem(self, itemName, quantity):
		self.item = Inventory.getInventoryItem(itemName)
		self.quantity = quantity

	def incrementQty(self, quantity):
		self.quantity += quantity

	def decrememtQty(self, quantity):
		self.quantity -= quantity

	def getPrice(self):
		return item.getPrice()



if __name__ == "__main__":
	T = int(input())
	for i in range(T):
		while True:
			cmd = input()
			if cmd == "END":
				break
			print(cmd)
		

