from flask import Flask
from flask import render_template
from flask import *
import keras
import numpy as np
import cv2
import os
from keras.preprocessing import image

model = keras.models.load_model("model/model.h5")
app = Flask(__name__)

folder = "uploads"

def predict():
    try:
        test_img = image.load_img('uploads/1.jpg',target_size = (150,150))
        test_img = image.img_to_array(test_img)
        test_img = np.expand_dims(test_img,axis = 0)    
        # return 100
        ans = model.predict(test_img)
        ans = np.argmax(ans)
        if ans == 0:
            return "Actinic keratoses"

        elif ans == 1:
            return "Basal cell carcinoma"
        
        elif ans == 2:
            return "Benign keratosis-like lesions "
        
        elif ans == 3:
            return "Melanocytic nevi"
        
        elif ans == 4:
            return "Melanoma"
        
        elif ans == 5:
            return "Dermatofibroma"
        
        
        elif ans == 6:
            return "Vascular lesions"    

        return "normal"
    except:
        return "Please choose jpg or png file only"
@app.route("/",methods = ["GET","POST"])
def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            location = os.path.join(
                folder,
                "1.jpg"
            )
            image_file.save(location)
            ans = predict()
            return render_template("index.html",prediction=ans)
    return render_template("index.html",prediction="None")

if __name__ == "__main__":
    app.run(port = 12000,debug = True)