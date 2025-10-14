#Inventory Management: A small store needs a system to keep track of its inventory. For each product, they need to store the product name, ID, and quantity in stock. What data structures would be suitable for this task, and how would you choose between them?
#通过使用字典中的字典的方式来完成快速检索
fruit_dict = {
    101:{"name": "apple", "stock":"100"},
    102:{"name": "momo", "stock": "20"}
}
print(fruit_dict[101])