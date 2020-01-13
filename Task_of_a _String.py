'''
Problem Statement ->>

Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:
deletes all the vowels,
inserts a character "." before each consonant,
replaces all uppercase consonants with corresponding lowercase ones.
Vowels are letters "A", "O", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.
Help Petya cope with this easy task.

Input Format:
The first line represents input string s of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.

Constraints

1 < |s| <= 100

Output Format

Print the resulting string. It is guaranteed that this string is not empty.

Sample Input 0:
tour
Sample Output 0:
.t.r

Sample Input 1:
aBAcAba
Sample Output 1:
.b.c.b

'''
#Hackerrank Que..

inputString = input()
inputString.lower()         # to convert input on lowerCase
for i in inputString:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" :
        continue
    print("."+i,end="")