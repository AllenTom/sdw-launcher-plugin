import os

import gradio as gr
import requests
from fastapi import FastAPI

from modules import script_callbacks, shared

baseCallbackUrl = "http://localhost:6745"
enable_plugin = False


def app_started(_: gr.Blocks, app: FastAPI):
    global baseCallbackUrl
    baseCallbackUrl = shared.cmd_opts.launcher_callback
    global enable_plugin
    enable_plugin = shared.cmd_opts.launcher_enable
    print("launcher plugin started")
    if enable_plugin:
        r = requests.post(baseCallbackUrl + "/sdw/appstarted", json={
            "pid": os.getpid(),
            "session": shared.cmd_opts.launcher_session,
        })


script_callbacks.on_app_started(app_started)
