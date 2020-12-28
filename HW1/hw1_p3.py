# variable 'price' initialization
price = 0

while True:
    # get inputs (which mask, which size, and how many)
    which = input("KF80/KF94?")
    size = input("small/medium/large?")
    quantity = int(input("quantity?"))



    # TODO 1. calculate the price of the mask(s)KFK
    if which == 'KF80':
        
        if size == 'small':
            price += 900*quantity
            
        elif size == 'medium':
            price += 1200*quantity
            
        elif size == 'large':
            price += 1500*quantity
    
    else: 
        
        if size == 'small':
            price += 1100*quantity
            
        elif size == 'medium':
            price += 1500*quantity
            
        elif size == 'large':
            price += 1900*quantity
        


    # decide whether to buy more mask or not
    buy_mask = input("more mask?(yes/no)")

    # TODO 2. exit while loop when you decided not to buy more masks
    if buy_mask == 'no':
        break
    
        
# TODO 3. when total price is less than 30,000won, add shipping fee 3,000won
if price < 30000:
    price += 3000


# print the total price (variable 'price')
print(f"price: {price}won")
