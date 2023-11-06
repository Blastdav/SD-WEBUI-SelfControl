import gradio as gr

from modules import scripts, script_callbacks
from modules.shared import opts, OptionInfo
from modules.ui_components import FormRow, FormColumn, FormGroup, ToolButton
import datetime

NAME = "SD Self Control"

class Script(scripts.Script):

  def title(self):
    return NAME


  def show(self, _is_img2img):
    return scripts.AlwaysVisible

  def process(self, component, **kwargs):
    # if the current time is in the allowed hours of use, then print "allowed"
    # else print "not allowed"
    allowedTimes = opts.Allowed_hours.split(",")
    if datetime.datetime.now().hour in allowedTimes:
        print("allowed")
    else:
        print("not allowed")

def on_ui_settings():

  section = ("Self control", NAME)

  settings_options = [
    ("Allowed_hours","17,18,19,20,21,22,23,24","Allowed hours of use CSV of hour in 24 hour format (17,18,19)"),
  ]
  
  for setting_name, *data in settings_options:
    opts.add_option(setting_name, OptionInfo(*data, section=section))
