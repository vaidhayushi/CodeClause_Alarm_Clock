import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
import datetime
import pygame
import threading

class ClockWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Select Time")
        self.transient(master)
        self.grab_set()

        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()

        self.hour_var.set("0")
        self.minute_var.set("0")

        hour_label = tk.Label(self, text="Hour:", font=("Arial", 14))
        hour_label.grid(row=0, column=0, padx=10, pady=10)

        hour_combobox = ttk.Combobox(self, textvariable=self.hour_var, values=[str(i).zfill(2) for i in range(24)], font=("Arial", 12))
        hour_combobox.grid(row=0, column=1)

        minute_label = tk.Label(self, text="Minute:", font=("Arial", 14))
        minute_label.grid(row=1, column=0, padx=10, pady=10)

        minute_combobox = ttk.Combobox(self, textvariable=self.minute_var, values=[str(i).zfill(2) for i in range(60)], font=("Arial", 12))
        minute_combobox.grid(row=1, column=1)

        set_button = tk.Button(self, text="Set", command=self.set_time, font=("Arial", 14), bg="#4caf50", fg="white")
        set_button.grid(row=2, column=0, columnspan=2, pady=10)

    def set_time(self):
        hour = self.hour_var.get()
        minute = self.minute_var.get()
        selected_time = f"Selected Time: {hour}:{minute}"
        selected_time_label.config(text=selected_time)
        self.destroy()

def open_clock_window():
    global clock_window
    clock_window = ClockWindow(window)

def set_alarm():
    alarm_hour = int(clock_window.hour_var.get())
    alarm_minute = int(clock_window.minute_var.get())

    alarm_time = datetime.time(alarm_hour, alarm_minute)

    def check_alarm():
        pygame.mixer.init()
        while True:
            current_time = datetime.datetime.now().time()
            if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
                alarm_message = f"Alarm set for {alarm_hour} hour(s) {alarm_minute} minute(s)"
                print(alarm_message)
                pygame.mixer.music.load("gasolina.mp3")  
                pygame.mixer.music.play()
                break

    threading.Thread(target=check_alarm).start()


window = tk.Tk()
window.title("Alarm Clock")

background_image = ImageTk.PhotoImage(Image.open("Background_image.jpg"))

background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


window.geometry(f"{background_image.width()}x{background_image.height()}")

selection_frame = tk.Frame(background_label, bg="#f0f0f0")
selection_frame.pack(pady=20)

time_button = tk.Button(selection_frame, text="Set Time", command=open_clock_window, font=("Arial", 14), bg="#4caf50", fg="white")
time_button.pack(side=tk.LEFT, padx=10, pady=10)

selected_time_label = tk.Label(background_label, text="Selected Time: 00:00", font=("Arial", 14), bg="#f0f0f0")
selected_time_label.pack(pady=20)

button = tk.Button(background_label, text="Set Alarm", command=set_alarm, font=("Arial", 14), bg="#4caf50", fg="white")
button.pack(pady=20)

footer_label = tk.Label(background_label, text="Developed by Aayushi", font=("Arial", 10), bg="#f0f0f0", fg="#777777")
footer_label.pack(side=tk.BOTTOM, pady=10)


window.mainloop()
