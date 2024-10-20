import google.generativeai as genai
import os

def init_conversation():
    user_input = input("If you want to exit the application type 'exit'\n\n"
                       "How can I help you today?\n"
                       "> ")
    response = model.generate_content(user_input)
    print("Gemini: " + response.text)

def conversation():
    while True:
        convo_user_input = input("> ")
        if convo_user_input == "exit":
            return
        convo_response = model.generate_content(convo_user_input)
        print("Education Buddy: " + convo_response.text)

if __name__ == "__main__":
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash"
                                  , system_instruction="You are an Educator and your objective is, to help students as good as you can with their problems and help them to study efficiently.")
    init_conversation()
    conversation()