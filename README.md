# 🧠 ASL Recognition using CNN

This project focuses on recognizing American Sign Language (ASL) characters using Convolutional Neural Networks (CNNs). The model was trained and evaluated on a dataset containing grayscale images of ASL letters and digits, achieving **98.01% test accuracy**.  

The model handles classification of both **letters (A–Z)** and **digits (0–9)**, making it suitable for real-time sign language interpretation applications.

---

## 📂 Dataset

- **Source:** [ASL Dataset on Kaggle](https://www.kaggle.com/datasets/ayuraj/asl-dataset)  
- **Content:** Images of hand signs representing 36 classes (0–9 and A–Z), stored in folders named after each character.

---

## 🧠 Model Overview

- **Input Shape:** 64x64 grayscale images  
- **Architecture:** Custom CNN  
- **Color Space:** Grayscale & tested with YUV  
- **Augmentation:** Applied to boost generalization  
- **Final Test Accuracy:** `98.01%`

---

## 📈 Results

### 🔹 Confusion Matrix:


![image](https://github.com/user-attachments/assets/5c27f576-e0be-4ea5-9c49-0f770f6904a7)


The model performs with high precision across nearly all classes with minimal misclassification.

---

## 🚀 Tech Stack

- Python  
- TensorFlow / Keras  
- NumPy, Matplotlib, Seaborn  
- OpenCV (for preprocessing)  
- Scikit-learn

---

## 👨‍💻 Author

**Abdelrhman Hamdy**  
- [LinkedIn](https://www.linkedin.com/in/abdelrahman-hamdii/)  
- Data Scientist | Computer Vision Enthusiast  

---

## 📜 License

This project is licensed under the MIT License — feel free to use, modify, and share.

---

## 💡 Future Improvements

- Real-time prediction with webcam integration  
- Extend to dynamic gestures and full words  
- Deploy as a web/mobile app

