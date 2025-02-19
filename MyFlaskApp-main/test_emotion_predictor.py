from emotion_predictor import emotion_predictor

text = "I am very happy today!"
result = emotion_predictor(text)
print(result)  # {"text": "I am very happy today!", "emotions": {...}}