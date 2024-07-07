import customtkinter as ctk
import requests
from requests.exceptions import Timeout
import webbrowser
import threading
import pygame
import time
from PIL import Image, ImageTk
import sys
import os

def resource_path(relative_path):
   
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class NotificationWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x100")
        self.title("Notification")
        self.label = ctk.CTkLabel(self, text="Website is now pingable!", font=("Arial", 16))
        self.label.pack(pady=20)

class PingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.set_window_icon()
        self.title("Website Ping Tool by Amir Sekkal")
        self.geometry("500x400")
        pygame.mixer.init()
        self.notification_sound = pygame.mixer.Sound(resource_path("notification.mp3"))

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.url_entry = ctk.CTkEntry(self, width=300, placeholder_text="Enter website URL")
        self.url_entry.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.grid(row=1, column=0, padx=20, pady=10)
        self.button_frame.grid_columnconfigure((0, 1), weight=1)

        self.ping_button = ctk.CTkButton(self.button_frame, text="Ping", command=self.ping_website)
        self.ping_button.grid(row=0, column=0, padx=(0, 10))

        self.reset_button = ctk.CTkButton(self.button_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=0, column=1, padx=(10, 0))

        self.status_text = ctk.CTkTextbox(self, width=300, height=200)
        self.status_text.grid(row=3, column=0, padx=20, pady=(10, 20), sticky="nsew")

        self.ping_thread = None
        self.stop_event = threading.Event()
    def set_window_icon(self):
      icon_path = resource_path("ping.png")
    
      icon = Image.open(icon_path)
      photo = ImageTk.PhotoImage(icon)
      self.wm_iconphoto(True, photo)
      self.iconphoto(True, photo)
    def ping_website(self):
        self.stop_ping()
        time.sleep(0.1) 

        url = self.url_entry.get()
        print("Pinging:", url)
        if url == "":
            self.status_text.insert("end", "Please enter a valid URL.\n")
            return
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        self.status_text.delete("0.0", "end")
        self.status_text.insert("end", f"Pinging {url}...\n")
        
        self.stop_event.clear()

        def ping_thread():
            while not self.stop_event.is_set():
                try:
                    response = requests.get(url, timeout=0.5)
                    if response.status_code == 200:
                        self.status_text.insert("end", "Ping successful! Website is reachable.\n")
                        self.play_sound()
                        self.show_notification()
                        webbrowser.open(url)
                        break
                    else:
                        self.status_text.insert("end", f"Unexpected status code: {response.status_code}\n")
                except Timeout:
                    self.status_text.insert("end", "Request timed out. Retrying...\n")
                except requests.ConnectionError:
                    self.status_text.insert("end", "Connection error. Retrying...\n")
                except Exception as e:
                    self.status_text.insert("end", f"An error occurred: {str(e)}\n")
                
                for _ in range(10):
                    if self.stop_event.is_set():
                        self.status_text.insert("end", "Pinging stopped.\n")
                        return
                    time.sleep(0.1)

        self.ping_thread = threading.Thread(target=ping_thread, daemon=True)
        self.ping_thread.start()

    def play_sound(self):
        self.notification_sound.play()

    def show_notification(self):
        notification = NotificationWindow(self)
        notification.focus()

    def stop_ping(self):
        if self.ping_thread and self.ping_thread.is_alive():
            self.stop_event.set()
            self.ping_thread.join(timeout=2)
            if self.ping_thread.is_alive():
                self.status_text.insert("end", "Failed to stop the ping thread.\n")
            else:
                self.status_text.insert("end", "Ping process stopped.\n")

    def reset(self):
        self.stop_ping()
        time.sleep(0.1)  

        self.url_entry.delete(0, 'end')
        self.status_text.delete("0.0", "end")
        self.url_entry.focus()
        self.stop_event.clear()

        self.status_text.insert("end", "Reset complete. Ready for new ping.\n")

if __name__ == "__main__":
    app = PingApp()
    icon_path = resource_path("ping.png")
    app.mainloop()