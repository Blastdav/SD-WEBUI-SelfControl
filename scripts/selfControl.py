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
    options = {
               [opts.00_option, "0"],
               [opts.01_option, "1"],
               [opts.02_option, "2"],
               [opts.03_option, "3"],
               [opts.04_option, "4"],
               [opts.05_option, "5"],
               [opts.06_option, "6"],
               [opts.07_option, "7"],
               [opts.08_option, "8"],
               [opts.09_option, "9"],
               [opts.10_option, "10"],
               [opts.11_option, "11"],
               [opts.12_option, "12"],
               [opts.13_option, "13"],
               [opts.14_option, "14"],
               [opts.15_option, "15"],
               [opts.16_option, "16"],
               [opts.17_option, "17"],
               [opts.18_option, "18"],
               [opts.19_option, "19"],
               [opts.20_option, "20"],
               [opts.21_option, "21"],
               [opts.22_option, "22"],
               [opts.23_option, "23"]
               }
    
    for option in options:
        if option[0]:
            allowedTimes.append(option[1])
       
    if not current_time in allowedTimes:
        print(f"The current hour is {current_time} and you are not allowed to generate")
        if opts.Shutdown_on_disallowed:
            gr.Warning(f"The current hour is {current_time} and you are not allowed to generate")
            os._exit(0)
        else:
            gr.Warning(f"The current hour is {current_time}, you shoudn't be generating right now")

    else:
        print(f"The current hour is {current_time} and you are allowed to generate")

    pass

def on_ui_settings():

  section = ("Self control", NAME)

  settings_options = [
    ("00_option",False,"00:00"),
    ("01_option",False,"01:00"),
    ("02_option",False,"02:00"),
    ("03_option",False,"03:00"),
    ("04_option",False,"04:00"),
    ("05_option",False,"05:00"),
    ("06_option",False,"06:00"),
    ("07_option",False,"07:00"),
    ("08_option",False,"08:00"),
    ("09_option",False,"09:00"),
    ("10_option",False,"10:00"),
    ("11_option",False,"11:00"),
    ("12_option",False,"12:00"),
    ("13_option",False,"13:00"),
    ("14_option",False,"14:00"),
    ("15_option",False,"15:00"),
    ("16_option",False,"16:00"),
    ("17_option",True,"17:00"),
    ("18_option",True,"18:00"),
    ("19_option",True,"19:00"),
    ("20_option",True,"20:00"),
    ("21_option",True,"21:00"),
    ("22_option",True,"22:00"),
    ("23_option",True,"23:00"),
    ("Shutdown_on_disallowed",True,"Shutdown when trying to generate during disallowed hours")
  ]
  
  for setting_name, *data in settings_options:
    opts.add_option(setting_name, OptionInfo(*data, section=section))


script_callbacks.on_ui_settings(on_ui_settings)