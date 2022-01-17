from tabulate import tabulate
from datetime import date

class Sales_order:
    def __init__(self):
        self.product_details = {}
        self.stock_details = {}
        self.customer_details = {}
        self.customer_add_details = {}
        self.sales_order_details = {}

    def manage_product(self):
        """
        to manage product as prepare for get value and create for storing data of product
        :return: None
        """
        product_values = self.prepare_product()
        self.create_product(product_values)

    def prepare_product(self):
        """
        get the product details from users
        :return: dictionary of details product details and initial stock
        """
        product_name = input("Insert Product Name:")
        product_unit_price = input("Insert Product Unit Price:")
        product_cost_price = input("Insert Product cost Price:")
        stock = input("Insert Product stock Quantity:")
        return {'product_name': product_name,
                'product_unit_price': product_unit_price,
                'product_cost_price': product_cost_price,
                'stock': stock
                }

    def create_product(self, product_value):
        """
        store the product details and stock details in their dictionary
        :param product_value: to get value from user
        :return: SKU (identify as generated product detail's primary key)
        """
        index = 1 if bool(self.product_details) == False else int(list(self.product_details.keys())[-1][-1]) + 1
        SKU = 'PRD'+ str(index)
        self.product_details.update({SKU: {'product_name': product_value.get('product_name'),
                                      'product_unit_price': product_value.get('product_unit_price'),
                                      'product_cost_price': product_value.get('product_cost_price')}})
        self.stock_details.update({SKU: {'available_product_qty': product_value.get('stock')}})

        return SKU

    def update_stock(self,order_key = 0):
        if order_key == 0:
            while True:
                for key, values in self.product_details.items():
                    #print(tabulate([key, value.get('product_name')], headers=['Product_Key', 'Product_Name']))
                    print(tabulate([[key, values.get('product_name')]], headers=['Product_Key', 'Product_Name']))
                selected_product_key = input("Select Product key for increase the Stock of product")

                if selected_product_key in list(self.product_details.keys()):
                    update_stock = int(input("How many stock you want to increase?"))
                    self.stock_details.update({selected_product_key:
                    {'available_product_qty': int(self.stock_details.get(selected_product_key)['available_product_qty']) + update_stock
                    }})
                    break
                else:
                    print("Please select proper Product Key")
        else:
            for key, value in self.sales_order_details.items():
                print(key,value)

    def manage_customer(self):
        """
        to manage customer as prepare for get value and create for storing data of customer
        :return: None
        """
        customer_values = self.prepare_customer()
        self.create_customer(customer_values)

    def prepare_customer(self):
        """
        get the customer details from users
        :return: dictionary of details customer details
        """
        customer_name = input("Insert customer Name:")
        email_address = input("Insert Email Address:")
        phone_number = input("Insert Phone Number:")
        Address1 = input("Insert Address :")
        Address2 = input("Insert More Address :")
        city = input("Insert City :")
        state = input("Insert State :")
        country = input("Insert Country :")
        zipcode = input("Insert Zipcode :")

        return {'customer_name': customer_name,
                'email_address': email_address,
                'phone_number': phone_number,
                'Address1': Address1,
                'Address2': Address2,
                'city': city,
                'state': state,
                'country': country,
                'zipcode': zipcode
                }

    def create_customer(self, customer_value):
        """
        store the customer details in their dictionary
        :param customer_value: to get value from user
        :return: cust_1 like key (identify as generated customer detail's primary key)
        """
        index = 1 if bool(self.customer_details) == False else int(list(self.customer_details.keys())[-1][-1]) + 1
        cust_key = 'cust_' + str(index)

        self.customer_details.update({cust_key: {'customer_name': customer_value.get('customer_name'),
                                            'email_address': customer_value.get('email_address'),
                                            'phone_number': customer_value.get('phone_number')}})
        self.customer_add_details.update({cust_key: {'Address1': customer_value.get('Address1'),
                                                'Address2': customer_value.get('Address2'),
                                                'city': customer_value.get('city'),
                                                'state': customer_value.get('state'),
                                                'country': customer_value.get('country'),
                                                'zipcode': customer_value.get('zipcode')
                                                }})
        return cust_key

    def manage_order(self):
        """
        to manage order as prepare for get value and create for storing data of order
        :return: None
        """
        if len(self.customer_details.keys()) > 0 and len(self.product_details.keys()) == 0:
            print("please add Product")
        elif len(self.customer_details.keys()) == 0 and len(self.product_details.keys()) > 0:
            print("please create customer")
        elif len(self.customer_details.keys()) == 0 and len(self.product_details.keys()) == 0:
            print("add customer and product details")
        else:
            cust_key, order_lines, order_total_amount = self.prepare_order()
            order_key = self.create_order(cust_key, order_lines, order_total_amount)
        return order_key

    def prepare_order(self):
        """
        get the order details from users
        :return: dictionary of details order details
        """
        order_lines = []
        order_total_amount = 0
        cust_key, order_line = self.display_details()

        for values in order_line:
                total = int(self.product_details[values.get('product_key')].get('product_unit_price')) * int(
                    values.get('quantity'))
                order_total_amount += total
                order_lines.append({'product_key': values.get('product_key'),
                                    'unit_price': self.product_details[values.get('product_key')].get('product_unit_price'),
                                    'quantity': values.get('quantity'),
                                    'subtotal': total,
                                    'state': 'Draft'
                                    })
        return cust_key, order_lines, order_total_amount

    def display_details(self):
        cust_key = False
        order_line = []
        customer = True
        product = True

        while customer:
            print("{:<8} {:<25}".format('Customer_Key', 'Customer_name'))
            for key, value in self.customer_details.items():
                print("{:<8} {:<25} ".format(key, value.get('customer_name')))

            selected_customer = input("Select customer key for choose the customer")
            if selected_customer in self.customer_details.keys():
                cust_key = selected_customer
                customer = False
            else:
                print("Inserted customer is wrong")
                print("1. Want to select again customer")
                print("2. Exit")
                option = int(input("select option"))
                if option == 2:
                    customer = False
                    product = False

        while product:
            print("{:<8} {:<25}".format('Product_Key', 'Product_Name'))
            for key, value in self.product_details.items():
                print("{:<8} {:<25} ".format(key, value.get('product_name')))

            selected_product = input("Select Product key for order")
            if selected_product in list(self.product_details.keys()):
                quantity = input("Entry Quantity")
                order_line.append({'product_key': selected_product, 'quantity': quantity})
                print("1. do you want to place more order?")
                print("2. exit")
                more_product = int(input("select option"))
                if more_product == 2:
                    product = False
            else:
                print("Inserted product is wrong")
                print("1. Want to select again product")
                print("2. Exit")
                option = int(input("select option"))
                if option == 2:
                    product = False
                    cust_key = False
        return cust_key, order_line

    def create_order(self, cust_key, order_lines, order_total_amount):
        """
        store the order details in their dictionary
        :param : order_value to store dictionary
        :return:
        """
        order_key = False
        if cust_key is not False:
            index = 1 if bool(self.sales_order_details) == False else int(list(self.sales_order_details.keys())[0][-1]) + 1
            order_key = 'SO_' + str(index)
            self.sales_order_details.update({order_key:
                                                 {
                                                     'customer': cust_key,
                                                     'order_lines': order_lines,
                                                     'order_date': date.today(),
                                                     'state': 'Draft',
                                                     'order_total_amount': order_total_amount
                                                 }})
            for key, value in self.sales_order_details.items():
                print(key, value)
        return order_key

    def update_state(self, update_state):
        while True:
            for key, values in self.sales_order_details.items():
                print(key,values)
            selected_order = input("Select Order of update order state")
            exist_state = self.sales_order_details[selected_order].get('state')
            if selected_order in list(self.sales_order_details.keys()):
                if update_state == 'Draft':
                    if exist_state == 'Cancel':
                        self.sales_order_details[selected_order]['state'] = update_state
                        self.sales_order_details[selected_order]['order_lines']['state'] = update_state
                    else:
                        print("state should be cancel")
                elif update_state == 'Confirm':
                    if exist_state == 'Draft':
                        self.sales_order_details[selected_order]['state'] = update_state
                        for key in self.sales_order_details[selected_order]['order_lines']:
                            key['state'] = update_state
                    else:
                        print("state should be draft")
                elif update_state == 'Done':
                    if exist_state == 'Confirm':
                        self.sales_order_details[selected_order]['state'] = update_state
                        self.sales_order_details[selected_order]['order_lines']['state'] = update_state
                    else:
                        print("state should be confirm")
                else:
                    if exist_state != 'Done':
                        self.sales_order_details[selected_order]['state'] = update_state
                        self.sales_order_details[selected_order]['order_lines']['state'] = update_state
                    else:
                        print("done order can't be cancel")
                break
            else:
                print("Please select proper Product Key")

    def orderdata(self):
        for key , value in self.sales_order_details.items():
            print(key,value)

sale_order = Sales_order()

while True:
    print("\nMAIN MENU")
    print("1. Add Product")
    print("2. Update Product Stock")
    print("3. Add Customer")
    print("4. Generate Sales order")
    print("5. Change Order to confirm")
    print("6. Change Order to Done")
    print("7. Change Order to Cancel")
    print("8. Change Order to Draft")
    print("9. Print sale order")
    print("0. Exit")
    selected_menu = int(input("Select Menu Number:"))

    if selected_menu == 1:
        sale_order.manage_product()

    elif selected_menu == 2:
        sale_order.update_stock()

    elif selected_menu == 3:
        sale_order.manage_customer()

    elif selected_menu == 4:
        sale_order.manage_order()

    elif selected_menu == 5:
        sale_order.update_state('Confirm')

    elif selected_menu == 6:
        sale_order.update_state('Done')

    elif selected_menu == 7:
        sale_order.update_state('Cancel')

    elif selected_menu == 8:
        sale_order.update_state('Draft')

    elif selected_menu == 9:
        sale_order.orderdata()

    elif selected_menu == 0:
        break

    else:
        print("Please Select Proper Menu..")

