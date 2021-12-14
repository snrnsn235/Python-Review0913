from tkinter import *
from tkinter import messagebox

window=Tk()

#함수정의부분
#chk.get() 함수로 체크버튼에 설정된 값 가져와 메시지 출력
def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("", "체크버튼이 켜졌어요,")

#메인 코드 부분
#Intvar()는 정수형 형식의 변수를 생성하는 함수
chk=IntVar()

#checkbutton() 위젯으로부터 체크버튼 cb1인스턴스 생성
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, comman=myFunc)
#체크버튼을 켜면 chk에 1이, 끄면 chk에 0이 대입됨
#체크버튼을 켜거나, 끄면 myfunc함수가 실행됨

#체크버튼 cb1표
cb1.pack()

window.mainloop()
