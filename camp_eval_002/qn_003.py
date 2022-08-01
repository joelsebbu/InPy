# Q3. The denominations in Indian currency are:
# |1, |2, |5, |10, |,20, |50, |100, |200, |500, |2000.
# Given an amount N, print how many coins/notes make up N
# Sample input:
# Enter the amount: 2640
# Output:
# 2000 1
# 500 1
# 100 1
# 10 4
# Also test your program with N=3781, 4928, and 5134


def denominate(n):
    denominations =[2000,500,200,100,50,20,10,5,2,1]
    print("Output:")
    for denomination in denominations:
        noteCount = n//denomination
        if noteCount > 0:
            print(denomination,noteCount)
            n -= denomination * noteCount
denominate(2640)
# Output:
# 2000 1
# 500 1
# 100 1
# 20 2
denominate(3781)
# Output:
# 2000 1
# 500 3
# 200 1
# 50 1
# 20 1
# 10 1
# 1 1
denominate(4928)
# Output:
# 2000 2
# 500 1
# 200 2
# 20 1
# 5 1
# 2 1
# 1 1
denominate(5134)
# Output:
# 2000 2
# 500 2
# 100 1
# 20 1
# 10 1
# 2 2