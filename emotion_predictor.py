def emotion_predictor(text):
    authenticator = IAMAuthenticator('your-iam-apikey')
    nlu = NaturalLanguageUnderstandingV1(
        version='2021-03-25',
        authenticator=authenticator
    )
    nlu.set_service_url('your-service-url')

    response = nlu.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()

    emotions = response['emotion']['document']['emotion']
    formatted_output = {
        "text": text,
        "emotions": emotions
    }
    return formatted_output