from tkinter import *
import time 
color1 = '#4D908E'
color2 = '#577590'
color3 = '#43AA8B'
color4 = '#F9844A'
color5 = '#F94144'
global arr           #main_array = arr
global arrrep        #array_replica = arrrep
global arrcomp       #array_compare = arrcomp
arr = []
arrrep = []
arrcomp = []
global n 
global lastmidx
global lastendy
global circle_list 
global text_list
global line_list
global sortedarray
global sortedcircle_list 
sortedcircle_list = []
sortedarray = []
circle_list = []
text_list = []
line_list = []
lastmidx = []
lastendy = []

class Drawing(Tk):
    def __init__(self):
        self.main = Tk()
        self.main.title("HeapSort")
        self.main.geometry('1080x680')
        self.main.configure(bg=color1)
        self.canvas1 = Canvas(width=1000, height=500, bg=color3)
        self.canvas1.pack(padx=40, pady=40)
        self.labelm1 = Label(self.main, text=f"Array: {arr}",font=('calibre',25,'bold'),bg=color1)
        self.labelm1.place(x=40,y=560)
        self.name = "SORT.png"
        self.image_name = PhotoImage(file=self.name)
        self.button1 = Button(self.main, image=self.image_name,borderwidth=0,command = self.next)
        self.button1.place(x=500,y=620,height=40,width=80)
        self.xd = 0
        self.yd = 0
    def next(self):
        self.labelm1.destroy()
        self.canvas1.destroy()
        self.button1.destroy()
        self.canvas1 = Canvas(width=1080, height=680, bg=color3)
        self.canvas1.pack()
        self.labelf = Label(self.main, text='Sorted Array:',font=('calibre',15,'bold'),bg=color3)
        self.labelf.place(x=5,y=560)
        lastmidx.clear()
        lastendy.clear()
        circle_list.clear()
        text_list.clear()
        self.bt()
        while len(circle_list)>1:
            self.build_heap()
            self.sprun()
            self.canvas1.delete(line_list[-1])
            line_list.pop(-1)
            self.canvas1.update()
        sortedarray.append(0)
        sortedarray[-1] = arr[-1]
        arr.pop(-1)
        time.sleep(0.2)
        self.labelm1.destroy()
        self.labelm1 = Label(self.main, text='Moving Last Node to Sorted Array :)',font=('calibre',15,'bold'),bg=color3)
        self.labelm1.place(x=40,y=5)
        self.roottosa()
    def roottosa(self):
        if len(sortedarray)>1 and len(sortedarray)<=15:
            if len(sortedarray)>len(sortedcircle_list):
                sortedcircle_list.append(sortedcircle_list[-1]+61)
                self.xd = sortedcircle_list[-1] - lastmidx[-1]
                self.yd = 560 - lastendy[-1]
                self.xd/=20
                self.yd/=20
            self.canvas1.move(circle_list[-1],self.xd,self.yd)
            self.canvas1.move(text_list[-1],self.xd,self.yd)
            cl = self.canvas1.bbox(circle_list[-1])
            cl_x1,cl_y1,cl_x2,cl_y2=cl
            self.canvas1.update()
            time.sleep(0.02)
            if cl_y2 <560:
                self.roottosa()
        elif len(sortedarray)==16:
            if len(sortedarray)>len(sortedcircle_list):
                sortedcircle_list.append(105)
                self.xd = 105 - lastmidx[-1]
                self.yd = 650 - lastendy[-1]
                self.xd/=20
                self.yd/=20
            self.canvas1.move(circle_list[-1],self.xd,self.yd)
            self.canvas1.move(text_list[-1],self.xd,self.yd)
            cl = self.canvas1.bbox(circle_list[-1])
            cl_x1,cl_y1,cl_x2,cl_y2=cl
            self.canvas1.update()
            time.sleep(0.02)
            if cl_y2 <650:
                self.roottosa()
        elif len(sortedarray)>16:
            if len(sortedarray)>len(sortedcircle_list):
                sortedcircle_list.append(sortedcircle_list[-1]+61)
                self.xd = sortedcircle_list[-1] - lastmidx[-1]
                self.yd = 650 - lastendy[-1]
                self.xd/=20
                self.yd/=20
            self.canvas1.move(circle_list[-1],self.xd,self.yd)
            self.canvas1.move(text_list[-1],self.xd,self.yd)
            cl = self.canvas1.bbox(circle_list[-1])
            cl_x1,cl_y1,cl_x2,cl_y2=cl
            self.canvas1.update()
            time.sleep(0.02)
            if cl_y2 <650:
                self.roottosa()
    def highlight(self,l,r):
        self.canvas1.itemconfig(circle_list[l], fill=color5)
        self.canvas1.itemconfig(circle_list[r], fill=color5)
        self.canvas1.update()
        time.sleep(0.1)
    def restore(self,l,r):
        self.canvas1.itemconfig(circle_list[l], fill=color4)
        self.canvas1.itemconfig(circle_list[r], fill=color4)
        self.canvas1.update()
        time.sleep(0.1)
    def build_heap(self):
        n = int((len(arr)//2)-1)
        for j in range(n,-1,-1):
            self.heapification(j)
    def heapification(self,j):
        le = len(arr)
        l = self.left(j)
        r = self.right(j)
        if l < le and arr[l] > arr[j]:
            largest = l
        else:
            largest = j
        if r < le and arr[r] > arr[largest]:
            largest = r
            self.labelm1.destroy()
            self.labelm1 = Label(self.main, text='Comparing the child nodes',font=('calibre',15,'bold'),bg=color3)
            self.labelm1.place(x=40,y=5)
            self.highlight(l,r)
            self.restore(l,r)
        if largest != j:
            time.sleep(0.2)
            arr[j], arr[largest] = arr[largest], arr[j]
            self.highlight(largest,j)
            self.labelm1.destroy()
            self.labelm1 = Label(self.main, text='Interchanging the larger child node with the parent node',font=('calibre',15,'bold'),bg=color3)
            self.labelm1.place(x=40,y=5)
            self.interchange(largest,j)
            circle_list[largest],circle_list[j] = circle_list[j],circle_list[largest]
            text_list[largest],text_list[j] = text_list[j],text_list[largest]
            time.sleep(0.2)
            self.restore(largest,j)
            self.heapification(largest)
    def reachtosorted(self): 
        if len(sortedarray)==1:
            if len(sortedarray)>len(sortedcircle_list):
                sortedcircle_list.append(170)
                self.xd = 170 - lastmidx[-1]
                self.yd = 560 - lastendy[-1]
                self.xd/=20
                self.yd/=20
            self.canvas1.move(circle_list[-1],self.xd,self.yd)
            self.canvas1.move(text_list[-1],self.xd,self.yd)
            cl = self.canvas1.bbox(circle_list[-1])
            cl_x1,cl_y1,cl_x2,cl_y2=cl
            self.canvas1.update()
            time.sleep(0.02)
            if cl_y2 <560:
                self.reachtosorted()
        elif len(sortedarray)>1 and len(sortedarray)<=15:
            if len(sortedarray)>len(sortedcircle_list):
                sortedcircle_list.append(sortedcircle_list[-1]+61)
                self.xd = sortedcircle_list[-1] - lastmidx[-1]
                self.yd = 560 - lastendy[-1]
                self.xd/=20
                self.yd/=20
            self.canvas1.move(circle_list[-1],self.xd,self.yd)
            self.canvas1.move(text_list[-1],self.xd,self.yd)
            cl = self.canvas1.bbox(circle_list[-1])
            cl_x1,cl_y1,cl_x2,cl_y2=cl
            self.canvas1.update()
            time.sleep(0.02)
            if cl_y2 <560:
                self.reachtosorted()
        elif len(sortedarray)==16:
            if len(sortedarray)>len(sortedcircle_list):
                sortedcircle_list.append(105)
                self.xd = 105 - lastmidx[-1]
                self.yd = 650 - lastendy[-1]
                self.xd/=20
                self.yd/=20
            self.canvas1.move(circle_list[-1],self.xd,self.yd)
            self.canvas1.move(text_list[-1],self.xd,self.yd)
            cl = self.canvas1.bbox(circle_list[-1])
            cl_x1,cl_y1,cl_x2,cl_y2=cl
            self.canvas1.update()
            time.sleep(0.02)
            if cl_y2 <650:
                self.reachtosorted()
        elif len(sortedarray)>16:
            if len(sortedarray)>len(sortedcircle_list):
                sortedcircle_list.append(sortedcircle_list[-1]+61)
                self.xd = sortedcircle_list[-1] - lastmidx[-1]
                self.yd = 650 - lastendy[-1]
                self.xd/=20
                self.yd/=20
            self.canvas1.move(circle_list[-1],self.xd,self.yd)
            self.canvas1.move(text_list[-1],self.xd,self.yd)
            cl = self.canvas1.bbox(circle_list[-1])
            cl_x1,cl_y1,cl_x2,cl_y2=cl
            self.canvas1.update()
            time.sleep(0.02)
            if cl_y2 <650:
                self.reachtosorted()
                # - 2*self.yd
    def sprun(self):
        arr[0], arr[-1] = arr[-1], arr[0]
        self.highlight(-1,0)
        self.labelm1.destroy()
        self.labelm1 = Label(self.main, text='Interchanging the First node with the Last node',font=('calibre',15,'bold'),bg=color3)
        self.labelm1.place(x=40,y=5)
        self.rootandparent(0,-1)
        circle_list[-1],circle_list[0] = circle_list[0],circle_list[-1]
        text_list[-1],text_list[0] = text_list[0],text_list[-1]
        time.sleep(0.2)
        self.restore(0,-1)
        self.insortedarray()
        circle_list.pop(-1)
        text_list.pop(-1)
        lastmidx.pop(-1)
        lastendy.pop(-1)
        
        # line_list[-1].delete()
    def insortedarray(self):
        sortedarray.append(0)
        sortedarray[-1] = arr[-1]
        arr.pop(-1)
        self.reachtosorted()
        
    def rootandparent(self,root,last):
        cl = self.canvas1.bbox(circle_list[last])
        cl_x1,cl_y1,cl_x2,cl_y2=cl
        xd = lastmidx[root] - lastmidx[last]
        yd = lastendy[root] - lastendy[last]
        xd/=20
        yd/=20
        self.canvas1.move(circle_list[last],xd,yd)
        self.canvas1.move(text_list[last],xd,yd)
        self.canvas1.move(circle_list[root],-xd,-yd)
        self.canvas1.move(text_list[root],-xd,-yd)
        self.canvas1.update()
        time.sleep(0.02)
        if cl_y2 + 2*yd>lastendy[root]:
            self.rootandparent(root,last)
    def interchange(self,largest,j): 
        cl = self.canvas1.bbox(circle_list[largest])
        cl_x1,cl_y1,cl_x2,cl_y2=cl 
        if largest%2!=0:
            xd = (lastmidx[j] - lastmidx[largest])/10
            yd = 9
            self.canvas1.move(circle_list[largest],xd,-yd)
            self.canvas1.move(circle_list[j],-xd,yd)
            self.canvas1.move(text_list[largest],xd,-yd)
            self.canvas1.move(text_list[j],-xd,yd)
            self.canvas1.update()
            time.sleep(0.025)
            if cl_y2-18>(lastendy[j]):
                self.interchange(largest,j)
        else:
            xd = (lastmidx[largest] - lastmidx[j])/10
            yd = 9
            self.canvas1.move(circle_list[largest],-xd,-yd)
            self.canvas1.move(circle_list[j],xd,yd)
            self.canvas1.move(text_list[largest],-xd,-yd)
            self.canvas1.move(text_list[j],xd,yd)
            self.canvas1.update()
            time.sleep(0.025)
            if cl_y2-18>(lastendy[j]):
                self.interchange(largest,j)
    def bt(self):
        lastmidx.clear()
        lastendy.clear()
        circle_list.clear()
        text_list.clear()
        line_list.clear()
        le = len(arr)
        lastmidx.append(500)
        lastendy.append(40)
        v = 0
        n = int((le//2)-1)
        for k in range(0,n+1):
            l = self.left(k)
            r = self.right(k)
            if k==0:
                circle_list.append(0)
                text_list.append(0)
                circle_list[0]=self.canvas1.create_oval(lastmidx[0]-30,lastendy[0],lastmidx[0]+30,lastendy[0]+60,fill=color4)
                text_list[0]=self.canvas1.create_text(500,70,text=f'{arr[v]}', fill="black", font=('Helvetica 25 bold'))
                lastmidx.append(lastmidx[0])
                lastmidx.pop(0)
                lastendy.append(lastendy[0]+60)
                lastendy.pop(0)
            if l==1 or r==2:
                #For left child node
                v += 1
                if l<le:
                    circle_list.append(0)
                    text_list.append(0)
                    line_list.append(0)
                    x2 = (lastmidx[0]-4)//2
                    line_list[v-1]=self.canvas1.create_line(lastmidx[0],lastendy[0],500-x2,lastendy[0]+30)
                    circle_list[v]=self.canvas1.create_oval(500-x2-30,lastendy[0]+30,500-x2+30,lastendy[0]+90,fill=color4)
                    text_list[v]=self.canvas1.create_text(500-x2,lastendy[0]+60,text=f'{arr[v]}', fill="black", font=('Helvetica 25 bold'))
                    lastmidx.append(500-x2)
                    lastendy.append(lastendy[0]+90)
                #For right child node
                v += 1
                if r<le:
                    circle_list.append(0)
                    text_list.append(0)
                    line_list.append(0)
                    line_list[v-1]=self.canvas1.create_line(lastmidx[0],lastendy[0],x2+500,lastendy[0]+30)
                    circle_list[v]=self.canvas1.create_oval(x2+500-30,lastendy[0]+30,x2+500+30,lastendy[0]+90,fill=color4)
                    text_list[v]=self.canvas1.create_text(x2+500,lastendy[0]+60,text=f'{arr[v]}', fill="black", font=('Helvetica 25 bold'))
                    lastmidx.append(x2+500)
                    lastendy.append(lastendy[0]+90)
            else:
                #For left child node
                v += 1
                if l<le:
                    circle_list.append(0)
                    text_list.append(0)
                    line_list.append(0)
                    if k%2!=0:
                        d = (lastmidx[self.parent(k)]-lastmidx[k])//2
                    else:
                        d = (-lastmidx[self.parent(k)]+lastmidx[k])//2
                    x2 = lastmidx[k] - d
                    line_list[v-1]=self.canvas1.create_line(lastmidx[k],lastendy[k],x2,lastendy[k]+30)
                    circle_list[v]=self.canvas1.create_oval(x2-30,lastendy[k]+30,x2+30,lastendy[k]+90,fill=color4)
                    text_list[v]=self.canvas1.create_text(x2,lastendy[k]+60,text=f'{arr[v]}', fill="black", font=('Helvetica 25 bold'))
                    lastmidx.append(x2)
                    lastendy.append(lastendy[k]+90)
                #For right child node
                v += 1
                if r<le:
                    circle_list.append(0)
                    text_list.append(0)
                    line_list.append(0)
                    x2 = lastmidx[k] + d
                    line_list[v-1]=self.canvas1.create_line(lastmidx[k],lastendy[k],x2,lastendy[k]+30)
                    circle_list[v]=self.canvas1.create_oval(x2-30,lastendy[k]+30,x2+30,lastendy[k]+90,fill=color4)
                    text_list[v]=self.canvas1.create_text(x2,lastendy[k]+60,text=f'{arr[v]}', fill="black", font=('Helvetica 25 bold'))
                    lastmidx.append(x2)
                    lastendy.append(lastendy[k]+90)
    def left(self,k):
        return 2 * k + 1
    def right(self,k):
        return 2 * k + 2
    def parent(self,k):
        return (k-1)//2
    def close(self):
        self.main.mainloop()

class Arrayinput:
    def __init__(self):
        self.first = Tk()
        self.first.title("HeapSort")
        self.first.geometry('1080x680')
        self.first.configure(bg=color1)
        self.label1 = Label(self.first, text='Enter the Array you want to impliment heap sort on: ',font=('Helvetica 25 bold'),bg=color1,fg='black')
        self.label1.place(x=40,y=300)
        self.label2 = Label(self.first, text='(in space seperated form ex: [1,2,3] = 1 2 3)',font=('Helvetica 25 bold'),bg=color1,fg='black')
        self.label2.place(x=40,y=340)
        self.entrybox = Entry(self.first, bg=color2, font=('Helvetica 25 bold'))
        self.entrybox.place(y=390,x=40,width=900,height=40)
        self.name = "ENTER.png"
        self.image_name = PhotoImage(file=self.name)
        self.button1 = Button(self.first, image=self.image_name,borderwidth=0,command = self.savennew)
        self.button1.place(x=960,y=390,height=40,width=80)
    def savennew(self):
        self.array = list(map(int, self.entrybox.get().strip().split()))
        for i in self.array:
            arr.append(i)
            arrrep.append(i)
            arrcomp.append(i)
        self.first.destroy()
    def closeai(self):
        self.first.mainloop() 

arrayinput = Arrayinput()
arrayinput.closeai()
draw = Drawing()
# build binary tree code/function
draw.bt()
draw.close()