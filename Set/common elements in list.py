def common_member(ar1, ar2, ar3):
    a_set = set(ar1)
    b_set = set(ar2)
    c_set = set(ar3)
    
    if (a_set & b_set & c_set):
        print(a_set & b_set & c_set,"is common")
        
    else:
        print("No common elements") 
          
  
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

common_member(ar1, ar2, ar3)
  
