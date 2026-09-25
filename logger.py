import logging
import tkinter as tk
from tkinter import ttk, scrolledtext
import message
#logging system
class TkinterLogHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record) + '\n'
        self.text_widget.after(0, self.update_text_widget, msg)

    def update_text_widget(self, msg):
        self.text_widget.config(state='normal')  # Enable editing
        self.text_widget.insert(tk.END, msg)     # Insert the log
        self.text_widget.see(tk.END)            # Auto-scroll to the bottom
        self.text_widget.config(state='disabled') # Disable editing again