str = "countthis"
print(len(str))

def rev_string(string):  
   
    words = string.split(' ')  
    
    reverse_string = ' '.join(reversed(words))  
    
    return reverse_string  
  
if __name__ == "__main__":  
    input = 'example string reverse a is This'
    print (rev_string(input)) 