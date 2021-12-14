from tkinter import *
window=Tk()
window.geometry("210x210")

#이미지 준비-> 리스트와 for문을 활용하기
photoList=[""]*10
for i in range(1, 10, 1):
    photoList[i] = PhotoImage(file="gif/puz"+str(i)+".gif")
print(photoList)

#이미지를 입힌 버튼 생성->리스트와 for문을 활용하기
btnList=[None]*10
for i in range(1, 10, 1):
    btnList[i]=Button(window, image=photoList[i])


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



































