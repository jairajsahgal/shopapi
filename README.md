# shopapi


product
product/pk/reviews

order
order/pk/items

payment
payment/pk



<!-- 
endpoints

category
category/id

product
product/id
product/id/review
product/id/review/id

customer
customer/id
customer/id/address
customer/id/address/id


customer/id
customer/id/order
customer/id/order/id
 -->









many=true only done for onetomany relationship

category
category/pk

product
product/pk

order
order/pk
order/pk/items
order/pk/items/pk
order/pk/payment


payment
payment/pk



http://127.0.0.1:8000/store/product/?category=1








TIPS

# return either error or data
def validate():
		return Validationerror
	return data




use django filter library for filtering data in view api


























