'''
def say():
    return 'Hi'

a= say()
print(a)




def add(a,b):
    print("%d ,%d의 합은 %d 입니다" % (a,b,a+b))

a=add(3,4)
print(a)


def say():
    print("Hi")

say()



def add(a,b):
    return a+b

result= add(3,7)
print(result)
'''

#여러개의 입력값을 받는 함수 만들기
'''
def add_many(*args):   #*args처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어 준다
    result=0
    for i in args:
        result=result+i

    return result

#result = add_many(1,2,3)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)
'''
'''
def add_mul(choice , *args):
    if choice == "add":
        result=0
        for i in args:
            result=result+i
    elif choice=="mul":
        result=1
        for i in args:
            result=result*i
    return result

    
    #result= add_mul("add",1,2,3,4,5)
    result= add_mul('mul',1,2,3,4,5)
    print(result)
'''

#키워드 파라미터
'''
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
{'a':1}
print_kwargs(name='foo',age=3)
'''

#함수의 결과는 언제나 하나이다
'''
def add_add_mul(a,b):
    return a+b , a*b

#result = add_add_mul(3,4)
result1 , result2 = add_add_mul(3,4)
print (result1,result2)
'''

'''
def add_add_mul(a,b):
    return a+b
    return a*b

result = add_add_mul(2,3)
print(result)
'''
 

 #return의 또 다른 쓰임새
'''
def say_nick(nick):
    if nick =='에릭':
        return
    print("나의 별명은 %s 입니다" %nick)

say_nick('야호')
say_nick('에릭')  #입력한 값에 에릭 이 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져나감
'''

#매개변수에 초깃값 미리 설정하기
'''
def say_myself(name,old,man=True):  #man 이 매개변수에 True 라는 초깃값을 설정
    print("나의 이름은 %s 입니다" %name)
    print("나의 나이는 %d 입니다" %old)
    if man:
        print("남자입니다")
    else :
        print("여자입니다")


say_myself("박응용" ,27)
say_myself("박응용" ,27,True)
'''

'''
def say_myself(name,old,man=False):  #man 이 매개변수에 False 라는 초깃값을 설정
    print("나의 이름은 %s 입니다" %name)
    print("나의 나이는 %d 입니다" %old)
    if man:
        print("남자입니다")
    else :
        print("여자입니다")


say_myself("박응용" ,27)
say_myself("박응용" ,27,True)
'''

#vartest.py
'''
a=1
def vartest(a):
    a=a+1

vartest(a)
print(a)
'''

#vartest_error.py
#함수 안에서 선언한 매개변수는 함수 안에서만 사용된다!

'''
a=1
def vartest(a):
    a=a+1
    return a
a=vartest(a)
print(a)
'''


#vartest_global.py
#global 함수를 사용하면 외부에서도 변수를 활용할 수 있지만 권장하지는 않는다
'''
a=1
def vartest():
    global a
    a=a+1

vartest()
print(a)
'''

#lambda
'''
add=lambda a, b: a+b
result = add(3,4)
print(result)
'''


def add(a,b):
    return a+b

result=add(3,4)
print(result)