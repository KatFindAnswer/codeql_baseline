import numpy as np
import cv2
import face_recognition_models

imgAnh = face_recognition_models.load_image_file("ibrahimovic.jpg")
imgAnh = cv2.cvtColor(imgAnh,cv2.COLOR_BGR2RGB)

imgCheck = face_recognition_models.load_image_file("ibrahimovic1.jpg")
imgCheck = cv2.cvtColor(imgCheck,cv2.COLOR_BGR2RGB)

# imgAnh
#xac dinh vi tri khuon mat
faceLoc = face_recognition_models.face_locations(imgAnh)[0]
print(faceLoc) # (y1,x2,y2,x1)
#ma hoa hinh anh
encodeAnh = face_recognition_models.face_encodings(imgAnh)[0]
cv2.rectangle(imgAnh ,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

#img Anh_check
#xac dinh vi tri khuon mat
faceCheck = face_recognition_models.face_locations(imgCheck)[0]
#ma hoa hinh anh
encodeCheck = face_recognition_models.face_encodings(imgCheck)[0]
cv2.rectangle(imgCheck ,(faceCheck[3],faceCheck[0]),(faceCheck[1],faceCheck[2]),(255,0,255),2)

#So sanh 2 buc anh
result =face_recognition_models.compare_faces([encodeAnh],encodeCheck)
print(result)

#khi so sanh nhieu hinh thi can biet khoang (sai so) giua 1 buc anh la bao nhieu
faceDis =face_recognition_models.face_distance([encodeAnh],encodeCheck)
print(result,faceDis)
cv2.putText(imgCheck ,f'{result},Khop:{round(1-faceDis[0],3)}',(40,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)


cv2.imshow("Anh",imgAnh)
cv2.imshow("Anh_check",imgCheck)
cv2.waitKey()
