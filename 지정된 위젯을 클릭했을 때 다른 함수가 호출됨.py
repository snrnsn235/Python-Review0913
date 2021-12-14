from tkinter import *
from tkinter import messagebox

#함수 정의 부분
def clickImage(event):
    messagebox.showinfo("마우스", "토끼에서 마우스가 클릭됨")

#메인 코드 부분
window=Tk()
window.geometry("400x400")
photo=PhotoImage(file="gif/rabbit.gif")
label1=Label(window, image=photo)

label1.bind("<Button>", clickImage) #이미지에서 마우스를 클릭했을 때 함수 표출
                                    #이미지는 윈도우 위에 있으므로 왼쪽 버튼 클릭시 
label1.pack(expand=1, anchor=CENTER)
window.mainloop()
