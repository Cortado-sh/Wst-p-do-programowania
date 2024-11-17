index = 10
number = 0
while(index>0):
    if(number>1) and (number%2!=0 or number==2) and (number%3!=0 or number==1) and (number%7!=0 or number==7) and (number%5!=0 or number==5):
        print(number)
        index -= 1
    number+=1