"""
Created by Chuchu for Binary Search Lab
"""
class BinarySearch(list):
  
  def __init__(self, a, b):#init class
    self.a = a
    self.b = b
    #init instance variable length including the step
    for i in range(self.a):
      list.append(self, self.b)
      self.b += b
      i += 1
    self.length = i
    
  def search(self, needle):
    start = 0
    end  = self.length-1
    found = False
    final = {"count": 0, "index": -1}
    
    while start is not end and not found:
      middle = (start + end)//2
      if (self[middle] is needle): # check to see if the middle value is equal to value being searched for 
        found = True
        final["count"] += 1
        final["index"] = middle
      elif (needle < self[middle]):
        end = middle -1
        final["count"] += 1
      else:
        start = middle + 1 
        final["count"] += 1
    return final
    

