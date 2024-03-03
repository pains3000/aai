def conditiona(): 
    pass_stats=0.15 
    pass_codingWstats=0.60 
    pass_codingWOstats=0.40 
    prob_both=pass_stats*pass_codingWstats 
    print("The probability that applicant passes both is",round(prob_both,3)) 
    prob_coding=(prob_both)+((1-pass_stats)*pass_codingWOstats) 
    print("Probability that he/she passes only coding is",round(prob_coding,3)) 
    status_given_coding=prob_both/prob_coding 
    print("Conditional Probability is",round(status_given_coding,3)) 
print("MARKUS") 
conditiona()
 
def get_valid_probability_input(prompt): 
    while True: 
        try: 
            probability=float(input(prompt)) 
            if 0<= probability <=1: 
                return probability 
            else: 
                print("probability must be between 0 and 1. please try") 
        except ValueError: 
            print("Invalid input. please enter a valid probability between o and 1.") 
P_B= get_valid_probability_input("Enter the probability of event B(0 to 1):") 
P_A_and_B=get_valid_probability_input("Enter the probability of events A and B (0 to 1):") 
P_A_given_B= P_A_and_B/P_B 
if P_A_given_B >1: 
    print("Inconsistent result.Please check the inputs again.") 
else: 
    formatted_result = "{:.2f}".format(P_A_given_B) 
    print("P(A|B)=", formatted_result)
