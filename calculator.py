from tkinter import *
root=Tk()
root.title('Calculator')
e=Entry(root)
e.grid(row=0,column=0,columnspan=3)
"""
but_1=Button(root,text='1',command=lambda :num('1'))
but_2=Button(root,text='2',command=lambda :num('2'))
but_3=Button(root,text='3',command=lambda :num('3'))
but_4=Button(root,text='4',command=lambda :num('4'))
but_5=Button(root,text='5',command=lambda :num('5'))
but_6=Button(root,text='6',command=lambda :num('6'))
but_7=Button(root,text='7',command=lambda :num('7'))
but_8=Button(root,text='8',command=lambda :num('8'))
but_9=Button(root,text='9',command=lambda :num('9'))
but_0=Button(root,text='0',command=lambda :num('0'))

but_1.grid(row=0,column=0)

"""
def numb(r,c):
   
    num=str(numl[r][c])
    global no
    no=e.get()
    e.delete(0,END)
    no=str(no)+str(num)
    e.insert(0,no)
def plus():
    fir_num=e.get()
    global f_num
    f_num=int(fir_num)   
    e.delete(0,END)

def clear():
    e.delete(0,END)



def ans():
    s_num=e.get()

    s_num=int(s_num)
    s=f_num+s_num
    e.delete(0,END)
    e.insert(0,s)

num=0
but=[[1,2,3],[4,5,6],[7,8,9]]
numl=[[1,2,3],[4,5,6],[7,8,9],[0]]
for i in range(0,3):
    for j in range(0,3):
        num=num+1
        but[i][j]=Button(root,text=num,padx=25,pady=10,command=lambda r=i,c=j: numb(r,c))
        but[i][j].grid(row=i+1,column=j)
but_0= Button(root,text='0',padx=55,pady=10,command=lambda r=3,c=0: numb(r,c))
but_0.grid(row=i+2,column=0,columnspan=2)
enter= Button(root,text='=',padx=25,pady=10,command= ans)
enter.grid(row=i+2,column=2,columnspan=1)
add= Button(root,text='+',padx=15,pady=30,command=plus)
add.grid(row=1,column=3,rowspan=2)
clear= Button(root,text='clear',padx=8,pady=30,command=clear)
clear.grid(row=3,column=3,rowspan=2)




mainloop()