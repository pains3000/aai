while True: 
        try: 
            P_A=float(input("Enter the probability of event A(0 to 1):")) 
            if 0<= P_A <=1: 
                break 
            else: 
                print("probability must be between 0 and 1. please try again") 
        except ValueError: 
            print("Invalid input. please enter a valid probability between o and 1.") 
while True: 
        try: 
            P_B=float(input("Enter the probability of event B(0 to 1):")) 
            if 0<= P_B <=1: 
                break 
            else: 
                print("probability must be between 0 and 1. please try again") 
        except ValueError: 
            print("Invalid input. please enter a valid probability between o and 1.") 
P_A_and_B=P_A*P_B 
formatted_result = "{:.2f}".format(P_A_and_B) 
print("P(A and B)",formatted_result) 
