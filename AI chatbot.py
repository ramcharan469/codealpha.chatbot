def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit the conversation.")
    
    # Simple loop for continuous interaction
    while True:
        # Input from user
        user_input = input("You: ").lower().strip()

        # Rule-based logic using if-elif
        # Predefined replies
        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi!, how  can i help you ")
        
        elif user_input in ["how are you", "how's it going"]:
            print("Chatbot: I'm fine, thanks!")
        
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot:  Hi! I'm Ramya  chatbot. your AI chatbot .")
            
        elif user_input in ["bye", "goodbye", "exit"]:
            print("Chatbot: Goodbye!")
            break
        elif user_input in ["tell me a joke", "joke"]:
            print("Chatbot: Why don't scientists trust atoms?")
            print("Chatbot: Because they make up everything!")
            
        elif user_input in ["who created you", "who developed you", "who are you"]:
                print("Chatbot: I Am Ramya  an Ai chatbot developed by Akula.Ram charan.")
        break
    else:
     print("Chatbot: I'm sorry, I don't understand that. Can you try again?")
                                    
if __name__ == "__main__":
    chatbot()

