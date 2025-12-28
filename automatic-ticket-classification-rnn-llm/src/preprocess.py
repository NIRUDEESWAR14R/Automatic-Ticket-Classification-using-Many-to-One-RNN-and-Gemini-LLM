from keras.utils import pad_sequences

def clean_text(text: str) -> str:
    return text.lower().replace("\n", " ").strip()

def preprocess_text(text: str, tokenizer, max_len: int):
    cleaned = clean_text(text)
    seq = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(seq, maxlen=max_len, padding="post", truncating="post")
    return padded
