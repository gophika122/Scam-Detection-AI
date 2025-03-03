import nltk
import tkinter as tk
from tkinter import messagebox
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Scam detection function
SCAM_KEYWORDS = ["lottery", "prize", "winner", "urgent", "bank", "transfer", "account", "congratulations", "limited time"]

def is_scam(text):
    words = word_tokenize(text.lower())  # Tokenize & convert to lowercase
    words = [word for word in words if word.isalnum()]  # Remove punctuation
    words = [word for word in words if word not in stopwords.words("english")]  # Remove stopwords

    return any(word in SCAM_KEYWORDS for word in words)

# Function to check scam message
def check_message():
    user_text = entry.get()
    if is_scam(user_text):
        messagebox.showwarning("Scam Alert", "🚨 Scam detected!")
    else:
        messagebox.showinfo("Safe", "✅ Message is safe.")

# Creating the GUI
root = tk.Tk()
root.title("Scam Detection")
root.geometry("400x300")

# UI Elements
tk.Label(root, text="Enter your message:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Check Message", command=check_message).pack(pady=10)

# Run the GUI
root.mainloop()
