from analyzer import detect_message_type

reply_templates = {
    "greeting": [
        "Hey! How are you?",
        "Hello! Nice to hear from you."
    ],
    "meeting": [
        "Sure, let me check my schedule.",
        "I am available tomorrow."
    ],
    "general": [
        "Sounds good.",
        "Okay, noted."
    ]
}

def generate_reply(message):
    
    message_type = detect_message_type(message)
    
    return reply_templates[message_type][0]


if __name__ == "__main__":
    
    text = "Hey, are you available for a meeting?"
    
    print(generate_reply(text))