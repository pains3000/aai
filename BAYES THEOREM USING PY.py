def drug_user(prob_th=0.8, 
              sensitivity=0.79, 
              specificity=0.79, 
              prevelence=0.02, 
              verbose=True): 
    p_user=prevelence 
    p_non_user=1-prevelence 
    p_pos_user=sensitivity 
    p_neg_user=specificity 
    p_pos_non_user=1-specificity 
 
    num=p_pos_user*p_user 
    den=p_pos_non_user*p_user+p_pos_non_user 
 
    prob=num/den 
    if verbose: 
        if prob>prob_th: 
            print("The test-taker could be an user") 
        else: 
            print("The test-taker may not be an user") 
    return prob 
 
print("markus") 
p=drug_user(prob_th=0.5,sensitivity=0.97,specificity=0.95,prevelence=0.005) 
print("probability of test-taker being a drug user is:",round(p,3))

 
def bayes_theorem(prior_prob,likelihood,evidence): 
    posterior_prob=(likelihood*prior_prob)/evidence 
    return posterior_prob 
 
if __name__=="__main__": 
    prior_prob=0.01 
    likelihood_cancer=0.95 
    likelihood_no_cancer=0.10 
    evidence=(likelihood_cancer*prior_prob)+(likelihood_no_cancer*(1-prior_prob)) 
    posterior_prob=bayes_theorem(prior_prob,likelihood_cancer,evidence) 
    print("Prior Probability of Cancer:",likelihood_cancer) 
    print("Likelihood of Positive Test Given No Cancer:",round(posterior_prob,2)) 
