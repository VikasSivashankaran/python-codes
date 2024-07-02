dict1={'name':'car',
       'wheels':'4',
       'color': None}
print("Original dictionary:",dict1)

dict1={key:values for (key,values)in dict1.items() if values is not None}
print(dict1)

dict2={'name':'siva',
       'age':'25',
       'gender':None}
print(dict2)

dict2={key:value for (key,value) in dict2.items() if value is not None}
print(dict2)