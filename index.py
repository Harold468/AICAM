from tkinter import * 
import cv2
from random import randrange

def faceid():
    trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # img = cv2.imread('ironaman2.jpg')
    webcam = cv2.VideoCapture(0)
    while True:
        m, frame = webcam.read()
        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)
        cv2.imshow('Harold Osei Frimpong Kwabena Face Detector', frame)
        key=cv2.waitKey(1) #q ascii key
        if key ==81 or key==113:
            break
    webcam.release()

def selfdrivingcar():
    img_file = 'car.jpg'
    classifier_file = 'cars.xml'
    car_tracker = cv2.CascadeClassifier(classifier_file)
    pedestrain_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')
    img = cv2.imread(img_file)
    webcam = cv2.VideoCapture(0)
    while True:
        s, frame = webcam.read()
        black_n_white = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_tracker.detectMultiScale(black_n_white)
        humans = pedestrain_tracker.detectMultiScale(black_n_white)
        for x, y, w, h in humans:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, randrange(256), 0), 2)
        for x, y, w, h in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, randrange(256)), 2)
        cv2.imshow('Harold Osei Frimpong Kwabena car detector', frame)
        key = cv2.waitKey(1)
        if key == 81 or key == 113:
            break
        print("Code completed")
    webcam.release()


root=Tk()
root.geometry('800x600')
root.title('AICAM by Harold Osei Frimpong Kwabena')
root.iconbitmap('manfacescan.bmp')
file1=PhotoImage(file='manfacescan.png')

file2=PhotoImage(file='selfdrivecar.png')

l1 = Label(root,width=50,text='Face & Car scanner by Harold Osei Frimpong Kwabena',bg='blue',fg='white',font=('Times',32,'bold'))
l1.place(relx=0,rely=0.01)


frame1 = Frame(root,width=500,height=500)
frame1.place(relx=0.05,rely=0.25)
btn1=Button(frame1,image=file1,width=400,height=400,activebackground='gold',command=faceid)
btn1.grid(row=0,column=0)
l2 = Label(frame1,width=40,text='Scan Face',bg='blue',fg='white',font=('Times',12,'bold'))
l2.grid(row=1,column=0)


frame2 = Frame(root,width=500,height=500)
frame2.place(relx=0.5,rely=0.25)
btn2=Button(frame2,image=file2,width=400,height=400,activebackground='gold',command=selfdrivingcar)
btn2.grid(row=0,column=0)
l2 = Label(frame2,width=40,text='Self Driving Car Scanner',bg='blue',fg='white',font=('Times',12,'bold'))
l2.grid(row=1,column=0)




    
if __name__=='__main__':
    root.mainloop()