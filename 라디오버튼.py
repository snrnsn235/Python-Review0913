#라디오버튼은 여러개 중 하나를 선택하기 위해 사용되는 위젯
#Radiobutton(부모 윈도우, 옵션)
from tkinter import *
window=Tk()

#함수정의부분
#var변수의 값에 따라 윈도우 하단 라벨 label1의 텍스트를 변경
#위젯명.configure(옵션=값)은 해당 위젯의 옵션값을 변경해주는 함
def myFunc():
    if var.get() == 1:
        label1.configure(text="파이썬")
    elif var.get()==2:
        label1.configure(text="C++")
    else :
        label1.configure(text="Java")

#메인코드부분
#3개의 라디오 버튼 준비 
var=IntVar()
#rb1 버튼을 선택하면 var의 값으로 1이 대입
rb1 = Radiobutton(window, text="파이썬", variable=var, value=1, command=myFunc)
#rb2 버튼을 선택하면 var의 값으로 2이 대입
rb2 = Radiobutton(window, text="C++", variable=var, value=2, command=myFunc)
#rb3 버튼을 선택하면 var의 값으로 3이 대입
rb3 = Radiobutton(window, text="Java", variable=var, value=3, command=myFunc)
#Label로 텍스트 위젯 label1을 생성
label1 = Label(window, text="선택한 언어 : ", fg="red")

#3개의 라디오버튼과 1개의 텍스트를 윈도우에 디스플레잉해주는 곳
rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()
