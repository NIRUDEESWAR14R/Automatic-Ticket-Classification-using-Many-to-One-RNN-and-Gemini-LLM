import pickle
import tensorflow as tf

from config import (
    MODEL_PATH,
    TOKENIZER_PATH,
    LABEL_ENCODER_PATH,
    MAX_LEN,
    GEMINI_API_KEY
)
from preprocess import preprocess_text
from inference_gemini import generate_reply


def main():
    # Load model & artifacts
    model = tf.keras.models.load_model(MODEL_PATH)

    with open(TOKENIZER_PATH, "rb") as f:
        tokenizer = pickle.load(f)

    with open(LABEL_ENCODER_PATH, "rb") as f:
        label_encoder = pickle.load(f)

    # Sample input
    ticket_text = input("Enter customer ticket:\n")

    # Preprocess
    X = preprocess_text(ticket_text, tokenizer, MAX_LEN)

    # Predict queue
    pred = model.predict(X)
    queue = label_encoder.inverse_transform([pred.argmax()])[0]

    # Generate Gemini reply
    reply = generate_reply(GEMINI_API_KEY, ticket_text, queue)

    print("\nPredicted Queue:", queue)
    print("\nGenerated Reply:\n", reply)


if __name__ == "__main__":
    main()
