# Simple-Chatbot

## Overview
Chatbot Robo is a simple text-based chatbot designed to answer user queries based on a predefined text corpus. It utilizes **Natural Language Processing (NLP)** techniques such as **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to generate responses.

## Features
- Responds to user input using a predefined dataset.
- Recognizes and replies to common greetings.
- Uses **TF-IDF vectorization** to determine the best-matching response.
- Handles unknown queries gracefully by prompting users to rephrase.
- Simple and easy-to-use console-based interface.

## Technologies Used
- **Python**
- **NLTK (Natural Language Toolkit)**
- **Scikit-learn**
- **NumPy**

## Installation
Ensure you have **Python 3.x** installed on your system.

1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/chatbot-robo.git
   cd chatbot-robo
   ```

2. Install dependencies:
   ```sh
   pip install numpy scikit-learn nltk
   ```

3. (Optional) Download additional NLTK resources:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   ```

## Usage
1. Prepare a text file (`chatbot.txt`) containing relevant data for the chatbot to learn from.
2. Run the script:
   ```sh
   python chatbot.py
   ```
3. Start chatting with the bot! Type "exit" to quit.

## Example Interaction
```
BOT: Hello! I'm ChatBot. Type 'exit' to end our conversation.
User: Hi
BOT: Hey there!
User: What is a chatbot?
BOT: A chatbot is a program designed to simulate conversation with humans.
User: Thank you
BOT: You're welcome!
```

## Future Improvements
- Add a **GUI** using Tkinter or a web framework.
- Integrate **Machine Learning models** for smarter responses.
- Expand the knowledge base with dynamic data sources.

## License
This project is open-source and available under the MIT License.

