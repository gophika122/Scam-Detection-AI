import nltk

nltk.download('punkt')      
nltk.download('stopwords')   
nltk.download('names')        

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('stopwords')



SCAM_KEYWORDS = ["lottery", "prize", "winner", "urgent", "bank", "transfer", "account", "congratulations", "limited time"]

def is_scam(text):
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum()]  
    words = [word for word in words if word not in stopwords.words("english")]  

    return any(word in SCAM_KEYWORDS for word in words)


message = input("Enter a message: ")
if is_scam(message):
    print("🚨 Scam detected!")
else:
    print("✅ Message is safe.")
