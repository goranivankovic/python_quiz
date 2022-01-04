
#procentage win
procWin=0

#Questions variables
q1=''
q2=''
q3=''

q4=''
q5=''
q6=''

q7=''
q8=''
q9=''
q10=''



#Qustion 1 function
def ques1():

    global q1
    global procWin
    q1= input('Name the currency used in Japan?')

    if q1=='Yen' or q1=='yen' or q1=='YEN':

        procWin += 10


#Qustion 2 function
def ques2():

    global q2
    global procWin
    q2= input('In which country is the Leaning Tower of Pisa located?')

    if q2=='Italy' or q2=='italy' or q2=='ITALY':

        procWin += 10


#Qustion 3 function
def ques3():

    global q3
    global procWin
    q3= input('Name the fictional city Batman calls home?')

    if q3=='Gotham' or q3=='gotham' or q3=='GOTHAM':

        procWin += 10


#Qustion 4 function
def ques4():

    global q4
    global procWin
    q4= input('Who wrote Hamlet, lastname?')

    if q4=='Sekspir' or q4=='sekspir' or q4=='SEKSPIR':

        procWin += 10


#Qustion 5 function
def ques5():

    global q5
    global procWin
    q5= input('In what year did World War II end?')

    if q5=='1945':

        procWin += 10




#Qustion 6 function
def ques6():

    global q6
    global procWin
    q6= input('What is the technical term for a lie detector?')

    if q6=='Polygraph' or q6=='polygraph' or q6 =='POLYGRAPH':

        procWin += 10


#Qustion 7 function
def ques7():

    global q7
    global procWin
    q7= input('Babe Ruth is a legend of which sport?')

    if q7=='Baseball' or q7=='baseball' or q7 =='BASEBALL':

        procWin += 10

  
    
#Qustion 8 function
def ques8():

    global q8
    global procWin
    q8= input('What Is the smallest country in the world?')

    if q8=='Vatican' or q8=='vatican' or q8 =='VATICAN':

        procWin += 10

  


 #Qustion 9 function
def ques9():

    global q9
    global procWin
    q9= input('What is the capital of Serbia?')

    if q9=='Belgrad' or q9=='belgrad' or q9 =='BELGRAD':

        procWin += 10

       
 #Qustion 10 function
def ques10():

    global q10
    global procWin
    q10= input('What was the official name of Thailand before 1939?')

    if q10=='Siam' or q10=='siam' or q10 =='SIAM':

        procWin += 10


#Wining if else function

def winFunction():
    global procWin

    if procWin <= 50:
        print(f'You must study more, your winning percentage is {procWin}%')
    
    elif procWin == 70:
        print(f'You are not bad, your winning percentage is {procWin}%')

    elif procWin == 80:
        print(f'You are great, your winning percentage is {procWin}%')

    elif procWin == 100:
        print(f'You are grandmaster, your winning percentage is {procWin}%')



ques1()
ques2()
ques3()
ques4()
ques5()
ques6()
ques7()
ques8()
ques9()
ques10()

winFunction()

    
    




