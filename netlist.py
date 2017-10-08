from numpy import *

class element():
    def __init__(self,type,id, n1,n2, value):
        self.type = type
        self.id = id
        self.n1 = n1
        self.n2 = n2
        self.value = value
    def spice_print(self):
        print( '{0}{1} {2} {3} {4}'.format(self.type,self.id,self.n1, self.n2, self.value))
        
        
class circuit():
    """ The circuit is a collection of component """
    def __init__(self,name,dict_component={}):
        self.dict_component = dict_component
        self.name = name        
    def add_element(self, name, element):
        """ add an element bewteen node_1 and node 2"""
        self.dict_component[name] = element
    def C(self,id,n1,n2,value):
        """ add a Capacitor between node n1 and node n2. """
        self.dict_component['C{0}'.format(id)] = element('C',id,n1,n2,value)
    def L(self,id,n1,n2,value):
        """ add a inductor between node n1 and node n2. """
        self.dict_component['L{0}'.format(id)] = element('L',id,n1,n2,value)
    def R(self,id,n1,n2,value):
        """ add a resistor between node n1 and node n2. """
        self.dict_component['R{0}'.format(id)] = element('R',id,n1,n2,value)        
    def spice_print(self):
        print(self.name)
        for e in self.dict_component.values():
            e.spice_print()
        print('.end')
    def capacitor(self):
        """ return the list of all the capacitor of the circuit """
        return [ e for e in self.dict_component.values() if e.type=='C']
    def inductor(self):
        """ return the list of all the inductor of the circuit """
        return [e for e in self.dict_component.values() if e.type=='L']
            
            
if __name__=='__main__':
    e = element('R',1, 0,1,1e3)
    e.spice_print()
    c = circuit('Example of circuit')
    c.C(1,0,1,350e-6)
    c.L(1,0,1,2)
    c.R(1,0,1,1)
    c.spice_print()
    for l in c.inductor():
        l.spice_print()