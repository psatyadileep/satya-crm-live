"""
#*** (1) Returns all customers from customer table
customers = Customer.objects.all()

#(2) Returns first customer in table
first Customer = Customer.objects.first()

#(3) Returns last customer in table
lastCustomer = Customer.objects. last()

#(4) Returns single customer by name
customer ByName = Customer.objects.get(name='Peter Piper')

#***(5) Returns single customer by name
customerById = Customer.objects.get(id=4)

#***(6) Returns all orders related to customer (firstCustomer variable set above)
first Customer.order_set.all()

#(7) ***Returns orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

#(8) ***Returns products from products table with value of "Out Door" in category attribute
products Product.objects. filter (category="Out Door")

# (9) ***Order/Sort Objects by id
least ToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# (10) Returns all products with tag of "Sports": (Query Many to Many Fields)
products Filtered = Product.objects.filter (tags_name="Sports")

(11) Bonus
Q: If the customer has more than 1 ball, how would you reflect it in the database?

"""