'''
from tkinter import *
window=Tk()

#버튼 인스턴스3개 생성
button1=Button(window,text="버튼1")
button2=Button(window,text="버튼2")
button3=Button(window,text="버튼3")
#버튼 3개를 화면에 가로로 디스플레이
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

window.mainloop()
'''
#리스트와 for문을 이용한 버튼 생성 및 출력
from tkinter import *
window=Tk()
window.geometry("400x400")

button=[""]*3 
'''
#빈 인덱스 3개를 만들자
#btnlist=[none]*3과 같다.
#리스트를 이용한 위젯 생성
button[0] = Button(window, text="버튼1")
button[1] = Button(window, text="버튼2")
button[2] = Button(window, text="버튼3")
'''

#리스트를 이용한 위젯을 for문으로 코드 간결화
for i in range(0,3):
    button[i]=Button(window, text="버튼"+str(i+1))#버튼을 인덱스 순서대로 생성 
    #button[i].pack() #버튼을 인덱스 순서대로 출력
'''  
for i in range(0,3):
    #button[i]=Button(window, text="버튼"+str(i+1))#버튼을 인덱스 순서대로 생성 
    button[i].pack(side=LEFT) #버튼을 인덱스 순서대로 출력
'''
for btn in button: #for변수 in 리스트
    #위젯의 폭 맞추기 'fill=X'
    #위젯 사이에 여백을 주려면 'padx=픽셀값', 'pady=픽셀값'
    btn.pack(side=TOP, fill=X, padx=10, pady=10, ipadx=20, ipady=20)#버튼을 인덱스 순서대로 출력 fill은 가로폭만 맞출수 있따.
print(button)

window.mainloop()
