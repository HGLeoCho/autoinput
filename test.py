class PrimarySIM:
  def __init__(self, VoLTE_able, number, CID):
    self.VoLTE_able = VoLTE_able
    self.number = number
    self.CID = CID
   
  def print_attribute(self):
    print(str(self.number) + " is " + str(self.VoLTE_able) + ", " + self.CID)
  
  
class CarrierA(PrimarySIM):
  def sound(self):
    print("AAA")
    
class CarrierB(PrimarySIM):
  def sound(self):
    print("BBB")
  
# ================

# EXECUTION

# ================

numb1 = PrimarySIM("TRUE", "4169999999", "AAA")
numb1.print_attribute()

numb2 = CarrierA("FALSE", "6471111111", "AAA")
numb2.sound()
