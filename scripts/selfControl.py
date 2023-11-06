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

    allowedTimes = []
    for key in options:
        if options[key]:
            allowedTimes.append(key)

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
    ("options00",False,"00:00"),
    ("options01",False,"01:00"),
    ("options02",False,"02:00"),
    ("options03",False,"03:00"),
    ("options04",False,"04:00"),
    ("options05",False,"05:00"),
    ("options06",False,"06:00"),
    ("options07",False,"07:00"),
    ("options08",False,"08:00"),
    ("options09",False,"09:00"),
    ("options10",False,"10:00"),
    ("options11",False,"11:00"),
    ("options12",False,"12:00"),
    ("options13",False,"13:00"),
    ("options14",False,"14:00"),
    ("options15",False,"15:00"),
    ("options16",False,"16:00"),
    ("options17",True,"17:00"),
    ("options18",True,"18:00"),
    ("options19",True,"19:00"),
    ("options20",True,"20:00"),
    ("options21",True,"21:00"),
    ("options22",True,"22:00"),
    ("options23",True,"23:00"),
    ("Shutdown_on_disallowed",True,"Shutdown when trying to generate during disallowed hours")
  ]
  
  for setting_name, *data in settings_options:
    opts.add_option(setting_name, OptionInfo(*data, section=section))


script_callbacks.on_ui_settings(on_ui_settings)