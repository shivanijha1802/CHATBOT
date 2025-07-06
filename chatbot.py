# chatbot.py
# Author: Shivani Jha
# Date: 2025-07-06
# Description: A simple, fun, and interactive rule-based chatbot.


print("ChatBot: Hello! I am your friendly chatbot. \n Type 'help' to see what can I help you with. Type 'bye' anytime to exit.")

while True:
    user_input = input("You: ").lower().strip()         # Input Handling

    # Condition to exit
    if user_input == "bye":
        print("ChatBot: Goodbye! Take care.")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("ChatBot: Hi there! How can I help you?")

    # Help command which displays the list of commands
    elif "help" in user_input:
        print("ChatBot: I'm here for you help! \n Here are some things I can help you with: ")
        print(" - 'hello', 'hi', 'how are you'")
        print(" - 'time', 'date'")
        print(" - 'joke', 'quote', 'fact'")
        print(" - 'suggest a movie', 'tell me a riddle', 'it's my birthday', 'what is life'")
        print(" - 'bye' to exit")
        print("Just type it!")

    elif "how are you" in user_input:
        print("ChatBot: I'm doing great, thanks for asking!")

    elif "time" in user_input:
        from datetime import datetime
        print("ChatBot: The current time is: ", datetime.now().strftime("%H:%M:%S"))

    elif "date" in user_input:
        from datetime import datetime
        print("ChatBot: The current date is: ", datetime.now().strftime("%d/%m/%Y"))

    elif "joke" in user_input:
        print("ChatBot: Her's a Joke: \n Why do Java programmers have to wear glasses? Because they don't C#.")

    elif "quote" in user_input:
        print("ChatBot: Here's a quote- \n You're braver than you believe, stronger than you seem, and smarter than you think!")

    elif "fact" in user_input:
        print("ChatBot: Here's a fact- \n Did you know that an Octopus has three hearts and nine brains? \n Shocking fact right?")

    elif "suggest a movie" in user_input:
        print("ChatBot: Here's a best movie to watch- 3 Idiots -- Don’t aim for success, instead chase excellence.")
    
    elif "tell me a riddle" in user_input:
        print("ChatBot: Her's a riddle for you- \n What has keys but can’t open locks? A piano!")

    elif "it's my birthday" in user_input:
        print("ChatBot: Happy Birthday! May your code always run error-free!")

    elif "what is life" in user_input:
        print("ChatBot: Life is a loop of inputs and outputs... with the occasional bug, and we have to resolve those bugs and move foreward happily!")

    else :
        print("ChatBot: Hmm... Sorry! I didn't get that. Try asking something else or just type 'help'.")