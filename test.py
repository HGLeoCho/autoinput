class LineNumber:
  def __init__(self, VoLTE_able, number, CID):
    self.VoLTE_able = VoLTE_able
    self.number = number
    self.CID = CID
   
  def print_attribute(self):
    return str(self.number) + " is " + str(self.VoLTE_able) + ", " + self.CID
  
  
  
# ================

EXECUTION

# ================

numb1 = LineNumber("TRUE", "4169999999", "AAA")
numb1.print_attribute()
