def make_car(manu,model,**car_items):
    car={}
    car['manufacturer']=manu
    car['model']=model
    for key,value in car_items.items():
        car[key]= value
    return car

car =make_car('Honda','Civic',variant='Oreal',color='Grey')
print (car)