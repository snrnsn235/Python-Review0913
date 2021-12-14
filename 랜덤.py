from tkinter import *
import random
#이미지를 랜덤하게 넣기
window=Tk()
window.geometry("210x210")
'''
#이미지를 준비
photo1 = PhotoImage(file="gif/puz1.gif")
photo2 = PhotoImage(file="gif/puz2.gif")
photo3 = PhotoImage(file="gif/puz3.gif")
photo4 = PhotoImage(file="gif/puz4.gif")
photo5 = PhotoImage(file="gif/puz5.gif")
photo6 = PhotoImage(file="gif/puz6.gif")
photo7 = PhotoImage(file="gif/puz7.gif")
photo8 = PhotoImage(file="gif/puz8.gif")
photo9 = PhotoImage(file="gif/puz9.gif")
'''
# 리스트에 랜덤한 이미지 배치
fnameList=["gif/puz1.gif"]
for i in range(2, 10):
    fnameList.append("gif/puz"+str(i)+".gif")
random.shuffle(fnameList) #리스트 섞기 

    
#이미지 준비-> 리스트와 for문을 활용하기
photoList=[""]*10
for i in range(1, 10, 1):
    #photoList[i] = PhotoImage(file="gif/puz"+str(i)+".gif")
    photoList[i] = PhotoImage(file=fnameList[i-1]) #랜덤함수로 재배치된 이미지 리스트 불러옴
print(photoList)

'''
#이미지를 입힌 버튼 생성
btn1=Button(window, image=photo1)
btn2=Button(window, image=photo2)
btn3=Button(window, image=photo3)
btn4=Button(window, image=photo4)
btn5=Button(window, image=photo5)
btn6=Button(window, image=photo6)
btn7=Button(window, image=photo7)
btn8=Button(window, image=photo8)
btn9=Button(window, image=photo9)
'''
#이미지를 입힌 버튼 생성->리스트와 for문을 활용하기
btnList=[None]*10
for i in range(1, 10, 1):
    btnList[i]=Button(window, image=photoList[i])

'''
#버튼 배치
btn1.place(x=0,y=0)
btn2.place(x=70,y=0)
btn3.place(x=140,y=0)
btn4.place(x=0,y=70)
btn5.place(x=70,y=70)
btn6.place(x=140,y=70)
btn7.place(x=0,y=140)
btn8.place(x=70,y=140)
btn9.place(x=140,y=140)
'''
#버튼 배치 ->for문을 활용하기
xPos, yPos = 0, 0 #place의 x,y 좌표값
i=1 #버튼의 인덱스 초기화 
for col in range(1,4): #행의 개수만큼 반복
    for row in range(1,4): #열의 개수만큼 반복
        btnList[i].place(x=xPos, y=yPos)
        xPos+=70 #버튼을 x축으로 증가시켜 배치
        i+=1 #버튼의 인덱스 증가
        #여기선 y값을 넣으면 안되는데 넣으면 사선으로 배치가 된다.
    xPos=0 #버튼의 열 갯수만큼 배치하여 줄바꿈한 후 x를 0으로 배치
    yPos+=70 #버튼을 세로로 70씩 증가시켜 배

window.mainloop()

'''
#변수 선언 부분
btnList = [None]*9

fnameList = ["eclair]
'''



































