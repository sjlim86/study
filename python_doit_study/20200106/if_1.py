'''
money = True
if money:
    print("택시")
else:
    print("걸어")




money=2000
if money>=3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


money=2000
card=True
if money >=3000 or card:
    print("택시를 타고 가")
else:
    print("걸어가자")
    
pocket=['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타고 가자")
else:
    print("걸어가자")


pocket=["paper" , "money" , "cellphone"]
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
    

    #주머니에 돈이 있으면 택시를 타고 , 
    #주머니에 돈은 없지만 카드가 있으면 택시를 타고 , 
    #돈도 없고 카드도 없으면 걸어가

    #1
    pocket=['paper','cellphone']
    card=True
    if 'money' in pocket:
        print("택시를 타")
    else:
        if card:
            print("택시를 타")
        else:
            print("걸어가자")
  '''


pocket=["paper","cellphone"]
card=True
if 'money' in pocket:
    print("택시를 타자")
elif card:
    print("택시를 타자")
else:
        print("걸어가자")