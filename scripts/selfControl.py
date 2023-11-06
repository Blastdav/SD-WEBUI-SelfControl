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
               "0": opts.options00,
               "1": opts.options01,
               "2": opts.options02,
               "3": opts.options03,
               "4": opts.options04,
               "5": opts.options05,
               "6": opts.options06,
               "7": opts.options07,
               "8": opts.options08,
               "9": opts.options09,
               "10": opts.options10,
               "11": opts.options11,
               "12": opts.options12,
               "13": opts.options13,
               "14": opts.options14,
               "15": opts.options15,
               "16": opts.options16,
               "17": opts.options17,
               "18": opts.options18,
               "19": opts.options19,
               "20": opts.options20,
               "21": opts.options21,
               "22": opts.options22,
               "23": opts.options23
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
    ("option00",False,"00:00"),
    ("option01",False,"01:00"),
    ("option02",False,"02:00"),
    ("option03",False,"03:00"),
    ("option04",False,"04:00"),
    ("option05",False,"05:00"),
    ("option06",False,"06:00"),
    ("option07",False,"07:00"),
    ("option08",False,"08:00"),
    ("option09",False,"09:00"),
    ("option10",False,"10:00"),
    ("option11",False,"11:00"),
    ("option12",False,"12:00"),
    ("option13",False,"13:00"),
    ("option14",False,"14:00"),
    ("option15",False,"15:00"),
    ("option16",False,"16:00"),
    ("option17",True,"17:00"),
    ("option18",True,"18:00"),
    ("option19",True,"19:00"),
    ("option20",True,"20:00"),
    ("option21",True,"21:00"),
    ("option22",True,"22:00"),
    ("option23",True,"23:00"),
    ("Shutdown_on_disallowed",True,"Shutdown when trying to generate during disallowed hours")
  ]
  
  for setting_name, *data in settings_options:
    opts.add_option(setting_name, OptionInfo(*data, section=section))


script_callbacks.on_ui_settings(on_ui_settings)