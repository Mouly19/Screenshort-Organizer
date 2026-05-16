from PIL import Image
import pytesseract
import shutil
import os


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# CATEGORY KEYWORDS


categories = {

    "OTP": [
        "otp",
        "verification",
        "verify",
        "login code",
        "authentication",
    ],

    "Coding": [
        "python",
        "java",
        "c++",
        "html",
        "css",
        "javascript",
        "import",
        "print",
        "def",
        "class",
        "return",
        "error",
        "exception",
        "syntax",
        "console",
        "function",
        "public static void",
        "#include",
    ],

    "Notes": [
        "chapter",
        "unit",
        "introduction",
        "definition",
        "example",
        "theory",
        "question",
        "answer",
        "important",
        "summary",
    ],

    "Shopping": [
        "amazon",
        "flipkart",
        "order",
        "delivered",
        "invoice",
        "payment",
        "discount",
        "price",
        "buy",
        "shipping",
    ]
}

# -----------------------------
# CREATE FOLDERS
# -----------------------------

for category in categories:
    os.makedirs(category, exist_ok=True)

os.makedirs("Others", exist_ok=True)

# -----------------------------
# SOURCE FOLDER
# -----------------------------

source_folder = "Screenshots"

# -----------------------------
# PROCESS FILES
# -----------------------------

for file_name in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file_name)

    try:
        image = Image.open(file_path)

        # Convert image to grayscale
        image = image.convert("L")

        # Increase contrast
        image = image.point(lambda x: 0 if x < 140 else 255)

        text = pytesseract.image_to_string(image).lower()

      
        
        print(f"\nProcessing: {file_name}")

        # Store scores
        scores = {}

        # Count keyword matches
        for category, keywords in categories.items():

            score = 0

            for keyword in keywords:
                if keyword in text:
                    score += 1

            scores[category] = score

        print("Scores:", scores)

        

        # Find best category
        best_category = max(scores, key=scores.get)

        print("Selected Category:", best_category)
        # If no keywords matched
        if scores[best_category] == 0:
            best_category = "Others"

        # Destination path
        destination = os.path.join(best_category, file_name)

        # Move file
        shutil.move(file_path, destination)

        print(f"Moved to {best_category}")

    except Exception as e:
        print(f"Error processing {file_name}: {e}")