import datetime as dt
from datetime import timedelta, datetime
import pandas as pd
from geopy.geocoders import Nominatim


################################################################################
# Get age from birthdate.
################################################################################
def calc_age(birthdate):
    """ This function calculates the age of an individual using their birthdate.
    
    Args:
        **birthdate** (string): The birthday of the individual.
            
    Returns:
        **age** (int): The age of the individual.
    
    
    """
    
    birth_year,birth_month,birth_day = birthdate.split('-')
    born = dt.datetime(int(birth_year),int(birth_month),int(birth_day))
    today = datetime.now()
    age= today.year-born.year - ((today.month,today.day) < (born.month, born.day))

    return age



################################################################################
# Converts a string to a datetime object.
################################################################################
def get_date_from_string(datestring):
    """ This function converts the date as a string to a datetime object.
    
    Args:
        **datestring** (string): the date as a string.
    
    Returns: 
        **date** (datetime object): the date as a datetime object.
        
    """
    
    date=pd.to_datetime(datestring)
    return date



################################################################################
# Converts zip code to coordinates.
################################################################################
def convert_to_coordinates(zip_code):
    """ Converts the list of zip codes to latitude and ongitude coordinates. 
    
    Args:
        **zip_code** (string): The zip code to be converted.
        
        
    Return:    
        **location.latitude** (float): The latitude corrdinate of the zip code.
        
        **location.longitude** (float): The longitude coordinate of the zip code.

    """
    geolocator = Nominatim()

    zc=str(int(zip_code))

    zipState=zc + ", New York"
    location = geolocator.geocode(zipState, timeout=10)
    if (location !=None):
        return location.latitude, location.longitude        
        
        
################################################################################
################################################################################
def pretty_print(inds,dump_all=False):
    """ This function prints the dictionaries passed to it in a way that is very easy to read.
    
    Args:
        **inds** (list): The list of dictionaries that 
        **dump_all** (bool): If True, this shows the category name. If False, this function just prints out the numerical values without the decription.
        
        
    """

    if type(inds)==dict:
        inds = [inds]

    for ind in inds: 
        print("================================")
        print((ind['Personal ID']))
        #print((ind['Age']))
        print((ind['DOB']))
        for program in ind['Programs']:
            #print "------"
            output = ""
            if dump_all:
                for key in program:
                    output += "%-15s: %-15s " % (key,program[key])
                #output += "\n"
            else:
                output += "%-35s " % (program["Project type"])
                output += "%s: %-10s - %-10s " % ("In/Out",program["Admission date"], program["Discharge date"])
                output += "(%s days) " % (program["Length of stay"].days)
                output += "\t Zip code: %s" % (program['Project Zip Code'])
                #output += "\n"


            print(output)


################################################################################
################################################################################
