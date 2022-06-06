import kivy 
from kivy.app import App 

from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 

class childApp(gridlayout):

  def  __init__(self, **kwargs):
      super(childApp, self ).__init__()
      self.cols = 2
      self.add.widget(Label(text = 'Student Name'))
      self.s_name = TextInput()
      self.add_widget(self.s_name)

      