import random as rdm

lottery_num = rdm.randint(1, 60)
print(lottery_num)

train_set = [1, 2, 3, 5]
#ramd = rdm.shuffle(train_set)#操作是原址的，所以这一步并不会返回任何值。
rdm.shuffle(train_set)
print(train_set)

print(rdm.sample(train_set, 2))