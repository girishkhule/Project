# Imported the required libraries for Text to speech
# Please note that kivymd version 0.104.2 is required for Interface functionalities

# ******************** Text to Speech Converter **********************************************************************
# Author : Girish Khule - 23PGAI0057 & Harshal Dhuri - 23PGAI0024 
# Project - Speech Processing
# Mentor - Dr.Jagmohan Chauhan
# ********************************************************************************************************************

# Import Python text-to-speech library
import pyttsx3
# Need to perform parallel execution on application so importing threading libraries
import threading
# Access to application window properties
from kivy.core.window import Window
# Define the behavior of button
from kivy.uix.behaviors import ButtonBehavior
# Arrange widgets in a horizontal or vertical box
from kivy.uix.boxlayout import BoxLayout
# Position the widgets using floating point co-ordinates
from kivy.uix.floatlayout import FloatLayout
# Create kivy applications with Material Design Components
from kivymd.app import MDApp
# Kivy library for Material Design button
from kivymd.uix.button import MDRaisedButton
# Need dialog box to put text
from kivymd.uix.dialog import MDDialog
# Display Icons
from kivymd.uix.label import MDIcon
# Used to select the location of file during export
from plyer import filechooser

# Initialize the pyttsx3 instance & set the window size
engine = pyttsx3.init()
Window.size = (480, 720)


# Dialog_content inherits BoxLayout
class Dialog_Content(BoxLayout):
    pass


# Click Icon inherits button behavior and MDIcon
class Click_Icon(ButtonBehavior, MDIcon):
    pass


# FloatLayout is required to choose file & for exporting purpose
class Interface(FloatLayout):
    # Set the exporting location
    def exporting(self, location):
        print(location[0])
        objects = self.dialog.content_cls.children
        file_name = objects[0].text
        original_text = self.ids.input_text.text
        location_new = str(location[0] + "\\" + file_name + ".mp3")
        engine.save_to_file(text=original_text, filename=location_new)
        engine.runAndWait()
        self.dialog.dismiss()

    # Selection method for choosing location
    def selection(self, instances):
        filechooser.choose_dir(title="Please select an audio folder", on_selection=self.exporting)

    # Set the title & dialog box
    def exporting_menu(self):
        self.dialog: MDDialog = MDDialog(
            size_hint=[.8, None],
            title="Filename Here",
            type="custom",
            content_cls=Dialog_Content(),
            buttons=[MDRaisedButton(text="Export", on_release=self.selection)]

        )
        self.dialog.open()

    # Select male & female voice as well as the set the icon for play & pause
    def running(self):
        voices = engine.getProperty('voices')
        if self.ids.female.active:
            engine.setProperty('voice', voices[1].id)
        elif self.ids.male.active:
            engine.setProperty('voice', voices[0].id)
        engine.say(self.ids.input_text.text)
        engine.runAndWait()
        self.ids.icon_button.icon = "play.png"

    # Change of icons while playing & pausing the audio
    def changing(self):
        if self.ids.icon_button.icon == "play.png":
            process = threading.Thread(target=self.running)
            process.start()

            self.ids.icon_button.icon = "pause.png"
        else:
            self.ids.banner.show()

    # Banner setting
    def closing(self):
        self.ids.banner.hide()


# Design a class to set the color of application
class TTSApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"


# Run the application now
TTSApp().run()
