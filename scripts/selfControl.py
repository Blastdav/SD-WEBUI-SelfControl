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
               [opts.00option, "0"],
               [opts.01option, "1"],
               [opts.02option, "2"],
               [opts.03option, "3"],
               [opts.04option, "4"],
               [opts.05option, "5"],
               [opts.06option, "6"],
               [opts.07option, "7"],
               [opts.08option, "8"],
               [opts.09option, "9"],
               [opts.10option, "10"],
               [opts.11option, "11"],
               [opts.12option, "12"],
               [opts.13option, "13"],
               [opts.14option, "14"],
               [opts.15option, "15"],
               [opts.16option, "16"],
               [opts.17option, "17"],
               [opts.18option, "18"],
               [opts.19option, "19"],
               [opts.20option, "20"],
               [opts.21option, "21"],
               [opts.22option, "22"],
               [opts.23option, "23"]
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
    ("00option",False,"00:00"),
    ("01option",False,"01:00"),
    ("02option",False,"02:00"),
    ("03option",False,"03:00"),
    ("04option",False,"04:00"),
    ("05option",False,"05:00"),
    ("06option",False,"06:00"),
    ("07option",False,"07:00"),
    ("08option",False,"08:00"),
    ("09option",False,"09:00"),
    ("10option",False,"10:00"),
    ("11option",False,"11:00"),
    ("12option",False,"12:00"),
    ("13option",False,"13:00"),
    ("14option",False,"14:00"),
    ("15option",False,"15:00"),
    ("16option",False,"16:00"),
    ("17option",True,"17:00"),
    ("18option",True,"18:00"),
    ("19option",True,"19:00"),
    ("20option",True,"20:00"),
    ("21option",True,"21:00"),
    ("22option",True,"22:00"),
    ("23option",True,"23:00"),
    ("Shutdown_on_disallowed",True,"Shutdown when trying to generate during disallowed hours")
  ]
  
  for setting_name, *data in settings_options:
    opts.add_option(setting_name, OptionInfo(*data, section=section))


script_callbacks.on_ui_settings(on_ui_settings)