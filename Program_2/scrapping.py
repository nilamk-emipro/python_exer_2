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
        :param : req_produce_qty is parameter use for how many items want to produce
        :return: none
        """
        if (self.raw_material_qty / self.raw_material_ratio) < req_produce_qty:
            print("Not enough raw material available to produce bicycle, please do the purchase")
        else:
            self.raw_material_qty -= (req_produce_qty*self.raw_material_ratio)
            self.finished_qty += req_produce_qty
            print("production is done.")

    def display_raw_material_stock(self):
        """
        :return: view how many raw material available
        """
        # print("Raw_material stock is ", self.raw_material_qty)
        # print("{:<10} {:<500}".format('RawMaterial_Product', 'Quantity'))
        # print("{:<10} {:<500}".format(self.raw_material_product, self.raw_material_qty))
        print(tabulate([[self.raw_material_product, self.raw_material_qty]], headers=['RawMaterial_Product', 'Quantity']))

    def display_finished_product_stock(self):
        """
        :return: view how many finished product available
        """
        print(tabulate([[self.finished_product, self.finished_qty]], headers=['Finished_Product', 'Quantity']))

    def purchase_raw_material(self, purchased_raw_material):
        """
        :param purchased_raw_material: is use to purchase raw material
        :return:none
        """
        self.raw_material_qty += purchased_raw_material


class Scrapping(ManuFacturing):

    def __init__(self, raw_material_product, raw_material_ratio, finished_product, raw_material_qty, finished_qty):
        ManuFacturing.raw_material_product = raw_material_product
        ManuFacturing.finished_product = finished_product
        ManuFacturing.raw_material_ratio = raw_material_ratio
        ManuFacturing.raw_material_qty = 0 if (raw_material_qty is None) else raw_material_qty
        ManuFacturing.finished_qty = 0 if (finished_qty is None) else finished_qty

    def scrapping_raw_material(self, scrapping_raw_material):
        """
        :param : scrapping_raw_material is use for generate scrap from raw material
        :return: none
        """
        if self.raw_material_qty >= scrapping_raw_material:
            self.raw_material_qty -= scrapping_raw_material
        else:
            print("RawMaterial is not enough available to generate scrap")

    def scrapping_finish_product(self, scrapping_finish_product):
        """
        :param : scrapping_finish_product is use to generate scrap form finished product
        :return: none
        """
        if self.finished_qty >= scrapping_finish_product:
            self.finished_qty -= scrapping_finish_product
        else:
            print("Finished product is not enough available to generate scrap")


Scrap = Scrapping("Wheel", 2, "Bicycle", None, None)
while True:

    print("\nMAIN MENU")
    print("1. Purchase RawMaterial Product")
    print("2. Manufacture Finish Product")
    print("3. Show RawMaterial Quantity")
    print("4. Show Actual Product Quantity")
    print("5. Scrapping the raw material product")
    print("6. Scrapping the finished product")
    print("0. Exit")
    selectedMenuNo = int(input("Enter the number:"))

    if selectedMenuNo == 1:
        raw_mat_qty = input("How many RawMaterial Quantity want to purchase?")
        Scrap.purchase_raw_material(int(raw_mat_qty or 0))

    elif selectedMenuNo == 2:
        produce_qty = input("How many Quantity Produce?")
        Scrap.produce(int(produce_qty))

    elif selectedMenuNo == 3:
        Scrap.display_raw_material_stock()

    elif selectedMenuNo == 4:
        Scrap.display_finished_product_stock()

    elif selectedMenuNo == 5:
        scrap_raw_qty = input("How many scraped from RawMaterial?")
        Scrap.scrapping_raw_material(int(scrap_raw_qty))

    elif selectedMenuNo == 6:
        scrap_finish_qty = input("How many scraped from Finished ?")
        Scrap.scrapping_finish_product(int(scrap_finish_qty))

    elif selectedMenuNo == 0:
        break

    else:
        print("Please Select Proper Menu..")

