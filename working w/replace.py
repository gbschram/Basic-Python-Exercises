test_str = 'Python is best for programming and CS'
  
 
print("The original string is : " + str(test_str)) 
  
word_list = ["best", 'CS', 'for'] 
    
repl_wrd = 'oops'
  
res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()]) 
  
# printing result  
print("String after multiple replace : " + str(res))  