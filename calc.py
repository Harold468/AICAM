from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.uix.toolbar import MDTopAppBar
import cv2
from random import randrange
from kivymd.uix.button import MDRaisedButton


class HomeScreen(Screen):
    def faceid(self, instance):
        trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # img = cv2.imread('ironaman2.jpg')
        webcam = cv2.VideoCapture(0)
        while True:
            m, frame = webcam.read()
            grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
            for (x, y, w, h) in face_coordinates:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)
            cv2.imshow('Dennis Face Detector', frame)
            key=cv2.waitKey(1) #q ascii key
            if key ==81 or key==113:
                break
        webcam.release()

    def selfdrivingcar(self, instance):
        img_file = 'car.jpg'
        classifier_file = 'cars.xml'
        car_tracker = cv2.CascadeClassifier(classifier_file)
        pedestrain_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')
        img = cv2.imread(img_file)
        webcam = cv2.VideoCapture('how.mp4')
        while True:
            s, frame = webcam.read()
            black_n_white = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cars = car_tracker.detectMultiScale(black_n_white)
            humans = pedestrain_tracker.detectMultiScale(black_n_white)
            for x, y, w, h in humans:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, randrange(256), 0), 2)
            for x, y, w, h in cars:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, randrange(256)), 2)
            cv2.imshow('Dennis car detector', frame)
            key = cv2.waitKey(1)
            if key == 81 or key == 113:
                break
            print("Code completed")
        webcam.release()

    def __init__(self,**kwargs):
        super().__init__()
        self.box=MDBoxLayout()
        self.box.orientation='horizontal'
        self.topappbar = MDTopAppBar(title='AI CAM by Dennis Asante',
                                     pos_hint={'top': 1})
        self.faceidbutton = MDRaisedButton(
            text='Face Recognition',
            pos_hint={'center_x': 0.2, 'center_y': 0.5},
            size_hint=(0.25, 0.25),
            # size=(64, 64),
            on_release=self.faceid
        )

        self.selfdrivingcarbutton = MDRaisedButton(
            text='Self driving car scanner',
            pos_hint={'center_x': 0.7, 'center_y': 0.5},
            size_hint=(0.25, 0.25),
            on_release=self.selfdrivingcar
        )

        self.add_widget(self.box)
        self.add_widget(self.topappbar)
        self.add_widget(self.faceidbutton)
        self.add_widget(self.selfdrivingcarbutton)


class FaceID(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        pass


class SelfDrivingCarID(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        pass


class AICAM(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name='home'))
        #self.sm.add_widget(FaceID(name='faceid'))
        #self.sm.add_widget(SelfDrivingCarID(name='selfdrivingcar'))
        #file = Builder.load_file('calc.kv')

        return self.sm


if __name__ == '__main__':
    AICAM().run()
