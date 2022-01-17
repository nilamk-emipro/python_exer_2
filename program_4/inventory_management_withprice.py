from tabulate import tabulate


class Inventory_management:
    def __init__(self):
        self.product_details = {}

    def purchase(self, purchase_qty, price):
        """
        :param price: is use for set price of product
        :param purchase_qty: is use for how many product purchased
        :return:
        """
        value_dict ={}
        value_dict.update({'price': price,'Quantity': purchase_qty,'subtotal':price*purchase_qty})
        if not bool(self.product_details):
            key = 1
        else:
            key = (list(self.product_details.keys())[-1])+1
        self.product_details.update({key: value_dict})
        #print(self.product_details)

    def sale(self, sale_qty):
        """
        :param : sale_qty is use for how many items want to sale
        :return: none
        """
        total = 0
        for key, value in self.product_details.items():
            total += value['Quantity']

        while True:
            if sale_qty != 0:
                if not bool(self.product_details):
                    sale_qty = 0
                    print("Quantity is not enough for sale")
                else:
                    for k in list(self.product_details.keys()):
                        v = self.product_details.get(k)
                        if list(v.values())[1] == 0:
                            self.product_details.pop(k)
                        else:
                            for key, value in self.product_details.items():
                                if total > sale_qty:
                                    if sale_qty >= list(value.values())[1]:
                                        deducted_value = list(value.values())[1]-list(value.values())[1]
                                        sale_qty -= list(value.values())[1]
                                        value_dict = {}
                                        value_dict.update({'price': list(value.values())[0], 'Quantity': deducted_value, 'subtotal': list(value.values())[1] * deducted_value})
                                        self.product_details.update({key: value_dict})

                                    elif sale_qty == list(value.values())[1]:
                                        deducted_value = list(value.values())[1]-list(value.values())[1]
                                        sale_qty -= list(value.values())[1]
                                        value_dict = {}
                                        value_dict.update({'price': list(value.values())[0], 'Quantity': deducted_value, 'subtotal': list(value.values())[0] * deducted_value})
                                        self.product_details.update({key: value_dict})

                                    else:
                                        deducted_value = list(value.values())[1] - sale_qty
                                        sale_qty = 0
                                        value_dict = {}
                                        value_dict.update({'price': list(value.values())[0], 'Quantity': deducted_value, 'subtotal': list(value.values())[0] * deducted_value})
                                        self.product_details.update({key: value_dict})
                                        # print(deducted_value)
                                        # print(list(value.keys())[1])
                                        # print(sale_qty)
                                else:
                                    sale_qty = 0
                                    print("Quantity is not enough for sale")
            else:
                for k in list(self.product_details.keys()):
                    v = self.product_details.get(k)
                    if list(v.values())[1] == 0:
                        self.product_details.pop(k)
                break

    def display_available_product(self):
        """
        :return: view how many Product available
        """
        header=["Price","Quantity","Subtotal"]
        print("{:<8} {:<15} {:<10}".format('Price', 'Quantity', 'Subtotal'))
        for key,value in self.product_details.items():
            print("{:<8} {:<15} {:<10}".format(list(value.values())[0], list(value.values())[1], list(value.values())[2]))

    def display_valuation(self):
        """
        :return: view valuation of available Qty
        """
        totalqty = 0
        total = 0
        for key, value in self.product_details.items():
            totalqty += value['Quantity']
            total += value['subtotal']
        result = total / totalqty
        print("Valuation :" + str(result))

inventory = Inventory_management()
while True:

    print("\nMAIN MENU")
    print("1. Purchase Product")
    print("2. Sale Product")
    print("3. View Available Product Quantity")
    print("4. Show Valuation")
    print("0. Exit")
    selected_menu_no = int(input("Enter the number:"))

    if selected_menu_no == 1:
        purchase_qty = input("How many Quantity want to purchase?")
        price = input("what is the price of the product?")
        inventory.purchase(int(purchase_qty or 0), int(price or 0))

    elif selected_menu_no == 2:
        sale_qty = input("How many Quantity want to sale?")
        inventory.sale(int(sale_qty or 0))

    elif selected_menu_no == 3:
        inventory.display_available_product()

    elif selected_menu_no == 4:
        inventory.display_valuation()

    elif selected_menu_no == 0:
        break

    else:
        print("Please Select Proper Menu..")

