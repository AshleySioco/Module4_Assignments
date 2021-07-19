products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
# CODE CELL
# PROBLEM 1

def get_product(code):
    return products[code]
get_product('espresso')

# CODE CELL
# PROBLEM 2

def get_property(code,property):
    return products[code][property]
get_property('espresso','name')

# CODE CELL
# PROBLEM 3

def main():
    order_list=[]
    while True:
        order=input('Enter product code and quantity ("{product_code},{quantity}"): ')
        if order=='/':
            break
        order_list.append(order.split(','))

    no_repeats=[x[0] for x in order_list]
    no_repeats=list(set(no_repeats))
    no_repeats.sort()


    final_list=[]
    for product in no_repeats:
        item_quantity=[product,0]
        for i in order_list:
            if i[0]==product:
                item_quantity[1]+=int(i[1])

        final_list.append(item_quantity)

    with open('receipt.txt','w') as receipt:
        receipt.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
    ''')

    grandtotal=0
    for item in final_list:
        subtotal=int(item[1])*get_property(item[0],'price')
        grandtotal+=subtotal
        name=get_property(item[0],'name')
        with open('receipt.txt','a') as receipt:
            receipt.write('\n'+f'{item[0]}\t\t{name}\t\t{item[1]}\t\t\t\t{subtotal}')


    with open('receipt.txt','a+') as receipt:
        receipt.write(f'''

Total:\t\t\t\t\t\t\t\t\t\t{grandtotal}
==
    ''')
        receipt.seek(0)
        print(receipt.read())


main()
