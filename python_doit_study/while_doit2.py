'''
coffee=10
money=300
while money: #머니가 300 고정이므로 해당 조건은 항상 참이다 , 즉 무한으로 반복
    print("돈 들어옴 커피 ㄱㄱ")
    coffee = coffee-1
    print("남은 커피의 양은 %d개 입니다" % coffee)
    if coffee==0:
        print("커피가 없습니다 판매를 중지합니다")
        break
  

#coffee.py

coffee=10
while True:
    money=int(input("돈을 넣어 주세요:"))
    if money==300:
        print("커피 ㄱ")
        coffee = coffee - 1
        print("남은 커피는 %d개 입니다" %coffee)
    elif money > 300:
        print("거스름돈 %d를 주고 커피 ㄱ" %(money-300))
        coffee = coffee - 1
        print("남은 커피는 %d개 입니다" %coffee)
    else:
            print("커피값이 모자랍니다")
            print("남은 커피는 %d개 입니다" %coffee)
    if coffee==0:
            print("남은 커피가 없습니다")
            break
  

#홀수 출력  
a=0
while a<10:
      a=a+1
      if a%2==0 : continue
      print(a)
      
#1부터 10까지의 숫자 중에서 3의 배수를 뺸 나머지 값을 출력

a=0
while a<10:
    a=a+1
    if a%3==0: continue
    print(a)


while True:
    print("Ctrl+C 를 눌러야 While문을 빠져나갈 수 있습니다")

 '''


test_list=['one','two','three']
for i in test_list:
    print(i)