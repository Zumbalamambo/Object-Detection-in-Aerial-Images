# -*- coding:utf-8 -*-
import cv2
from trainer import Model
from trainer import Model_final


dict = {0:"Backgound", 1:"Car"}

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    #cascade_path = "/home/antara/Downloads/opencv-2.4.10/data/haarcascades/haarcascade_frontalface_alt.xml"
    model = Model()
    model_final = Model_final()
    model.load()
    model_final.load()
    i = 0 
    key = 0
    
    img1 = cv2.imread('1.png')
    img2 = cv2.imread('7.png')
    result = model.predict(img1)
    max_prob = max(result[0])
    for i in xrange(len(result[0])):
        if(result[0][i] == max_prob):
            key = i


    try:
        print (dict[key])
        #cv2.putText(frame,dict[key],tuple(rect[0:2]), font, 1,color,2,cv2.CV_AA)
    except KeyError:
        pass


    print("******************************")    

    key = 0
    result = model.predict(img2)
    max_prob = max(result[0])
    for i in xrange(len(result[0])):
        if(result[0][i] == max_prob):
            key = i


    try:
        print (dict[key])
        #cv2.putText(frame,dict[key],tuple(rect[0:2]), font, 1,color,2,cv2.CV_AA)
    except KeyError:
        pass
                
                

    '''
    while True:
        print (i)
        i +=1 
        _, frame = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #cascade = cv2.CascadeClassifier(cascade_path)
        #facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
        #facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(3, 3))
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #if len(facerect) > 0:
            #print('face detected')
        #    color = (255, 255, 255)  
        #   for rect in facerect:
                #cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

        #        x, y = rect[0:2]
        #        width, height = rect[2:4]
        #        image = frame[y - 10: y + height, x : x + 3*(width/2)]
        #        cv2.imshow("slide",image)
        result = model.predict(frame)
        for i in xrange(len(result[0])):
            if(result[0][i] == 1):
                key = i

        try:
            print (dict[key])
            #cv2.putText(frame,dict[key],tuple(rect[0:2]), font, 1,color,2,cv2.CV_AA)
        except KeyError:
            pass
        cv2.imshow('Image',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    '''
