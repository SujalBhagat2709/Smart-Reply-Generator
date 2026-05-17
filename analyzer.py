greeting_keywords = [
    "hello",
    "hi",
    "hey"
]

meeting_keywords = [
    "meeting",
    "schedule",
    "call"
]

def detect_message_type(message):
    
    message = message.lower()
    
    for word in greeting_keywords:
        
        if word in message:
            return "greeting"
    
    for word in meeting_keywords:
        
        if word in message:
            return "meeting"
    
    return "general"


if __name__ == "__main__":
    
    text = "Hey, are you available for a meeting?"
    
    print(detect_message_type(text))