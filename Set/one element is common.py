def common_member(ar1, ar2):
    a_set = set(ar1)
    b_set = set(ar2)
    
    if (a_set & b_set):
        print("True")
        
    else:
        print("false") 
          
  
ar1 = [1, 5, 10, 30, 40, 80]
ar2 = [6, 7, 20, 80, 100]


common_member(ar1, ar2)
  
