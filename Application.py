# Importing Libraries

import numpy as np  # Importing the NumPy library for numerical operations

import cv2  # Importing the OpenCV library for computer vision tasks
import os, sys  # Importing the os and sys modules for interacting with the operating system
import time  # Importing the time module for time-related functions
import operator  # Importing the operator module for efficient operations

from string import ascii_uppercase  # Importing the ascii_uppercase constant from the string module

import tkinter as tk  # Importing the tkinter library for creating GUI applications
from PIL import Image, ImageTk  # Importing the Image and ImageTk modules from the Pillow library for image processing

from hunspell import Hunspell  # Importing the Hunspell library for spell checking
import enchant  # Importing the enchant library for spell checking

from keras.models import model_from_json  # Importing the model_from_json function from the keras.models module

os.environ["THEANO_FLAGS"] = "device=cuda, assert_no_cpu_op=True"  # Setting environment variables for Theano library


#Application :

class Application:

import cv2
import tkinter as tk
from hunspell import Hunspell
from keras.models import model_from_json
from string import ascii_uppercase

class SignLanguageConverter:
    def __init__(self):
        # Initialize variables and models

        # Initialize Hunspell spell checker for English language
        self.hs = Hunspell('en_US')

        # Open video capture for webcam
        self.vs = cv2.VideoCapture(0)

        # Initialize variables for current image and JSON file paths
        self.current_image = None
        self.current_image2 = None
        self.json_file = open("Models\model_new.json", "r")
        self.model_json = self.json_file.read()
        self.json_file.close()

        # Load the model from JSON and weights files
        self.loaded_model = model_from_json(self.model_json)
        self.loaded_model.load_weights("Models\model_new.h5")

        self.json_file_dru = open("Models\model-bw_dru.json", "r")
        self.model_json_dru = self.json_file_dru.read()
        self.json_file_dru.close()

        self.loaded_model_dru = model_from_json(self.model_json_dru)
        self.loaded_model_dru.load_weights("Models\model-bw_dru.h5")

        self.json_file_tkdi = open("Models\model-bw_tkdi.json", "r")
        self.model_json_tkdi = self.json_file_tkdi.read()
        self.json_file_tkdi.close()

        self.loaded_model_tkdi = model_from_json(self.model_json_tkdi)
        self.loaded_model_tkdi.load_weights("Models\model-bw_tkdi.h5")

        self.json_file_smn = open("Models\model-bw_smn.json", "r")
        self.model_json_smn = self.json_file_smn.read()
        self.json_file_smn.close()

        self.loaded_model_smn = model_from_json(self.model_json_smn)
        self.loaded_model_smn.load_weights("Models\model-bw_smn.h5")

        # Initialize dictionary to count occurrences of each character
        self.ct = {}
        self.ct['blank'] = 0
        self.blank_flag = 0

        # Initialize counters for each uppercase letter
        for i in ascii_uppercase:
            self.ct[i] = 0

        print("Loaded model from disk")

        # Create a Tkinter window
        self.root = tk.Tk()
        self.root.title("Sign Language To Text Conversion")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.geometry("900x900")

        # Create a panel to display the current image
        self.panel = tk.Label(self.root)
        self.panel.place(x=100, y=10, width=580, height=580)

        # Create a second panel to display a smaller version of the current image
        self.panel2 = tk.Label(self.root)
        self.panel2.place(x=400, y=65, width=275, height=275)

        # Create a label for the title
        self.T = tk.Label(self.root)
        self.T.place(x=60, y=5)
        self.T.config(text="Sign Language To Text Conversion", font=("Courier", 30, "bold"))

        # Create a label for the current symbol
        self.panel3 = tk.Label(self.root)
        self.panel3.place(x=500, y=540)

        self.T1 = tk.Label(self.root)
        self.T1.place(x=10, y=540)
        self.T1.config(text="Character :", font=("Courier", 30, "bold"))

        # Create a label for the current word
        self.panel4 = tk.Label(self.root)
        self.panel4.place(x=220, y=595)

        self.T2 = tk.Label(self.root)
        self.T2.place(x=10, y=595)
        self.T2.config(text="Word :", font=("Courier", 30, "bold"))

        # Create a label for the current sentence
        self.panel5 = tk.Label(self.root)
        self.panel5.place(x=350, y=645)

        self.T3 = tk.Label(self.root)
        self.T3.place(x=10, y=645)
        self.T3.config(text="Sentence :", font=("Courier", 30, "bold"))

        # Create a label for suggestions
        self.T4 = tk.Label(self.root)
        self.T4.place(x=250, y=690)
        self.T4.config(text="Suggestions :", fg="red", font=("Courier", 30, "bold"))

        # Create buttons for actions
        self.bt1 = tk.Button(self.root, command=self.action1, height=0, width=0)
        self.bt1.place(x=26, y=745)

        self.bt2 = tk.Button(self.root, command=self.action2, height=0, width=0)
        self.bt2.place(x=325, y=745)

        self.bt3 = tk.Button(self.root, command=self.action3, height=0, width=0)
        self.bt3.place(x=625, y=745)

        # Initialize variables for storing text
        self.str = ""
        self.word = " "
        self.current_symbol = "Empty"
        self.photo = "Empty"

        # Start the video loop
        self.video_loop()

    # def video_loop(self):
    #     # Main loop to capture video frames and process them
    #     ok, frame = self.vs.read()  # Read frame from video stream
    #     if ok:
    #         cv2image = cv2.flip(frame, 1)
    #         x1 = int(0.5 * frame.shape[1])
    #         y1 = 10
    #         x2 = frame.shape[1] - 10
    #         y2 = int(0.5 * frame.shape[1])
    #         cv2.rectangle(cv2image, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (0, 255, 0), 1)
    #         cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)
    #         current_image = Image.fromarray(cv2image)
    #         imgtk = ImageTk.PhotoImage(image=current_image)
    #         self.panel.imgtk = imgtk
    #         self.panel.config(image=imgtk)
    #     self.root.after(30, self.video_loop)  # Call the same function after 30 milliseconds

    # def destructor(self):
    #     # Release the video capture and close the Tkinter window
    #     self.root.destroy()
    #     self.vs.release()

    # def action1(self):
    #     # Perform action for button 1
    #     pass

    # def action2(self):
    #     # Perform action for button 2
    #     pass

    # def action3(self):
    #     # Perform action for button 3
    #     pass


# Create an instance of the SignLanguageConverter class
converter = SignLanguageConverter()



def video_loop(self):
        ok, frame = self.vs.read()

        if ok:
            cv2image = cv2.flip(frame, 1)

            x1 = int(0.5 * frame.shape[1])
            y1 = 10
            x2 = frame.shape[1] - 10
            y2 = int(0.5 * frame.shape[1])

            cv2.rectangle(frame, (x1 - 1, y1 - 1), (x2 + 1, y2 + 1), (255, 0, 0) ,1)
            cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)

            self.current_image = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image = self.current_image)

            self.panel.imgtk = imgtk
            self.panel.config(image = imgtk)

            cv2image = cv2image[y1 : y2, x1 : x2]

            gray = cv2.cvtColor(cv2image, cv2.COLOR_BGR2GRAY)

            blur = cv2.GaussianBlur(gray, (5, 5), 2)

            th3 = cv2.adaptiveThreshold(blur, 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

            ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            
            self.predict(res)

            self.current_image2 = Image.fromarray(res)

            imgtk = ImageTk.PhotoImage(image = self.current_image2)

            self.panel2.imgtk = imgtk
            self.panel2.config(image = imgtk)

            self.panel3.config(text = self.current_symbol, font = ("Courier", 30))

            self.panel4.config(text = self.word, font = ("Courier", 30))

            self.panel5.config(text = self.str,font = ("Courier", 30))

            predicts = self.hs.suggest(self.word)
            
            if(len(predicts) > 1):

                self.bt1.config(text = predicts[0], font = ("Courier", 20))

            else:

                self.bt1.config(text = "")

            if(len(predicts) > 2):

                self.bt2.config(text = predicts[1], font = ("Courier", 20))

            else:

                self.bt2.config(text = "")

            if(len(predicts) > 3):

                self.bt3.config(text = predicts[2], font = ("Courier", 20))

            else:

                self.bt3.config(text = "")


        self.root.after(5, self.video_loop)

    def predict(self, test_image):

        test_image = cv2.resize(test_image, (128, 128))

        result = self.loaded_model.predict(test_image.reshape(1, 128, 128, 1))


        result_dru = self.loaded_model_dru.predict(test_image.reshape(1 , 128 , 128 , 1))

        result_tkdi = self.loaded_model_tkdi.predict(test_image.reshape(1 , 128 , 128 , 1))

        result_smn = self.loaded_model_smn.predict(test_image.reshape(1 , 128 , 128 , 1))

        prediction = {}

        prediction['blank'] = result[0][0]

        inde = 1

        for i in ascii_uppercase:

            prediction[i] = result[0][inde]

            inde += 1

        #LAYER 1

        prediction = sorted(prediction.items(), key = operator.itemgetter(1), reverse = True)

        self.current_symbol = prediction[0][0]


        #LAYER 2

        if(self.current_symbol == 'D' or self.current_symbol == 'R' or self.current_symbol == 'U'):

        	prediction = {}

        	prediction['D'] = result_dru[0][0]
        	prediction['R'] = result_dru[0][1]
        	prediction['U'] = result_dru[0][2]

        	prediction = sorted(prediction.items(), key = operator.itemgetter(1), reverse = True)

        	self.current_symbol = prediction[0][0]

        if(self.current_symbol == 'D' or self.current_symbol == 'I' or self.current_symbol == 'K' or self.current_symbol == 'T'):

        	prediction = {}

        	prediction['D'] = result_tkdi[0][0]
        	prediction['I'] = result_tkdi[0][1]
        	prediction['K'] = result_tkdi[0][2]
        	prediction['T'] = result_tkdi[0][3]

        	prediction = sorted(prediction.items(), key = operator.itemgetter(1), reverse = True)

        	self.current_symbol = prediction[0][0]

        if(self.current_symbol == 'M' or self.current_symbol == 'N' or self.current_symbol == 'S'):

        	prediction1 = {}

        	prediction1['M'] = result_smn[0][0]
        	prediction1['N'] = result_smn[0][1]
        	prediction1['S'] = result_smn[0][2]

        	prediction1 = sorted(prediction1.items(), key = operator.itemgetter(1), reverse = True)

        	if(prediction1[0][0] == 'S'):

        		self.current_symbol = prediction1[0][0]

        	else:

        		self.current_symbol = prediction[0][0]
        
        if(self.current_symbol == 'blank'):

            for i in ascii_uppercase:
                self.ct[i] = 0

        self.ct[self.current_symbol] += 1

        if(self.ct[self.current_symbol] > 60):

            for i in ascii_uppercase:
                if i == self.current_symbol:
                    continue

                tmp = self.ct[self.current_symbol] - self.ct[i]

                if tmp < 0:
                    tmp *= -1

                if tmp <= 20:
                    self.ct['blank'] = 0

                    for i in ascii_uppercase:
                        self.ct[i] = 0
                    return

            self.ct['blank'] = 0

            for i in ascii_uppercase:
                self.ct[i] = 0

            if self.current_symbol == 'blank':

                if self.blank_flag == 0:
                    self.blank_flag = 1

                    if len(self.str) > 0:
                        self.str += " "

                    self.str += self.word

                    self.word = ""

            else:

                if(len(self.str) > 16):
                    self.str = ""

                self.blank_flag = 0

                self.word += self.current_symbol

    def action1(self):

    	predicts = self.hs.suggest(self.word)

    	if(len(predicts) > 0):

            self.word = ""

            self.str += " "

            self.str += predicts[0]

    def action2(self):

    	predicts = self.hs.suggest(self.word)

    	if(len(predicts) > 1):
            self.word = ""
            self.str += " "
            self.str += predicts[1]

    def action3(self):

    	predicts = self.hs.suggest(self.word)

    	if(len(predicts) > 2):
            self.word = ""
            self.str += " "
            self.str += predicts[2]

    def action4(self):

    	predicts = self.hs.suggest(self.word)

    	if(len(predicts) > 3):
            self.word = ""
            self.str += " "
            self.str += predicts[3]

    def action5(self):

    	predicts = self.hs.suggest(self.word)

    	if(len(predicts) > 4):
            self.word = ""
            self.str += " "
            self.str += predicts[4]
            
    def destructor(self):

        print("Closing Application...")

        self.root.destroy()
        self.vs.release()
        cv2.destroyAllWindows()
    
print("Starting Application...")

(Application()).root.mainloop()