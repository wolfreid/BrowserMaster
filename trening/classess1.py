class Duck():
    def __init__(self,name):
        self.hidden_name = name             #hidden_name is a private name
    def get_name (self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self,name):
        print("inside the setter")
        self.hidden_name = name
    name = property(get_name, set_name)



class Fuck():
    def __init__(self,input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self,input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck('Howard')
fowl.name = 'Daffy'
# fowl.name('Maffy') #работает чисто сеттер
print(fowl.name) #обрабатывается геттером 



def funcname(self, parameter_list):
    def sadas():



# class human():
#     def __init__(self,name):
#         self.name = name 
#     def exclaim(self):
#         print("I am a human")

# class sex(human):
#     def need_a_push(self):
#         print("opa")

# persona = human("Elisa")
# character = sex("John")

# human.exclaim(human)
# character.exclaim()
# print(character.name,persona.name)

# # class Person():
# #     def __init__(self,name):
# #         self.name = name

# # class EmailPerson(Person):
# #     def __init__(self,name,email):
# #         super().__init__(name)# the super gets the definition of the parent class,Person
# #         self.email = email

# # one = Person("Igor")
# # check = EmailPerson("John","Bob")
# # print(one.name,check.name,check.email)

