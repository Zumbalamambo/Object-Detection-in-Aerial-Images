# -*- coding:utf-8 -*-
import cv2
from trainer import Model
from trainer import Model_final
from trainer import Model_classification
import numpy as np

color = (255, 255, 255)
dict = {0:"Backgound", 1:"Car"}
classifiction = {0:"car", 1:"Truck" , 2:"construction" ,3:"camping_car" , 4:"van"}

def classify_frame(frame):

    result = model_classification.predict(frame)
    max_prob = max(result[0])
    for v in  range(len(result[0])):
        if(result[0][v] == max_prob):
            print (classifiction[v])	
            print "vechile classified"
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img_final,classifiction[v],(Y_new[i]+q1,X_new[i]+p1), font, 1,color,2,cv2.CV_AA)
            cv2.putText(img_final_1,classifiction[v],(Y_new[i]+q1,X_new[i]+p1), font, 1,color,2,cv2.CV_AA)
                               


if __name__ == '__main__':
    #cap = cv2.VideoCapture(0)
    #cascade_path = "/home/antara/Downloads/opencv-2.4.10/data/haarcascades/haarcascade_frontalface_alt.xml"
    model = Model()
    model_final = Model_final()
    model_classification = Model_classification()
    model.load()
    model_final.load()
    model_classification.load()
    i = 0 
    key = 0
    count = 0
    car_count = 0
    while(count == 0 ):    
      
        path= input('Enter the image path')
        img = cv2.imread(path)
        img_final_1 = cv2.imread(path)
        img_final = cv2.imread(path)
        cv2.imshow('image',img)
        #cv2.waitKey(0)        
        #img2 = cv2.imread('00000016.png')
        prob = []
        p=0
        q = 0
        X = []
        Y = []
        m = 125
        n = 125
        k = 0
        block = 0
        #for i in range(0,500,30):
        #    for j in range(0,500,30):
        avg_prob = 0
        threshold = 0
        while((p+m)<510):
            q = 0
            while((q+n)<512):       
                frame = img[p:p+m,q:q+n,:]
                '''
                cv2.imshow('frame',frame)
                k = cv2.waitKey(33)
                if k == -1:
                    cv2.imwrite('yolo.png',frame)
                else:
                    print k
                '''    
                result = model.predict(frame)
                #car_count += 1
                X.append(p)
                X.append(p+m)
                Y.append(q)
                Y.append(q+n)
                prob.append(result[0][1])
                print result[0][1] 
                #cv2.rectangle(img_inter,(q,p),(q+n,p+m),(0,255,0),3)
                img_disp = cv2.imread(path)        
                cv2.rectangle(img_disp,(q,p),(q+n,p+m),(0,255,0),3)
                #cv2.imshow('image',img_disp)
                #cv2.waitKey(1)
 
                #cv2.rectangle.erase(img_disp,(q,p),(q+30,p+40),(0,255,0),3)
                '''
                try:
                    print (dict[key])
                #cv2.putText(frame,dict[key],tuple(rect[0:2]), font, 1,color,2,cv2.CV_AA)
                except KeyError:
                    pass
                print '********************************'
                '''
                q = q + n
                print(p,q)
            p = p + m    
        print X
        print Y    
        print car_count
        X_min = min(X)
        X_max = max(X)        
        Y_min = min(Y)
        Y_max = max(Y)
        print X_max
        print X_min
        print Y_max
        print Y_min
        #cv2.rectangle(img_disp,(Y_min,X_min),(Y_max,X_max),(0,255,0),3)
        #cv2.imshow('image',img)
        #cv2.waitKey(0)
        '''
        for k in range(len(prob)):
                if(prob[k]) == max(prob):
                        block = k
        cv2.rectangle(img_final,(Y[2*block],X[2*block]),(Y[2*block]+n,X[2*block]+m),(0,255,0),3)
        prob[block] = 0 
        for k in range(len(prob)):
                if(prob[k]) == max(prob):
                        block = k
        cv2.rectangle(img_final,(Y[2*block],X[2*block]),(Y[2*block]+n,X[2*block]+m),(0,255,0),3)
        '''
        X_new = []
        Y_new = []
        prob_new = [] 
        threshold =  np.mean(prob)
        for k in range(len(prob)):
                if(prob[k]) > threshold:
                        cv2.rectangle(img_final,(Y[2*k],X[2*k]),(Y[2*k]+n,X[2*k]+m),(0,255,0),3)
                        X_new.append(X[2*k])
                        Y_new.append(Y[2*k])
                        prob_new.append(prob[k])
        

        cv2.imshow('image',img_final)
        cv2.waitKey(0)
        print len(prob_new)
        #125*125++++++
        m1 = 30
        n1 = 20
        count_prev = 0
        inter = 22
        for i in  range(len(prob_new)):
                frame  = img[X_new[i] : X_new[i] + m , Y_new[i] : Y_new[i] + n , : ]
                #cv2.imshow('frame' , frame)
                #cv2.waitKey(0)
                p1 = 0
                q1 = 0
                while(p1+m1 < 125 ):
                        q1 =0 
                        while(q1+n1 < 125 ):
                               final_frame = frame[p1:p1+m1 , q1:q1+n1 , :]
                               #cv2.imshow('frame' , final_frame)
                               #cv2.waitKey(1)  
                               result = model_final.predict(final_frame)
                               cv2.rectangle(img_final,(Y_new[i]+q1,X_new[i]+p1),(Y_new[i]+q1+n1,X_new[i]+p1+m1),(0,255,0),3)
                               cv2.imshow('image',img_final)
                               cv2.waitKey(1)      
                               max_prob = max(result[0])
                               if(result[0][1] == max_prob):
                                     if(count_prev == 1):
                                         final_frame = frame[p1:p1+m1,q1-n1:q1+n1,:]
                                         cv2.rectangle(img_final_1,(Y_new[i]+q1,X_new[i]-p1),(Y_new[i]+q1+n1,X_new[i]+p1+m1),(0,255,0),3)
                                         classify_frame(final_frame)
                                     
                                         cv2.imshow('vechile' , final_frame)
                                         
                                         cv2.waitKey(0)
                                         img_path = (str(inter)+'.png')
                                         cv2.imwrite(img_path,final_frame)
                                         inter+=1  
                               	     else:
                               	         cv2.rectangle(img_final_1,(Y_new[i]+q1,X_new[i]+p1),(Y_new[i]+q1+n1,X_new[i]+p1+m1),(0,255,0),3)
                                         classify_frame(final_frame)
                                     
                                         cv2.imshow('vechile' , final_frame)
                                         cv2.waitKey(0)
                                         cv2.imwrite((str(inter)+'.png'),final_frame)
                                         inter+=1  
                               		 count_prev = 1	
                               else:
                               	     count_prev = 0  
                               q1+= n1
                               print(p1,q1)  
                        p1+= m1
                        print ("******")
        cv2.imshow('image',img_final_1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        count = input('Enter 0 to continue')        
         
        

    '''    

    print("******************************")    
    
    result = model.predict(img2)
    for i in xrange(len(result[0])):
        if(result[0][i] == 1):
            key = i


    try:
        print (dict[key])
        #cv2.putText(frame,dict[key],tuple(rect[0:2]), font, 1,color,2,cv2.CV_AA)
    except KeyError:
        pass
                
                

    
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
