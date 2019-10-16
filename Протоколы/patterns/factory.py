class Button(object):
   html = ""
   def get_html(self):
      return self.html

class Image(Button):
   html = "<img></img>"

class Input(Button):
   html = "<input></input>"

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():
   def create_button(self, _type):
      # targetclass = typ.capitalize()
      # return globals()[targetclass]()
      return _type()

button_obj = ButtonFactory()
button = [Button, Input, Flash]
for b in button:
   print(button_obj.create_button(b).get_html())

# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_factory.htm