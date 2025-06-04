from abc import ABC, abstractmethod 
'''
# ABC stand for abstract base classes

class vehicle(ABC): 
# As far as I understand this an abstarct class, hasnt a shape but only a meaning like space vectorial is abstarct but hilbert space has a shape and sense 
 # @: decorator
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def back(self):
        pass

#V_object = vehicle() ==> TypeError: Can't instantiate abstract class vehicle without an implementation for abstract methods 'back', 'go'
# Its like u want to create a controler to something does not exist only in your mind, children classes will do the work for ya

class  car(vehicle):
# TypeError: Can't instantiate abstract class car without an implementation for abstract method 'back'
# look at this if take a class inherite from the abstarct class and you dont call the methods in the abstract class it will not work
    def go(self):
        print('Car is moving')

    def back(self):
        print('Car is reversing')

    def stop(self):
        print('car is stopping')

car = car()

car.go()
car.back()
car.stop()
'''
############################################################

#Code structure

# Define the product interference
class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Implement Concrete Product

class Esspresso(Coffee):

    def prepare(self):
        
        return 'Preparing for you Esspresso coffee'
    
class Latte(Coffee):

    def prepare(self):
        
        return 'Preparing for you Latte coffee'
    
class Coppucino(Coffee):

    def prepare(self):
        
        return 'Preparing for you Coppucino coffee'

# Implement the factory (Coffee Machine)

class Factory:

    def Product(self, coffe_type):

        if coffe_type == 'Esspresso':

            return Esspresso().prepare()
        
        elif coffe_type == 'Latte':
            
            return Latte().prepare()
        
        elif coffe_type == 'Coppucino':
            
            return Coppucino().prepare()
        
        else:
            return 'The fuck is this coffee you want?'
    
# Use the facatory to create product

if __name__ == '__main__':

    obj = Factory()

    coffee = obj.Product('Esspresso')
    print(coffee)
    
    coffee = obj.Product('Latte')
    print(coffee)

    coffee = obj.Product('Coppucino')
    print(coffee)

    coffee = obj.Product('arabasta')
    print(coffee)