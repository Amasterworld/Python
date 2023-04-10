#length class in Python Course Bodenseo Data analys
#implement a class, namely Length to convert the length to meter
#for example : x = Length(100, "cm") +Length(1) = 1,1m
#Solution: we use  hashtable<string, double> (dict)  to contain key is unit, double 
# or int contains the values


class Length:
    # note  __var that means it is private var
    __metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "1km" : 1000, "in" : 0.0254, "ft": 0.3048, "yd": 0.9144, "mi":1609.344}
    
    #like constructor in C++
    def __init__(self, value, unit ='m') -> None:
        self.value = value
        self.unit = unit
    #converter to meter
    def convert2meter(self):
        #not like C++ in Python we can use name_of_class to access its var or function
        
        return self.value * Length.__metric[self.unit]
    
    #what if we want to write like this: Length(4.08, "yd") + Length(2, "yd") = ?m
    #we should define  operator+ -> __add__
    def __add__(self, other):
        
        l = self.convert2meter() + other.convert2meter()
        # convert l in meter to the original unit
        return Length(l/ Length.__metric[self.unit], self.unit)
          
    #in main if we want to conver x = Length(3,"cm"); so we have to
    #  write: print(x.convert2meter()), it is a bit unconvinience, to solve this problem we can do:
    def __str__(self):
        return str(self.convert2meter())

    def __repr__(self):
        return "Length ("+str(self.value) + ", '" + self.unit +"')" 

    #now what if we want to:  z = Length(1.2,"mi"); then we want to have:  z += Length(1.1,"mi"); we should define __iadd__

    def __iadd__(self, other):
        l = self.convert2meter() + other.convert2meter()
        return Length(l/Length.__metric[self.unit], self.unit)
if __name__ == '__main__':

    x = Length(1,"mi")
    print(x)
    y = Length(2.0, "yd") +  Length(1, "m")
    print(y) #note that when write only print(y) -> def __str__(self) is executed
    #then it convert the current value and its unit to meter
    print(repr(y)) #  def __repr__(self) -> is executed then return current value (in string type) + its unit

    x += Length(2000,"cm")
    print(x)
    

