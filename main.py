import re

def clean_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_messages = []
    for line in lines:
        # Use regex to remove date, time, and user names
        message = re.sub(r'^\[\d{2}\.\d{2}\.\d{4}, \d{2}:\d{2}:\d{2}\] [^:]+: ', '', line)
        cleaned_messages.append(message.strip())

    # Write cleaned messages to a new file
    with open('cleaned_chat.txt', 'w', encoding='utf-8') as output_file:
        for message in cleaned_messages:
            if message:  # Only write non-empty messages
                output_file.write(message + '\n')

if __name__ == "__main__":
    clean_chat('_chat.txt')
