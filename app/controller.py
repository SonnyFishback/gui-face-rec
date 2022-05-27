from os import kill
from tkinter.constants import END
from model import Model
from view import View
from tkinter import filedialog as fd
import cv2
from PIL import Image, ImageTk
# import face_recognition

class Controller():
    def __init__(self) -> None:
        self.model = Model()
        self.view = View(self)
        self.selected_image = None
    
    def _main(self):
        self.view.main()

    def kill_camera(self):
        cv2.destroyAllWindows()
        self.vid.release()
    
    def _handle_upload_button_click(self):
            self.selected_image_location = self.return_file_location()
            self.converted_image = ImageTk.PhotoImage(Image.open(self.selected_image_location))
            self.set_image_to_new(self.converted_image)

    def _handle_image_capture(self):

        self.vid = cv2.VideoCapture(0)
        
        while True:
            ret, frame = self.vid.read()
            cv2.imshow('Default Camera', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.kill_camera()
                break
            if cv2.waitKey(1) & 0xFF == ord('c'):
                self.kill_camera()

                # self.captured_image = ImageTk.PhotoImage(self.captured_frame)
                # Convert captured frame to numpy array to be processed by face_recognition libray.
                # self.frame_as_nump_arr = img_to_numpy_arr(frame)
                # Pull faces from captured frame.
                # self.captured_faces = self.pull_faces_from_image(self.frame_as_nump_arr)
                # print(self.captured_faces)
                return frame
# Might want to move this to the model.
    def return_file_location(self):
        file_path = fd.askopenfilename()
        return file_path

    def _submit_user_data(self):
        # still needs to be saved and stored in the model.
        self.view.first_name_entry.delete(0, END)
        self.view.last_name_entry.delete(0, END)

    # def _launch_controller(self):
    #     self.view.main()

if __name__ == '__main__':
    app = Controller()
    app._main()