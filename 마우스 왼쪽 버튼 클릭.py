from tkinter import *
from tkinter import messagebox


#함수 정의 부분
def clickLeft(event) :
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼 클림됨")
def clickCenter(event) :
    messagebox.showinfo("마우스", "중간 마우스 버튼 클림됨")
def clickRight(event) :
    messagebox.showinfo("마우스", "오른쪽 마우스 버튼 클림됨")

#메인 코드 부분
window=Tk()

window.bind("<Button-1>", clickLeft)
window.bind("<Button-2>", clickCenter)
window.bind("<Button-3>", clickRight)


window.mainloop()
