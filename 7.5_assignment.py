def calculation(queue):
    served = []
    bill25 = 0      #bisa pake dictionary {25:0,50:0,100:0}
    bill50 = 0
    bill100 = 0
    for i in queue:
        if i == 25:
            bill25 += 1
            sell = 'Yes'
            served.append(i)
        elif i == 50:
            if bill25 > 0: #ada kembalian
                bill50 += 1
                bill25 -= 1
                sell = 'Yes'
                served.append(i)
            else:
                sell = 'No'
                break
        elif i == 100:
            if bill25 >= 3:
                bill100 += 1
                bill25 -= 3
                sell = 'Yes'
                served.append(i)
            elif bill25 > 0 and bill25 < 3 and bill50 > 0:
                bill100 += 1
                bill25 -= 1
                bill50 -= 1
                sell = 'Yes'
                served.append(i)
            else:
                sell = 'No'
                break
    print(f'Bill 25 = {bill25}')
    print(f'Bill 50 = {bill50}')
    print(f'Bill 100 = {bill100}')
    print(f'Antrian = {queue}')
    print(f'Dilayani = {served}')
    print(sell)

calculation([25,25,50,50,25,25,100,50,25,50])





