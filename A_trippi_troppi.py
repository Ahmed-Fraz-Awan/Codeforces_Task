# taking the input --> number of test cases
t = int(input())  
# for each test case 
for _ in range(t):
    # get each string and split them into three
    first, second, third = input().split()  
    
    # building the modern name
    modern = first[0] + second[0] + third[0]  
    
    print(modern)