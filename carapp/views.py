
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import FilterForm
from .models import *
from django.db.models import Avg
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

def index(request):
    form = FilterForm(request.POST or None)
    context = {
        'query_search':False,
        'form':form
    }
    if request.method == 'POST':
        year_make_model=request.POST.get('year_make_model')
        mileage=request.POST.get('mileage')
        print(year_make_model)
        print(mileage)
        splitted_list=year_make_model.split(" ")
        try:
            q_year=splitted_list[0]
        except:
            q_year=0
        make=splitted_list[1]
        model=splitted_list[2]
        make_input = "%%%s%%" % make
        model_input = "%%%s%%" % model
        similar_cars=CarData.objects.raw('SELECT cs.* FROM car_data cs where (cs.year  = %s OR %s =0) and coalesce(cs.make,"") like  %s ' +
        ' and coalesce(cs.model,"") like %s order by cs.listing_mileage desc,cs.listing_price desc limit 100;',
        [q_year,q_year,make_input,model_input])
        #similar_cars=CarData.objects.filter(year=q_year,make__like=make_input,model__like=model_input)[:100] 
        print(similar_cars)

        def computepricefromMileage(x):
            print(float(slope),float(x),float(intercept))
            return slope * np.float64(x) + intercept

        if mileage == '':
            print("mileage is empty")
            average_price=0
            for each_car in similar_cars:
                if each_car.listing_price=="":
                    each_car.listing_price=0
                average_price=average_price+int(each_car.listing_price)
            average_price=average_price/len(similar_cars)  
            #average_price=similar_cars.aggregate(Avg('listing_price'))
        else:
            list_of_prices=[]
            list_of_mileage=[]
            for each_car in similar_cars:
                try:
                    list_of_prices.append(int(each_car.listing_price))
                except:
                    list_of_prices.append(0)
                try:
                    list_of_mileage.append(int(each_car.listing_mileage))
                except:
                    list_of_mileage.append(0)
            print(list_of_prices)
            print(list_of_mileage)
            slope, intercept, r, p, std_err = stats.linregress(list_of_mileage, list_of_prices)
            print(slope)
            print(intercept)
            average_price=computepricefromMileage(mileage)

        context = {
        'query_search':False,
        'form':form,
        'similar_cars':similar_cars,
        'average_price':int(average_price)
        }
    
    return render(request, 'carapp/filterform.html', context=context)
