import cv2

cap = cv2.VideoCapture(0)

while True:
    face_cascade = cv2.CascadeClassifier('C:\\Users\Swarad\\Downloads\\haarcascade_frontalface_alt.xml')
    ret,frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if ret == False:         # Webcam is not working
        continue
        
    faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
        
    cv2.imshow("Video Frame",frame)
    cv2.imshow("Gray Frame",gray_frame)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    
    key_pressed = cv2.waitKey(1) & 0xFF        
    if key_pressed == ord('q'):           # If 'q' is pressed , the program will terminate
        break
    
cap.release()
cv2.destroyAllWindows()

