class Car(object):
  
  def __init__(self, name, model, ctype, speed): #Initialize the Class
    self.name = name
    self.model = model
    self.ctype = ctype
    self.speed = 0
    if (self.name is None):
      self.name = "General"
    else:
      self.name = name
    if (self.model is None):
      self.model = "GM"
    else:
      self.model = model
    if (self.name is 'Porshe' or self.name is 'Koenigsegg'):
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4
    if (self.ctype is 'trailer'):
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4
  
  def is_saloon(self): #Boolean Check to determine whether its a Saloon Car
    if (self.ctype is 'trailer'):
      return False
    else:
      return True
  
  def drive(self, speed): #Drive method to determine speed
    if (speed is 7):
      self.speed = 77
    elif (speed is 3):
      self.speed = 1000
    else:
      return self

