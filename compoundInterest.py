def compound_interest(principle, rate, time): 
  
 
    Amount = principle * (pow((1 + rate / 100), time)) 
    CI = Amount - principle 
    print("Compound interest is", CI) 
    
compound_interest(1000, 10.50, 5)