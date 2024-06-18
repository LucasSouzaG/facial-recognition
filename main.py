import cv2
import numpy as np
import pandas as pd
import os
import uuid
import zipfile
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Verifica se a pasta Modelo já existe, se não existir ela é extraída
if not os.path.isdir('./Modelo'):
    path = 'Modelo.zip'
    zip_object = zipfile.ZipFile(file = path, mode = 'r')
    zip_object.extractall('./')
    zip_object.close

cascade_faces = 'Modelo/haarcascade_frontalface_default.xml'
caminho_modelo = 'Modelo/modelo_01_expressoes.h5'
face_detection = cv2.CascadeClassifier(cascade_faces)
classificador_emocoes = load_model(caminho_modelo, compile = False)
expressoes = ['Raiva', 'Nojo', 'Medo', 'Feliz', 'Triste', 'Surpreso', 'Neutro']

# Setup Pathsq
CAPTURE_PATH = os.path.join('data', 'capture')

# Verifica se existe menos que 3 fotos, se existir 3 ou mais não abre a câmera
if len(os.listdir(CAPTURE_PATH)) < 3:
    # Establish a connection to the webcam
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        
        # # Cut down frame to 250x250px
        # frame = frame[120:120+250, 200:200+250, :]
            
        # Show image back to screen
        cv2.imshow('Image Collection',frame)
        
        # Collect anchors
        if cv2.waitKey(1) & 0XFF == ord('c'):
            # Create the unique file path
            imgname = os.path.join(CAPTURE_PATH, '{}.jpg'.format(uuid.uuid1()))
            # Write out anchor image 
            cv2.imwrite(imgname,frame)

        # Breaking gracefully
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break

    # Release the webcam
    cap.release()
    # Close the image show frame
    cv2.destroyAllWindows()

resultados = []

for nome_arquivo in os.listdir(CAPTURE_PATH):
    imagem = cv2.imread(os.path.join(CAPTURE_PATH, nome_arquivo))
    # cv2.imshow("Display", imagem)
    # cv2.waitKey(0)
    original = imagem.copy()
    faces = face_detection.detectMultiScale(original, scaleFactor = 1.1,
                                        minNeighbors = 3, minSize = (20,20))
    
    cinza = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Display", cinza)
    # cv2.waitKey(0)
    for (x, y, l, a) in faces:
        cv2.rectangle(original, (x,y), (x+l, y+a), (0, 255, 0), 2)
        # cv2.imshow("Display", original)
        # cv2.waitKey(0)
        roi = cinza[y:y + a, x:x + l]
        # cv2.imshow("Display", roi)
        # cv2.waitKey(0)
        roi = cv2.resize(roi, (48, 48))
        # cv2.imshow("Display", roi)
        # cv2.waitKey(0)
        roi = roi.astype('float')
        roi /= 255
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis = 0)
        preds = classificador_emocoes.predict(roi)[0]
        emotion_probability = np.max(preds)
        label = expressoes[preds.argmax()]

        resultados.append({"imagem": nome_arquivo,"expressao":label})
        
        # > Imagem com label
        # cv2.putText(original, label, (faces[0][0], faces[0][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.65, 
        #             (0,0,255), 2, cv2.LINE_AA)
        # cv2.rectangle(original, (faces[0][0], faces[0][1]), (faces[0][0] + faces[0][2], faces[0][1] + faces[0][3]), (0,0,255), 2)
        # cv2.imshow("Display", original)
        # cv2.waitKey(0)
    
print(resultados)
print(os.listdir(CAPTURE_PATH))

from result_stats import dataReport

dataReport(resultados)
