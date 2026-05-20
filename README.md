# 📸 Screenshot Organizer (OCR + Flask App)

A simple web-based tool that automatically classifies and organizes screenshots using OCR (Optical Character Recognition) and rule-based text detection.

---

## 🚀 Features

- Upload screenshots via web interface
- Extract text from images using OCR
- Automatically classify images into categories:
  - OTP Screenshots
  - Coding Screenshots
  - Shopping Screenshots
  - Others
- Displays result with uploaded image
- Simple and clean Flask web UI

---

## 🛠️ Tech Stack

- Python
- Flask (Web Framework)
- pytesseract (OCR engine)
- Pillow (Image processing)
- HTML, CSS (Frontend)

---


## 📂 Project Structure

```text
SCREENSHOTORG/
├── webapp.py
├── templates/
│   ├── index.html
│   └── result.html
├── uploads/
└── static/
```
---
## 2. Install dependencies
```text
pip install flask pytesseract pillow
```

## 3. Install Tesseract OCR

### Download and install from:
```
👉 https://github.com/UB-Mannheim/tesseract/wiki

```

### Then set path in webapp.py:

```
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

```

### 🚀 Run the Project
```
python webapp.py

```

### Open in browser:

```
http://127.0.0.1:5000
```

## 📸 How It Works

User uploads screenshot → OCR extracts text → keywords are analyzed → image is classified → result is displayed on UI.

## 🎯 Future Improvements
- Machine Learning based classification
- Drag & drop upload UI
- Cloud deployment (Render / AWS)
- Better image preprocessing
- Multi-language OCR support

## 👨‍💻 Author

Built as a learning project to understand:
- OCR systems
- Flask web development
- Automation using Python

---
MOULY SIKDAR 

