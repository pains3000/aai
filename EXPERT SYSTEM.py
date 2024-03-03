import time
time.clock = time.time
import aiml 
def main(): 
  kernel = aiml.Kernel() 
  kernel.learn("flu.aiml") 
  print("Welcome to the flu diag center") 
  while True: 
    user_input = input("You: ").strip().lower() 
    if user_input == 'exit': 
      print("Goodbye!") 
      break 
    response = kernel.respond(user_input) 
    print("Expert System: " + response) 
if __name__ == "__main__":main() 
 
