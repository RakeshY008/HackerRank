'''
You are given a string where each char of string represents a candy. Find the total different types of candies.

Input Format

First line contains T, number of testcases, Next T lines contains a string S representing box of candies.

Constraints

0 < |S| < 100000000

Output Format

For each testcase in T, print number of types of candies.

Sample Input 0

1
abc
Sample Output 0

3

'''

#Hackerrank Que ...

intInput = int(input())         # int dat type of input recieved
for i in range(0,intInput):     #loop will be running for 'intInput' no. of times
    stringInput = input()
    stringInput = set(stringInput)  #storing inputs in set to remove data duplicacy
    print(len(stringInput)) #length of input will be displayed
