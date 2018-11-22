from dealership import Dealership
from car import Car
from seller import Seller
from buyer import Buyer

deal = Dealership('Brasal')
pol = Car('VW','Polo',2019,60000,'MTO1337')
gti = Car('VW','Golf',2018,80000,'MLR0003')
amk = Car('VW','Amarok',2018,130000,'MED4551')
deal.add_car(pol)
deal.add_car(amk)

for cr in deal.get_cars():
    print(cr.get_data())

sel = Seller('Bill','1955')
buy = Buyer('Elon','06281971')

pol.sell(sel,buy)
print(pol.get_sale())
deal.save_cars()