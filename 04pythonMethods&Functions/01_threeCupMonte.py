from random import shuffle

example = [1, 2, 3, 4, 5, 6, 7]
shuffle(example)
print(example)

def shufflelist(mylist):
    shuffle(mylist)
    return mylist

#player is going to guess the location

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input('pick a number: 0,1,2 ---')

    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess]=='o':
        print('correct')
    else:
        print('wrong guess')
        print(mylist)


#Initial list
mylist=['','o','']

#shuffle list
mixedup_list=shufflelist(mylist)

#user guess
guess=player_guess()

#check guess
check_guess(mixedup_list,guess)
