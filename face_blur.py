import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cv2.namedWindow("Gercek Zamanli Yüz Blurlama", cv2.WINDOW_NORMAL)

while True:
    ret, frame= cap.read()
  
    if not ret: 
        print('Kamera verisi alınamadı')
        break

    try:
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=5)
    except Exception as e:
        print("Yüz algılama hatası:",e)
        faces = []

    for (x, y, w, h) in faces:
        x1 = x+w
        y1 = y+h
        
        face = frame[y:y1,x:x1]
        face = cv2.GaussianBlur(face,(75,75),15)
        frame[y:y1,x:x1] = face

        cv2.rectangle(frame,(x,y),(x1,y1),(0,0,255),1)

    cv2.imshow("Gercek Zamanli Yüz Blurlama",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()