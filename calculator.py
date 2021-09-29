from tkinter import *
from tkinter import font 

window = Tk()
window.title('Calculator')
window.geometry('350x500')
window.resizable(False,False)

algerian_font11 = font.Font(family='Algerian', size=11, weight=font.BOLD)
num_input = ''

def render(number):
    global num_input
    num_input = num_input + str(number)
    label['text'] = num_input

def clear():
    global num_input
    num_input = ''
    label['text'] = num_input

def equal_clicked():
    global num_input
    add=str(eval(num_input))
    label['text'] = add
    num_input=''



# Organise the UI elements in frames 
frame_1 = Frame(window)
frame_1.pack(expand=True,fill=BOTH)

frame_2 = Frame(window)
frame_2.pack(expand=True,fill=BOTH)

frame_3 = Frame(window)
frame_3.pack(expand=True,fill=BOTH)

frame_4 = Frame(window)
frame_4.pack(expand=True,fill=BOTH)


# The label/screen of the calculator
label = Label(
    frame_1,
    textvariable='',
    font=('Arial', 30),
    anchor = SE,
    bg = '#ffffff',
    fg = 'black',
    #width=23
    )
label.pack(expand=True, fill=BOTH, side=TOP)
# Buttons

#Second frame
button_1 = Button(
    frame_1,
    text='1',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    #bg='#ffffff',
    command= lambda: render('1'),
    height=5,
    width=1
    )
button_1.pack(expand=True,fill=BOTH,side=LEFT)

button_2 = Button(
    frame_1,
    text='2',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('2'),
    #bg='#141414'
    )
button_2.pack(expand=True,fill=BOTH,side=LEFT)

button_3 = Button(
    frame_1,
    text='3',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('3')
    )
button_3.pack(expand=True,fill=BOTH,side=LEFT)

button_add = Button(
    frame_1,
    text='+',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('+')
    )
button_add.pack(expand=True,fill=BOTH,side=LEFT)

#Third frame
button_4 = Button(
    frame_2,
    text='4',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('4')
    )
button_4.pack(expand=True,fill=BOTH,side=LEFT)

button_5 = Button(
    frame_2,
    text='5',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('5')
    )
button_5.pack(expand=True,fill=BOTH,side=LEFT)

button_6 = Button(
    frame_2,
    text='6',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('6')
    )
button_6.pack(expand=True,fill=BOTH,side=LEFT)


button_subtract = Button(
    frame_2,
    text='-',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('-')
    )
button_subtract.pack(expand=True,fill=BOTH,side=LEFT)

#Fourth frame
button_7 = Button(
    frame_3,
    text='7',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('7')
    )
button_7.pack(expand=True,fill=BOTH,side=LEFT)

button_8 = Button(
    frame_3,
    text='8',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('8')
    )
button_8.pack(expand=True,fill=BOTH,side=LEFT)

button_9 = Button(
    frame_3,
    text='9',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('9')
    )
button_9.pack(expand=True,fill=BOTH,side=LEFT)

button_divide = Button(
    frame_3,
    text='/',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('/'))
button_divide.pack(expand=True,fill=BOTH,side=LEFT)

button_clear = Button(
    frame_4,
    text='C',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= clear)
button_clear.pack(expand=True, fill=BOTH, side=LEFT)

button_0= Button(
    frame_4,
    text='0',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command= lambda: render('0'))
button_0.pack(expand=True, fill=BOTH, side=LEFT)

button_equal= Button(
    frame_4,
    text='=',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command=equal_clicked
    )
button_equal.pack(expand=True, fill=BOTH, side=LEFT)

button_equal= Button(
    frame_4,
    text='*',
    border=1,
    relief=FLAT,
    font= algerian_font11,
    command=lambda: render("*")
    )
button_equal.pack(expand=True, fill=BOTH, side=LEFT)


window.mainloop()