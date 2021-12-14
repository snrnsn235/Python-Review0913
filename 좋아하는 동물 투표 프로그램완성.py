#라벨, 라디오버튼, 버튼, 이미지활용
from tkinter import *
window=Tk()
window.geometry("400x400") #크기지정
window.title("애완동물 선택하기")#윈도우창 제목 정하기

#함수 정의 부분
def myFunc():
    if var.get() == 1:#버튼1을 선택했다면.
        labelImage.configure(image=photo1)
    elif var.get() == 2:#버튼2을 선택했다면.
        labelImage.configure(image=photo2)
    else :#버튼3을 선택했다면.
        labelImage.configure(image=photo3)

#메인 코드 부분
#글씨의 폰트와 글자색깔, 그리고 text에 들어갈 문구지정        
labelText = Label(window, text="좋아하는 동물 투표 ", fg="blue", font=("나눔고딕", 20))
#정수형 형식의 변수를 생성하는 함수
var=IntVar()
#라디오 버튼을 선택하면 var변수 값을 각각 1,2,3으로 대입
rb1=Radiobutton(window, text="강아지", variable=var, value=1, command=myFunc)
rb2=Radiobutton(window, text="고양이", variable=var, value=2, command=myFunc)
rb3=Radiobutton(window, text="토끼", variable=var, value=3, command=myFunc)
buttonOk=Button(window, text="사진보기", command=myFunc)

#절대 경로X, 상대경로(O)
#각각의 라디오버튼과 연결된 이미지 준비해서 지
photo1=PhotoImage(file="gif/dog4.gif")
photo2=PhotoImage(file="gif/cat.gif")
photo3=PhotoImage(file="gif/rabbit.gif")
#이미지위젯 labelImage 생성, 빈 이미지 표시(처음엔 아무것도 없음)
labelImage=Label(window, width=200, height=200, bg="yellow",image=None)
#가로세로 200, 배경은 노란색, 빈 이미지박스(처음부터 이미지가 나오는 걸 보고 싶다면 Image에 photo1,2,3을 넣으면 된다.

#디스플레이되는 곳
labelText.pack(padx=5, pady=5) #가로 세로 여백을 x,y로 나누고 여백 지
rb1.pack(padx=5, pady=5)
rb2.pack(padx=5, pady=5)
rb3.pack(padx=5, pady=5)
buttonOk.pack(padx=5, pady=5)
labelImage.pack(padx=5, pady=5)

window.mainloop()
