import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

longitud, altura = 150, 150
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("pred: CLASS_01")
  elif answer == 1:
    print("pred: CLASS_02")
  elif answer == 2:
   print("pred: CLASS_03")
  elif answer == 3:
   print("pred: CLASS_04")
  elif answer == 4:
   print("pred: CLASS_05")
  elif answer == 5:
   print("pred: CLASS_06")
  elif answer == 6:
   print("pred: CLASS_07")
  elif answer == 7:
   print("pred: CLASS_08")
  return answer

predict('prueba1.png')