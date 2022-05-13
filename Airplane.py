class Boat:
    def __init__(self,ID,seater,boatType,schedule1,schedule2):
        self.ID = ID
        self.seater = seater
        self.boatType = boatType
        self.occupied1=0
        self.occupied2=0
        self.schedule1 = schedule1
        self.schedule2 = schedule2
    def addSeat(self,time,num):
      if(self.schedule1==time):
        if(self.occupied1+num<=self.seater):
          self.occupied1+=num
          return True
        else:
          return False
      elif (self.schedule2==time):
        if(self.occupied2+num<=self.seater):
          self.occupied2+=num
          return True
        else:
          return False
    
    def getSchedule1(self):
      return self.schedule1
      
    def getSchedule2(self):
      return self.schedule2
      
    def printBoat(self):
      print(self.ID,"\t",self.seater,"\t",self.boatType,"\t",self.occupied1,"\t",self.occupied2)

class Booking:
  def __init__(self):
    self.BoatList=[]
  def addBoat(self,boat):
    self.BoatList.append(boat)
  def bookSeat(self,time,num):
    booked = False
    for i in range(10):
      if(self.BoatList[i].getSchedule1()==time):
        booked=self.BoatList[i].addSeat(time,num)
        if booked==True:
          print("Seat booked")
        return
        if(self.BoatList[i].getSchedule2()==time):
          booked=self.BoatList[i].addSeat(time,num)
          if booked==True:
            print("Seat booked")
        return
        if booked==False:
          print("Seat not available")

  def menu(self):
    print("P-to Purchase Ticket")
    print("V-to View Seating Arrangement")
    print("Q-To Quit the system")

  def input(self):
    choice=0
    classs=0
    while choice!="Q":
      self.menu()
      choice =input("Enter choice:")
      if(choice=="P"):
          print("B-to purchase ticket for business class")
          print("E-to purchase ticket for Economy class")
          print("M-to return to main Menu")
          classs=input("Enter Choice: ")
          if(classs=="B" or classs=="E"):
              time = int(input("Enter schedule time(8,10,12,2)pm:  "))
              num = int(input("Enter number of seats:"))
              self.bookSeat(time,num)
      if(choice=="V"):
        self.printBoat()
      
  def printBoat(self):
    print("ID\t Seater\tBoatType\tSchedule1\tSchedule2")
    for i in range(10):
      self.BoatList[i].printBoat()


b1 = Boat(11,4,"B1",8,12)
b2 = Boat(12,8,"E1",8,12)
b3 = Boat(13,8,"E1",8,12)
b4 = Boat(14,8,"B1",8,12)
b5 = Boat(15,8,"E1",8,12)
b6 = Boat(16,8,"E1",10,2)
b7 = Boat(17,8,"B1",10,2)
b8 = Boat(18,8,"E1",10,2)
b9 = Boat(19,8,"B1",10,2)
b10 = Boat(20,8,"E1",10,2)

B = Booking()
B.addBoat(b1)
B.addBoat(b2)
B.addBoat(b3)
B.addBoat(b4)
B.addBoat(b5)
B.addBoat(b6)
B.addBoat(b7)
B.addBoat(b8)
B.addBoat(b9)
B.addBoat(b10)

B.input()
