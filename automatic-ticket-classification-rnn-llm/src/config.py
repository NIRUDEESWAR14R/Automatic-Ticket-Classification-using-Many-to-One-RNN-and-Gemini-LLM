import os
from dotenv import load_dotenv

load_dotenv()

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "ticket_lstm_model.keras")
TOKENIZER_PATH = os.path.join(BASE_DIR, "models", "tokenizer.pkl")
LABEL_ENCODER_PATH = os.path.join(BASE_DIR, "models", "label_encoder.pkl")

# Preprocessing
MAX_LEN = 200

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
