import gradio as gr

from modules import scripts, script_callbacks
from modules.shared import opts, OptionInfo
from modules.ui_components import FormRow, FormColumn, FormGroup, ToolButton
import datetime
import os

NAME = "SD Self Control"


class Script(scripts.Script):

  def title(self):
    return NAME

  def show(self, _is_img2img):
    return scripts.AlwaysVisible

  def process(self, component, **kwargs):

    allowedTimes = opts.Allowed_hours.split(",")
    current_time = str(datetime.datetime.now().hour)

    print("Checking if you are allowed to generate")

    if not current_time in allowedTimes:
        print(f"The current hour is {current_time} and you are not allowed to generate")
        if opts.Shutdown_on_disallowed:
            gr.Error(f"The current hour is {current_time} and you are not allowed to generate")
            os._exit(0)
        else:
            gr.Error(f"The current hour is {current_time}, you shoudn't be generating right now")

    else:
        print(f"The current hour is {current_time} and you are allowed to generate")

    pass

def on_ui_settings():

  section = ("Self control", NAME)

  settings_options = [
    ("Allowed_hours","17,18,19,20,21,22,23","Allowed hours of use CSV of hour in 24 hour format (17,18,19)"),
    ("Shutdown_on_disallowed",True,"Shutdown when trying to generate during disallowed hours")
  ]
  
  for setting_name, *data in settings_options:
    opts.add_option(setting_name, OptionInfo(*data, section=section))


script_callbacks.on_ui_settings(on_ui_settings)