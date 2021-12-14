from tkinter import*

window=Tk()
window.geometry("500x500")

#for문으로 버튼에 이미지 입히고 버튼 가로 배치하기(3*3)
btnList=[None]*10
xPos, yPos =0,0

for i in range(1, 10):
    #버튼 생성
    btnList[i]=Button(window, text="버튼"+str(i))

i=1 #버튼의 인덱스 초기화
for col in range(1,5): #행의 갯수만큼 반복
    for row in range(1,3): #열의 갯수만큼 반복
    #버튼 배치
     btnList[i].place(x=xPos, y=yPos)
     xPos+=70 #버튼을 가로로 50씩 증가시켜 배치
     i+=1     #버튼의 인덱스 증가
 xPos=0       #버튼을 열 갯수만큼 배치하여 줄바꿈한 후 x를 o으로 배치
 yPos+=70     #버튼을 세로로 30씩 증가시켜 배치

window.mainloop()
