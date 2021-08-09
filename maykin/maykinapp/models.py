from django.db import models
from django.utils import tree

class City(models.Model):
    """ city names and code are always unique and we do not want to store null values """
    city_code = models.CharField(max_length=3, default='CIT', null=False, unique=True) # as the city codes given in CSV are of max 3 char long
    city_name = models.CharField(max_length=86, default='Default City', null=False, unique=True)  #86 because longest name of city is 85 char max # Guinness World Record 

   
    def __str__(self) -> str:
        return self.city_code

class Hotel(models.Model):
    """ we have provided default values so that they are not null """
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)  # link to the city
    ''' city hotel code must be unique as its a number with short code relative to city '''
    city_hotel_code = models.CharField(max_length=3, default='CHC', null=False, unique=True) # city code with hotel number
    ''' hotel name always must be unique '''
    hotel_name = models.TextField(default='Default hotel name', null=False, unique=True) # this is text field hotel name can be long 

    def __str__(self) -> str:
        return str(self.city_hotel_code)+": "+str(self.hotel_name)