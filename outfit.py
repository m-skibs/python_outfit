import sys
import json
import requests

from secrets import api_key

class outfit():

    #initialize and take in zip code
    def __init__(self):
        self.zip = str(sys.argv[1])
        self.faren = 0
        self.shirt = ''
        self.pants = ''
        self.accessories = ''

    #get temperature data
    def get_temp_data(self):
        req_url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}'.format(self.zip, api_key)
        response = requests.get(req_url)
        data_dictionary = response.json()
        self.kelvin = data_dictionary['main']['feels_like']

    #convert temperature to farenheit
    def kelvin_to_farenheit(self):
        self.get_temp_data()
        self.farenheit = (1.8 * (self.kelvin - 273)) + 32

    #recommend shirt
    def get_shirt(self):
        f = int(self.farenheit)
        if f > 72:
            self.shirt = ('tank top')
        elif f > 55 and f <= 72:
            self.shirt = ('short sleeves')
        elif f >= 40 and f <= 55:
            self.shirt = ('long sleeves')
        else:
            self.shirt = ('sweater')
        
    #recommend pants
    def get_pants(self):
        if int(self.farenheit) > 58:
            self.pants = ('shorts')
        else:
            self.pants = ('long pants')

    #recommend accessories
    def get_accessories(self):
        f = int(self.farenheit)
        if f < 40 and f > 32:
            self.accessories = ('hat')
        elif f <= 32:
            self.accessories = ('hat and gloves')
        else:
            self.accessories = ''

    #consolidate and print out recommendations
    def assemble_outfit(self):
        self.kelvin_to_farenheit()
        self.get_shirt()
        self.get_pants()
        self.get_accessories()
        print('')
        print('temperature feels like ' + str(self.farenheit) + ' F')
        print(self.shirt)
        print(self.pants)
        print(self.accessories)

my_outfit = outfit()
my_outfit.assemble_outfit()
