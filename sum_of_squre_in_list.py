
#sum of squares of numbers given in list
def sum_of_squares(list_num):
    result=0
    l=len(list_num)
    for i in list_num:
        result+=(i**2)
        i+=1
    return result

list_num=[1,2,3,4,5,6]
M=sum_of_squares(list_num)
print("The sum is",M)
