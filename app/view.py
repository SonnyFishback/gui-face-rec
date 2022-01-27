# View

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class View(tk.Tk):

    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller
        self.default_image_location = './assets/smileimage.png'
        self.current_image_location = self.default_image_location
        self.title('FaceTrack')
        self.geometry('850x450+300+300')
        self._create_layout()

    '''create all UI elements. called during view initializaton.'''
    def _create_layout(self):
        '''---------------------- LEFT FRAME ----------------------'''
        self.left_frame = ttk.Frame(self, style='leftFrame.TFrame')
        self.left_frame.config(width=424, height=449)
        self.left_frame.grid_propagate(0)
        self.left_frame.grid(row=0, column=0, padx=1, pady=1)
        '''---------------------- LEFT FRAME WIDGETS ----------------------'''
        self.current_displayed_image = ImageTk.PhotoImage(Image.open(self.current_image_location))
        self.image_placeholer_frame = ttk.Frame(self.left_frame)
        self.image_placeholer_frame.config(width=300, height=300)
        self.image_placeholer_frame.grid(row=0, column=0, padx=10, pady=10)
        '''image container'''
        self.img_container = ttk.Label(self.image_placeholer_frame, image=self.current_displayed_image)
        self.img_container.place(x=0, y=0)
        '''upload image button'''
        self.upload_image_button = ttk.Button(self.left_frame, text="Upload Image", command=self.controller.handle_upload_button_click)
        self.upload_image_button.grid( column=0, row=1)
        '''capture image button'''
        self.capture_image_button = ttk.Button(self.left_frame, text="Capture Image", command=self.controller.handle_image_capture)
        self.capture_image_button.grid( column=0, row=2)
        '''---------------------- RIGHT FRAME ----------------------'''
        self.right_frame = ttk.Frame(self)
        self.right_frame.config(width=424, height=449)
        self.right_frame.grid_propagate(0)
        self. right_frame.grid(row=0, column=2)
        '''---------------------- RIGHT FRAME WIDGETS ----------------------'''
        self.form_label = ttk.Label(self.right_frame, text='User data')
        self.form_label.grid(row=0, column=0)
        '''first name input'''
        self.first_name_label = ttk.Label(self.right_frame ,text = 'First Name')
        self. first_name_label.grid(row = 0,column = 0)
        self.first_name_entry = ttk.Entry(self.right_frame)
        self.first_name_entry.grid(row = 0,column = 1)
        '''last name input'''
        self.last_name_label = ttk.Label(self.right_frame ,text = 'Last Name')
        self.last_name_label.grid(row = 1,column = 0)
        self.last_name_entry = ttk.Entry(self.right_frame)
        self.last_name_entry.grid(row = 1,column = 1)
        '''submit button'''
        self.submit_form_btn = ttk.Button(self.right_frame, command= self.controller.submit_user_data)
        self.submit_form_btn.configure(text='Save')
        self.submit_form_btn.grid(row=2, column=0)

    def main(self):
        self.mainloop()
        