# Class 1
class Nigeria():
    def capital(self):
        print("Abuja is the capital of Nigeria.")
 
    def language(self):
        print("Yoruba is the most widely spoken language of Nigeria.")
 
    def type(self):
        print("Nigeria is a developing country.")
 
# Class 2
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 
# Object Creation
obj_Nig = Nigeria()
obj_usa = USA()

# Common Interface
for country in (obj_Nig, obj_usa):
    country.capital()
    country.language()
    country.type()