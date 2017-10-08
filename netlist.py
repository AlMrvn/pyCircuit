from numpy import *
import networkx as nx

class element():
    """ Electrocinetic element. Define an element type between two nodes n1 and n2"""
    def __init__(self,type,id, n1,n2, value):
        self.type = type
        self.id = id
        self.n1 = n1
        self.n2 = n2
        self.value = value
    def spice(self):
        return('{0}{1} {2} {3} {4}'.format(self.type,self.id,self.n1, self.n2, self.value))
        
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
            print(e.spice())
        print('.end')
    def save(self,filename):
        f = open(filename,'w')
        f.write(self.name + '\n')
        for e in self.dict_component.values():
            f.write(e.spice()+'\n' )
        f.write('.end')
        f.close()    
        
    def capacitor(self):
        """ return the list of all the capacitor of the circuit """
        return [ e for e in self.dict_component.values() if e.type=='C']
    def capacitor_graph(self):
        """ return the capacitor graph of the circuit """
        G = nx.Graph()
        for cap in self.capacitor():
            G.add_edge(cap.n1, cap.n2, name = cap.type + str(cap.id), value = cap.value )
        return G
    def inductor_graph(self):
        """ return the capacitor graph of the circuit """
        G = nx.Graph()
        for cap in self.inductor():
            G.add_edge(cap.n1, cap.n2, name = cap.type + str(cap.id), value = cap.value )
        return G
    def inductor(self):
        """ return the list of all the inductor of the circuit """
        return [e for e in self.dict_component.values() if e.type=='L']

def load_circuit(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    c = circuit(lines[0])
    for i in range(1, len(lines) - 1):
        u = lines[i].split(' ')
        name = u[0]
        e = element(u[0][0], u[0][1], u[1], u[2], u[3])
        c.add_element(u[0],e)
    return c        
    
if __name__=='__main__':
    e = element('R',1, 0,1,1e3)
    print(e.spice())
    c = circuit('Example of circuit')
    c.C(1,0,1,350e-6)
    c.L(1,0,1,2)
    c.R(1,0,1,1)
    c.C(2,0,2,350e-6)
    c.C(3,1,2,50e-6)
    c.spice_print()
    c.save('test.txt')
    C_graph = c.capacitor_graph()

