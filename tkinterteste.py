from tkinter import *

janela = Tk()

janela.title('Teste')

janela.geometry('500x500')

changeColor = fg = 'blue'
option1 = Button(text='clique', command = changeColor)
option1.pack()
janela.mainloop()


