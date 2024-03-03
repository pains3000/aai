import time
time.clock = time.time
import aiml 
kernel = aiml.Kernel() 
kernel.learn("bot1.aiml") 
while True: 
  user_input = input("You: ") 
  if user_input.lower() == "exit": 
    print("Bot: Goodbye!") 
    break 
  bot_response = kernel.respond(user_input) 
  print("Bot:", bot_response) 
  bot_response = kernel.respond(user_input) 
  print("Chatbot:", bot_response) 
