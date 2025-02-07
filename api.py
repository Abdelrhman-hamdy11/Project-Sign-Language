import os # Import the os module
from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
import io

app = FastAPI()

# Check if the model file exists before loading
model_path = "E:\\API\\my_model.keras" # or "my_model.h5" if it's an h5 file
if not os.path.exists(model_path): # Use os.path.exists to check file existence
    raise FileNotFoundError(f"Model file not found at: {model_path}")

# تحميل النموذج
model = load_model(model_path)

# قائمة الفئات (الحروف والأرقام)
categories = sorted([
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z"
])

# دالة التنبؤ
def predict_image(image_bytes):
    # قراءة الصورة
    image = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    
    # تجهيز الصورة للنموذج
    img = cv2.resize(img, (64, 64))  # تغيير الحجم
    img = img.reshape(1, 64, 64, 1)  # إعادة تشكيل
    img = img / 255.0  # تطبيع

    # التنبؤ
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    
    return categories[predicted_class], float(prediction[0][predicted_class])

# نقطة النهاية لتلقي الصور والتنبؤ بها
@app.post("/predict/")
async def predict(file: UploadFile = File(r"E:\predict")):
    image_bytes = await file.read()
    label, confidence = predict_image(image_bytes)
    return {"predicted_label": label, "confidence": f"{confidence * 100:.2f}%"}

# نقطة اختبار
@app.get("/")
def home():
    return {"message": "API is running! Upload an image to /predict/"}
