class bird:
  def setdata(self):
    self.colour=input("enter the input for color ")
    self.weight=input("enter the input for weight ")
    self.behaviour=input("enter the input for behaviour ")
  def display(self):
    print("colour: ", self.colour)   
    print("weight: ", self.weight)    
    print("behaviour: ", self.behaviour) 

class peackock(bird):
    def setdata(self):
      self.flyingheight=input("enter the flying height: ")
    def display(self):  
      print("flying height of eagle is: ",self.flyingheight)

class eagle(bird):
    def setdata(self):
      self.flyingheight=input("enter the flying height: ") 
    def display(self):      
      print("flying height of eagle is: ",self.flyingheight)
 
     

a=bird()
a.setdata()
a.display()

b=peackock()
b.setdata()
b.display()

c=eagle()
c.setdata()
c.display()