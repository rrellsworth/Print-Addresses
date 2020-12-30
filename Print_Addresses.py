import csv
from Options import *

# Default Options:
FILE_NAME = "Address_Template.csv"
OUTPUT = "ALL"


class Fields:
    def __init__(self):
        # Indexes:
        self.output_idx = None
        self.first_name_idx = None
        self.last_name_idx = None
        self.street_idx = None
        self.city_idx = None
        self.state_idx = None
        self.zipcode_idx = None
        self.country_idx = None
        
    def check_fields(self):
        prompt = False
        if (self.output_idx == None):
            print(" ! No Print Option Field")
            prompt = True
        elif (self.first_name_idx == None):
            print(" ! No First Name Field")
            prompt = True
        elif (self.last_name_idx == None):
            print(" ! No Last Name Field")
            prompt = True
        elif (self.street_idx == None):
            print(" ! No Street Field")
            prompt = True
        elif (self.city_idx == None):
            print(" ! No City Field")
            prompt = True
        elif (self.state_idx == None):
            print(" ! No State Field")
            prompt = True
        elif (self.zipcode_idx == None):
            print(" ! No Zipcode Field")
            prompt = True
        elif (self.country_idx == None):
            print(" ! No Country Field")
            prompt = True
        else:
            print("All Fields Located...\n")
            
        if (prompt):
            user = input("\nDo you wish to continue? (y/n) ").lower()
            if (user == "y"):
                return True
            else:
                return False
        else:
            return True
        
    def set_field_idx(self, field, index):
        def set_output_idx(self, i):
            self.output_idx = i
        def set_first_name_idx(self, i):
            self.first_name_idx = i
        def set_last_name_idx(self, i):
            self.last_name_idx = i
        def set_street_address_idx(self, i):
            self.street_idx = i
        def set_city_idx(self, i):
            self.city_idx = i
        def set_state_idx(self, i):
            self.state_idx = i
        def set_zipcode_idx(self, i):
            self.zipcode_idx = i
        def set_country_idx(self, i):
            self.country_idx = i
            
        switch = {
            "print? (y/n)" : set_output_idx,
            "first name" : set_first_name_idx,
            "last name" : set_last_name_idx,
            "street address" : set_street_address_idx,
            "city" : set_city_idx,
            "state" : set_state_idx,
            "zipcode" : set_zipcode_idx,
            "country" : set_country_idx
            }
        
        func = switch.get(field, lambda x=None: print("Field input '"  + field + "' does not match"))
        func(self, index)


class Address:
    def __init__(self, first_name, last_name, street_address, city, state, zipcode, country):
        self.first_name = first_name
        self.last_name = last_name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country
        
    def get(self):
        string = (self.first_name + " " + self.last_name + "\n" +
                  self.street_address + "\n" +
                  self.city + " " + self.state + ", " + self.zipcode + " " + self.country)
        return string
    

def clean_string(str):
    out_str = str
    if "  " in out_str:
        out_str = out_str.replace("  ", " ")
    else:
        return out_str


def main():
    address_list = []
    field_properties = Fields()
    
    with open(FILE_NAME, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        
        # Arange Field Order:
        for i in range(len(fields)):
            field_properties.set_field_idx(fields[i].lower(), i)  
    
        user = field_properties.check_fields()
        if (user):
            for row in csvreader:
                if (OUTPUT == "ALL" or OUTPUT == row[field_properties.output_idx].lower):
                    address_list.append(Address(first_name=row[field_properties.first_name_idx],
                                                last_name=row[field_properties.last_name_idx],
                                                street_address=row[field_properties.street_idx],
                                                city=row[field_properties.city_idx],
                                                state=row[field_properties.state_idx],
                                                zipcode=row[field_properties.zipcode_idx],
                                                country=row[field_properties.country_idx]))
            for i in address_list:
                print(i.get() + "\n")
        else:
            print("END")
  
  
if __name__ == "__main__":
    main()
