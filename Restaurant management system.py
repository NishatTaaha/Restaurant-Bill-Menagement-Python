from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests

##################### menu functions ############################
def reset():
    textReciept.delete(1.0,END)

    e_roti.set('0')
    e_daal.set('0')
    e_sabji.set('0')
    e_chawal.set('0')
    e_fish.set('0')
    e_kabab.set('0')
    e_mutton.set('0')
    e_chicken.set('0')
    e_paneer.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_shikanji.set('0')
    e_jhaljeera.set('0')
    e_roohafza.set('0')
    e_masalatea.set('0')
    e_badammilk.set('0')
    e_colddrinks.set('0')

    e_oreo.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_apple.set('0')
    e_blackforest.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')

    textroti.config(stat=DISABLED)
    textdaal.config(stat=DISABLED)
    textsabji.config(stat=DISABLED)
    textchawal.config(stat=DISABLED)
    textfish.config(stat=DISABLED)
    textkabab.config(stat=DISABLED)
    textmutton.config(stat=DISABLED)
    textchicken.config(stat=DISABLED)
    textpaneer.config(stat=DISABLED)
    textlassi.config(stat=DISABLED)
    textcoffee.config(stat=DISABLED)
    textfaluda.config(stat=DISABLED)
    textshikanji.config(stat=DISABLED)
    textjhaljeera.config(stat=DISABLED)
    textroohafza.config(stat=DISABLED)
    textmasalatea.config(stat=DISABLED)
    textbadammilk.config(stat=DISABLED)
    textcolddrinks.config(stat=DISABLED)
    textoreo.config(stat=DISABLED)
    textapple.config(stat=DISABLED)
    textkitkat.config(stat=DISABLED)
    textvanilla.config(stat=DISABLED)
    textbanana.config(stat=DISABLED)
    textbrownie.config(stat=DISABLED)
    textpineapple.config(stat=DISABLED)
    textchocolate.config(stat=DISABLED)
    textblackforest.config(stat=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofFoodVar.set('')
    costofDrinkVar.set('')
    costofCakeVar.set('')
    subtotalVar.set('')
    servicetaxVar.set('')
    totalcostVar.set('')

def send():
    if textReciept.get(1.0, END) == '\n':
        messagebox.showerror('Error','No item was selected!!')
    else:
        def send_msg():
            message = textarea.get(1.0, END)
            number = numberField.get()
            auth = 'woVHAjOGldMsPhnT7gS6XRIi4cYr0ym3FZkEWfKv9Qxauq8J2DHDWus7AqZKnkeXlVzQJa3fIRrp925S'
            url = 'https://www.fast2sms.com/dev/bulk'

            params = {
                'authorization': auth,
                'message': message,
                'numbers': number,
                'sender-id': 'FSTSMS',
                'route': 'p',
                'language': 'english'
            }
            response = requests.get(url, params=params)
            dic = response.json()
            result = dic.get('return')
            if result == True:
                messagebox.showinfo('Send Successfully', 'Message sent succesfully')

            else:
                messagebox.showerror('Error', 'Something went wrong')


        root2=Toplevel()

        root2.title('Send Bill')
        root2.config(bg='violet')
        root2.geometry('485x670+50+50')

        logoImage=PhotoImage(file='sender.png')
        label=Label(root2,image=logoImage,bg='violet')
        label.pack(pady=5)

        numberLabel=Label(root2,text='Mobile Number', font=('arial',18,'bold underline'),bg='violet',fg='black')
        numberLabel.pack(pady=5)

        numberField=Entry(root2,font=('arial',22,'bold'),bd=3,width=24)
        numberField.pack(pady=5)

        billLabel=Label(root2,text='Bill Detail', font=('arial',18,'bold underline'),bg='violet',fg='black')
        billLabel.pack(pady=5)

        textarea = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
        textarea.pack(pady=5)
        textarea.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n\n')

        if costofFoodVar.get() != '0 Tk':
            textarea.insert(END, f'Cost of Foods\t\t\t{priceoffood}Tk\n\n')
        if costofDrinkVar.get() != '0 Tk':
            textarea.insert(END, f'Cost of Drinks\t\t\t{priceofdrinks}Tk\n\n')
        if costofCakeVar.get() != '0 Tk':
            textarea.insert(END, f'Cost of Cakes\t\t\t{priceofcakes}Tk\n\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofitems}Tk\n\n')
        textarea.insert(END, f'Service tax\t\t\t{50}Tk\n\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalofitems + 50}Tk\n\n')


        sendButton=Button(root2,text='Send',font=('arial',19,'bold'),bg='black',fg='violet',bd=7,relief=GROOVE,command=send_msg)
        sendButton.pack(pady=5)

        root2.mainloop()


def save():
    if textReciept.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:
            bill_data= textReciept.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Saved successfully!!')


def receipt():
    global billnumber,date

    if costofFoodVar.get()!='' or costofCakeVar.get()!='' or costofDrinkVar.get()!='':

        textReciept.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReciept.insert(END,'Reciept Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReciept.insert(END,'**************************************************\n')
        textReciept.insert(END,'Items:\t\t Cost of Items(Rs)\n')
        textReciept.insert(END,'**************************************************\n')

        if e_roti.get()!='0':
            textReciept.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')
        if e_daal.get()!='0':
            textReciept.insert(END,f'Daal\t\t\t{int(e_daal.get())*60}\n\n')
        if e_sabji.get()!='0':
            textReciept.insert(END,f'Sabji\t\t\t{int(e_sabji.get())*100}\n\n')
        if e_chawal.get()!='0':
            textReciept.insert(END,f'Chawal\t\t\t{int(e_chawal.get())*50}\n\n')
        if e_fish.get()!='0':
            textReciept.insert(END,f'Fish\t\t\t{int(e_fish.get())*40}\n\n')
        if e_kabab.get()!='0':
            textReciept.insert(END,f'Kabab\t\t\t{int(e_kabab.get())*30}\n\n')
        if e_mutton.get()!='0':
            textReciept.insert(END,f'Mutton\t\t\t{int(e_mutton.get())*120}\n\n')
        if e_chicken.get()!='0':
            textReciept.insert(END,f'Chicken\t\t\t{int(e_chicken.get())*100}\n\n')
        if e_paneer.get()!='0':
            textReciept.insert(END,f'Paneer\t\t\t{int(e_paneer.get())*120}\n\n')


        if e_lassi.get()!='0':
            textReciept.insert(END,f'Lassi\t\t\t{int(e_lassi.get())*50}\n\n')
        if e_coffee.get()!='0':
            textReciept.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*40}\n\n')
        if e_faluda.get()!='0':
            textReciept.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*80}\n\n')
        if e_shikanji.get()!='0':
            textReciept.insert(END,f'Shikanji\t\t\t{int(e_shikanji.get())*30}\n\n')
        if e_jhaljeera.get()!='0':
            textReciept.insert(END,f'jhaljeera\t\t\t{int(e_jhaljeera.get())*40}\n\n')
        if e_roohafza.get()!='0':
            textReciept.insert(END,f'Roohafza\t\t\t{int(e_roohafza.get())*60}\n\n')
        if e_masalatea.get()!='0':
            textReciept.insert(END,f'Masala Tea\t\t\t{int(e_masalatea.get())*20}\n\n')
        if e_badammilk.get()!='0':
            textReciept.insert(END,f'Badam Milk\t\t\t{int(e_badammilk.get())*50}\n\n')
        if e_colddrinks.get()!='0':
            textReciept.insert(END,f'Cold Drinks\t\t\t{int(e_colddrinks.get())*80}\n\n')


        if e_oreo.get()!='0':
            textReciept.insert(END,f'Oreo Cake\t\t\t{int(e_oreo.get())*400}\n\n')
        if e_apple.get()!='0':
            textReciept.insert(END,f'Apple Cake\t\t\t{int(e_apple.get())*300}\n\n')
        if e_kitkat.get()!='0':
            textReciept.insert(END,f'Kitkat Cake\t\t\t{int(e_kitkat.get())*500}\n\n')
        if e_vanilla.get()!='0':
            textReciept.insert(END,f'Vanilla Cake\t\t\t{int(e_vanilla.get())*550}\n\n')
        if e_banana.get()!='0':
            textReciept.insert(END,f'Banana Cake\t\t\t{int(e_banana.get())*450}\n\n')
        if e_brownie.get()!='0':
            textReciept.insert(END,f'Brownie\t\t\t{int(e_brownie.get())*800}\n\n')
        if e_pineapple.get()!='0':
            textReciept.insert(END,f'Pineapple Cake\t\t\t{int(e_pineapple.get())*600}\n\n')
        if e_chocolate.get()!='0':
            textReciept.insert(END,f'Chocolate\t\t\t{int(e_chocolate.get())*200}\n\n')
        if e_blackforest.get()!='0':
            textReciept.insert(END,f'Black Forest\t\t\t{int(e_blackforest.get())*850}\n\n')

        textReciept.insert(END,'**************************************************\n')

        if costofFoodVar.get()!='0 Tk':
            textReciept.insert(END,f'Cost of Foods\t\t\t{priceoffood}Tk\n\n')
        if costofDrinkVar.get()!='0 Tk':
            textReciept.insert(END, f'Cost of Drinks\t\t\t{priceofdrinks}Tk\n\n')
        if costofCakeVar.get()!='0 Tk':
            textReciept.insert(END, f'Cost of Cakes\t\t\t{priceofcakes}Tk\n\n')


        textReciept.insert(END,f'Sub Total\t\t\t{subtotalofitems}Tk\n\n')
        textReciept.insert(END,f'Service tax\t\t\t{50}Tk\n\n')
        textReciept.insert(END,f'Total Cost\t\t\t{subtotalofitems+50}Tk\n\n')

    else:
        messagebox.showerror('Error','No item is selected')

# total
def totalcost():
    global priceoffood, priceofdrinks, priceofcakes,subtotalofitems

    if(var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0
        or var5.get()!=0 or var6.get()!=0 or var7.get()!=0 or var8.get()!=0
        or var9.get()!=0 or var10.get()!=0 or var11.get()!=0 or var12.get()!=0
        or var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or var16.get()!=0
        or var17.get()!=0 or var18.get()!=0 or var19.get()!=0 or var20.get()!=0
        or var21.get()!=0 or var22.get()!=0 or var23.get()!=0 or var24.get()!=0
        or var25.get()!=0 or var26.get()!=0 or var27.get()!=0):
            item1=int(e_roti.get())
            item2 = int(e_daal.get())
            item3 = int(e_sabji.get())
            item4 = int(e_chawal.get())
            item5 = int(e_fish.get())
            item6 = int(e_kabab.get())
            item7 = int(e_mutton.get())
            item8 = int(e_chicken.get())
            item9 = int(e_paneer.get())

            item10 = int(e_lassi.get())
            item11 = int(e_coffee.get())
            item12 = int(e_faluda.get())
            item13 = int(e_shikanji.get())
            item14 = int(e_jhaljeera.get())
            item15 = int(e_roohafza.get())
            item16 = int(e_masalatea.get())
            item17 = int(e_badammilk.get())
            item18 = int(e_colddrinks.get())

            item19 = int(e_oreo.get())
            item20 = int(e_apple.get())
            item21 = int(e_kitkat.get())
            item22 = int(e_vanilla.get())
            item23 = int(e_banana.get())
            item24 = int(e_brownie.get())
            item25 = int(e_pineapple.get())
            item26= int(e_chocolate.get())
            item27= int(e_blackforest.get())

            priceoffood= (item1*10)+(item2*60)+(item3*100)+(item4*50)+(item5*40)+(item6*30)+(item7*120)+(item8*100)+(item9*120)
            priceofdrinks= (item10*50)+(item11*40)+(item12*80)+(item13*30)+(item14*40)+(item15*60)+(item16*20)+(item17*50)+(item18*80)
            priceofcakes= (item19*400)+(item20*300)+(item21*500)+(item22*550)+(item23*450)+(item24*800)+(item25*600)+(item26*200)+(item27*550)

            costofFoodVar.set(str(priceoffood)+' Tk')
            costofDrinkVar.set(str(priceofdrinks)+' Tk')
            costofCakeVar.set(str(priceofcakes)+' Tk')

            subtotalofitems=priceoffood+priceofdrinks+priceofcakes
            subtotalVar.set(str(subtotalofitems)+' Tk')

            servicetaxVar.set('50 Tk')

            totalcost= subtotalofitems+50
            totalcostVar.set(str(totalcost)+' Tk')

    else:
        messagebox.showerror('Error','No Item is selected!!')

# foods
def roti():
    if var1.get()==1:
        textroti.config(stat=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(stat=DISABLED)
        e_roti.set('0')
def daal():
    if var2.get()==1:
        textdaal.config(stat=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()
    else:
        textdaal.config(stat=DISABLED)
        e_daal.set('0')
def sabji():
    if var3.get()==1:
        textsabji.config(stat=NORMAL)
        textsabji.delete(0,END)
        textsabji.focus()
    else:
        textsabji.config(stat=DISABLED)
        e_sabji.set('0')
def chawal():
    if var4.get()==1:
        textchawal.config(stat=NORMAL)
        textchawal.delete(0,END)
        textchawal.focus()
    else:
        textchawal.config(stat=DISABLED)
        e_chawal.set('0')
def fish():
    if var5.get()==1:
        textfish.config(stat=NORMAL)
        textfish.delete(0,END)
        textfish.focus()
    else:
        textfish.config(stat=DISABLED)
        e_fish.set('0')
def kabab():
    if var6.get()==1:
        textkabab.config(stat=NORMAL)
        textkabab.delete(0,END)
        textkabab.focus()
    else:
        textkabab.config(stat=DISABLED)
        e_kabab.set('0')
def muttoon():
    if var7.get()==1:
        textmutton.config(stat=NORMAL)
        textmutton.delete(0,END)
        textmutton.focus()
    else:
        textmutton.config(stat=DISABLED)
        e_mutton.set('0')
def chicken():
    if var8.get()==1:
        textchicken.config(stat=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(stat=DISABLED)
        e_chicken.set('0')
def paneer():
    if var9.get()==1:
        textpaneer.config(stat=NORMAL)
        textpaneer.delete(0,END)
        textpaneer.focus()
    else:
        textpaneer.config(stat=DISABLED)
        e_paneer.set('0')


# drinks
def lassi():
    if var10.get()==1:
        textlassi.config(stat=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    else:
        textlassi.config(stat=DISABLED)
        e_lassi.set('0')
def coffee():
    if var11.get()==1:
        textcoffee.config(stat=NORMAL)
        textcoffee.delete(0,END)
        textcoffee.focus()
    else:
        textcoffee.config(stat=DISABLED)
        e_coffee.set('0')
def faluda():
    if var12.get()==1:
        textfaluda.config(stat=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    else:
        textfaluda.config(stat=DISABLED)
        e_faluda.set('0')
def shikanji():
    if var13.get()==1:
        textshikanji.config(stat=NORMAL)
        textshikanji.delete(0,END)
        textshikanji.focus()
    else:
        textshikanji.config(stat=DISABLED)
        e_shikanji.set('0')
def jhaljeera():
    if var14.get()==1:
        textjhaljeera.config(stat=NORMAL)
        textjhaljeera.delete(0,END)
        textjhaljeera.focus()
    else:
        textjhaljeera.config(stat=DISABLED)
        e_jhaljeera.set('0')
def roohafza():
    if var15.get()==1:
        textroohafza.config(stat=NORMAL)
        textroohafza.delete(0,END)
        textroohafza.focus()
    else:
        textroohafza.config(stat=DISABLED)
        e_roohafza.set('0')
def masalatea():
    if var16.get()==1:
        textmasalatea.config(stat=NORMAL)
        textmasalatea.delete(0,END)
        textmasalatea.focus()
    else:
        textmasalatea.config(stat=DISABLED)
        e_masalatea.set('0')
def badammilk():
    if var17.get()==1:
        textbadammilk.config(stat=NORMAL)
        textbadammilk.delete(0,END)
        textbadammilk.focus()
    else:
        textbadammilk.config(stat=DISABLED)
        e_badammilk.set('0')
def colddrinks():
    if var18.get()==1:
        textcolddrinks.config(stat=NORMAL)
        textcolddrinks.delete(0,END)
        textcolddrinks.focus()
    else:
        textcolddrinks.config(stat=DISABLED)
        e_colddrinks.set('0')


# cakes
def oreo():
    if var19.get()==1:
        textoreo.config(stat=NORMAL)
        textoreo.delete(0,END)
        textoreo.focus()
    else:
        textoreo.config(stat=DISABLED)
        e_oreo.set('0')
def apple():
    if var20.get()==1:
        textapple.config(stat=NORMAL)
        textapple.delete(0,END)
        textapple.focus()
    else:
        textapple.config(stat=DISABLED)
        e_apple.set('0')
def kitkat():
    if var21.get()==1:
        textkitkat.config(stat=NORMAL)
        textkitkat.delete(0,END)
        textkitkat.focus()
    else:
        textkitkat.config(stat=DISABLED)
        e_kitkat.set('0')
def vanilla():
    if var22.get()==1:
        textvanilla.config(stat=NORMAL)
        textvanilla.delete(0,END)
        textvanilla.focus()
    else:
        textvanilla.config(stat=DISABLED)
        e_vanilla.set('0')
def banana():
    if var23.get()==1:
        textbanana.config(stat=NORMAL)
        textbanana.delete(0,END)
        textbanana.focus()
    else:
        textbanana.config(stat=DISABLED)
        e_banana.set('0')
def brownie():
    if var24.get()==1:
        textbrownie.config(stat=NORMAL)
        textbrownie.delete(0,END)
        textbrownie.focus()
    else:
        textbrownie.config(stat=DISABLED)
        e_brownie.set('0')
def pineapple():
    if var25.get()==1:
        textpineapple.config(stat=NORMAL)
        textpineapple.delete(0,END)
        textpineapple.focus()
    else:
        textpineapple.config(stat=DISABLED)
        e_pineapple.set('0')
def chocolate():
    if var26.get()==1:
        textchocolate.config(stat=NORMAL)
        textchocolate.delete(0,END)
        textchocolate.focus()
    else:
        textchocolate.config(stat=DISABLED)
        e_chocolate.set('0')
def blackforest():
    if var27.get()==1:
        textblackforest.config(stat=NORMAL)
        textblackforest.delete(0,END)
        textblackforest.focus()
    else:
        textblackforest.config(stat=DISABLED)
        e_blackforest.set('0')


################## set window ####################
root=Tk()
root.geometry('1330x690+0+0')
root.resizable(0,0)
root.title('Restaurant Management System')
root.config(bg='violet')

################# top frame #####################
topframe= Frame(root, bd=10, relief=RIDGE, bg='darkgray')
topframe.pack(side=TOP)
labelTitle=Label(topframe, text='Restaurant Management system', font=('arial',30,'bold'),
                 bd=9,fg='white', bg='black', width=51)
labelTitle.grid(row=0, column=0)

##################frames####################

# left freame
menuFrame = Frame(root, bd=10, relief=RIDGE, bg='black')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg='black', pady=10)
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame, text='Food', font=('arial', 19, 'bold'),
                       bd=10, relief=RIDGE, fg='black')
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame, text='Drinks', font=('arial', 19, 'bold'),
                         bd=10, relief=RIDGE, fg='black')
drinksFrame.pack(side=LEFT)

cakesFrame = LabelFrame(menuFrame, text='Cakes', font=('arial', 19, 'bold'),
                        bd=10, relief=RIDGE, fg='black')
cakesFrame.pack(side=LEFT)


# right frame
rightFrame= Frame(root,bd=15,bg='darkgray', relief=RIDGE)
rightFrame.pack(side=RIGHT)
calculatorFrame=Frame(rightFrame, bd=1, relief=RIDGE)
calculatorFrame.pack()
recieptFrame=Frame(rightFrame, bd=4, relief=RIDGE)
recieptFrame.pack()
buttonFrame=Frame(rightFrame, bd=3, relief=RIDGE)
buttonFrame.pack()

################variables#####################
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()



################# empty field variable ###################
e_roti=StringVar()
e_daal=StringVar()
e_sabji=StringVar()
e_chawal=StringVar()
e_fish=StringVar()
e_kabab=StringVar()
e_mutton=StringVar()
e_chicken=StringVar()
e_paneer=StringVar()

e_lassi=StringVar()
e_coffee=StringVar()
e_faluda=StringVar()
e_shikanji=StringVar()
e_jhaljeera=StringVar()
e_roohafza=StringVar()
e_masalatea=StringVar()
e_badammilk=StringVar()
e_colddrinks=StringVar()

e_oreo = StringVar()
e_kitkat = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()

costofFoodVar= StringVar()
costofDrinkVar= StringVar()
costofCakeVar= StringVar()
subtotalVar= StringVar()
servicetaxVar= StringVar()
totalcostVar= StringVar()


################# initially set 0 in empty field ################
e_roti.set('0')
e_daal.set('0')
e_sabji.set('0')
e_chawal.set('0')
e_fish.set('0')
e_kabab.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_paneer.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_shikanji.set('0')
e_jhaljeera.set('0')
e_roohafza.set('0')
e_masalatea.set('0')
e_badammilk.set('0')
e_colddrinks.set('0')

e_oreo.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_apple.set('0')
e_blackforest.set('0')
e_banana.set('0')
e_brownie.set('0')
e_pineapple.set('0')
e_chocolate.set('0')

################## food ######################
roti=Checkbutton(foodFrame,text='Roti',font=('arial',18,'bold'),
                 onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)
daal=Checkbutton(foodFrame,text='Daal',font=('arial',18,'bold'),
                 onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)
sabji=Checkbutton(foodFrame,text='Sabji',font=('arial',18,'bold'),
                  onvalue=1,offvalue=0,variable=var3,command=sabji)
sabji.grid(row=2,column=0,sticky=W)
chawal=Checkbutton(foodFrame,text='Chawal',font=('arial',18,'bold'),
                   onvalue=1,offvalue=0,variable=var4,command=chawal)
chawal.grid(row=3,column=0,sticky=W)
fish=Checkbutton(foodFrame,text='Fish',font=('arial',18,'bold'),
                 onvalue=1,offvalue=0,variable=var5,command=fish)
fish.grid(row=4,column=0,sticky=W)
kabab=Checkbutton(foodFrame,text='Kabab',font=('arial',18,'bold'),
                  onvalue=1,offvalue=0,variable=var6,command=kabab)
kabab.grid(row=5,column=0,sticky=W)
mutton=Checkbutton(foodFrame,text='Mutton',font=('arial',18,'bold'),
                   onvalue=1,offvalue=0,variable=var7,command=muttoon)
mutton.grid(row=6,column=0,sticky=W)
chicken=Checkbutton(foodFrame,text='Chicken',font=('arial',18,'bold'),
                    onvalue=1,offvalue=0,variable=var8,command=chicken)
chicken.grid(row=7,column=0,sticky=W)
paneer=Checkbutton(foodFrame,text='Paneer',font=('arial',18,'bold'),
                   onvalue=1,offvalue=0,variable=var9,command=paneer)
paneer.grid(row=8,column=0,sticky=W)

# entry fields
textroti= Entry(foodFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_roti)
textroti.grid(row=0,column=1)
textdaal= Entry(foodFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_daal)
textdaal.grid(row=1,column=1)
textsabji= Entry(foodFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_sabji)
textsabji.grid(row=2,column=1)
textchawal= Entry(foodFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_chawal)
textchawal.grid(row=3,column=1)
textfish= Entry(foodFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_fish)
textfish.grid(row=4,column=1)
textkabab= Entry(foodFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_kabab)
textkabab.grid(row=5,column=1)
textmutton= Entry(foodFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_mutton)
textmutton.grid(row=6,column=1)
textchicken= Entry(foodFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=7,column=1)
textpaneer= Entry(foodFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_paneer)
textpaneer.grid(row=8,column=1)


######################### drinks ###########################

lassi= Checkbutton(drinksFrame, text='Lassi',font=('arial',18,'bold'),
                   onvalue=1, offvalue=0,variable= var10,command=lassi)
lassi.grid(row=0, column=0, sticky=W)
coffee= Checkbutton(drinksFrame, text='Coffee',font=('arial',18,'bold'),
                   onvalue=1, offvalue=0,variable= var11,command=coffee)
coffee.grid(row=1, column=0, sticky=W)
faluda= Checkbutton(drinksFrame, text='Faluda',font=('arial',18,'bold'),
                   onvalue=1, offvalue=0,variable= var12,command=faluda)
faluda.grid(row=2, column=0, sticky=W)
shikanji= Checkbutton(drinksFrame, text='Shikanji',font=('arial',18,'bold'),
                   onvalue=1, offvalue=0,variable= var13,command=shikanji)
shikanji.grid(row=3, column=0, sticky=W)
jaljeera= Checkbutton(drinksFrame, text='Jaljeera' ,font=('arial',18,'bold'),
                   onvalue=1, offvalue=0,variable= var14,command=jhaljeera)
jaljeera.grid(row=4, column=0, sticky=W)
roohafza= Checkbutton(drinksFrame, text='Roohafza',font=('arial',18,'bold'),
                   onvalue=1, offvalue=0,variable= var15,command=roohafza)
roohafza.grid(row=5, column=0, sticky=W)
masala_tea= Checkbutton(drinksFrame, text='Masala-tea',font=('arial',18,'bold'),
                   onvalue=1, offvalue=0,variable= var16,command=masalatea)
masala_tea.grid(row=6, column=0, sticky=W)
badam_milk= Checkbutton(drinksFrame, text='Badam-milk',font=('arial',18,'bold'),
                   onvalue=1, offvalue=0,variable= var17,command=badammilk)
badam_milk.grid(row=7, column=0, sticky=W)
cold_drinks= Checkbutton(drinksFrame, text='Cold-drinks',font=('arial',18,'bold'),
                   onvalue=1, offvalue=0,variable= var18,command=colddrinks)
cold_drinks.grid(row=8, column=0, sticky=W)


# entry fields
textlassi= Entry(drinksFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_lassi)
textlassi.grid(row=0,column=1)
textcoffee= Entry(drinksFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1,column=1)
textfaluda= Entry(drinksFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_faluda)
textfaluda.grid(row=2,column=1)
textshikanji= Entry(drinksFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_shikanji)
textshikanji.grid(row=3,column=1)
textjhaljeera= Entry(drinksFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_jhaljeera)
textjhaljeera.grid(row=4,column=1)
textroohafza= Entry(drinksFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_roohafza)
textroohafza.grid(row=5,column=1)
textmasalatea= Entry(drinksFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_masalatea)
textmasalatea.grid(row=6,column=1)
textbadammilk= Entry(drinksFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_badammilk)
textbadammilk.grid(row=7,column=1)
textcolddrinks= Entry(drinksFrame, font=('arial',18,'bold'),bd=7,
                width=6, state=DISABLED, textvariable=e_colddrinks)
textcolddrinks.grid(row=8,column=1)




####################### cakes ##############################

oreocake =Checkbutton(cakesFrame,text='Oreo',font=('arial', 18, 'bold'),
                      onvalue=1, offvalue=0,variable=var19,command=oreo)
oreocake.grid(row=0,column=0,sticky=W)
applecake =Checkbutton(cakesFrame,text='Apple',font=('arial', 18, 'bold'),
                       onvalue=1,offvalue=0,variable=var20,command=apple)
applecake.grid(row=1,column=0,sticky=W)
kitkatcake =Checkbutton(cakesFrame,text='Kitkat',font=('arial',18,'bold'),
                        onvalue=1,offvalue=0,variable=var21,command=kitkat)
kitkatcake.grid(row=2, column=0, sticky=W)
vanillacake =Checkbutton(cakesFrame,text='Vanilla',font=('arial',18,'bold'),
                         onvalue=1,offvalue=0,variable=var22,command=vanilla)
vanillacake.grid(row=3,column=0,sticky=W)
bananacake=Checkbutton(cakesFrame,text='Banana',font=('arial',18,'bold'),
                       onvalue=1,offvalue=0,variable=var23,command=banana)
bananacake.grid(row=4, column=0, sticky=W)
browniecake =Checkbutton(cakesFrame, text='Brownie', font=('arial', 18, 'bold'),
                         onvalue=1, offvalue=0,variable=var24,command=brownie)
browniecake.grid(row=5,column=0,sticky=W)
pineapplecake=Checkbutton(cakesFrame,text='Pineapple',font=('arial',18,'bold'),
                          onvalue=1,offvalue=0,variable=var25,command=pineapple)
pineapplecake.grid(row=6,column=0,sticky=W)
chocolatecake=Checkbutton(cakesFrame,text='Chocolate',font=('arial',18,'bold'),
                          onvalue=1,offvalue=0,variable=var26,command=chocolate)
chocolatecake.grid(row=7,column=0,sticky=W)
blackforestcake=Checkbutton(cakesFrame,text='Black Forest',font=('arial',18,'bold'),
                            onvalue=1,offvalue=0,variable=var27,command=blackforest)
blackforestcake.grid(row=8,column=0,sticky=W)


# entry fields for cakes

textoreo = Entry(cakesFrame,font=('arial',18,'bold'),bd=7,
                 width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)
textapple=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,
                width=6,state=DISABLED,textvariable=e_apple)
textapple.grid(row=1,column=1)
textkitkat=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,
                 width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=2,column=1)
textvanilla=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,
                  width=6,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=3,column=1)
textbanana=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,
                 width=6,state=DISABLED,textvariable=e_banana)
textbanana.grid(row=4,column=1)
textbrownie=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,
                  width=6,state=DISABLED,textvariable=e_brownie)
textbrownie.grid(row=5,column=1)
textpineapple=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,
                    width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=6,column=1)
textchocolate=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,
                    width=6,state=DISABLED,textvariable=e_chocolate)
textchocolate.grid(row=7,column=1)
textblackforest=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,
                      width=6,state=DISABLED,
                        textvariable=e_blackforest)
textblackforest.grid(row=8,column=1)



###################### costlabel food ##########################
# costs

labelCostofFood=Label(costFrame,text='Cost of Foods',
                      font=('arial',16,'bold'),bg='black',fg='white')
labelCostofFood.grid(row=0,column=0)
textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,
                     width=14,state='readonly',textvariable=costofFoodVar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofDrink=Label(costFrame,text='Cost of Drinks',
                       font=('arial',16,'bold'),bg='black',fg='white')
labelCostofDrink.grid(row=1,column=0)
textCostofDrink=Entry(costFrame,font=('arial',16,'bold'),bd=6,
                      width=14,state='readonly',textvariable=costofDrinkVar)
textCostofDrink.grid(row=1,column=1,padx=41)

labelCostofCake=Label(costFrame,text='Cost of Cakes',
                      font=('arial',16,'bold'),bg='black',fg='white')
labelCostofCake.grid(row=2,column=0)
textCostofCake=Entry(costFrame,font=('arial',16,'bold'),bd=6,
                     width=14,state='readonly',textvariable=costofCakeVar)
textCostofCake.grid(row=2,column=1,padx=41)

# subtotal/tax/total cost

labelSubtotal=Label(costFrame,text='Subtotal',
                    font=('arial',16,'bold'),bg='black',fg='white')
labelSubtotal.grid(row=0,column=2)
textSubtotal=Entry(costFrame,font=('arial',16,'bold'),
                   bd=6,width=14,state='readonly',textvariable=subtotalVar)
textSubtotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',
                      font=('arial',16,'bold'),bg='black',fg='white')
labelServiceTax.grid(row=1,column=2)
textServiceTax=Entry(costFrame,font=('arial',16,'bold'),
                     bd=6,width=14,state='readonly',textvariable=servicetaxVar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',
                     font=('arial',16,'bold'),bg='black',fg='white')
labelTotalCost.grid(row=2,column=2)
textTotalCost=Entry(costFrame,font=('arial',16,'bold'),
                    bd=6,width=14,state='readonly',textvariable=totalcostVar)
textTotalCost.grid(row=2,column=3,padx=41)


###################### right bottom buttons############################

buttonTotal= Button(buttonFrame,text='Total',font=('arial',16,'bold'),
                    fg='white',bg='black',bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReciept= Button(buttonFrame,text='Reciept',font=('arial',16,'bold'),
                    fg='white',bg='black',bd=3,padx=5,command=receipt)
buttonReciept.grid(row=0,column=1)

buttonSave= Button(buttonFrame,text='Save',font=('arial',16,'bold'),
                    fg='white',bg='black',bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=2)

buttonSend= Button(buttonFrame,text='Send',font=('arial',16,'bold'),
                    fg='white',bg='black',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',16,'bold'),
                    fg='white',bg='black',bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=4)


########################### rightside textarea ######################

textReciept=Text(recieptFrame,font=('arial',16,'bold'),bd=3,width=42,height=11)
textReciept.grid(row=0,column=0)

############################## calculator ################################

# functions
operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

# entry lebal
calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=33,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

# buttons
button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),
               fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('7'))
button7.grid(row=1,column=0)
button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),
               fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('8'))
button8.grid(row=1,column=1)
button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),
               fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('9'))
button9.grid(row=1,column=2)
buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),
                  fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)
button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),
               fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('4'))
button4.grid(row=2,column=0)
button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),
               fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('5'))
button5.grid(row=2,column=1)
button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),
               fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('6'))
button6.grid(row=2,column=2)
buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),
                   fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)
button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),
               fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('1'))
button1.grid(row=3,column=0)
button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),
               fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('2'))
button2.grid(row=3,column=1)
button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),
               fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('3'))
button3.grid(row=3,column=2)
buttonMultiply=Button(calculatorFrame,text='*',font=('arial',16,'bold'),
                      fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('*'))
buttonMultiply.grid(row=3,column=3)
buttonAns=Button(calculatorFrame,text='=',font=('arial',16,'bold'),
                 fg='white',bg='black',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)
buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),
                   fg='white',bg='black',bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)
buttonZero=Button(calculatorFrame,text='0',font=('arial',16,'bold'),
                  fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('0'))
buttonZero.grid(row=4,column=2)
buttonDivide=Button(calculatorFrame,text='/',font=('arial',16,'bold'),
                    fg='white',bg='black',bd=6,width=6,command= lambda:buttonClick('/'))
buttonDivide.grid(row=4,column=3)


root.mainloop()
