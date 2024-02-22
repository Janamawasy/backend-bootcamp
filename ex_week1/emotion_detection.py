# pre processing the text :: remove Punctuation + lowercase()


# emotions dict
emotion_dict = {'happy': ['happy', 'joy', 'excited', 'delighted'],
                'sad': ['sad', 'unhappy', 'depressed', 'gloomy']}


def detect_emotions(text, emotion_dict):
    happy_score = 0
    sad_score = 0
    
    for word in text.split():
        for emotion, expressions in emotion_dict.items():
            if word.lower() in expressions:
                if emotion == 'happy':
                    happy_score += 1
                elif emotion == 'sad':
                    sad_score += 1
    
    return happy_score, sad_score


text = "I am feeling happy today and joy and delighted and a little bit sad"
happy_score, sad_score = detect_emotions(text, emotion_dict)

print("Happy score:", happy_score)
print("Sad score:", sad_score)
