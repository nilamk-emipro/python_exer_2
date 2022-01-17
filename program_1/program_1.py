from tabulate import tabulate

class ManuFacturing:
    def __init__(self, raw_material_product, raw_material_ratio, finished_product, raw_material_qty, finished_qty):
        self.raw_material_product = raw_material_product
        self.finished_product = finished_product
        self.raw_material_ratio = raw_material_ratio
        self.raw_material_qty = 0 if(raw_material_qty is None) else raw_material_qty
        self.finished_qty = 0 if(finished_qty is None) else finished_qty

    def produce(self, req_produce_qty):
        """
        :param req_produce_qty is parameter use for how many items want to produce :
        :return: none
        """
        if (self.raw_material_qty / self.raw_material_ratio) < req_produce_qty:
            print("Not enough raw material available to produce bicycle, please do the purchase")
        else:
            self.raw_material_qty = self.raw_material_qty-(req_produce_qty*self.raw_material_ratio)
            self.finished_qty = self.finished_qty+req_produce_qty
            print("production is done.")

    def display_raw_material_stock(self):
        """
        :return:
        """
        # print("Raw_material stock is ", self.raw_material_qty)
        # print("{:<10} {:<500}".format('RawMaterial_Product', 'Quantity'))
        # print("{:<10} {:<500}".format(self.raw_material_product, self.raw_material_qty))
        print(tabulate([[self.raw_material_product,self.raw_material_qty]], headers=['RawMaterial_Product', 'Quantity']))

    def display_finished_product_stock(self):
        """

        :return:
        """
        print(tabulate([[self.finished_product, self.finished_qty]], headers=['Finished_Product', 'Quantity']))

    def purchase_raw_material(self, purchased_raw_material):
        """

        :param purchased_raw_material:
        :return:
        """
        self.raw_material_qty = self.raw_material_qty + int(purchased_raw_material or 0)

manu_fac = ManuFacturing("Wheel", 2, "Bicycle", None, None)

while True:

    print("\nMAIN MENU")
    print("1. Purchase RawMaterial Product")
    print("2. Manufacture Finish Product")
    print("3. Show RawMaterial Quantity")
    print("4. Show Actual Product Quantity")
    print("5. Exit")
    selectedMenuNo = int(input("Enter the number:"))

    if selectedMenuNo == 1:
        raw_mat_qty = input("How many RawMaterial Quantity want to purchase?")
        manu_fac.purchase_raw_material(raw_mat_qty)

    elif selectedMenuNo == 2:
        produce_qty = int(input("How many Quantity Produce?"))
        manu_fac.produce(produce_qty)

    elif selectedMenuNo == 3:
        manu_fac.display_raw_material_stock()

    elif selectedMenuNo == 4:
        manu_fac.display_finished_product_stock()

    elif selectedMenuNo == 5:
        break

    else:
        print("Please Select Proper Menu..")

