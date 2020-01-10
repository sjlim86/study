'''
test_list=['one','two','three']
for i in test_list:
    print(i)


a=[(1,2),(3,4),(5,6)]
for (first , last) in a:
    print(first+last)



#marks1.py

marks = [90,25,67,45,80]
number=0

for mark in marks:
    number=number+1
    if mark >=60:
        print("%d 학생은 합격입니다" %number)
    else:
        print("%d 학생은 불합격입니다" %number)


#marks2.py

marks = [90,25,67,45,80]
number=0
for mark in marks:
    number=number+1
    if mark<60: continue
    print("%d번 축하합니다" %number)



#range 함수

a=range(10)
print(a)


add=0
for i in range(1,11):
    add=add+i

print(add)


#marks3.py

marks = [90,25,67,45,80]
for number in range(len(marks)):
    if marks[number] <60: continue
    print("%d번 학생 축하합니다" %(number+1))


#print("C:\\\\Windows")



for i in range(2,10):
    for j in range(1,10):
        print(i*j , end=" ")
    print('')
 


a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print(result)


a=[1,2,3,4]
result=[num*3 for num in a if num%2==0]
print(result)
'''

# 1~1000 까지의 자연수 중 3의 배수의 합

result=0
i=1
while i<=1000:
    if i%3!=0: continue
    result += i
    i+=i
print(result)
