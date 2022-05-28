from PIL import Image
import face_recognition
from numpy import asarray


class Model():
    def __init__(self) -> None:
        '''
            self.image display = 'image'
        '''
        pass

    def img_to_numpy_arr(img):
                return asarray(img)

    def numpyarr_to_img(arr):
        return Image.fromarray(arr)

    def pull_faces_from_image(self, image):
        face_locations = face_recognition.face_locations(image)
        for each_face_location in face_locations:
            top, right, bottom, left =  each_face_location
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
        return pil_image




    