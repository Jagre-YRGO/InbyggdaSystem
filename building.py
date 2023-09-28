class building:
   def __init__(self, address='Main street'):
      self.adr = address
      self.width = 0
      self.height = 0
      self.length = 0

   def set_dimension(self, new_dimension):
      self.width = new_dimension['width']
      self.height = new_dimension['height']
      self.length = new_dimension['length']

   def calc_vol(self):
      vol1 = (self.height/2) * self.width * self.length
      vol2 = ((self.height/2) * self.width * self.length)/2
      return vol1 + vol2
   
class church(building):
   def __init__(self, address='Main street'):
      building.__init__(self,address)
      self.clocktower_height = 0
      self.tower_width = 0
      self.tower_length = 0

   def set_clocktower_height(self,height):
      self.clocktower_height = height

   def set_dimension(self, new_dimension):
      building.set_dimension(self,new_dimension)
      self.tower_width = self.width
      self.tower_length = self.width

   def calc_vol(self):
      base_vol = building.calc_vol(self)
      tower_vol = self.clocktower_height * self.tower_width * self.tower_length
      return base_vol + tower_vol

def main():
   

   first_building = building()
   second_building = building('Arizona Street')

   print(f'first_building is at:{first_building.adr}')
   print(f'second_building is at:{second_building.adr}')

   first_building.adr = 'Caroline street'
   print(f'first_building changed to:{first_building.adr}')
   
   first_building.set_dimension({'height':10,'width':5 ,'length':15})
   second_building.set_dimension({'height':10,'width':5 ,'length':150})
   print(f'Volume of first_building:{first_building.calc_vol()}')
   print(f'Volume of second_building:{second_building.calc_vol()}')

   my_church = church()
   print(f'my_church volume is:{my_church.calc_vol()}')
   my_church.set_dimension({'height':20,'width':10 ,'length':20})
   my_church.set_clocktower_height(40)
   print(f'my_church volume is:{my_church.calc_vol()}')
   
   print(f'I am in {__name__}')
   #print(f'Volume of house is {calc_vol(dimensions)}')

if __name__ == '__main__':
   main()

