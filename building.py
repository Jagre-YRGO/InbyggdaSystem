class building:
   def __init__(self, address='Main street'):
      self.adr = address

   def set_dimension(self, new_dimension):
      self.width = new_dimension['width']
      self.height = new_dimension['height']
      self.length = new_dimension['length']

   # def calc_vol(my_arg = {'height':0, 'width':0 ,'length':0}):
   #    print(f'I am in {__name__}')
   #    vol1 = (my_arg['height']/2) * my_arg['width'] * my_arg['length']
   #    vol2 = ((my_arg['height']/2) * my_arg['width'] * my_arg['length'])/2
   #    return vol1 + vol2 

def main():
   first_building = building()
   second_building = building('Arizona Street')

   print(f'first_building is at:{first_building.adr}')
   print(f'second_building is at:{second_building.adr}')

   first_building.adr = 'Caroline street'
   print(f'first_building changed to:{first_building.adr}')
   
   first_building.set_dimension({'height':10,'width':5 ,'length':15})
   

   print(f'I am in {__name__}')
   #print(f'Volume of house is {calc_vol(dimensions)}')

if __name__ == '__main__':
   main()

