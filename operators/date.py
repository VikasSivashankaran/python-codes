'''Write a Python program to display the examination schedule. (extract the date from     exam_st_date).
    exam_st_date = (11, 12, 2014)
    Sample Output : The examination will start from : 11 / 12 / 2014
'''
exam_st_date = (11, 12, 2014)
d,m,y=exam_st_date
print(f"The examination will start from :{d}/{m}/{y}")