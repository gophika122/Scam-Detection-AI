import nltk

nltk.download('punkt')        # For word tokenization
nltk.download('stopwords')    # For removing common words
nltk.download('names')        # (Optional) For name recognition

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK resources (Run once)
nltk.download('punkt')
nltk.download('stopwords')


# Sample scam keywords
SCAM_KEYWORDS = ["lottery", "prize", "winner", "urgent", "bank", "transfer", "account", "congratulations", "limited time"]

def is_scam(text):
    words = word_tokenize(text.lower())  # Tokenize & convert to lowercase
    words = [word for word in words if word.isalnum()]  # Remove punctuation
    words = [word for word in words if word not in stopwords.words("english")]  # Remove stopwords

    return any(word in SCAM_KEYWORDS for word in words)

# Test the function
message = input("Enter a message: ")
if is_scam(message):
    print("🚨 Scam detected!")
else:
    print("✅ Message is safe.")
