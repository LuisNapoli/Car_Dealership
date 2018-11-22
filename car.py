class Car:
    def __init__(self,brand,model,year,price,plate):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.plate = plate
        self.buyer = None
        self.seller = None

    def sell(self,buyer,seller):
        self.buyer = buyer
        self.seller = seller

    def get_model(self):
        return self.model

    def get_sale(self):
        return f'Buyer: {self.buyer.get_name()} / Seller: {self.seller.get_name()}'

    def get_data(self):
        return self.brand, self.model, self.year, self.price, self.plate
