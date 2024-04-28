# # without nltk
# import random

# class CustomerSupportChatbot:
#     def __init__(self):
#         self.greetings = ["Hi there! How can I assist you today?", "Hello! What can I help you with?", "Hey! How may I help you?"]
#         self.responses = {
#             "order status": "To check your order status, please provide your order number.",
#             "payment issue": "For payment issues, please contact our billing department at billing@example.com.",
#             "product information": "To learn more about our products, please visit our website at www.example.com/products.",
#             "technical support": "For technical support, please visit our support page at www.example.com/support.",
#             "general inquiry": "For general inquiries, you can reach out to us at info@example.com."
#         }

#     def respond_to_inquiry(self, inquiry):
#         inquiry = inquiry.lower()
#         for key, value in self.responses.items():
#             if key in inquiry:
#                 return value
#         return "I'm sorry, I couldn't understand your inquiry. Please provide more details or try a different question."

# chatbot = CustomerSupportChatbot()
# print(random.choice(chatbot.greetings))
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         print("Goodbye! Have a great day!")
#         break
#     else:
#         response = chatbot.respond_to_inquiry(user_input)
#         print("Bot:",response)



# with nltk
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

class CustomerSupportChatbot:
    def __init__(self):
        self.greetings = ["Hi there! How can I assist you today?", "Hello! What can I help you with?", "Hey! How may I help you?"]
        self.responses = {
            "order_status": "To check your order status, please provide your order number.",
            "payment_issue": "For payment issues, please contact our billing department at billing@example.com.",
            "product_information": "To learn more about our products, please visit our website at www.example.com/products.",
            "technical_support": "For technical support, please visit our support page at www.example.com/support.",
            "general_inquiry": "For general inquiries, you can reach out to us at info@example.com."
        }
        self.stop_words = set(stopwords.words('english'))

    def preprocess_input(self, text):
        tokens = word_tokenize(text.lower())
        filtered_tokens = [word for word in tokens if word.isalnum() and word not in self.stop_words]
        return filtered_tokens

    def greet_user(self):
        return 

    def respond_to_inquiry(self, inquiry):
        inquiry_tokens = self.preprocess_input(inquiry)
        for key, value in self.responses.items():
            if key in inquiry_tokens:
                return value
        return "I'm sorry, I couldn't understand your inquiry. Please provide more details or try a different question."

chatbot = CustomerSupportChatbot()
print(random.choice(chatbot.greetings))
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye! Have a great day!")
        break
    else:
        response = chatbot.respond_to_inquiry(user_input)
        print("Bot:",response)




# import random
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords

# nltk.download('punkt')
# nltk.download('stopwords')

# stop_words = set(stopwords.words('english'))



# greeting = ["Hello","Hey, how can i assist you?","Namaste"]
# bye = ["Bye Bye","Tata","see you soon"]

# def chat():
#     while True:
#         x = input("You: ").lower()

#         tokens = word_tokenize(x)
#         filtered_tokens = [word for word in tokens if word not in stop_words]
#         # print("\n",filtered_tokens)

#         if any(word in filtered_tokens for word in ["hello", "hey"]):
#             print(random.choice(greeting))
#         elif any(word in filtered_tokens for word in ["bye", "see you later"]):
#             print(random.choice(bye)+"!")  
#         else:
#             print("Not in data base yet.") 
# chat()


