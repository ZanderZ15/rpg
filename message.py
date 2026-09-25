from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import logging

class Message:
    message = "sigma phony zebras"

    def Call_Sign(self):
        logging.info(self.message)

    def Change_Message_From_Entry(self, entry_widget):
        # .get() pulls whatever text is typed into the Entry widget right now
        user_text = entry_widget.get()
        if user_text:  # Only update if they typed something
            self.message = user_text
            # 3. Add a log entry confirming the update
            logging.info("Message Updated!")
            
            # Optional: Clear the input text box after saving
            entry_widget.delete(0, END)
        else:
            logging.error("No Message Found")