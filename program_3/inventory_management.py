from tabulate import tabulate


class InventoryManagement:
    def __init__(self, product_qty=0):
        self.product_qty = product_qty

    def purchase(self, purchase_qty):
        """
        :param : is use for how many items want to purchase
        :return: none
        """
        self.product_qty += purchase_qty

    def sale(self, sale_qty):
        """
        :param : sale_qty is use for how many items want to sale
        :return: none
        """
        if self.product_qty >= sale_qty:
            self.product_qty -= sale_qty
        else:
            print("product is not enough available to sale")

    def display_available_product(self):
        """
        :return: view how many Product available
        """
        print(tabulate([['Product', self.product_qty]], headers=['Product', 'Quantity']))


InvMan = InventoryManagement()
while True:

    print("\nMAIN MENU")
    print("1. Purchase Product")
    print("2. Sale Product")
    print("3. View Available Product Quantity")
    print("0. Exit")
    selectedMenuNo = int(input("Enter the number:"))

    if selectedMenuNo == 1:
        purchase_qty = input("How many Quantity want to purchase?")
        InvMan.purchase(int(purchase_qty or 0))

    elif selectedMenuNo == 2:
        sale_qty = input("How many Quantity want to sale?")
        InvMan.sale(int(sale_qty or 0))

    elif selectedMenuNo == 3:
        InvMan.display_available_product()

    elif selectedMenuNo == 0:
        break

    else:
        print("Please Select Proper Menu..")

