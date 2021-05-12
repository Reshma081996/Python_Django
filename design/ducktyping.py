"""
DUCK TYPING IS A CONCEPT RELATED TO  DYNAMIC TYPING,
WHERE TYPE OR CLASS IS LESS IMPORTANT THAN METHODS IT DEFINES.
CHECK FOR THE PRESENCE OF A GIVEN METHOD OR ATTRIBUTE """

class Swift:
    def drive(self):
        print("driving swift cars")
class Sonet:
    def drive(self):
        print("driving sonet cars")
class Person:
    def start(self,car):
        car.drive()

sw=Swift()
p=Person()
p.start(sw)

