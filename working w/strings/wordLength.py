def string_k(k, str): 
      
    string = [] 
      
    text = str.split(" ") 
      
    for x in text: 
          
        if len(x) > k: 
              
            string.append(x) 
              
    return string 
        
k = 3
str ="This program will eliminate any word in this string that is less than specified in K"
print(string_k(k, str))