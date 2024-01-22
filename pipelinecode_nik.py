from tkinter import *
import re
'''inst= ["mov r1 #1",
       "add r1 r2",
       "mov r1 #9",
       "sub r1 #2",
       "div r3 #0",
       "mov r1 #2",
       "mul r1 r2",
       "mov r1 #2"
       ]
'''
inst=[""]*7

mainw=Tk()
mainw.title("Instruction input")
mainw.configure(bg="yellow")
mainw.geometry("500x300")

mainw.columnconfigure(0,weight=1)
mainw.columnconfigure(1,weight=1)
mainw.columnconfigure(2,weight=1)

Label(mainw,text="Enter the instructions in each text box",bg="yellow").grid(column=1,row=1)
Label(mainw,text="(the format is <operation> <key1> <key2>)",bg="yellow").grid(column=1,row=2)
Label(mainw,text="",bg="yellow").grid(column=0,row=3)


instrlab1=Label(mainw,text="Instruction 1",bg="cyan")
instrlab1.grid(column=0,row=4)
instrimp1=Entry()
instrimp1.grid(column=1,row=4)

instrlab2=Label(mainw,text="Instruction 2",bg="cyan")
instrlab2.grid(column=0,row=5)
instrimp2=Entry()
instrimp2.grid(column=1,row=5)

instrlab3=Label(mainw,text="Instruction 3",bg="cyan")
instrlab3.grid(column=0,row=6)
instrimp3=Entry()
instrimp3.grid(column=1,row=6)

instrlab4=Label(mainw,text="Instruction 4",bg="cyan")
instrlab4.grid(column=0,row=7)
instrimp4=Entry()
instrimp4.grid(column=1,row=7)

instrlab5=Label(mainw,text="Instruction 5",bg="cyan")
instrlab5.grid(column=0,row=8)
instrimp5=Entry()
instrimp5.grid(column=1,row=8)

instrlab6=Label(mainw,text="Instruction 6",bg="cyan")
instrlab6.grid(column=0,row=9)
instrimp6=Entry()
instrimp6.grid(column=1,row=9)

instrlab7=Label(mainw,text="Instruction 7",bg="cyan")
instrlab7.grid(column=0,row=10)
instrimp7=Entry()
instrimp7.grid(column=1,row=10)

def getinp():
    inst[0]=instrimp1.get()
    inst[1]=instrimp2.get()
    inst[2]=instrimp3.get()
    inst[3]=instrimp4.get()
    inst[4]=instrimp5.get()
    inst[5]=instrimp6.get()
    inst[6]=instrimp7.get()
    mainw.destroy()
    return

Label(mainw,text="",bg="yellow").grid(column=0,row=11)


gobutton=Button(mainw,text="GO",command=getinp)
gobutton.grid(column=1,row=12)

mainw.mainloop()


for i in range(7):
    print(inst[i])


#******************************************************************************************************************************

#can take in a maximum of 7 instructions
rows = 17
cols = 20
pipeline_matrix = [["" for _ in range(cols)] for _ in range(rows)]

count=0

#"[    F   ]"
#"[    D   ]"
#"[////////]"
#"[    E   ]"
#""

'''data=inst[0].split()
print(type(int(data[2].split("#")[1])))'''

delay=0
instrprint=0
div0=0
# mov>>>1
# add>>>2
# sub>>>3
r=[0]*5  #stores the register data [r1,r2,r3,r4,r5]

def opercheck(x):
    global oper
    x[0]=x[0].lower()
    if(x[0]=='mov'):oper=1
    elif(x[0]=='add'):oper=2
    elif(x[0] =='sub'):oper=3
    elif(x[0]=='mul'):oper=4
    elif(x[0]=="div"):
        oper=5
        if x[2].split("#")[1]=='0':
            global div0
            div0=1
    return oper

def checker(lis1,lis2):
    if (lis1[1] in lis2) or (lis1[2] in lis2):
        return True
    else:
        return False


def execute(op,data1,data2,i,j):

    try:
        global div0
        if div0==1:
            pipeline_matrix[i][j]="[//ERROR//]"
            print("[//ERROR//]")

            div0=0
        else:
            pipeline_matrix[i][j]="[    E   ]"
            print("[    E   ]")

        print(inst[instrprint],end=" :")

        if op==1:
            if data1=='r1':
                nuw=int(data2.split("#")[1])
            #direct addressing mode
            elif data2.split("#")[0]=="":
                r[1]=int(data2.split("#")[1])
            #register addressing mode
            else:

                print("",end="")
                #r[1]=int(data2.split("#")[1])

        elif op==2:
            if data2.isdigit():
                r[0]+=data2
            elif data1=='r1' and data2=='r2':
                r[0]+=r[1]

        elif op==3:
            print("",end="")

        elif op==4:
            print("",end="")
    except:
        return None

def decode(data,i,j, prevdata=" . . ."):
    global delay
    pinstr=prevdata.split()
    instr=data.split()
    if (checker(instr,pinstr)):
        pipeline_matrix[i][j]="[////////]"
        print("[////////]",end=" ")
        j+=1
        delay=delay+1
        pipeline_matrix[i][j]="[    D   ]"
        print("[    D   ]",end=" ")

    else:
        pipeline_matrix[i][j]="[    D   ]"
        print("[    D   ]",end=" ")
    opern=opercheck(instr)

    global instrprint
    instrprint+=1

    execute(opern,instr[1],instr[2],i,j+1)


flag=0
def fetch(data,n):
    x=0
    y=0
    pipeline_matrix[x][y]=data[0]
    y+=1

    print(data[0],end=" :")

    pipeline_matrix[x][y]="[    F   ]"
    y+=1

    print("[    F   ]",end=" ")

    decode(data[0],x,y)
    print("           ",end="")
    pipeline_matrix[1][0]=""
    for i in range(1,n):
        x+=1
        y=0
        pipeline_matrix[x][y]=data[i]
        y+=1+i+delay
        pipeline_matrix[x][y]="[    F   ]"
        y+=1
        print("[    F   ]",end=" ")
        decode(data[i],x,y,data[i-1])

        print("           "*(i+1+delay),end="")
    print()


counts=0
for i in inst:
    print(i)
    if i!='':
        count+=1
print(count)

fetch(inst,count)
'''
print(pipeline_matrix[0])
print(pipeline_matrix[1])
print(pipeline_matrix[2])
print(pipeline_matrix[3])
print(pipeline_matrix[4])
print(pipeline_matrix[5])
print(pipeline_matrix[6])'''

