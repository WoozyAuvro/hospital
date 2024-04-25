from time import time
import cv2
import os
import datetime
date_time = datetime.datetime.now()
try:
        import pyautogui
except:
    from pip._internal import main as pip
    pip(['install', '--user', 'pyautogui'])
    import pyautogui

try:
    import face_recognition
except:
    # if doesnt work, install cmake > wheel > dlib then run this again
    from pip._internal import main as pip
    pip(['install', '--user', 'face-recognition'])
    import face_recognition

try:
    import pandas as pn
except:
    from pip._internal import main as pip
    pip(['install', '--user', '-r requirements.txt'])
    import pandas

def siesvi(name):
    newname = name.replace(" ", "-")
    df = pn.read_csv(r'E:\cOdiNg\Automated-Health-Facility\hospital\sheeesh\registry.csv')
    if name in str(df['name']):
        row = df.loc[df['name'] == newname]
        regTime = str(row.iloc[0, 1])
        return regTime

def men(name, path):
  import os
  print(name)
  pathi = r'../images/a.png'
  shepherd = pathi
  RegTime = siesvi(name)
  wrote = """
  <!DOCTYPE html>
  <html>
  <head>
  <style>
  * {text-align: center;}
  body
  {
  text-align: center;
  font-family: 'Lexend Deca', sans-serif;
  background-color: lightblue;
  text-shadow: aquamarine;
  }
  </style>
  </head>
  <body>
  <h1>Welcome Back! %s</h1>
  <p></p>
  <img src="%s">
  <p style="background-color:cyan;">this user registered their application at: %s</p>
  <br><br>
  <h3><a href="http://192.168.0.108/">CHECK PAST RECORD</h3>
  </body>
  </html>
  """ % (name, path, RegTime)

  with open('index.html', 'w') as f:
      f.write(wrote)
  os.system("index.html")
import shutil
def reg():
    name = pyautogui.prompt("Your Name")
    dob = pyautogui.prompt("Your Date of Birth")
    datee = date_time.strftime("%D")
    wdate = f"{datee}; {date_time.hour}:{date_time.minute}" 
    with open("registry.csv", "a+") as fi:
        namae = name.replace(" ", "-")
        fi.write(f"{namae}, {wdate},\n")
    shutil.copy("Image.png", fr"E:\cOdiNg\Automated-Health-Facility\hospital\sheeesh\images\{namae}.png")
    #face_cascade = cv2.CascadeClassifier(r'E:\cOdiNg\Automated-Health-Facility\hospital\sheeesh\cascades\data\haarcascade_frontalface_alt2.xml')
    #cap = cv2.VideoCapture(0)
    ## recognizer = cv2.face.LBPHFaceRecognizer_create()
    ## recognizer.read("trainer.yml")
#
    #while True:
    #    ret, frame = cap.read()
    #    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    #    for(x,y,w,h) in faces:
    #        print(x,y,w,h)
    #        roi_gray = gray[y:y+h, x:x+w]
    #        roi_color = frame[y:y+h, x:x+w]
#
    #        # id_, conf = recognizer.predict(roi_gray)
    #        # if conf>=45 and conf <= 85:
    #        #     print(id_)
    #        sav = name.replace(" ", "-")
    #        img_item = f"images/{sav}.png"
    #        cv2.imwrite(img_item, roi_color)
    #            
#
    #        color = (0, 50, 250)
    #        stroke = 2
    #        end_cord_x = x + w
    #        end_cord_y = y + w
    #        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
#
    #        # os.system('compare.py')
    #        cap.release()
    #        cv2.destroyAllWindows()
    #    cv2.imshow('video', frame)
    #    if cv2.waitKey(20) == ord('q'):
    #        break
    #

try:
    path = r"E:\cOdiNg\Automated-Health-Facility\hospital\sheeesh\images"

    imgs = []
    classNames = []
    imgDir = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        curImg = cv2.imread(f"{path}\{cl}")
        imgs.append(curImg)
        imgDir.append(cl)
        classNames.append(os.path.splitext(cl)[0])

    for i in myList:

        img1 = cv2.imread('Image.png')
        # img1 = cv2.imread('Image.png')
        rgb_1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        enc1 = face_recognition.face_encodings(rgb_1)[0]

        img2 = cv2.imread(f"{path}\{i}")
        rgb_2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        enc2 = face_recognition.face_encodings(rgb_2)[0]

        result = face_recognition.compare_faces([enc1], enc2)
        if str(result) == "[True]":
            print(result)
            #os.system('Image.png')
            #os.system(f'{path}\{i}')
            y = os.path.splitext(i)[0]
            x = i[3:]
            men(y,f"{path}\{i}")
            break

        elif str(result) == "[False]":
            print("ok", result)

    print(type(result))
    if str(result) == "[False]":
        reg() 

except IndexError:
    print("Coudn't find a face. Run main.py again")
    pyautogui.alert("NO FACE FOUND. TRY AGAIN")
    # os.system('main.py')