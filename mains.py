#task1
#way1

list1 = [10, 21, 4, 45, 66, 93]
for num in list1:
    if num % 2 == 0:
        print(num, end=" ")
#way2

list1 = [10, 21, 4, 45, 66, 93]
even_nos = [num for num in list1 if num % 2 == 0]
print("Ro'yxatdagi juft raqamlar: ", even_nos)

# 1-listdan 2-listga faqat juftlarini olib kelish 

#task2
#way1
num = 97402
num_string = str(num)
reverse_num = ''
for i in range(0,len(num_string)):
    reverse_num = num_string[i] + reverse_num
print("Teskari raqam: " + reverse_num)

#way2

num = 97402
num_string = str(num)
size = len(num_string)
reversed_num = num_string[size::-1]
print("Teskari raqam: " + reversed_num)

#o'zgaruvchi ichidagi sonlarni teskari tartibda chiqarish

################################################
def isPalindrome(s):
    return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
#################################################
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Teskari: " + str(reversed_num))
##################################################
list1 = [10, 21, 4, 45, 66, 93]
even_nos = [num for num in list1 if num % 2 == 0]
print("Ro'yxatdagi juft raqamlar: ", even_nos)
##################################################
import datetime
# Datetime object
millenium_turn = datetime.datetime(2022, 11, 3, 0, 0, 0)
print(millenium_turn)

