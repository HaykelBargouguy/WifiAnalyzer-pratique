# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:28:39 2022

@author: 21650

"""

from puissance import distance_wifi,get_puissance
import matplotlib.pyplot as plt 
from marklocation import mark_points
from circles import draw_circles 
import tkinter as tk
x0,y0,x1,y1,x2,y2=(0,0,0,0,0,0)
ssid0,ssid1,ssid2=('','','')
def add_infos(f):
    canvas1.create_window(500, 250 ,width = 1000, height = 500, window=f)
    
def select_aps(Lframe):  
    ########
    ssf1 = tk.Frame(Lframe,width = 300, height = 20,background="black")
    label=tk.Label(ssf1, text="SSID de AP0",background="#e3ecff", font=('Arial', 14, 'bold'))
    label.pack(side=tk.LEFT)
    global e0
    e0= tk.Entry(ssf1, width= 20)
    e0.focus_set()
    e0.pack(side=tk.LEFT)
    def get_ssid0():
       global e0
       string0=e0.get()
       global ssid0
       ssid0=str(' ')+string0
    ssf1.pack(side=tk.TOP)
    ########
    ssf2 = tk.Frame(Lframe,width = 300, height = 20,background="black")
    label=tk.Label(ssf2, text="SSID de AP1",background="#e3ecff",font=('Arial', 14, 'bold'))
    label.pack(side=tk.LEFT)
    global e1
    e1= tk.Entry(ssf2, width= 20)
    e1.focus_set()
    e1.pack(side=tk.LEFT)
    def get_ssid1():
       global e1
       string1=e1.get()
       global ssid1
       ssid1=str(' ')+string1
    ssf2.pack(side=tk.TOP)
    ########
    ssf3 = tk.Frame(Lframe,width = 300, height = 20,background="black")
    label=tk.Label(ssf3, text="SSID de AP2",background="#e3ecff", font=('Arial', 14, 'bold'))
    label.pack(side=tk.LEFT)
    global e2
    e2= tk.Entry(ssf3, width= 20)
    e2.focus_set()
    e2.pack(side=tk.LEFT)
    def get_ssid2():
       global e2
       string2=e2.get()
       global ssid2
       ssid2=str(' ')+string2
    ssf3.pack(side=tk.TOP)
    ########
    def get_ssid():
        get_ssid0()
        get_ssid1()
        get_ssid2()
    ssf3.pack(side=tk.TOP)
    #Button to validate Entry Widget
    button4=tk.Button(Lframe, text= "Définir les valeurs",width= 15, bg='lightsteelblue2', command= get_ssid, font=('Arial', 10, 'bold'))
    button4.pack(side=tk.TOP)
    
def set_ap_location(Lframe):  
    l=tk.Label(Lframe, text=" ",background="#e3ecff", font=('Arial', 14, 'bold'))
    l.pack(side=tk.TOP)
    sf1 = tk.Frame(Lframe,width = 300, height = 20,background="black")
    label=tk.Label(sf1, text="Les coordonnés de AP0 (x0,y0):", background="#e3ecff", font=('Arial', 14, 'bold'))
    label.pack(side=tk.LEFT)
    global entry0
    entry0= tk.Entry(sf1, width= 20)
    entry0.focus_set()
    entry0.pack(side=tk.LEFT)
    def get_coordonees0():
       global entry0
       string0=entry0.get()
       tab0=string0.split(",")
       global x0
       global y0
       x0=int(tab0[0])
       y0=int(tab0[1])
    sf1.pack(side=tk.TOP)
    ########
    sf2 = tk.Frame (Lframe,width = 300, height = 20,background="black")
    label1=tk.Label(sf2, text="Les coordonnés de AP1 (x1,y2):", background="#e3ecff",font=('Arial', 14, 'bold'))
    label1.pack(side=tk.LEFT)
    global entry1
    entry1= tk.Entry(sf2, width= 20)
    entry1.focus_set()
    entry1.pack(side=tk.LEFT)
    def get_coordonees1():
       global entry1
       string1=entry1.get()
       tab1=string1.split(",")
       global x1
       global y1
       x1=int(tab1[0])
       y1=int(tab1[1]) 
    sf2.pack(side=tk.TOP)
    ########
    sf3 = tk.Frame (Lframe,width = 300, height = 20,background="black")
    label2=tk.Label(sf3, text="Les coordonnés de AP2 (x2,y2):",background="#e3ecff", font=('Arial', 14, 'bold'))
    label2.pack(side=tk.LEFT)
    global entry2
    entry2= tk.Entry(sf3, width= 20)
    entry2.focus_set()
    entry2.pack(side=tk.LEFT)
    def get_coordonees2():
       global entry2
       string2=entry2.get()
       tab2=string2.split(",")
       global x2
       global y2
       x2=int(tab2[0])
       y2=int(tab2[1])
    def get_coordonees():
        get_coordonees0()
        get_coordonees1()
        get_coordonees2()
        f = tk.Frame (root,width = 600, height = 500)
        s="Les coordonnés\nAP0(x,y)=("+str(x0)+','+str(y0)+')'+'\nAP1(x,y)=('+str(x1)+','+str(y1)+')'+'\nAP2(x,y)=('+str(x2)+','+str(y2)+')'
        linfo = tk.Label(f,bg='#e3ecff',fg='black', text=s, font=('Arial', 11, 'bold'))
        linfo.pack(side=tk.LEFT)
        add_infos(f)
    sf3.pack(side=tk.TOP)
    #Button to validate Entry Widget
    button4=tk.Button(Lframe, text= "Définir les valeurs",width= 15, bg='lightsteelblue2', command= get_coordonees,font=('Arial', 10, 'bold') )
    button4.pack(side=tk.TOP)

    
def create_graph():
    global x0,x1,x2,y0,y1,y2
    fig = plt.figure() 
    ax = fig.add_subplot(111)
    plt.axis("equal")
    ax.set_xlim((0, 100))
    ax.set_ylim((0, 100))
    #get puissance 
    #rssi0,rssi1,rssi2=(100,100,80)
    global ssid0,ssid1,ssid2
    print('777')
    print(ssid0)
    print(ssid1)
    print(ssid2)
    rssi0=float(get_puissance(ssid0))
    print(rssi0)
    
    rssi1=float(get_puissance(ssid1))
    print(rssi1)
    
    rssi2=float(get_puissance(ssid2))
    print(rssi2)

    #get distances
    d0= distance_wifi(rssi0)
    d1=distance_wifi(rssi1) 
    d2=distance_wifi(rssi2)

    #draw the 3 circles
    draw_circles((x0,y0,d0),(x1,y1,d1),(x2,y2,d2),ax)
    
    #mark intersection points and estimate location point
    mark_points((x0,y0,d0),(x1,y1,d1),(x2,y2,d2),ax)
    
    plt.show()





#WINDOW principal
root= tk.Tk()
root.title("TP3 WLAN")

#menu des boutons
frame1 = tk.Frame (root,width = 1000, height = 50,background="black")
frame1.pack()

button1 = tk.Button (frame1, text=' Afficher le graphe ',command=create_graph, bg='palegreen2', font=('Arial', 14, 'bold')) 
button1.pack(side=tk.LEFT)

#Left frame
Lframe = tk.Frame (root,width = 400, height = 500,background="#e3ecff", )
Lframe.pack(side=tk.LEFT)
select_aps(Lframe)
set_ap_location(Lframe) 

#right frame
frame2 = tk.Frame (root,width = 600, height = 500)
frame2.pack()

button6 = tk.Button (frame1, text='X', command=root.destroy, bg='#FF3535',fg="white", font=('Arial', 14, 'bold'))
button6.pack(side=tk.LEFT)

canvas1 = tk.Canvas(frame2, width = 600, height = 500)
canvas1.pack()


root.mainloop()

