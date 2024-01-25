from guizero import *

def update_text():
    global i
    text.value = 'ei' + str(i) + ' rockar'

def increment_year():
    global i
    i += int(increment.value)


i = 22

#skapar ett huvud-fönster (som är osynligt till att börja med)
app = App()

#arrangera och förse vårt fönster med "liv"
text = Text(app, text='ei22 rockar')
text.repeat(1000, update_text)
increment = TextBox(app)
my_button = PushButton(app, command=increment_year, text='inc')

app.display() #kommer ej returnera förrän fönstret stängts
print('will never print!')
