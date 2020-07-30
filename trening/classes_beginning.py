class Building():
    def __init__(self,name):
        self.name = name
    def itis(self):
        print("This is a building")

class Skyscrapper(Building):
    def __init__(self,name,projectname):
        super().__init__(name)   
        self.projectname = projectname
    def new_method(self):
        print("This is a Skyscrapper")
    def math(self,name,projectname):
        return self.projectname+self.name

def build(building):
    return building.name

house = Building("Neofuturism")
city_house = Skyscrapper("Neofuturism","Tower")

city_house.itis()
print(city_house.name,city_house.projectname)
print(city_house.math(city_house.name,city_house.projectname))