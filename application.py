from tkinter import *
from tkinter import ttk, scrolledtext
import logging

import message
import logger
import engine


#SCREEN SET UP
root = Tk()
root.minsize(500, 500)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky="nsew")

frame.rowconfigure(0, weight=1)
frame.columnconfigure((0, 1, 2), weight=1)

log_label = ttk.Label(frame, text="System Log Console:")
log_label.grid(column=0, row=0, sticky="nw")

log_box = scrolledtext.ScrolledText(frame, state='disabled', height=15, wrap='word')
log_box.grid(column=0, row=0, columnspan=3, pady=(25, 10), sticky="nsew")

app_logger = logging.getLogger()
app_logger.setLevel(logging.DEBUG)

tk_handler = logger.TkinterLogHandler(log_box)
formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s', '%H:%M:%S')
tk_handler.setFormatter(formatter)
app_logger.addHandler(tk_handler)

_message = message.Message()

# Row 0: Welcome Label
ttk.Label(frame, text="Hello World!").grid(column=1, row=0, pady=10)

# Row 1: The Input Field
message_entry = ttk.Entry(frame)
message_entry.grid(column=1, row=10, pady=5)


say_message_button = ttk.Button(
    frame, 
    text="Say Message", 
    command=_message.Call_Sign
).grid(column=0, row=2, padx=5)

change_message_button = ttk.Button(
    frame,
    text="Change Message",
    command=lambda: _message.Change_Message_From_Entry(message_entry)
).grid(column=1, row=2, padx=5)

quit_button = ttk.Button(
    frame, 
    text="Quit", 
    command=root.destroy
).grid(column=2, row=2, padx=5)

game = engine.Game()
play_button = ttk.Button(
    frame, 
    text="Play", 
    command=game.start
).grid(column=2, row=3, padx=5)


root.mainloop()  # starts listening



