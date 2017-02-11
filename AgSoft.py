# Author: Amjad Ali
# CoAuthor: Graeme C. Wake
# for AgKnowledge Ltd., Hamilton
# AGMARDT grant A14016
# January 2015


import tkinter as tk
from tkinter import ttk
import fileOpen
import fileOpen2
import firstFrame
import runOptimum
from datetime import datetime as dt
import tables
import showRslt


##import FileDialog
import matplotlib
matplotlib.use('TkAgg')
from pylab import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
##import tkFileDialog
#from matplotlib import style
from scipy.optimize import minimize




LARGE_FONT = ('Verdana', 12)
NORM_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)

#style.use("ggplot")

ryKConsts = np.array([125.09, 4.24, 7.84])
rySConsts = np.array([183.80, 0.09, 10.49])

y = dt.today()
TToday = float(y.year) * 365 + (float(y.month) - 1) * 30 + float(y.day) - 1

def quit():
    app.destroy()


class AgSoft(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
##
##        img = tk.PhotoImage(file='icon2.icns')
##        tk.Tk.call('wm','iconphoto',tk.Tk._w, img)
        tk.Tk.iconbitmap(self,"icon2.icns")

        tk.Tk.wm_title(self, "AgSoft")

        note = ttk.Notebook(self)

        homeTab = tk.Frame(note)
        userDefScenarioTab = tk.Frame(note)
        zeroScenarioTab = tk.Frame(note)
        maintScenarioTab = tk.Frame(note)
        optScenarioTab = tk.Frame(note)

        note.add(homeTab, text= 'Home', compound=tk.TOP)
        note.add(userDefScenarioTab, text = 'User Defined Treatments')
        note.add(zeroScenarioTab, text= 'Zero Treatments')
        note.add(maintScenarioTab,text='Maintenance Treatments')
        note.add(optScenarioTab,text='Optimum Treatments')
        note.grid(row=0, column=0)
        
        menubar = tk.Menu(note)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported as yet"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        def allParamHistoryP():
            FileResult = fileOpen2.PK()
            
            if FileResult == 'NoData':
                tk.messagebox.showerror(title='Error',message='You can simulate a minimum of one trial and a maximum of six trials.')
            else:
                TObs, Obs, TFert, Mass = FileResult[0],FileResult[1],FileResult[2],FileResult[3]
                resXP = runOptimum.PKP(TObs, Obs, TFert, Mass)
                
                try:
                    trials = np.shape(Obs)[1]
                except IndexError:
                    trials = 1
                t = np.linspace(TObs[0],TFert[-1]+365.0/2,500)
                if trials == 1:
                    p = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass, TObs[0], TFert)
                    showRslt.sh1(TObs,Obs,t,p,resXP[0],resXP[1],resXP[2])
                elif trials == 2:
                    p1 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,0], TObs[0], TFert)
                    p2 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,1], TObs[0], TFert)
                    showRslt.sh2(TObs,Obs[:,0],Obs[:,1],t,p1,p2,resXP[0],resXP[1],resXP[2])
                elif trials == 3:
                    p1 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,0], TObs[0], TFert)
                    p2 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,1], TObs[0], TFert)
                    p3 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,2], TObs[0], TFert)
                    showRslt.sh3(TObs,Obs[:,0],Obs[:,1],Obs[:,2],t,p1,p2,p3,resXP[0],resXP[1],resXP[2])
                elif trials == 4:
                    p1 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,0], TObs[0], TFert)
                    p2 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,1], TObs[0], TFert)
                    p3 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,2], TObs[0], TFert)
                    p4 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,3], TObs[0], TFert)
                    showRslt.sh4(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],t,p1,p2,p3,p4,resXP[0],resXP[1],resXP[2])
                elif trials == 5:
                    p1 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,0], TObs[0], TFert)
                    p2 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,1], TObs[0], TFert)
                    p3 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,2], TObs[0], TFert)
                    p4 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,3], TObs[0], TFert)
                    p5 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,4], TObs[0], TFert)
                    showRslt.sh5(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],t,p1,p2,p3,p4,p5,resXP[0],resXP[1],resXP[2])
                elif trials == 6:
                    p1 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,0], TObs[0], TFert)
                    p2 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,1], TObs[0], TFert)
                    p3 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,2], TObs[0], TFert)
                    p4 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,3], TObs[0], TFert)
                    p5 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,4], TObs[0], TFert)
                    p6 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,5], TObs[0], TFert)
                    showRslt.sh6(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],Obs[:,5],t,p1,p2,p3,p4,p5,p6,resXP[0],resXP[1],resXP[2])
        def allParamHistoryPXl():
            FileResult = fileOpen2.PKXl()
            
            if FileResult == 'NoData':
                tk.messagebox.showerror(title='Error',message='You can simulate a minimum of one trial and a maximum of six trials.')
            else:
                TObs, Obs, TFert, Mass = FileResult[0],FileResult[1],FileResult[2],FileResult[3]
                resXP = runOptimum.PKP(TObs, Obs, TFert, Mass)
                
                try:
                    trials = np.shape(Obs)[1]
                except IndexError:
                    trials = 1
                t = np.linspace(TObs[0],TFert[-1]+365.0/2,500)
                if trials == 1:
                    p = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass, TObs[0], TFert)
                    showRslt.sh1(TObs,Obs,t,p,resXP[0],resXP[1],resXP[2])
                elif trials == 2:
                    p1 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,0], TObs[0], TFert)
                    p2 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,1], TObs[0], TFert)
                    showRslt.sh2(TObs,Obs[:,0],Obs[:,1],t,p1,p2,resXP[0],resXP[1],resXP[2])
                elif trials == 3:
                    p1 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,0], TObs[0], TFert)
                    p2 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,1], TObs[0], TFert)
                    p3 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,2], TObs[0], TFert)
                    showRslt.sh3(TObs,Obs[:,0],Obs[:,1],Obs[:,2],t,p1,p2,p3,resXP[0],resXP[1],resXP[2])
                elif trials == 4:
                    p1 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,0], TObs[0], TFert)
                    p2 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,1], TObs[0], TFert)
                    p3 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,2], TObs[0], TFert)
                    p4 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,3], TObs[0], TFert)
                    showRslt.sh4(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],t,p1,p2,p3,p4,resXP[0],resXP[1],resXP[2])
                elif trials == 5:
                    p1 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,0], TObs[0], TFert)
                    p2 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,1], TObs[0], TFert)
                    p3 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,2], TObs[0], TFert)
                    p4 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,3], TObs[0], TFert)
                    p5 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,4], TObs[0], TFert)
                    showRslt.sh5(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],t,p1,p2,p3,p4,p5,resXP[0],resXP[1],resXP[2])
                elif trials == 6:
                    p1 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,0], TObs[0], TFert)
                    p2 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,1], TObs[0], TFert)
                    p3 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,2], TObs[0], TFert)
                    p4 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,3], TObs[0], TFert)
                    p5 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,4], TObs[0], TFert)
                    p6 = runOptimum.ff(t, resXP[0], resXP[1], resXP[2], Mass[:,5], TObs[0], TFert)
                    showRslt.sh6(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],Obs[:,5],t,p1,p2,p3,p4,p5,p6,resXP[0],resXP[1],resXP[2])        
                    
        def allParamHistoryK():
            FileResult = fileOpen2.PK()
            if FileResult == 'NoData':
                tk.messagebox.showerror(title='Error',message='You can simulate a minimum of one trial and a maximum of six trials.')
            else:
                TObs, Obs, TFert, Mass = FileResult[0],FileResult[1],FileResult[2],FileResult[3]
                resXK = runOptimum.PKK(TObs, Obs, TFert, Mass)
                
                try:
                    trials = np.shape(Obs)[1]
                except IndexError:
                    trials = 1
                t = np.linspace(TObs[0],TFert[-1]+365.0/2,500)
                if trials == 1:
                    k = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass, TObs[0], TFert)
                    showRslt.sh1k(TObs,Obs,t,k,resXK[0],resXK[1],resXK[2])
                elif trials == 2:
                    k1 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,0], TObs[0], TFert)
                    k2 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,1], TObs[0], TFert)
                    showRslt.sh2k(TObs,Obs[:,0],Obs[:,1],t,k1,k2,resXK[0],resXK[1],resXK[2])
                elif trials == 3:
                    k1 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,0], TObs[0], TFert)
                    k2 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,1], TObs[0], TFert)
                    k3 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,2], TObs[0], TFert)
                    showRslt.sh3k(TObs,Obs[:,0],Obs[:,1],Obs[:,2],t,k1,k2,k3,resXK[0],resXK[1],resXK[2])
                elif trials == 4:
                    k1 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,0], TObs[0], TFert)
                    k2 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,1], TObs[0], TFert)
                    k3 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,2], TObs[0], TFert)
                    k4 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,3], TObs[0], TFert)
                    showRslt.sh4k(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],t,k1,k2,k3,k4,resXK[0],resXK[1],resXK[2])
                elif trials == 5:
                    k1 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,0], TObs[0], TFert)
                    k2 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,1], TObs[0], TFert)
                    k3 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,2], TObs[0], TFert)
                    k4 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,3], TObs[0], TFert)
                    k5 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,4], TObs[0], TFert)
                    showRslt.sh5k(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],t,k1,k2,k3,k4,k5,resXK[0],resXK[1],resXK[2])
                elif trials == 6:
                    k1 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,0], TObs[0], TFert)
                    k2 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,1], TObs[0], TFert)
                    k3 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,2], TObs[0], TFert)
                    k4 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,3], TObs[0], TFert)
                    k5 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,4], TObs[0], TFert)
                    k6 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,5], TObs[0], TFert)
                    showRslt.sh6k(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],Obs[:,5],t,k1,k2,k3,k4,k5,k6,resXK[0],resXK[1],resXK[2])
        def allParamHistoryKXl():
            FileResult = fileOpen2.PKXl()
            if FileResult == 'NoData':
                tk.messagebox.showerror(title='Error',message='You can simulate a minimum of one trial and a maximum of six trials.')
            else:
                TObs, Obs, TFert, Mass = FileResult[0],FileResult[1],FileResult[2],FileResult[3]
                resXK = runOptimum.PKK(TObs, Obs, TFert, Mass)
                
                try:
                    trials = np.shape(Obs)[1]
                except IndexError:
                    trials = 1
                t = np.linspace(TObs[0],TFert[-1]+365.0/2,500)
                if trials == 1:
                    k = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass, TObs[0], TFert)
                    showRslt.sh1k(TObs,Obs,t,k,resXK[0],resXK[1],resXK[2])
                elif trials == 2:
                    k1 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,0], TObs[0], TFert)
                    k2 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,1], TObs[0], TFert)
                    showRslt.sh2k(TObs,Obs[:,0],Obs[:,1],t,k1,k2,resXK[0],resXK[1],resXK[2])
                elif trials == 3:
                    k1 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,0], TObs[0], TFert)
                    k2 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,1], TObs[0], TFert)
                    k3 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,2], TObs[0], TFert)
                    showRslt.sh3k(TObs,Obs[:,0],Obs[:,1],Obs[:,2],t,k1,k2,k3,resXK[0],resXK[1],resXK[2])
                elif trials == 4:
                    k1 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,0], TObs[0], TFert)
                    k2 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,1], TObs[0], TFert)
                    k3 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,2], TObs[0], TFert)
                    k4 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,3], TObs[0], TFert)
                    showRslt.sh4k(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],t,k1,k2,k3,k4,resXK[0],resXK[1],resXK[2])
                elif trials == 5:
                    k1 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,0], TObs[0], TFert)
                    k2 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,1], TObs[0], TFert)
                    k3 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,2], TObs[0], TFert)
                    k4 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,3], TObs[0], TFert)
                    k5 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,4], TObs[0], TFert)
                    showRslt.sh5k(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],t,k1,k2,k3,k4,k5,resXK[0],resXK[1],resXK[2])
                elif trials == 6:
                    k1 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,0], TObs[0], TFert)
                    k2 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,1], TObs[0], TFert)
                    k3 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,2], TObs[0], TFert)
                    k4 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,3], TObs[0], TFert)
                    k5 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,4], TObs[0], TFert)
                    k6 = runOptimum.ff(t, resXK[0], resXK[1], resXK[2], Mass[:,5], TObs[0], TFert)
                    showRslt.sh6k(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],Obs[:,5],t,k1,k2,k3,k4,k5,k6,resXK[0],resXK[1],resXK[2])
        


        def allParamHistoryS():
            FileResult = fileOpen2.PK()
            if FileResult == 'NoData':
                tk.messagebox.showerror(title='Error',message='You can simulate a minimum of one trial and a maximum of six trials.')
            else:
                TObs, Obs, TFert, Mass = FileResult[0],FileResult[1],FileResult[2],FileResult[3]
                resXS = runOptimum.PKS(TObs, Obs, TFert, Mass)
                
                try:
                    trials = np.shape(Obs)[1]
                except IndexError:
                    trials = 1
                t = np.linspace(TObs[0],TFert[-1]+365.0/2,500)
                if trials == 1:
                    s = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass, TObs[0], TFert)
                    showRslt.sh1s(TObs,Obs,t,s,resXS[0],resXS[1],resXS[2])
                elif trials == 2:
                    s1 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,0], TObs[0], TFert)
                    s2 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,1], TObs[0], TFert)
                    showRslt.sh2s(TObs,Obs[:,0],Obs[:,1],t,s1,s2,resXS[0],resXS[1],resXS[2])
                elif trials == 3:
                    s1 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,0], TObs[0], TFert)
                    s2 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,1], TObs[0], TFert)
                    s3 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,2], TObs[0], TFert)
                    showRslt.sh3s(TObs,Obs[:,0],Obs[:,1],Obs[:,2],t,s1,s2,s3,resXS[0],resXS[1],resXS[2])
                elif trials == 4:
                    s1 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,0], TObs[0], TFert)
                    s2 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,1], TObs[0], TFert)
                    s3 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,2], TObs[0], TFert)
                    s4 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,3], TObs[0], TFert)
                    showRslt.sh4s(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],t,s1,s2,s3,s4,resXS[0],resXS[1],resXS[2])
                elif trials == 5:
                    s1 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,0], TObs[0], TFert)
                    s2 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,1], TObs[0], TFert)
                    s3 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,2], TObs[0], TFert)
                    s4 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,3], TObs[0], TFert)
                    s5 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,4], TObs[0], TFert)
                    showRslt.sh5s(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],t,s1,s2,s3,s4,s5,resXS[0],resXS[1],resXS[2])
                elif trials == 6:
                    s1 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,0], TObs[0], TFert)
                    s2 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,1], TObs[0], TFert)
                    s3 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,2], TObs[0], TFert)
                    s4 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,3], TObs[0], TFert)
                    s5 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,4], TObs[0], TFert)
                    s6 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,5], TObs[0], TFert)
                    showRslt.sh6s(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],Obs[:,5],t,s1,s2,s3,s4,s5,s6,resXS[0],resXS[1],resXS[2])
        def allParamHistorySXl():
            FileResult = fileOpen2.PKXl()
            if FileResult == 'NoData':
                tk.messagebox.showerror(title='Error',message='You can simulate a minimum of one trial and a maximum of six trials.')
            else:
                TObs, Obs, TFert, Mass = FileResult[0],FileResult[1],FileResult[2],FileResult[3]
                resXS = runOptimum.PKS(TObs, Obs, TFert, Mass)
                
                try:
                    trials = np.shape(Obs)[1]
                except IndexError:
                    trials = 1
                t = np.linspace(TObs[0],TFert[-1]+365.0/2,500)
                if trials == 1:
                    s = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass, TObs[0], TFert)
                    showRslt.sh1s(TObs,Obs,t,s,resXS[0],resXS[1],resXS[2])
                elif trials == 2:
                    s1 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,0], TObs[0], TFert)
                    s2 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,1], TObs[0], TFert)
                    showRslt.sh2s(TObs,Obs[:,0],Obs[:,1],t,s1,s2,resXS[0],resXS[1],resXS[2])
                elif trials == 3:
                    s1 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,0], TObs[0], TFert)
                    s2 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,1], TObs[0], TFert)
                    s3 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,2], TObs[0], TFert)
                    showRslt.sh3s(TObs,Obs[:,0],Obs[:,1],Obs[:,2],t,s1,s2,s3,resXS[0],resXS[1],resXS[2])
                elif trials == 4:
                    s1 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,0], TObs[0], TFert)
                    s2 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,1], TObs[0], TFert)
                    s3 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,2], TObs[0], TFert)
                    s4 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,3], TObs[0], TFert)
                    showRslt.sh4s(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],t,s1,s2,s3,s4,resXS[0],resXS[1],resXS[2])
                elif trials == 5:
                    s1 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,0], TObs[0], TFert)
                    s2 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,1], TObs[0], TFert)
                    s3 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,2], TObs[0], TFert)
                    s4 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,3], TObs[0], TFert)
                    s5 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,4], TObs[0], TFert)
                    showRslt.sh5s(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],t,s1,s2,s3,s4,s5,resXS[0],resXS[1],resXS[2])
                elif trials == 6:
                    s1 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,0], TObs[0], TFert)
                    s2 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,1], TObs[0], TFert)
                    s3 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,2], TObs[0], TFert)
                    s4 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,3], TObs[0], TFert)
                    s5 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,4], TObs[0], TFert)
                    s6 = runOptimum.ff(t, resXS[0], resXS[1], resXS[2], Mass[:,5], TObs[0], TFert)
                    showRslt.sh6s(TObs,Obs[:,0],Obs[:,1],Obs[:,2],Obs[:,3],Obs[:,4],Obs[:,5],t,s1,s2,s3,s4,s5,s6,resXS[0],resXS[1],resXS[2])

        parmenu = tk.Menu(menubar, tearoff=0)
        subParPMenu = tk.Menu(parmenu)
        subParPMenu.add_command(label='Enter data through GUI')
        subParPMenu.add_command(label='Load data through a CSV file',command=allParamHistoryP)
        subParPMenu.add_command(label='Load data through an Excel file',command=allParamHistoryPXl)
        parmenu.add_cascade(label="Phosphorus", menu=subParPMenu)
        subParKMenu = tk.Menu(parmenu)
        subParKMenu.add_command(label='Enter data through GUI')
        subParKMenu.add_command(label='Load data through a CSV file',command=allParamHistoryK)
        subParKMenu.add_command(label='Load data through an Excel file',command=allParamHistoryKXl)
        parmenu.add_cascade(label="Potassium", menu=subParKMenu)
        subParSMenu = tk.Menu(parmenu)
        subParSMenu.add_command(label='Enter data through GUI')
        subParSMenu.add_command(label='Load data through a CSV file',command=allParamHistoryS)
        subParSMenu.add_command(label='Load data through an Excel file',command=allParamHistorySXl)
        parmenu.add_cascade(label="Sulphur", menu=subParSMenu)
        menubar.add_cascade(label="Parametrization", menu=parmenu)

        histmenu = tk.Menu(menubar, tearoff=0)
        subPMenu = tk.Menu(histmenu)
        subPMenu.add_command(label="Enter through GUI")
        subPMenu.add_command(label="Load through external text file")
        histmenu.add_cascade(label='Phosphorus', menu=subPMenu)
        subKMenu = tk.Menu(histmenu)
        subKMenu.add_command(label="Enter through GUI")
        subKMenu.add_command(label="Load through external text file")
        histmenu.add_cascade(label='Potassium', menu=subKMenu)
        subSMenu = tk.Menu(histmenu)
        subSMenu.add_command(label="Enter through GUI")
        subSMenu.add_command(label="Load through external text file")
        histmenu.add_cascade(label='Sulphur', menu=subSMenu)
        menubar.add_cascade(label="Use history", menu=histmenu)

        tk.Tk.config(self, menu=menubar)

        homeFrame = ttk.Frame(homeTab)
        homeFrame.grid(row=0, column=0, padx = 50, pady=50)

        entFrame = ttk.Frame(homeFrame)
        entFrame.grid(row=0,column=0)


        dateLab = ttk.LabelFrame(entFrame, text = 'Soil Test Date:')
        dateLab.grid(row=0, column=0, columnspan=3, padx=20)

        dayLab = ttk.Label(dateLab, text='day', font=SMALL_FONT)
        dayLab.grid(row=0, column=0)
        monthLab = ttk.Label(dateLab, text='month', font=SMALL_FONT)
        monthLab.grid(row=0, column=1)
        yearLab = ttk.Label(dateLab, text='year', font=SMALL_FONT)
        yearLab.grid(row=0, column=2)

        self.dvar = tk.StringVar()
        dayEnt = ttk.Combobox(dateLab, textvariable=self.dvar,
                              width=3, state='readonly')
        list1 = range(1,32)
        str1 = ' '.join(map(str, list1))
        dayEnt['values'] = str1
        dayEnt.current(14)
        dayEnt.grid(row=1,column=0, padx=10)

        self.mvar = tk.StringVar()
        monthEnt = ttk.Combobox(dateLab, textvariable=self.mvar,
                              width=3, state='readonly')
        list2 = range(1,13)
        str2 = ' '.join(map(str, list2))
        monthEnt['values'] = str2
        monthEnt.current(5)
        monthEnt.grid(row=1,column=1, padx=10)

        self.yvar = tk.StringVar()
        yearEnt = ttk.Combobox(dateLab, textvariable=self.yvar,
                              width=5, state='readonly')
        list3 = range(int(y.year) - 5,int(y.year) + 1)
        str3 = ' '.join(map(str, list3))
        yearEnt['values'] = str3
        yearEnt.current(5)
        yearEnt.grid(row=1,column=2, padx=10)

        valLab= ttk.LabelFrame(entFrame, text = 'Soil Test Values:')
        valLab.grid(row=0, column=3, columnspan=3, padx=(0,20))

        pLab = ttk.Label(valLab, text='Olsen P')
        pLab.grid(row=0, column=0)
        kLab = ttk.Label(valLab, text='QTK')
        kLab.grid(row=0, column=1)
        sLab = ttk.Label(valLab, text='EOS')
        sLab.grid(row=0, column=2)

        self.pvar = tk.StringVar()
        pEnt = ttk.Entry(valLab, textvariable=self.pvar, width=5)
        pEnt.grid(row=1,column=0, padx=10)
        self.pvar.set('30')

        self.kvar = tk.StringVar()
        kEnt = ttk.Entry(valLab, textvariable=self.kvar, width=5)
        kEnt.grid(row=1,column=1, padx=10)
        self.kvar.set('7')

        self.svar = tk.StringVar()
        sEnt = ttk.Entry(valLab, textvariable=self.svar, width=5)
        sEnt.grid(row=1,column=2, padx=10)
        self.svar.set('6')

        typeLab = ttk.LabelFrame(entFrame, text = 'Soil Type:')
        typeLab.grid(row=0, column=6, columnspan=3, padx=(0,20))

        self.pTypeVar = tk.StringVar()
        ptype = ttk.Combobox(typeLab, textvariable=self.pTypeVar,
                             width=12, state='readonly')
        ptype['values'] = ['Sedimentary', 'Volcanic', 'Pumice', 'Recent', 'Podzols','Sands']
        ptype.current(0)
        ptype.grid(row=0, column=0, padx=5, pady=5)

        self.sTypeVar = tk.StringVar()
        sType = ttk.Combobox(typeLab, textvariable=self.sTypeVar,
                             width=12, state='readonly')
        sType['values'] = ['Semi-arid', 'Pallic', 'Recent', 'Brown', 'Pumice','Allophane','Organic']
        sType.current(3)
        sType.grid(row=0, column=1, padx=5, pady=5)

        nextTrtDate = ttk.LabelFrame(entFrame, text='Next Treatment Date:')
        nextTrtDate.grid(row=1, column=0, columnspan=3, padx=20, pady=(20,0))

        dayLab = ttk.Label(nextTrtDate, text='day', font=SMALL_FONT)
        dayLab.grid(row=0, column=0)
        monthLab = ttk.Label(nextTrtDate, text='month', font=SMALL_FONT)
        monthLab.grid(row=0, column=1)
        yearLab = ttk.Label(nextTrtDate, text='year', font=SMALL_FONT)
        yearLab.grid(row=0, column=2)

        self.dvarN = tk.StringVar()
        dayEntN = ttk.Combobox(nextTrtDate, textvariable=self.dvarN,
                              width=3, state='readonly')

        list1N = range(1,32)
        str1N = ' '.join(map(str, list1N))
        dayEntN['values'] = str1N
        dayEntN.current(14)
        dayEntN.grid(row=1,column=0, padx=10)

        self.mvarN = tk.StringVar()
        monthEntN = ttk.Combobox(nextTrtDate, textvariable=self.mvarN,
                              width=3, state='readonly')
        list2N = range(1,13)
        str2N = ' '.join(map(str, list2N))
        monthEntN['values'] = str2N
        monthEntN.current(9)
        monthEntN.grid(row=1,column=1, padx=10)

        self.yvarN = tk.StringVar()
        yearEntN = ttk.Combobox(nextTrtDate, textvariable=self.yvarN,
                              width=5, state='readonly')

        list3N = range(int(y.year),int(y.year) + 10)
        str3N = ' '.join(map(str, list3N))
        yearEntN['values'] = str3N
        yearEntN.current(0)
        yearEntN.grid(row=1,column=2, padx=10)

        freqLab = ttk.LabelFrame(entFrame, text='Treatments Interval:')
        freqLab.grid(row=1, column=3, columnspan=3, padx=(0, 20),pady=(20,0))

        self.freqVar = tk.StringVar()
        freq = ttk.Combobox(freqLab, textvariable=self.freqVar,
                              width=10, state='readonly')
        freq['values'] = ['6 months', '12 months']
        freq.current(1)
        freq.grid(row=0, column=0, padx=10)

        farmLab = ttk.LabelFrame(entFrame, text='Farm Type:')
        farmLab.grid(row=1, column=6, columnspan=3, padx=(0, 20),pady=(20,0))

        self.farmVar = tk.StringVar()
        farm = ttk.Combobox(farmLab, textvariable=self.farmVar,
                              width=12, state='readonly')
        farm['values'] = ['Dairy', 'Dry Stock']
        farm.current(1)
        farm.grid(row=0, column=0, padx=10)

        self.note1 = ttk.Notebook(entFrame)
        self.note1.grid(row=3,column=0,columnspan=9)
        self.histTab = ttk.Frame(self.note1)
        self.note1.add(self.histTab, text= 'Use history', compound=tk.TOP)
        

        self.parTab = ttk.Frame(self.note1)
        self.note1.add(self.parTab, text= 'Choose parameters')



        def allParamFromHistory():
            FileResult = fileOpen.PK()
            if FileResult == 'NoData':
                tk.messagebox.showerror(title='Error',message='You can use a history file with four coulmns of data, first column for the dates (soil test and fertilizer application in dd/mm/yyyy) and three for the data (P, K, and S). The soil test data should be entered first and then at least two lines should be left blank before entering the fertilizer application data.')
            else:
                global TFert
                global MassP
                global MassK
                global MassS
                global TObs
                global ObsP
                global ObsK
                global ObsS
                TObs, ObsP, ObsK,ObsS, TFert, MassP,MassK,MassS = FileResult[0],FileResult[1],FileResult[2],FileResult[3],FileResult[4],FileResult[5],FileResult[6],FileResult[7]
                TObs=np.array(TObs)
                ObsP=np.array(ObsP)
                ObsK=np.array(ObsK)
                ObsS=np.array(ObsS)
                TFert=np.array(TFert)
                MassP=np.array(MassP)
                MassK=np.array(MassK)
                MassS=np.array(MassS)
                resXP = runOptimum.PKP(TObs, ObsP, TFert, MassP)
                resXK = runOptimum.PKK(TObs, ObsK, TFert, MassK)
                resXS = runOptimum.PKS(TObs, ObsS, TFert, MassS)
                global P0
                global K0
                global S0
                global alphaPP
                global alphaKK
                global alphaSS
                global cPP
                global cKK
                global cSS
                self.yvar.set(str(int(TFert[-1]/365)))
                self.mvar.set(str(int((TFert[-1]%365)/30)+1))
                self.dvar.set(str(int((TFert[-1]%365)%30)+1))

                PSTD = runOptimum.ff(TFert[-1], resXP[0], resXP[1], resXP[2], MassP, TObs[0], TFert)
                KSTD = runOptimum.ff(TFert[-1], resXK[0], resXK[1], resXK[2], MassK, TObs[0], TFert)
                SSTD = runOptimum.ff(TFert[-1], resXS[0], resXS[1], resXS[2], MassS, TObs[0], TFert)

                self.pvar.set(str(round(PSTD[0],1)))
                self.kvar.set(str(round(KSTD[0],1)))
                self.svar.set(str(round(SSTD[0],1)))

                
                alphaPP = resXP[1]
                cPP = resXP[2]
                P0 = resXP[0]
                alphaKK = resXK[1]
                cKK = resXK[2]
                K0 = resXK[0]
                alphaSS = resXS[1]
                cSS = resXS[2]
                S0 = resXS[0]
                self.alphaPText.config(state=tk.NORMAL)
                self.alphaPText.delete(1.0, tk.END)
                self.alphaPText.insert(tk.INSERT, '{0:.4f}'.format(alphaPP*10**4)+' x 10-4')
                self.alphaPText.tag_add('a','1.11','1.13')
                self.alphaPText.tag_configure('a',offset=2.3,font=SMALL_FONT)
                self.alphaPText.config(state=tk.DISABLED)

                self.cPText.config(state=tk.NORMAL)
                self.cPText.delete(1.0, tk.END)
                self.cPText.insert(tk.INSERT,"%.4f" %round(cPP,4))
                self.cPText.config(state=tk.DISABLED)

                self.alphaKText.config(state=tk.NORMAL)
                self.alphaKText.delete(1.0,tk.END)
                self.alphaKText.insert(tk.END, '{0:.4f}'.format(alphaKK*10**4)+' x 10-4')
                self.alphaKText.tag_add('b','1.11','1.13')
                self.alphaKText.tag_configure('b',offset=2.3,font=SMALL_FONT)
                self.alphaKText.config(state=tk.DISABLED)
                self.boxplotsPars.grid(row=0,column=0)
                self.cKText.config(state=tk.NORMAL)
                self.cKText.delete(1.0,tk.END)
                self.cKText.insert(tk.INSERT, "%.4f" %round(cKK,4))
                self.cKText.config(state=tk.DISABLED)

                self.alphaSText.config(state=tk.NORMAL)
                self.alphaSText.delete(1.0, tk.END)
                self.alphaSText.insert(tk.INSERT, '{0:.4f}'.format(alphaSS*10**4)+' x 10-4')
                self.alphaSText.tag_add('a','1.11','1.13')
                self.alphaSText.tag_configure('a',offset=2.3,font=SMALL_FONT)
                self.alphaSText.config(state=tk.DISABLED)

                self.cSText.config(state=tk.NORMAL)
                self.cSText.delete(1.0, tk.END)
                self.cSText.insert(tk.INSERT,"%.4f" %round(cSS,4))
                self.cSText.config(state=tk.DISABLED)
                
                self.boxplotsPars.grid_remove()
                self.boxplotsPars = firstFrame.show(self.parTab,aP,aK,aS,cP,cK,cS,[alphaPP,alphaKK,alphaSS,cPP,cKK,cSS])
                self.boxplotsPars.grid(row=0,column=0)

        def allParamFromHistoryXl():
            FileResult = fileOpen.PKXl()
            global TFert
            global MassP
            global MassK
            global MassS
            global TObs
            global ObsP
            global ObsK
            global ObsS
            TObs, ObsP, ObsK,ObsS, TFert, MassP,MassK,MassS = FileResult[0],FileResult[1],FileResult[2],FileResult[3],FileResult[4],FileResult[5],FileResult[6],FileResult[7]
            TObs=np.array(TObs)
            ObsP=np.array(ObsP)
            ObsK=np.array(ObsK)
            ObsS=np.array(ObsS)
            TFert=np.array(TFert)
            MassP=np.array(MassP)
            MassK=np.array(MassK)
            MassS=np.array(MassS)
            resXP = runOptimum.PKP(TObs, ObsP, TFert, MassP)
            resXK = runOptimum.PKK(TObs, ObsK, TFert, MassK)
            resXS = runOptimum.PKS(TObs, ObsS, TFert, MassS)
            global P0
            global K0
            global S0
            global alphaPP
            global alphaKK
            global alphaSS
            global cPP
            global cKK
            global cSS
            self.yvar.set(str(int(TFert[-1]/365)))
            self.mvar.set(str(int((TFert[-1]%365)/30)+1))
            self.dvar.set(str(int((TFert[-1]%365)%30)+1))

            PSTD = runOptimum.ff(TFert[-1], resXP[0], resXP[1], resXP[2], MassP, TObs[0], TFert)
            KSTD = runOptimum.ff(TFert[-1], resXK[0], resXK[1], resXK[2], MassK, TObs[0], TFert)
            SSTD = runOptimum.ff(TFert[-1], resXS[0], resXS[1], resXS[2], MassS, TObs[0], TFert)

            self.pvar.set(str(round(PSTD[0],1)))
            self.kvar.set(str(round(KSTD[0],1)))
            self.svar.set(str(round(SSTD[0],1)))

            
            alphaPP = resXP[1]
            cPP = resXP[2]
            P0 = resXP[0]
            alphaKK = resXK[1]
            cKK = resXK[2]
            K0 = resXK[0]
            alphaSS = resXS[1]
            cSS = resXS[2]
            S0 = resXS[0]
            self.alphaPText.config(state=tk.NORMAL)
            self.alphaPText.delete(1.0, tk.END)
            self.alphaPText.insert(tk.INSERT, '{0:.4f}'.format(alphaPP*10**4)+' x 10-4')
            self.alphaPText.tag_add('a','1.11','1.13')
            self.alphaPText.tag_configure('a',offset=2.3,font=SMALL_FONT)
            self.alphaPText.config(state=tk.DISABLED)

            self.cPText.config(state=tk.NORMAL)
            self.cPText.delete(1.0, tk.END)
            self.cPText.insert(tk.INSERT,"%.4f" %round(cPP,4))
            self.cPText.config(state=tk.DISABLED)

            self.alphaKText.config(state=tk.NORMAL)
            self.alphaKText.delete(1.0,tk.END)
            self.alphaKText.insert(tk.END, '{0:.4f}'.format(alphaKK*10**4)+' x 10-4')
            self.alphaKText.tag_add('b','1.11','1.13')
            self.alphaKText.tag_configure('b',offset=2.3,font=SMALL_FONT)
            self.alphaKText.config(state=tk.DISABLED)
            self.boxplotsPars.grid(row=0,column=0)
            self.cKText.config(state=tk.NORMAL)
            self.cKText.delete(1.0,tk.END)
            self.cKText.insert(tk.INSERT, "%.4f" %round(cKK,4))
            self.cKText.config(state=tk.DISABLED)

            self.alphaSText.config(state=tk.NORMAL)
            self.alphaSText.delete(1.0, tk.END)
            self.alphaSText.insert(tk.INSERT, '{0:.4f}'.format(alphaSS*10**4)+' x 10-4')
            self.alphaSText.tag_add('a','1.11','1.13')
            self.alphaSText.tag_configure('a',offset=2.3,font=SMALL_FONT)
            self.alphaSText.config(state=tk.DISABLED)

            self.cSText.config(state=tk.NORMAL)
            self.cSText.delete(1.0, tk.END)
            self.cSText.insert(tk.INSERT,"%.4f" %round(cSS,4))
            self.cSText.config(state=tk.DISABLED)
            
            self.boxplotsPars.grid_remove()
            self.boxplotsPars = firstFrame.show(self.parTab,aP,aK,aS,cP,cK,cS,[alphaPP,alphaKK,alphaSS,cPP,cKK,cSS])
            self.boxplotsPars.grid(row=0,column=0)

        
        self.HistFileButtonCSV = ttk.Button(self.histTab, text = 'Load History via CSV file', command=allParamFromHistory)
        self.HistFileButtonCSV.grid(row=0,column=1,columnspan=2,padx=10,pady=10)

        self.HistFileButtonXl = ttk.Button(self.histTab, text = 'Load History via Excel File', command=allParamFromHistoryXl)
        self.HistFileButtonXl.grid(row=0,column=3,columnspan=2,padx=10,pady=10)

        
        self.PhosLab = ttk.LabelFrame(self.histTab,text='Phosphorus Parameters:')

        self.PhosLab.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
        self.alphaPLab = tk.Text(self.PhosLab, width=4,height=1,background='snow2')
        self.alphaPLab.grid(row=0,column=0,sticky='e',pady=10,padx=10)
        self.alphaPLab.insert(tk.INSERT,u'\N{GREEK SMALL LETTER ALPHA}')
        self.alphaPLab.insert(tk.END,"p =")
        self.alphaPLab.tag_add("subscript",'1.1','1.2')
        self.alphaPLab.tag_add("main",'1.0','1.1')
        self.alphaPLab.tag_configure("subscript",offset=-2.3,font=SMALL_FONT)
        self.alphaPLab.tag_configure("main",font=LARGE_FONT)
        self.alphaPLab.configure(state=tk.DISABLED, borderwidth=-3)
        
        self.alphaPText = tk.Text(self.PhosLab, width=13, height=1)
        self.alphaPText.grid(row=0,column=1)
        self.alphaPText.configure(state=tk.DISABLED)

        self.alphaPLabUnit = tk.Text(self.PhosLab, width=6,height=1,background='snow2')
        self.alphaPLabUnit.grid(row=0,column=2,sticky='w',pady=10,padx=10)
        self.alphaPLabUnit.insert(tk.INSERT,'day-1')
        self.alphaPLabUnit.tag_add("superscript",'1.3','1.6')
        self.alphaPLabUnit.tag_add("main1",'1.0','1.3')
        self.alphaPLabUnit.tag_configure("superscript",offset=2.3,font=SMALL_FONT)
        self.alphaPLabUnit.tag_configure("main1",font=LARGE_FONT)
        self.alphaPLabUnit.configure(state=tk.DISABLED, borderwidth=-3)

        self.cPLab = tk.Text(self.PhosLab,width=4,height=1,background='snow2')
        self.cPLab.grid(row=1,column=0,sticky='e',padx=10,pady=10)
        self.cPLab.insert(tk.INSERT,'cp =')
        self.cPLab.tag_add("subscript1",'1.1','1.2')
        self.cPLab.tag_add("main2",'1.0','1.1')
        self.cPLab.tag_configure("subscript1",offset=-2.3,font=SMALL_FONT)
        self.cPLab.tag_configure("main2",font=LARGE_FONT)
        self.cPLab.configure(state=tk.DISABLED, borderwidth=-3)
        
        self.cPText = tk.Text(self.PhosLab, width=13,height=1)
        self.cPText.grid(row=1,column=1)
        self.cPText.configure(state=tk.DISABLED)
        
        self.cPLabUnit = tk.Text(self.PhosLab, width=18,height=1,background='snow2')
        self.cPLabUnit.grid(row=1,column=2, sticky='w',padx=10,pady=10)
        self.cPLabUnit.insert(tk.INSERT,'Olsen P (kg P ha-1)-1')
        self.cPLabUnit.tag_add("superscript2",'1.16','1.18')
        self.cPLabUnit.tag_add("superscript3",'1.19','1.21')
        self.cPLabUnit.tag_add("main3",'1.0','1.16')
        self.cPLabUnit.tag_add("main4",'1.18','1.19')
        self.cPLabUnit.tag_configure("superscript2",offset=2.3,font=SMALL_FONT)
        self.cPLabUnit.tag_configure("superscript3",offset=2.3,font=SMALL_FONT)
        self.cPLabUnit.tag_configure("main3",font=LARGE_FONT)
        self.cPLabUnit.tag_configure("main4",font=LARGE_FONT)
        self.cPLabUnit.configure(state=tk.DISABLED, borderwidth=-3)        


        self.PotasLab = ttk.LabelFrame(self.histTab,text='Potassium Parameters:')
        self.PotasLab.grid(row=1,column=2,columnspan=2,padx=10,pady=10)
        self.alphaKLab = tk.Text(self.PotasLab, width=4,height=1,background='snow2')
        self.alphaKLab.grid(row=0,column=0,sticky='e',padx=10,pady=10)
        self.alphaKLab.insert(tk.INSERT,u'\N{GREEK SMALL LETTER ALPHA}')
        self.alphaKLab.insert(tk.END,"k =")
        self.alphaKLab.tag_add("subscript3",'1.1','1.2')
        self.alphaKLab.tag_add("main6",'1.0','1.1')
        self.alphaKLab.tag_configure("subscript3",offset=-2.3,font=SMALL_FONT)
        self.alphaKLab.tag_configure("main6",font=LARGE_FONT)
        self.alphaKLab.configure(state=tk.DISABLED, borderwidth=-3)
        
        self.alphaKText = tk.Text(self.PotasLab, width=13, height=1)
        self.alphaKText.grid(row=0,column=1)
        self.alphaKText.configure(state=tk.DISABLED)
        
        self.alphaKLabUnit = tk.Text(self.PotasLab, width=6,height=1,background='snow2')
        self.alphaKLabUnit.grid(row=0,column=2,sticky='w',pady=10,padx=10)
        self.alphaKLabUnit.insert(tk.INSERT,'day-1')
        self.alphaKLabUnit.tag_add("superscript5",'1.3','1.6')
        self.alphaKLabUnit.tag_add("main7",'1.0','1.3')
        self.alphaKLabUnit.tag_configure("superscript5",offset=2.3,font=SMALL_FONT)
        self.alphaKLabUnit.tag_configure("main7",font=LARGE_FONT)
        self.alphaKLabUnit.configure(state=tk.DISABLED, borderwidth=-3)

        self.cKLab = tk.Text(self.PotasLab, width=4, height=1,background='snow2')
        self.cKLab.grid(row=1,column=0,sticky='e',padx=10,pady=10)
        self.cKLab.insert(tk.INSERT,'ck =')
        self.cKLab.tag_add("subscript4",'1.1','1.2')
        self.cKLab.tag_add("main8",'1.0','1.1')
        self.cKLab.tag_configure("subscript4",offset=-2.3,font=SMALL_FONT)
        self.cKLab.tag_configure("main8",font=LARGE_FONT)
        self.cKLab.configure(state=tk.DISABLED, borderwidth=-3)


        
        self.cKText = tk.Text(self.PotasLab, width=13,height=1)
        self.cKText.grid(row=1,column=1)
        self.cKText.configure(state=tk.DISABLED)
        
        self.cKLabUnit = tk.Text(self.PotasLab, width=16,height=1,background='snow2')
        self.cKLabUnit.grid(row=1,column=2, sticky='w',padx=10,pady=10)
        self.cKLabUnit.insert(tk.INSERT,'QTK (kg K ha-1)-1')
        self.cKLabUnit.tag_add("superscript10",'1.12','1.14')
        self.cKLabUnit.tag_add("superscript11",'1.15','1.17')
        self.cKLabUnit.tag_add("main12",'1.0','1.12')
        self.cKLabUnit.tag_add("main13",'1.14','1.15')
        self.cKLabUnit.tag_configure("superscript10",offset=2.3,font=SMALL_FONT)
        self.cKLabUnit.tag_configure("superscript11",offset=2.3,font=SMALL_FONT)
        self.cKLabUnit.tag_configure("main12",font=LARGE_FONT)
        self.cKLabUnit.tag_configure("main13",font=LARGE_FONT)
        self.cKLabUnit.configure(state=tk.DISABLED, borderwidth=-3)


        self.SulpLab = ttk.LabelFrame(self.histTab,text='Sulphur Parameters:')
        self.SulpLab.grid(row=1,column=4,columnspan=2,padx=10,pady=10)
        self.alphaSLab = tk.Text(self.SulpLab, width=4,height=1,background='snow2')
        self.alphaSLab.grid(row=0,column=0,sticky='e',pady=10,padx=10)
        self.alphaSLab.insert(tk.INSERT,u'\N{GREEK SMALL LETTER ALPHA}')
        self.alphaSLab.insert(tk.END,"s =")
        self.alphaSLab.tag_add("subscript",'1.1','1.2')
        self.alphaSLab.tag_add("main",'1.0','1.1')
        self.alphaSLab.tag_configure("subscript",offset=-2.3,font=SMALL_FONT)
        self.alphaSLab.tag_configure("main",font=LARGE_FONT)
        self.alphaSLab.configure(state=tk.DISABLED, borderwidth=-3)
        
        self.alphaSText = tk.Text(self.SulpLab, width=13, height=1)
        self.alphaSText.grid(row=0,column=1)
        self.alphaSText.configure(state=tk.DISABLED)

        self.alphaSLabUnit = tk.Text(self.SulpLab, width=6,height=1,background='snow2')
        self.alphaSLabUnit.grid(row=0,column=2,sticky='w',pady=10,padx=10)
        self.alphaSLabUnit.insert(tk.INSERT,'day-1')
        self.alphaSLabUnit.tag_add("superscript",'1.3','1.6')
        self.alphaSLabUnit.tag_add("main1",'1.0','1.3')
        self.alphaSLabUnit.tag_configure("superscript",offset=2.3,font=SMALL_FONT)
        self.alphaSLabUnit.tag_configure("main1",font=LARGE_FONT)
        self.alphaSLabUnit.configure(state=tk.DISABLED, borderwidth=-3)

        self.cSLab = tk.Text(self.SulpLab,width=4,height=1,background='snow2')
        self.cSLab.grid(row=1,column=0,sticky='e',padx=10,pady=10)
        self.cSLab.insert(tk.INSERT,'cs =')
        self.cSLab.tag_add("subscript1",'1.1','1.2')
        self.cSLab.tag_add("main2",'1.0','1.1')
        self.cSLab.tag_configure("subscript1",offset=-2.3,font=SMALL_FONT)
        self.cSLab.tag_configure("main2",font=LARGE_FONT)
        self.cSLab.configure(state=tk.DISABLED, borderwidth=-3)
        
        self.cSText = tk.Text(self.SulpLab, width=13,height=1)
        self.cSText.grid(row=1,column=1)
        self.cSText.configure(state=tk.DISABLED)
        
        self.cSLabUnit = tk.Text(self.SulpLab, width=18,height=1,background='snow2')
        self.cSLabUnit.grid(row=1,column=2, sticky='w',padx=10,pady=10)
        self.cSLabUnit.insert(tk.INSERT,'EOS (kg S ha-1)-1')
        self.cSLabUnit.tag_add("superscript2",'1.12','1.14')
        self.cSLabUnit.tag_add("superscript3",'1.15','1.17')
        self.cSLabUnit.tag_add("main3",'1.0','1.12')
        self.cSLabUnit.tag_add("main4",'1.14','1.15')
        self.cSLabUnit.tag_configure("superscript2",offset=2.3,font=SMALL_FONT)
        self.cSLabUnit.tag_configure("superscript3",offset=2.3,font=SMALL_FONT)
        self.cSLabUnit.tag_configure("main3",font=LARGE_FONT)
        self.cSLabUnit.tag_configure("main4",font=LARGE_FONT)
        self.cSLabUnit.configure(state=tk.DISABLED, borderwidth=-3)

        aP = runOptimum.aaP
        aK = runOptimum.aaK
        aS = runOptimum.aaS
        cP = runOptimum.ccP
        cK = runOptimum.ccK
        cS = runOptimum.ccS
        
        self.boxplotsPars = firstFrame.show(self.parTab,aP,aK,aS,cP,cK,cS,[aP[2],aK[2],aS[2],cP[2],cK[2],cS[2]])
        self.boxplotsPars.grid(row=0,column=0)

        


# User Defined Tab

        homeFrameUD = ttk.Frame(userDefScenarioTab)
        homeFrameUD.grid(row=0, column=0, padx = 50, pady=50)

        
        entFrameUD = ttk.Frame(homeFrameUD)
        entFrameUD.grid(row=1,column=0)


        nextTrtmnt = float(self.dvarN.get()) - 1 + (float(self.mvarN.get()) - 1) * 30 + float(self.yvarN.get()) * 365.0
        self.tableFrame =  tables.SimpleTable(entFrameUD, nextTrtmnt)
        self.tableFrame.grid(row=0,column=0,columnspan=10,padx=10,pady=10)
        

        def runUserDefScena():
            if self.pTypeVar.get() == 'Sedimentary':
                ryConsts = np.array((104.61,0,2.60),dtype=float)
            elif self.pTypeVar.get() == 'Volcanic':
                ryConsts = np.array((108.60,10.44,17.22),dtype=float)
            elif self.pTypeVar.get() == 'Pumice':
                ryConsts = np.array((106.60,15.52,23.41),dtype=float)
            elif self.pTypeVar.get() == 'Recent':
                ryConsts = np.array((105.00,28.49,34.75),dtype=float)
            elif self.pTypeVar.get() == 'Podzols':
                ryConsts = np.array((199.91,107.42,255.51),dtype=float)
            elif self.pTypeVar.get() == 'Sands':
                ryConsts = np.array((105.48,0.00,1.40),dtype=float)
            
            massNutrients = self.tableFrame.getVal()
            if self.freqVar.get() == '6 months':
                interval = 365.0/2
            else:
                interval = 365.0
            par = self.boxplotsPars.paR()
            STdate = float(self.dvar.get()) - 1 + (float(self.mvar.get()) - 1) * 30 + (float(self.yvar.get())) * 365.0

            fig1 = Figure(figsize=(13,6), dpi=70)
            a1 = fig1.add_subplot(231)
            a1.axes.get_xaxis().set_ticks([])
            a1.set_ylabel('Olsen P')
            b1 = fig1.add_subplot(234)
            b1.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            b1.set_ylabel('RY')
            b1.set_xlabel('Years')

            c1 = fig1.add_subplot(232)
            c1.axes.get_xaxis().set_ticks([])
            c1.set_ylabel('QTK')
            d1 = fig1.add_subplot(235)
            d1.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            d1.set_ylabel('RY')
            d1.set_xlabel('Years')

            e1 = fig1.add_subplot(233)
            e1.axes.get_xaxis().set_ticks([])
            e1.set_ylabel('EOS')
            f1 = fig1.add_subplot(236)
            f1.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            f1.set_ylabel('RY')
            f1.set_xlabel('Years')

            global AusrP
            global AusrK
            global AusrS
            global PusrEnd
            global KusrEnd
            global SusrEnd
            global AusrP0
            global AusrK0
            global AusrS0

            try:
                t1 = np.linspace(TObs[0],TFert[-1]+1, 300)
                t2 = np.linspace(TFert[-1]+1, TToday+365*10, 500)
                p1 = runOptimum.ff(t1, P0, par[0], par[3], MassP, TObs[0], TFert)
                ryP1 = runOptimum.rYieldFunc(t1,p1,ryConsts)
                p2 = runOptimum.ff(t2, p1[-1], par[0], par[3], massNutrients[1], t2[0], massNutrients[0])
                ryP2 = runOptimum.rYieldFunc(t2,p2,ryConsts)
                k1 = runOptimum.ff(t1, K0, par[1], par[4], MassK, TObs[0], TFert)
                ryK1 = runOptimum.rYieldFunc(t1,k1,ryKConsts)
                k2 = runOptimum.ff(t2, k1[-1], par[1], par[4], massNutrients[2], t2[0], massNutrients[0])
                ryK2 = runOptimum.rYieldFunc(t2,k2,ryKConsts)
                s1 = runOptimum.ff(t1, S0, par[2], par[5], MassS, TObs[0], TFert)
                ryS1 = runOptimum.rYieldFunc(t1,s1,rySConsts)
                s2 = runOptimum.ff(t2, s1[-1], par[2], par[5], massNutrients[3], t2[0], massNutrients[0])
                if self.sTypeVar.get() == 'Semi-arid':
                    s2 = s2.clip(max=7.0)
                elif self.sTypeVar.get() == 'Pallic':
                    s2 = s2.clip(max=15.0)
                elif self.sTypeVar.get() == 'Recent':
                    s2 = s2.clip(max=18.0)
                elif self.sTypeVar.get() == 'Brown':
                    s2 = s2.clip(max=19.0)
                elif self.sTypeVar.get() == 'Pumice':
                    s2 = s2.clip(max=27.0)
                elif self.sTypeVar.get() == 'Allophane':
                    s2 = s2.clip(max=40.0)
                elif self.sTypeVar.get() == 'Organic':
                    s2 = s2.clip(max=87.0)
                ryS2 = runOptimum.rYieldFunc(t2,s2,rySConsts)

                PusrEnd = p2[-1]
                KusrEnd = k2[-1]
                SusrEnd = s2[-1]
                
                AusrP=[]
                AusrK=[]
                AusrS=[]
                for i in range(10):
                    indexSt = np.argmax(t2 >= TToday + 365*i)
                    indexFh = np.argmax(t2 >= TToday + 365*(i+1))
                    BusrP = ryP2[indexSt:indexFh]
                    AusrP = np.append(AusrP,np.average(BusrP))
                    BusrK = ryK2[indexSt:indexFh]
                    AusrK = np.append(AusrK,np.average(BusrK))
                    BusrS = ryS2[indexSt:indexFh]
                    AusrS = np.append(AusrS,np.average(BusrS))

                AusrP0 = ryP2[np.argmax(t2 >= TToday)]
                AusrK0 = ryK2[np.argmax(t2 >= TToday)]
                AusrS0 = ryS2[np.argmax(t2 >= TToday)]

                
                a1.plot(t1/365, p1,t2/365,p2)
                a1.axis([TObs[0]/365,TToday/365+10.3,0,max(max(p1),max(p2))+5])
                c1.plot(t1/365, k1,t2/365,k2)
                c1.axis([TObs[0]/365,TToday/365+10.3,0,max(max(k1),max(k2))+5])
                e1.plot(t1/365, s1,t2/365,s2)
                e1.axis([TObs[0]/365,TToday/365+10.3,0,max(max(s1),max(s2))+5])
                b1.plot(t1/365, ryP1,t2/365,ryP2)
                b1.axis([TObs[0]/365,TToday/365+10.3,min(min(ryP1),min(ryP2))-5,102])
                d1.plot(t1/365, ryK1,t2/365,ryK2)
                d1.axis([TObs[0]/365,TToday/365+10.3,min(min(ryK1),min(ryK2))-5,102])
                f1.plot(t1/365, ryS1,t2/365,ryS2)
                f1.axis([TObs[0]/365,TToday/365+10.3,min(min(ryS1),min(ryS2))-5,102])
            except NameError:
                t = np.linspace(STdate, TToday + 365 * 10, 500)
                p = runOptimum.ff(t, float(self.pvar.get()), par[0], par[3], massNutrients[1], t[0], massNutrients[0])
                ryP = runOptimum.rYieldFunc(t,p,ryConsts)
                k = runOptimum.ff(t, float(self.kvar.get()), par[1], par[4], massNutrients[2], t[0], massNutrients[0])
                ryK = runOptimum.rYieldFunc(t,k,ryKConsts)
                s = runOptimum.ff(t, float(self.svar.get()), par[2], par[5], massNutrients[3], t[0], massNutrients[0])
                if self.sTypeVar.get() == 'Semi-arid':
                    s = s.clip(max=7.0)
                elif self.sTypeVar.get() == 'Pallic':
                    s = s.clip(max=15.0)
                elif self.sTypeVar.get() == 'Recent':
                    s = s.clip(max=18.0)
                elif self.sTypeVar.get() == 'Brown':
                    s = s.clip(max=19.0)
                elif self.sTypeVar.get() == 'Pumice':
                    s = s.clip(max=27.0)
                elif self.sTypeVar.get() == 'Allophane':
                    s = s.clip(max=40.0)
                elif self.sTypeVar.get() == 'Organic':
                    s = s.clip(max=87.0)
                ryS = runOptimum.rYieldFunc(t,s,rySConsts)

                PusrEnd = p[-1]
                KusrEnd = k[-1]
                SusrEnd = s[-1]
                
                
                AusrP=[]
                AusrK=[]
                AusrS=[]
                for i in range(10):
                    indexSt = np.argmax(t >= TToday + 365*i)
                    indexFh = np.argmax(t >= TToday + 365*(i+1))
                    BusrP = ryP[indexSt:indexFh]
                    AusrP = np.append(AusrP,np.average(BusrP))
                    BusrK = ryK[indexSt:indexFh]
                    AusrK = np.append(AusrK,np.average(BusrK))
                    BusrS = ryS[indexSt:indexFh]
                    AusrS = np.append(AusrS,np.average(BusrS))

                AusrP0 = ryP[np.argmax(t >= TToday)]
                AusrK0 = ryK[np.argmax(t >= TToday)]
                AusrS0 = ryS[np.argmax(t >= TToday)]
                
                a1.plot(t/365, p)
                a1.axis([t[0]/365,TToday/365+10.3,0,max(p)+5])
                c1.plot(t/365, k)
                c1.axis([t[0]/365,TToday/365+10.3,0,max(k)+5])
                e1.plot(t/365, s)
                e1.axis([t[0]/365,TToday/365+10.3,0,max(s)+5])
                b1.plot(t/365, ryP)
                b1.axis([t[0]/365,TToday/365+10.3,min(ryP)-5,102])
                d1.plot(t/365, ryK)
                d1.axis([t[0]/365,TToday/365+10.3,min(ryK)-5,102])
                f1.plot(t/365, ryS)
                f1.axis([t[0]/365,TToday/365+10.3,min(ryS)-5,102])
            
            self.canvas = FigureCanvasTkAgg(fig1, entFrameUD)
            self.canvas.show()
            self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=10, padx=10, pady=10, sticky='nsew')

            

        self.rsltBtn=ttk.Button(entFrameUD, text='Run', command=runUserDefScena)
        self.rsltBtn.grid(row=1, column=0, columnspan=10, padx=10, pady=10)




# Zero Treatments Tab


        homeFrameZero = ttk.Frame(zeroScenarioTab)
        homeFrameZero.grid(row=0, column=0,padx=50,pady=50)

        entFrameZero = ttk.Frame(homeFrameZero)
        entFrameZero.grid(row=0,column=0)

        def runZeroScenario():
            if self.pTypeVar.get() == 'Sedimentary':
                ryConsts = np.array((104.61,0,2.60),dtype=float)
            elif self.pTypeVar.get() == 'Volcanic':
                ryConsts = np.array((108.60,10.44,17.22),dtype=float)
            elif self.pTypeVar.get() == 'Pumice':
                ryConsts = np.array((106.60,15.52,23.41),dtype=float)
            elif self.pTypeVar.get() == 'Recent':
                ryConsts = np.array((105.00,28.49,34.75),dtype=float)
            elif self.pTypeVar.get() == 'Podzols':
                ryConsts = np.array((199.91,107.42,255.51),dtype=float)
            elif self.pTypeVar.get() == 'Sands':
                ryConsts = np.array((105.48,0.00,1.40),dtype=float)
            
            par = self.boxplotsPars.paR()
            STdate = float(self.dvar.get()) - 1 + (float(self.mvar.get()) - 1) * 30 + (float(self.yvar.get())) * 365.0

            fig2 = Figure(figsize=(13,6), dpi=70)
            a2 = fig2.add_subplot(231)
            a2.axes.get_xaxis().set_ticks([])
            a2.set_ylabel('Olsen P')
            b2 = fig2.add_subplot(234)
            b2.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            b2.set_ylabel('RY')
            b2.set_xlabel('Years')

            c2 = fig2.add_subplot(232)
            c2.axes.get_xaxis().set_ticks([])
            c2.set_ylabel('QTK')
            d2 = fig2.add_subplot(235)
            d2.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            d2.set_ylabel('RY')
            d2.set_xlabel('Years')

            e2 = fig2.add_subplot(233)
            e2.axes.get_xaxis().set_ticks([])
            e2.set_ylabel('EOS')
            f2 = fig2.add_subplot(236)
            f2.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            f2.set_ylabel('RY')
            f2.set_xlabel('Years')

            global PzerEnd
            global KzerEnd
            global SzerEnd
            global AzerP
            global AzerK
            global AzerS
            global AzerP0
            global AzerK0
            global AzerS0
            

            try:
                t1 = np.linspace(TObs[0],TFert[-1]+1, 300)
                t2 = np.linspace(TFert[-1]+1, TToday+365*10, 500)
                p1 = runOptimum.ff(t1, P0, par[0], par[3], MassP, TObs[0], TFert)
                ryP1 = runOptimum.rYieldFunc(t1,p1,ryConsts)
                p2 = p1[-1] * np.exp(-par[0] * (t2 - t2[0]))
                ryP2 = runOptimum.rYieldFunc(t2,p2,ryConsts)
                k1 = runOptimum.ff(t1, K0, par[1], par[4], MassK, TObs[0], TFert)
                ryK1 = runOptimum.rYieldFunc(t1,k1,ryKConsts)
                k2 = k1[-1] * np.exp(-par[1] * (t2 - t2[0]))
                ryK2 = runOptimum.rYieldFunc(t2,k2,ryKConsts)
                s1 = runOptimum.ff(t1, S0, par[2], par[5], MassS, TObs[0], TFert)
                ryS1 = runOptimum.rYieldFunc(t1,s1,rySConsts)
                s2 = s1[-1] * np.exp(-par[2] * (t2 - t2[0]))
                if self.sTypeVar.get() == 'Semi-arid':
                    s2 = s2.clip(max=7.0)
                elif self.sTypeVar.get() == 'Pallic':
                    s2 = s2.clip(max=15.0)
                elif self.sTypeVar.get() == 'Recent':
                    s2 = s2.clip(max=18.0)
                elif self.sTypeVar.get() == 'Brown':
                    s2 = s2.clip(max=19.0)
                elif self.sTypeVar.get() == 'Pumice':
                    s2 = s2.clip(max=27.0)
                elif self.sTypeVar.get() == 'Allophane':
                    s2 = s2.clip(max=40.0)
                elif self.sTypeVar.get() == 'Organic':
                    s2 = s2.clip(max=87.0)
                ryS2 = runOptimum.rYieldFunc(t2,s2,rySConsts)

                PzerEnd=p2[-1]
                KzerEnd=k2[-1]
                SzerEnd=s2[-1]
                
                AzerP=[]
                AzerK=[]
                AzerS=[]
                for i in range(10):
                    indexSt = np.argmax(t2 >= TToday + 365*i)
                    indexFh = np.argmax(t2 >= TToday + 365*(i+1))
                    BzerP = ryP2[indexSt:indexFh]
                    AzerP = np.append(AzerP,np.average(BzerP))
                    BzerK = ryK2[indexSt:indexFh]
                    AzerK = np.append(AzerK,np.average(BzerK))
                    BzerS = ryS2[indexSt:indexFh]
                    AzerS = np.append(AzerS,np.average(BzerS))

                AzerP0 = ryP2[np.argmax(t2 >= TToday)]
                AzerK0 = ryK2[np.argmax(t2 >= TToday)]
                AzerS0 = ryS2[np.argmax(t2 >= TToday)]
                
                a2.plot(t1/365, p1,t2/365,p2)
                a2.axis([TObs[0]/365,TToday/365+10.3,0,max(max(p1),max(p2))+5])
                c2.plot(t1/365, k1,t2/365,k2)
                c2.axis([TObs[0]/365,TToday/365+10.3,0,max(max(k1),max(k2))+5])
                e2.plot(t1/365, s1,t2/365,s2)
                e2.axis([TObs[0]/365,TToday/365+10.3,0,max(max(s1),max(s2))+5])
                b2.plot(t1/365, ryP1,t2/365,ryP2)
                b2.axis([TObs[0]/365,TToday/365+10.3,min(min(ryP1),min(ryP2))-5,102])
                d2.plot(t1/365, ryK1,t2/365,ryK2)
                d2.axis([TObs[0]/365,TToday/365+10.3,min(min(ryK1),min(ryK2))-5,102])
                f2.plot(t1/365, ryS1,t2/365,ryS2)
                f2.axis([TObs[0]/365,TToday/365+10.3,min(min(ryS1),min(ryS2))-5,102])
            except NameError:
                t = np.linspace(STdate, TToday + 365 * 10, 500)
                p = float(self.pvar.get()) * np.exp(-par[0] * (t - t[0]))
                ryP = runOptimum.rYieldFunc(t,p,ryConsts)
                k = float(self.kvar.get()) * np.exp(-par[1] * (t - t[0]))
                ryK = runOptimum.rYieldFunc(t,k,ryKConsts)
                s = float(self.svar.get()) * np.exp(-par[2] * (t - t[0]))
                if self.sTypeVar.get() == 'Semi-arid':
                    s = s.clip(max=7.0)
                elif self.sTypeVar.get() == 'Pallic':
                    s = s.clip(max=15.0)
                elif self.sTypeVar.get() == 'Recent':
                    s = s.clip(max=18.0)
                elif self.sTypeVar.get() == 'Brown':
                    s = s.clip(max=19.0)
                elif self.sTypeVar.get() == 'Pumice':
                    s = s.clip(max=27.0)
                elif self.sTypeVar.get() == 'Allophane':
                    s = s.clip(max=40.0)
                elif self.sTypeVar.get() == 'Organic':
                    s = s.clip(max=87.0)
                ryS = runOptimum.rYieldFunc(t,s,rySConsts)

                PzerEnd=p[-1]
                KzerEnd=k[-1]
                SzerEnd=s[-1]

                AzerP=[]
                AzerK=[]
                AzerS=[]
                for i in range(10):
                    indexSt = np.argmax(t >= TToday + 365*i)
                    indexFh = np.argmax(t >= TToday + 365*(i+1))
                    BzerP = ryP[indexSt:indexFh]
                    AzerP = np.append(AzerP,np.average(BzerP))
                    BzerK = ryK[indexSt:indexFh]
                    AzerK = np.append(AzerK,np.average(BzerK))
                    BzerS = ryS[indexSt:indexFh]
                    AzerS = np.append(AzerS,np.average(BzerS))

                AzerP0 = ryP[np.argmax(t >= TToday)]
                AzerK0 = ryK[np.argmax(t >= TToday)]
                AzerS0 = ryS[np.argmax(t >= TToday)]
                
                a2.plot(t/365, p)
                a2.axis([t[0]/365,TToday/365+10.3,0,max(p)+5])
                c2.plot(t/365, k)
                c2.axis([t[0]/365,TToday/365+10.3,0,max(k)+5])
                e2.plot(t/365, s)
                e2.axis([t[0]/365,TToday/365+10.3,0,max(s)+5])
                b2.plot(t/365, ryP)
                b2.axis([t[0]/365,TToday/365+10.3,min(ryP)-5,102])
                d2.plot(t/365, ryK)
                d2.axis([t[0]/365,TToday/365+10.3,min(ryK)-5,102])
                f2.plot(t/365, ryS)
                f2.axis([t[0]/365,TToday/365+10.3,min(ryS)-5,102])

            self.canvas = FigureCanvasTkAgg(fig2, entFrameZero)
            self.canvas.show()
            self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=10, padx=10, pady=10, sticky='nsew')


        runBtnZero = ttk.Button(entFrameZero, text='Run', command=runZeroScenario)
        runBtnZero.grid(row=0, column=0, pady=10, padx=10,sticky='w')


# Maintenance Treatments Tab

        homeFrameMaint = ttk.Frame(maintScenarioTab)
        homeFrameMaint.grid(row=0, column=0,padx=50,pady=50)

        entFrameMaint = ttk.Frame(homeFrameMaint)
        entFrameMaint.grid(row=0, column=0)

        def runMaintScenario():
            if self.pTypeVar.get() == 'Sedimentary':
                ryConsts = np.array((104.61,0,2.60),dtype=float)
            elif self.pTypeVar.get() == 'Volcanic':
                ryConsts = np.array((108.60,10.44,17.22),dtype=float)
            elif self.pTypeVar.get() == 'Pumice':
                ryConsts = np.array((106.60,15.52,23.41),dtype=float)
            elif self.pTypeVar.get() == 'Recent':
                ryConsts = np.array((105.00,28.49,34.75),dtype=float)
            elif self.pTypeVar.get() == 'Podzols':
                ryConsts = np.array((199.91,107.42,255.51),dtype=float)
            elif self.pTypeVar.get() == 'Sands':
                ryConsts = np.array((105.48,0.00,1.40),dtype=float)
            
            if self.freqVar.get() == '6 months':
                interval = 365.0/2
            else:
                interval = 365.0
                
            par = self.boxplotsPars.paR()
            STdate = float(self.dvar.get()) - 1 + (float(self.mvar.get()) - 1) * 30 + (float(self.yvar.get())) * 365.0

            fig3 = Figure(figsize=(13,6), dpi=70)
            a3 = fig3.add_subplot(231)
            a3.axes.get_xaxis().set_ticks([])
            a3.set_ylabel('Olsen P')
            b3 = fig3.add_subplot(234)
            b3.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            b3.set_ylabel('RY')
            b3.set_xlabel('Years')

            c3 = fig3.add_subplot(232)
            c3.axes.get_xaxis().set_ticks([])
            c3.set_ylabel('QTK')
            d3 = fig3.add_subplot(235)
            d3.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            d3.set_ylabel('RY')
            d3.set_xlabel('Years')

            e3 = fig3.add_subplot(233)
            e3.axes.get_xaxis().set_ticks([])
            e3.set_ylabel('EOS')
            f3 = fig3.add_subplot(236)
            f3.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            f3.set_ylabel('RY')
            f3.set_xlabel('Years')

            global PmaiEnd
            global KmaiEnd
            global SmaiEnd
            global mp
            global mk
            global ms

            mp = float(self.pvar.get()) * (np.exp(par[0] * (interval - nextTrtmnt + STdate)) - np.exp(-par[0] * (nextTrtmnt - STdate))) / par[3]
            mk = float(self.kvar.get()) * (np.exp(par[1] * (interval - nextTrtmnt + STdate)) - np.exp(-par[1] * (nextTrtmnt - STdate))) / par[4]
            ms = float(self.svar.get()) * (np.exp(par[2] * (interval - nextTrtmnt + STdate)) - np.exp(-par[2] * (nextTrtmnt - STdate))) / par[5]
            m = mp * np.ones(int(10 * 365.0/interval))
            m1 = mk * np.ones(int(10 * 365.0/interval))
            m2 = ms * np.ones(int(10 * 365.0/interval))
##            
##            t = np.linspace(STdate,STdate + 10 * 365)
##            p = runOptimum.f(t, P0, runOptimum.medianAlpha, runOptimum.medianc, m, STdate, T1, freq)
##            k = runOptimum.f(t, K0, runOptimum.medianAlphaK, runOptimum.mediancK, m1, STdate, T1, freq)

            tNutrients = linspace(nextTrtmnt,nextTrtmnt+10*365.0,int(round(365.0*10/interval,0)))
            global AmaiP
            global AmaiK
            global AmaiS
            global AmaiP0
            global AmaiK0
            global AmaiS0

            try:
                t1 = np.linspace(TObs[0],TFert[-1]+1, 300)
                t2 = np.linspace(TFert[-1]+1, TToday+365*10, 500)
                p1 = runOptimum.ff(t1, P0, par[0], par[3], MassP, TObs[0], TFert)
                ryP1 = runOptimum.rYieldFunc(t1,p1,ryConsts)
                p2 = runOptimum.ff(t2, p1[-1], par[0], par[3], m, t2[0], tNutrients)
                ryP2 = runOptimum.rYieldFunc(t2,p2,ryConsts)
                k1 = runOptimum.ff(t1, K0, par[1], par[4], MassK, TObs[0], TFert)
                ryK1 = runOptimum.rYieldFunc(t1,k1,ryKConsts)
                k2 = runOptimum.ff(t2, k1[-1], par[1], par[4], m1, t2[0], tNutrients)
                ryK2 = runOptimum.rYieldFunc(t2,k2,ryKConsts)
                s1 = runOptimum.ff(t1, S0, par[2], par[5], MassS, TObs[0], TFert)
                ryS1 = runOptimum.rYieldFunc(t1,s1,rySConsts)
                s2 = runOptimum.ff(t2, s1[-1], par[2], par[5], m2, t2[0], tNutrients)
                if self.sTypeVar.get() == 'Semi-arid':
                    s2 = s2.clip(max=7.0)
                elif self.sTypeVar.get() == 'Pallic':
                    s2 = s2.clip(max=15.0)
                elif self.sTypeVar.get() == 'Recent':
                    s2 = s2.clip(max=18.0)
                elif self.sTypeVar.get() == 'Brown':
                    s2 = s2.clip(max=19.0)
                elif self.sTypeVar.get() == 'Pumice':
                    s2 = s2.clip(max=27.0)
                elif self.sTypeVar.get() == 'Allophane':
                    s2 = s2.clip(max=40.0)
                elif self.sTypeVar.get() == 'Organic':
                    s2 = s2.clip(max=87.0)
                ryS2 = runOptimum.rYieldFunc(t2,s2,rySConsts)

                PmaiEnd=p2[-1]
                KmaiEnd=k2[-1]
                SmaiEnd=s2[-1]

                AmaiP=[]
                AmaiK=[]
                AmaiS=[]

                for i in range(10):
                    indexSt = np.argmax(t2 >= TToday + 365*i)
                    indexFh = np.argmax(t2 >= TToday + 365*(i+1))
                    BmaiP = ryP2[indexSt:indexFh]
                    AmaiP = np.append(AmaiP,np.average(BmaiP))
                    BmaiK = ryK2[indexSt:indexFh]
                    AmaiK = np.append(AmaiK,np.average(BmaiK))
                    BmaiS = ryS2[indexSt:indexFh]
                    AmaiS = np.append(AmaiS,np.average(BmaiS))

                AmaiP0 = ryP2[np.argmax(t2 >= TToday)]
                AmaiK0 = ryK2[np.argmax(t2 >= TToday)]
                AmaiS0 = ryS2[np.argmax(t2 >= TToday)]

                a3.plot(t1/365, p1,t2/365,p2)
                a3.axis([TObs[0]/365,TToday/365+10.3,0,max(max(p1),max(p2))+5])
                c3.plot(t1/365, k1,t2/365,k2)
                c3.axis([TObs[0]/365,TToday/365+10.3,0,max(max(k1),max(k2))+5])
                e3.plot(t1/365, s1,t2/365,s2)
                e3.axis([TObs[0]/365,TToday/365+10.3,0,max(max(s1),max(s2))+5])
                b3.plot(t1/365, ryP1,t2/365,ryP2)
                b3.axis([TObs[0]/365,TToday/365+10.3,min(min(ryP1),min(ryP2))-5,102])
                d3.plot(t1/365, ryK1,t2/365,ryK2)
                d3.axis([TObs[0]/365,TToday/365+10.3,min(min(ryK1),min(ryK2))-5,102])
                f3.plot(t1/365, ryS1,t2/365,ryS2)
                f3.axis([TObs[0]/365,TToday/365+10.3,min(min(ryS1),min(ryS2))-5,102])
            except NameError:
                t = np.linspace(STdate, TToday + 365 * 10, 500)
                p = runOptimum.ff(t, float(self.pvar.get()), par[0], par[3], m, t[0], tNutrients)
                ryP = runOptimum.rYieldFunc(t,p,ryConsts)
                k = runOptimum.ff(t, float(self.kvar.get()), par[1], par[4], m1, t[0], tNutrients)
                ryK = runOptimum.rYieldFunc(t,k,ryKConsts)
                s = runOptimum.ff(t, float(self.svar.get()), par[2], par[5], m2, t[0], tNutrients)
                if self.sTypeVar.get() == 'Semi-arid':
                    s = s.clip(max=7.0)
                elif self.sTypeVar.get() == 'Pallic':
                    s = s.clip(max=15.0)
                elif self.sTypeVar.get() == 'Recent':
                    s = s.clip(max=18.0)
                elif self.sTypeVar.get() == 'Brown':
                    s = s.clip(max=19.0)
                elif self.sTypeVar.get() == 'Pumice':
                    s = s.clip(max=27.0)
                elif self.sTypeVar.get() == 'Allophane':
                    s = s.clip(max=40.0)
                elif self.sTypeVar.get() == 'Organic':
                    s = s.clip(max=87.0)
                ryS = runOptimum.rYieldFunc(t,s,rySConsts)

                PmaiEnd=p[-1]
                KmaiEnd=k[-1]
                SmaiEnd=s[-1]

                AmaiP=[]
                AmaiK=[]
                AmaiS=[]
                for i in range(10):
                    indexSt = np.argmax(t >= TToday + 365*i)
                    indexFh = np.argmax(t >= TToday + 365*(i+1))
                    BmaiP = ryP[indexSt:indexFh]
                    AmaiP = np.append(AmaiP,np.average(BmaiP))
                    BmaiK = ryK[indexSt:indexFh]
                    AmaiK = np.append(AmaiK,np.average(BmaiK))
                    BmaiS = ryS[indexSt:indexFh]
                    AmaiS = np.append(AmaiS,np.average(BmaiS))

                AmaiP0 = ryP[np.argmax(t >= TToday)]
                AmaiK0 = ryK[np.argmax(t >= TToday)]
                AmaiS0 = ryS[np.argmax(t >= TToday)]
                    
                a3.plot(t/365, p)
                a3.axis([t[0]/365,TToday/365+10.3,0,max(p)+5])
                c3.plot(t/365, k)
                c3.axis([t[0]/365,TToday/365+10.3,0,max(k)+5])
                e3.plot(t/365, s)
                e3.axis([t[0]/365,TToday/365+10.3,0,max(s)+5])
                b3.plot(t/365, ryP)
                b3.axis([t[0]/365,TToday/365+10.3,min(ryP)-5,102])
                d3.plot(t/365, ryK)
                d3.axis([t[0]/365,TToday/365+10.3,min(ryK)-5,102])
                f3.plot(t/365, ryS)
                f3.axis([t[0]/365,TToday/365+10.3,min(ryS)-5,102])
            
            self.canvas = FigureCanvasTkAgg(fig3, entFrameMaint)
            self.canvas.show()
            self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=10, padx=10, pady=(0,10), sticky='nsew')

            self.PhosRsltLab=ttk.LabelFrame(entFrameMaint,text='Phosphorus:')
            self.PhosRsltLab.grid(row=4,column=0,padx=10,pady=10)
            labRsltP = tk.Text(self.PhosRsltLab,width=6,height=1)
            labRsltP.delete(1.0,tk.END)
            labRsltP.insert(tk.INSERT, "%.2f" %round(mp,2))
            labRsltP.tag_add('pmain','1.0','1.10')
            labRsltP.tag_configure('pmain',font=LARGE_FONT)
            labRsltP.configure(state=tk.DISABLED)
            labRsltP.grid(row=0,column=0,sticky='w',padx=5,pady=5)

            labRsltPu = tk.Text(self.PhosRsltLab,width=30,height=1,background='snow2')
            labRsltPu.insert(tk.INSERT,'kg P ha-1 treatment interval-1')
            labRsltPu.tag_add('resltn1','1.0','1.7')
            labRsltPu.tag_add('resltup1','1.7','1.9')
            labRsltPu.tag_add('resltn2','1.9','1.28')
            labRsltPu.tag_add('resltup2','1.28','1.30')
            labRsltPu.tag_configure('resltn1',font=LARGE_FONT)
            labRsltPu.tag_configure('resltup1',offset=2.5, font=SMALL_FONT)
            labRsltPu.tag_configure('resltn2',font=LARGE_FONT)
            labRsltPu.tag_configure('resltup2',offset=2.5, font=SMALL_FONT)
            labRsltPu.configure(state=tk.DISABLED,borderwidth=-3)
            labRsltPu.grid(row=0,column=1,sticky='w',padx=5,pady=5)

            self.PotRsltLab=ttk.LabelFrame(entFrameMaint,text='Potassium:')
            self.PotRsltLab.grid(row=4,column=1,padx=10,pady=10)
            labRsltK = tk.Text(self.PotRsltLab,width=6,height=1)
            labRsltK.delete(1.0,tk.END)
            labRsltK.insert(tk.INSERT, "%.2f" %round(mk,2))
            labRsltK.tag_add('kmain','1.0','1.10')
            labRsltK.tag_configure('kmain',font=LARGE_FONT)
            labRsltK.configure(state=tk.DISABLED)
            labRsltK.grid(row=0,column=0,sticky='w',padx=5,pady=5)

            labRsltKu = tk.Text(self.PotRsltLab,width=30,height=1,background='snow2')
            labRsltKu.insert(tk.INSERT,'kg K ha-1 treatment interval-1')
            labRsltKu.tag_add('kresltn1','1.0','1.7')
            labRsltKu.tag_add('kresltup1','1.7','1.9')
            labRsltKu.tag_add('kresltn2','1.9','1.28')
            labRsltKu.tag_add('kresltup2','1.28','1.30')
            labRsltKu.tag_configure('kresltn1',font=LARGE_FONT)
            labRsltKu.tag_configure('kresltup1',offset=2.5, font=SMALL_FONT)
            labRsltKu.tag_configure('kresltn2',font=LARGE_FONT)
            labRsltKu.tag_configure('kresltup2',offset=2.5, font=SMALL_FONT)
            labRsltKu.configure(state=tk.DISABLED,borderwidth=-3)
            labRsltKu.grid(row=0,column=1,sticky='w',padx=5,pady=5)

            self.SulRsltLab=ttk.LabelFrame(entFrameMaint,text='Sulphur:')
            self.SulRsltLab.grid(row=4,column=3,padx=10,pady=10)
            labRsltS = tk.Text(self.SulRsltLab,width=6,height=1)
            labRsltS.delete(1.0,tk.END)
            labRsltS.insert(tk.INSERT, "%.2f" %round(ms,2))
            labRsltS.tag_add('smain','1.0','1.10')
            labRsltS.tag_configure('smain',font=LARGE_FONT)
            labRsltS.configure(state=tk.DISABLED)
            labRsltS.grid(row=0,column=0,sticky='w',padx=5,pady=5)

            labRsltSu = tk.Text(self.SulRsltLab,width=30,height=1,background='snow2')
            labRsltSu.insert(tk.INSERT,'kg S ha-1 treatment interval-1')
            labRsltSu.tag_add('sresltn1','1.0','1.7')
            labRsltSu.tag_add('sresltup1','1.7','1.9')
            labRsltSu.tag_add('sresltn2','1.9','1.28')
            labRsltSu.tag_add('sresltup2','1.28','1.30')
            labRsltSu.tag_configure('sresltn1',font=LARGE_FONT)
            labRsltSu.tag_configure('sresltup1',offset=2.5, font=SMALL_FONT)
            labRsltSu.tag_configure('sresltn2',font=LARGE_FONT)
            labRsltSu.tag_configure('sresltup2',offset=2.5, font=SMALL_FONT)
            labRsltSu.configure(state=tk.DISABLED,borderwidth=-3)
            labRsltSu.grid(row=0,column=1,sticky='w',padx=5,pady=5)

##            labRslt.grid(row=4, column=0, columnspan=9, sticky='w', padx=10, pady=10)

        runBtnMaint = ttk.Button(entFrameMaint, text='Run', command=runMaintScenario)
        runBtnMaint.grid(row=2, column=0, columnspan=9, sticky='w', padx=20, pady=20)


# Optimum Treatments Tab

        homeFrameOpt = ttk.Frame(optScenarioTab)
        homeFrameOpt.grid(row=0, column=0,padx=50,pady=50)

        entFrameOpt = ttk.Frame(homeFrameOpt)
        entFrameOpt.grid(row=0, column=0,columnspan=10)


        stockLabOpt = ttk.LabelFrame(entFrameOpt, text='Dry Stock Productivity:')
        stockLabOpt.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='n')

        stockLbl = ttk.Label(stockLabOpt, text='Stock Rate')
        stockLbl.grid(row=0,column=0, sticky='e')

        self.stockVar = tk.StringVar()

        stockEnt = ttk.Entry(stockLabOpt, width=5, textvariable=self.stockVar)
        stockEnt.grid(row=0, column=1)
        self.stockVar.set(18)
        stockLab1 = ttk.Label(stockLabOpt, text='SU per ha')
        stockLab1.grid(row=0, column=2, sticky='w')


##
##        stMilPrcLbl = ttk.Label(stockLabOpt, text='Milk Price')
##        stMilPrcLbl.grid(row=2,column=0, sticky='e')
##
##        self.stMilPrcVar = tk.StringVar()
##
##        stMilPrcEnt = ttk.Entry(stockLabOpt, width=4, textvariable=self.stMilPrcVar)
##        stMilPrcEnt.grid(row=2, column=1)
##        self.stMilPrcVar.set(6)
##        stMilPrcLbl1 = ttk.Label(stockLabOpt, text='$ per kg MS')
##        stMilPrcLbl1.grid(row=2, column=2, sticky='w')

##        stVariLbl = ttk.Label(stockLabOpt, text='Variable Cost')
##        stVariLbl.grid(row=3,column=0, sticky='e')
##
##        self.stVariVar = tk.StringVar()
##
##        stVariEnt = ttk.Entry(stockLabOpt, width=4, textvariable=self.stVariVar)
##        stVariEnt.grid(row=3, column=1)
##        self.stVariVar.set(10)
##        stVariLbl1 = ttk.Label(stockLabOpt, text='$ per SU')
##        stVariLbl1.grid(row=3, column=2, sticky='w')

        drstValLbl = ttk.Label(stockLabOpt, text='Gross Margin')
        drstValLbl.grid(row=1,column=0, sticky='e')
        self.drstGrm = tk.StringVar()

        drstValEnt = ttk.Entry(stockLabOpt, width=5, textvariable=self.drstGrm)
        drstValEnt.grid(row=1, column=1)
        self.drstGrm.set(110)
        drstValLbl1 = ttk.Label(stockLabOpt, text='$ per SU')
        drstValLbl1.grid(row=1, column=2, sticky='w')

        stockPriceLbl = ttk.Label(stockLabOpt, text='Stock Price')
        stockPriceLbl.grid(row=2,column=0, sticky='e')

        self.stockPriceVar = tk.StringVar()

        stockPriceEnt = ttk.Entry(stockLabOpt, width=5, textvariable=self.stockPriceVar)
        stockPriceEnt.grid(row=2, column=1)
        self.stockPriceVar.set(120)
        stockPriceLab1 = ttk.Label(stockLabOpt, text='$ per SU')
        stockPriceLab1.grid(row=2, column=2, sticky='w')

        stockLabOptD = ttk.LabelFrame(entFrameOpt, text='Dairy Productivity:')
        stockLabOptD.grid(row=0, column=3, columnspan=3, padx=10, pady=10, sticky='n')

        stockLblD = ttk.Label(stockLabOptD, text='Stock Rate')
        stockLblD.grid(row=0,column=0, sticky='e')

        self.stockVarD = tk.StringVar()

        stockEntD = ttk.Entry(stockLabOptD, width=5, textvariable=self.stockVarD)
        stockEntD.grid(row=0, column=1)
        self.stockVarD.set(2.5)
        stockLab1D = ttk.Label(stockLabOptD, text='Cows per ha')
        stockLab1D.grid(row=0, column=2, sticky='w')

        stockMilkLblD = ttk.Label(stockLabOptD, text='Milk Production')
        stockMilkLblD.grid(row=1,column=0, sticky='e')

        self.stockMilkVarD = tk.StringVar()

        stockMilkEntD = ttk.Entry(stockLabOptD, width=5, textvariable=self.stockMilkVarD)
        stockMilkEntD.grid(row=1, column=1)
        self.stockMilkVarD.set(900)
        stockMilkLab1D = ttk.Label(stockLabOptD, text='kg MS per ha')
        stockMilkLab1D.grid(row=1, column=2, sticky='w')

        stMilPrcLblD = ttk.Label(stockLabOptD, text='Milk Price')
        stMilPrcLblD.grid(row=2,column=0, sticky='e')

        self.stMilPrcVarD = tk.StringVar()

        stMilPrcEntD = ttk.Entry(stockLabOptD, width=5, textvariable=self.stMilPrcVarD)
        stMilPrcEntD.grid(row=2, column=1)
        self.stMilPrcVarD.set(6)
        stMilPrcLbl1D = ttk.Label(stockLabOptD, text='$ per kg MS')
        stMilPrcLbl1D.grid(row=2, column=2, sticky='w')

        stVariLblD = ttk.Label(stockLabOptD, text='Variable Cost')
        stVariLblD.grid(row=3,column=0, sticky='e')

        self.stVariVarD = tk.StringVar()

        stVariEntD = ttk.Entry(stockLabOptD, width=5, textvariable=self.stVariVarD)
        stVariEntD.grid(row=3, column=1)
        self.stVariVarD.set(400)
        stVariLbl1D = ttk.Label(stockLabOptD, text='$ per Cow')
        stVariLbl1D.grid(row=3, column=2, sticky='w')

        drstValLbl = ttk.Label(stockLabOptD, text="Cow's Value")
        drstValLbl.grid(row=4,column=0, sticky='e')
        self.drstValVar = tk.StringVar()

        drstValEnt = ttk.Entry(stockLabOptD, width=5, textvariable=self.drstValVar)
        drstValEnt.grid(row=4, column=1)
        self.drstValVar.set(1000)
        drstValLbl1 = ttk.Label(stockLabOptD, text='$ per SU')
        drstValLbl1.grid(row=4, column=2, sticky='w')

        

        fertLabOpt = ttk.LabelFrame(entFrameOpt, text='Fertilisers Costs:')
        fertLabOpt.grid(row=0, column=6, columnspan=3, padx=10, pady=10, sticky='n')

        fertPLbl = ttk.Label(fertLabOpt, text='Phosphorus')
        fertPLbl.grid(row=0,column=0, sticky='e')

        self.fertPVar = tk.StringVar()

        fertPEnt = ttk.Entry(fertLabOpt, width=5, textvariable=self.fertPVar)
        fertPEnt.grid(row=0, column=1)
        self.fertPVar.set(3.00)
        fertPLab1 = ttk.Label(fertLabOpt, text='$ per kg P')
        fertPLab1.grid(row=0, column=2, sticky='w')

        fertKLbl = ttk.Label(fertLabOpt, text='Potassium')
        fertKLbl.grid(row=1,column=0, sticky='e')

        self.fertKVar = tk.StringVar()

        fertKEnt = ttk.Entry(fertLabOpt, width=5, textvariable=self.fertKVar)
        fertKEnt.grid(row=1, column=1)
        self.fertKVar.set(1.50)
        fertKLab1 = ttk.Label(fertLabOpt, text='$ per kg K')
        fertKLab1.grid(row=1, column=2, sticky='w')

        fertSLbl = ttk.Label(fertLabOpt, text='Sulphur')
        fertSLbl.grid(row=2,column=0, sticky='e')

        self.fertSVar = tk.StringVar()

        fertSEnt = ttk.Entry(fertLabOpt, width=5, textvariable=self.fertSVar)
        fertSEnt.grid(row=2, column=1)
        self.fertSVar.set(1.00)
        fertSLab1 = ttk.Label(fertLabOpt, text='$ per kg S')
        fertSLab1.grid(row=2, column=2, sticky='w')

        fertApLbl = ttk.Label(fertLabOpt, text='Application Cost')
        fertApLbl.grid(row=3,column=0, sticky='e')

        self.fertApVar = tk.StringVar()

        fertApEnt = ttk.Entry(fertLabOpt, width=5, textvariable=self.fertApVar)
        fertApEnt.grid(row=3, column=1)
        self.fertApVar.set(10.00)
        fertApLab1 = ttk.Label(fertLabOpt, text='$ per ha')
        fertApLab1.grid(row=3, column=2, sticky='w')




        fertConOpt = ttk.LabelFrame(entFrameOpt, text='Constraints:')
        fertConOpt.grid(row=0, column=9, columnspan=3, padx=10, pady=10, sticky='n')

        fertPConLbl = ttk.Label(fertConOpt, text='Phosphorus')
        fertPConLbl.grid(row=0,column=0, sticky='e')

        self.fertPConVar = tk.StringVar()

        fertPConEnt = ttk.Entry(fertConOpt, width=5, textvariable=self.fertPConVar)
        fertPConEnt.grid(row=0, column=1)
        self.fertPConVar.set(60)
        fertPConLab1 = ttk.Label(fertConOpt, text='kg P per ha')
        fertPConLab1.grid(row=0, column=2, sticky='w')

        fertKConLbl = ttk.Label(fertConOpt, text='Potassium')
        fertKConLbl.grid(row=1,column=0, sticky='e')

        self.fertKConVar = tk.StringVar()

        fertKConEnt = ttk.Entry(fertConOpt, width=5, textvariable=self.fertKConVar)
        fertKConEnt.grid(row=1, column=1)
        self.fertKConVar.set(60)
        fertKConLab1 = ttk.Label(fertConOpt, text='kg K per ha')
        fertKConLab1.grid(row=1, column=2, sticky='w')

        fertSConLbl = ttk.Label(fertConOpt, text='Sulphur')
        fertSConLbl.grid(row=2,column=0, sticky='e')

        self.fertSConVar = tk.StringVar()

        fertSConEnt = ttk.Entry(fertConOpt, width=5, textvariable=self.fertSConVar)
        fertSConEnt.grid(row=2, column=1)
        self.fertSConVar.set(60)
        fertSConLab1 = ttk.Label(fertConOpt, text='kg S per ha')
        fertSConLab1.grid(row=2, column=2, sticky='w')

        tprLbl = ttk.Label(fertConOpt, text='TPR')
        tprLbl.grid(row=3,column=0, sticky='e')

        self.tprVar = tk.StringVar()

        tprEnt = ttk.Entry(fertConOpt, width=5, textvariable=self.tprVar)
        tprEnt.grid(row=3, column=1)
        self.tprVar.set(5.0)
        tprLab1 = ttk.Label(fertConOpt, text='%')
        tprLab1.grid(row=3, column=2, sticky='w')

        resFrameOpt = ttk.Frame(homeFrameOpt)
        resFrameOpt.grid(row=1, column=0,rowspan=2)

        self.tframe = ttk.Frame(homeFrameOpt)
        self.tframe.grid(row=3,column=0)

        self.npvframe = ttk.LabelFrame(homeFrameOpt, text='Net Present Value:')
        self.npvframe.grid(row=1,column=8,columnspan=2,padx=5,pady=5)

        labbbUsrlab = ttk.Label(self.npvframe, text='User defined')
        labbbUsrlab.grid(row=0, column=0, padx=5,sticky='e')

        self.labbbUsrVar = tk.StringVar()
        labbbUsr = ttk.Label(self.npvframe, textvariable=self.labbbUsrVar)
        labbbUsr.grid(row=0, column=1, padx=5,sticky='w')

        labbbZerlab = ttk.Label(self.npvframe, text='Zero')
        labbbZerlab.grid(row=1, column=0, padx=5,sticky='e')

        self.labbbZerVar = tk.StringVar()
        labbbZer = ttk.Label(self.npvframe, textvariable=self.labbbZerVar)
        labbbZer.grid(row=1, column=1, padx=5,sticky='w')

        labbbmailab = ttk.Label(self.npvframe, text='Maintenance')
        labbbmailab.grid(row=2, column=0, padx=5,sticky='e')

        self.labbbMaiVar = tk.StringVar()
        labbbMai = ttk.Label(self.npvframe, textvariable=self.labbbMaiVar)
        labbbMai.grid(row=2, column=1, padx=5,sticky='w')

        labbbOptlab = ttk.Label(self.npvframe, text='Optimized')
        labbbOptlab.grid(row=3, column=0, padx=5,sticky='e')

        self.labbbOptVar = tk.StringVar()
        labbbOpt = ttk.Label(self.npvframe, textvariable=self.labbbOptVar)
        labbbOpt.grid(row=3, column=1, padx=5,sticky='w')

        self.irrframe = ttk.LabelFrame(homeFrameOpt, text='Internal Rate of Return:')
        self.irrframe.grid(row=2,column=8,columnspan=2,padx=5,pady=5)

        laBBUsrlab = ttk.Label(self.irrframe, text='User defined')
        laBBUsrlab.grid(row=0, column=0, padx=5,sticky='e')

        self.laBBUsrVar = tk.StringVar()
        laBBUsr = ttk.Label(self.irrframe, textvariable=self.laBBUsrVar)
        laBBUsr.grid(row=0, column=1, padx=5,sticky='w')

        laBBZerlab = ttk.Label(self.irrframe, text='Zero')
        laBBZerlab.grid(row=1, column=0, padx=5,sticky='e')

        self.laBBZerVar = tk.StringVar()
        laBBZer = ttk.Label(self.irrframe, textvariable=self.laBBZerVar)
        laBBZer.grid(row=1, column=1, padx=5,sticky='w')

        laBBmailab = ttk.Label(self.irrframe, text='Maintenance')
        laBBmailab.grid(row=2, column=0, padx=5,sticky='e')

        self.laBBMaiVar = tk.StringVar()
        laBBMai = ttk.Label(self.irrframe, textvariable=self.laBBMaiVar)
        laBBMai.grid(row=2, column=1, padx=5,sticky='w')
        def runOPtAlgo():
            if self.pTypeVar.get() == 'Sedimentary':
                ryConsts = np.array((104.61,0,2.60),dtype=float)
            elif self.pTypeVar.get() == 'Volcanic':
                ryConsts = np.array((108.60,10.44,17.22),dtype=float)
            elif self.pTypeVar.get() == 'Pumice':
                ryConsts = np.array((106.60,15.52,23.41),dtype=float)
            elif self.pTypeVar.get() == 'Recent':
                ryConsts = np.array((105.00,28.49,34.75),dtype=float)
            elif self.pTypeVar.get() == 'Podzols':
                ryConsts = np.array((199.91,107.42,255.51),dtype=float)
            elif self.pTypeVar.get() == 'Sands':
                ryConsts = np.array((105.48,0.00,1.40),dtype=float)
            
            try:
                Pstart = P0
            except NameError:
                Pstart = float(self.pvar.get())

            tpr = float(self.tprVar.get())/100
            alphaE = 1/(1 + tpr)

            par = self.boxplotsPars.paR() 
            TFertOpt = np.arange(nextTrtmnt,nextTrtmnt+10*365,365)
            
            STdate = float(self.dvar.get()) - 1 + (float(self.mvar.get()) - 1) * 30 + (float(self.yvar.get())) * 365.0
            tt = np.linspace(STdate,TToday+365*10,1000)
            if self.farmVar.get() == 'Dairy':
                gmsu = float(self.stockMilkVarD.get()) * float(self.stMilPrcVarD.get()) - float(self.stockVarD.get())*float(self.stVariVarD.get())
                valueStock=float(self.drstValVar.get())
            else:
                gmsu = float(self.drstGrm.get())
                valueStock = float(self.stockPriceVar.get())

            def OptiMisation(x):
                pp = runOptimum.ff(tt, Pstart, par[0], par[3], x, tt[0], TFertOpt)
                np.clip(pp,0.0,45.0,pp)
##                pp = pp.clip(max=20)
                ryPP = runOptimum.rYieldFunc(tt,pp,ryConsts)
                costP = float(self.fertPVar.get())/3
                costSpread = float(self.fertApVar.get())

                A=[]

                for i in range(10):
                    indexSt = np.argmax(tt >= TToday + 365*i)
                    indexFh = np.argmax(tt >= TToday + 365*(i+1))
                    B = ryPP[indexSt:indexFh]
                    A = np.append(A,np.average(B))
                if self.farmVar.get() == 'Dairy':
                    PotstockRate = 100 * float(self.stockVarD.get())/ryPP[np.argmax(tt >= TToday)]
                else:
                    PotstockRate = 100 * float(self.stockVar.get())/ryPP[np.argmax(tt >= TToday)]

                Term = np.zeros(10)

                for i in range(10):
                    if i == 0:
                        Term[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRate * A[i]/100 - costP * x[i] - costSpread)
                    else:
                        Term[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRate * A[i]/100 - costP * x[i] - PotstockRate * (A[i] - A[i-1]) * valueStock/100 - costSpread)
                NPV = sum(Term) + np.power(alphaE,10)*(costP*(pp[-1]-15)/par[3] + valueStock*PotstockRate*A[-1]/100)
                return -1 * NPV
            try:
                Kstart = K0
            except NameError:
                Kstart = float(self.kvar.get())
            
            def OptiMisationK(x):
                kk = runOptimum.ff(tt, Kstart, par[1], par[4], x, tt[0], TFertOpt)
                ryKK = runOptimum.rYieldFunc(tt,kk,ryKConsts)
                costK = float(self.fertKVar.get())/3
                costSpread = float(self.fertApVar.get())

                A=[]
                for i in range(10):
                    indexSt = np.argmax(tt >= TToday + 365*i)
                    indexFh = np.argmax(tt >= TToday + 365*(i+1))
                    B = ryKK[indexSt:indexFh]
                    A = np.append(A,np.average(B))

                if self.farmVar.get() == 'Dairy':
                    PotstockRate = 100*float(self.stockVarD.get())/ryKK[np.argmax(tt >= TToday)]
                else:
                    PotstockRate = 100*float(self.stockVarD.get())/ryKK[np.argmax(tt >= TToday)]

                Term = np.zeros(10)

                for i in range(10):
                    if i == 0:
                        Term[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRate * A[i]/100 - costK * x[i] - costSpread)
                    else:
                        Term[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRate * A[i]/100 - costK * x[i] - PotstockRate * (A[i] - A[i-1]) * valueStock/100 - costSpread)
                NPV = sum(Term) + np.power(alphaE,10)*(costK*(kk[-1]-2)/par[4] + valueStock*PotstockRate*A[-1]/100)
                return -1 * NPV

            try:
                Sstart = S0
            except NameError:
                Sstart = float(self.svar.get())

            def OptiMisationS(x):
                ss = runOptimum.ff(tt, Sstart, par[2], par[5], x, tt[0], TFertOpt)
                if self.sTypeVar.get() == 'Semi-arid':
                    ss = ss.clip(max=7.0)
                elif self.sTypeVar.get() == 'Pallic':
                    ss = ss.clip(max=15.0)
                elif self.sTypeVar.get() == 'Recent':
                    ss = ss.clip(max=18.0)
                elif self.sTypeVar.get() == 'Brown':
                    ss = ss.clip(max=19.0)
                elif self.sTypeVar.get() == 'Pumice':
                    ss = ss.clip(max=27.0)
                elif self.sTypeVar.get() == 'Allophane':
                    ss = ss.clip(max=40.0)
                elif self.sTypeVar.get() == 'Organic':
                    ss = ss.clip(max=87.0)
                    
                rySS = runOptimum.rYieldFunc(tt,ss,rySConsts)
                costS = float(self.fertSVar.get())/3
                costSpread = float(self.fertApVar.get())

                A=[]
                for i in range(10):
                    indexSt = np.argmax(tt >= TToday + 365*i)
                    indexFh = np.argmax(tt >= TToday + 365*(i+1))
                    B = rySS[indexSt:indexFh]
                    A = np.append(A,np.average(B))

                if self.farmVar.get() == 'Dairy':
                    PotstockRate = 100*float(self.stockVarD.get())/rySS[np.argmax(tt >= TToday)]
                else:
                    PotstockRate = 100*float(self.stockVar.get())/rySS[np.argmax(tt >= TToday)]

                Term = np.zeros(10)

                for i in range(10):
                    if i == 0:
                        Term[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRate * A[i]/100 - costS * x[i] - costSpread)
                    else:
                        Term[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRate * A[i]/100 - costS * x[i] - PotstockRate * (A[i] - A[i-1]) * valueStock/100 - costSpread)
                NPV = sum(Term) + np.power(alphaE,10)*(costS*(ss[-1]-2)/par[5] + valueStock*PotstockRate*A[-1]/100)
                return -1 * NPV

            pL = float(self.fertPConVar.get())
            kL = float(self.fertKConVar.get())
            sL = float(self.fertSConVar.get())
            x0 = np.ones(10)
            myboundsP = [(0,pL),(0,pL),(0,pL),(0,pL),(0,pL),(0,pL),(0,pL),(0,pL),(0,pL),(0,pL)]
            myboundsK = [(0,kL),(0,kL),(0,kL),(0,kL),(0,kL),(0,kL),(0,kL),(0,kL),(0,kL),(0,kL)]
            myboundsS = [(0,sL),(0,sL),(0,sL),(0,sL),(0,sL),(0,sL),(0,sL),(0,sL),(0,sL),(0,sL)]
            resP = minimize(OptiMisation, x0, method='L-BFGS-B',bounds=myboundsP)
            resK = minimize(OptiMisationK, x0, method='L-BFGS-B',bounds=myboundsK)
            resS = minimize(OptiMisationS, x0, method='L-BFGS-B',bounds=myboundsS)

            fig4 = Figure(figsize=(12,4), dpi=70)
            a4 = fig4.add_subplot(231)
            a4.axes.get_xaxis().set_ticks([])
            a4.set_ylabel('Olsen P')
            b4 = fig4.add_subplot(234)
            b4.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            b4.set_ylabel('RY')
            b4.set_xlabel('Years')

            c4 = fig4.add_subplot(232)
            c4.axes.get_xaxis().set_ticks([])
            c4.set_ylabel('QTK')
            d4 = fig4.add_subplot(235)
            d4.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            d4.set_ylabel('RY')
            d4.set_xlabel('Years')

            e4 = fig4.add_subplot(233)
            e4.axes.get_xaxis().set_ticks([])
            e4.set_ylabel('EOS')
            f4 = fig4.add_subplot(236)
            f4.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0f'))
            f4.set_ylabel('RY')
            f4.set_xlabel('Years')

            global AoptP
            global AoptK
            global AoptS
            global PoptEnd
            global KoptEnd
            global KoptEnd
            global AoptP0
            global AoptK0
            global AoptS0

            try:
                t1 = np.linspace(TObs[0],TFert[-1]+1, 300)
                t2 = np.linspace(TFert[-1]+1, TToday+365*10, 500)
                p1 = runOptimum.ff(t1, P0, par[0], par[3], MassP, TObs[0], TFert)
                ryP1 = runOptimum.rYieldFunc(t1,p1,ryConsts)
                p2 = runOptimum.ff(t2, p1[-1], par[0], par[3], resP.x, t2[0], TFertOpt)
                ryP2 = runOptimum.rYieldFunc(t2,p2,ryConsts)
                k1 = runOptimum.ff(t1, K0, par[1], par[4], MassK, TObs[0], TFert)
                ryK1 = runOptimum.rYieldFunc(t1,k1,ryKConsts)
                k2 = runOptimum.ff(t2, k1[-1], par[1], par[4], resK.x, t2[0], TFertOpt)
                ryK2 = runOptimum.rYieldFunc(t2,k2,ryKConsts)
                s1 = runOptimum.ff(t1, S0, par[2], par[5], MassS, TObs[0], TFert)
                ryS1 = runOptimum.rYieldFunc(t1,s1,rySConsts)
                s2 = runOptimum.ff(t2, s1[-1], par[2], par[5], resS.x, t2[0], TFertOpt)
                ryS2 = runOptimum.rYieldFunc(t2,s2,rySConsts)
                PoptEnd=p2[-1]
                KoptEnd=k2[-1]
                SoptEnd=s2[-1]

                
                AoptP=[]
                AoptK=[]
                AoptS=[]
                for i in range(10):
                    indexSt = np.argmax(t2 >= TToday + 365*i)
                    indexFh = np.argmax(t2 >= TToday + 365*(i+1))
                    BoptP = ryP2[indexSt:indexFh]
                    AoptP = np.append(AoptP,np.average(BoptP))
                    BoptK = ryK2[indexSt:indexFh]
                    AoptK = np.append(AoptK,np.average(BoptK))
                    BoptS = ryS2[indexSt:indexFh]
                    AoptS = np.append(AoptS,np.average(BoptS))
                AoptP0 = ryP2[np.argmax(t2 >= TToday)]
                AoptK0 = ryK2[np.argmax(t2 >= TToday)]
                AoptS0 = ryS2[np.argmax(t2 >= TToday)]
                
                a4.plot(t1/365, p1,t2/365,p2)
                a4.axis([TObs[0]/365,TToday/365+10.3,0,max(max(p1),max(p2))+5])
                c4.plot(t1/365, k1,t2/365,k2)
                c4.axis([TObs[0]/365,TToday/365+10.3,0,max(max(k1),max(k2))+5])
                e4.plot(t1/365, s1,t2/365,s2)
                e4.axis([TObs[0]/365,TToday/365+10.3,0,max(max(s1),max(s2))+5])
                b4.plot(t1/365, ryP1,t2/365,ryP2)
                b4.axis([TObs[0]/365,TToday/365+10.3,min(min(ryP1),min(ryP2))-5,102])
                d4.plot(t1/365, ryK1,t2/365,ryK2)
                d4.axis([TObs[0]/365,TToday/365+10.3,min(min(ryK1),min(ryK2))-5,102])
                f4.plot(t1/365, ryS1,t2/365,ryS2)
                f4.axis([TObs[0]/365,TToday/365+10.3,min(min(ryS1),min(ryS2))-5,102])
            except NameError:
                t = np.linspace(STdate, TToday + 365 * 10, 500)
                p = runOptimum.ff(t, float(self.pvar.get()), par[0], par[3], resP.x, t[0], TFertOpt)
                ryP = runOptimum.rYieldFunc(t,p,ryConsts)
                k = runOptimum.ff(t, float(self.kvar.get()), par[1], par[4], resK.x, t[0], TFertOpt)
                ryK = runOptimum.rYieldFunc(t,k,ryKConsts)
                s = runOptimum.ff(t, float(self.svar.get()), par[2], par[5], resS.x, t[0], TFertOpt)
                ryS = runOptimum.rYieldFunc(t,s,rySConsts)

                PoptEnd=p[-1]
                KoptEnd=k[-1]
                SoptEnd=s[-1]

                AoptP=[]
                AoptK=[]
                AoptS=[]

                for i in range(10):
                    indexSt = np.argmax(t >= TToday + 365*i)
                    indexFh = np.argmax(t >= TToday + 365*(i+1))
                    BoptP = ryP[indexSt:indexFh]
                    AoptP = np.append(AoptP,np.average(BoptP))
                    BoptK = ryK[indexSt:indexFh]
                    AoptK = np.append(AoptK,np.average(BoptK))
                    BoptS = ryS[indexSt:indexFh]
                    AoptS = np.append(AoptS,np.average(BoptS))

                AoptP0 = ryP[np.argmax(t >= TToday)]
                AoptK0 = ryK[np.argmax(t >= TToday)]
                AoptS0 = ryS[np.argmax(t >= TToday)]

                a4.plot(t/365, p)
                a4.axis([t[0]/365,TToday/365+10.3,0,max(p)+5])
                c4.plot(t/365, k)
                c4.axis([t[0]/365,TToday/365+10.3,0,max(k)+5])
                e4.plot(t/365, s)
                e4.axis([t[0]/365,TToday/365+10.3,0,max(s)+5])
                b4.plot(t/365, ryP)
                b4.axis([t[0]/365,TToday/365+10.3,min(ryP)-5,102])
                d4.plot(t/365, ryK)
                d4.axis([t[0]/365,TToday/365+10.3,min(ryK)-5,102])
                f4.plot(t/365, ryS)
                f4.axis([t[0]/365,TToday/365+10.3,min(ryS)-5,102])
            
            self.canvas = FigureCanvasTkAgg(fig4, resFrameOpt)
            self.canvas.show()
            self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=1, padx=10, pady=3, sticky='nsew')


            labbP = ttk.Label(self.tframe, text='Phosphorus')
            labbK = ttk.Label(self.tframe, text='Potassium')
            labbS = ttk.Label(self.tframe, text='Sulphur')
            labbP.grid(row=0, column=0, padx=15,sticky='e')
            labbK.grid(row=1, column=0, padx=15,sticky='e')
            labbS.grid(row=2, column=0, padx=15,sticky='e')
            self.entP1Var = tk.StringVar()
            self.entP2Var = tk.StringVar()
            self.entP3Var = tk.StringVar()
            self.entP4Var = tk.StringVar()
            self.entP5Var = tk.StringVar()
            self.entP6Var = tk.StringVar()
            self.entP7Var = tk.StringVar()
            self.entP8Var = tk.StringVar()
            self.entP9Var = tk.StringVar()
            self.entP10Var = tk.StringVar()
            self.entP1 = ttk.Label(self.tframe,textvariable=self.entP1Var)
            self.entP2 = ttk.Label(self.tframe,textvariable=self.entP2Var)
            self.entP3 = ttk.Label(self.tframe,textvariable=self.entP3Var)
            self.entP4 = ttk.Label(self.tframe,textvariable=self.entP4Var)
            self.entP5 = ttk.Label(self.tframe,textvariable=self.entP5Var)
            self.entP6 = ttk.Label(self.tframe,textvariable=self.entP6Var)
            self.entP7 = ttk.Label(self.tframe,textvariable=self.entP7Var)
            self.entP8 = ttk.Label(self.tframe,textvariable=self.entP8Var)
            self.entP9 = ttk.Label(self.tframe,textvariable=self.entP9Var)
            self.entP10 = ttk.Label(self.tframe,textvariable=self.entP10Var)
            self.entP1.grid(row=0, column=1, padx=15)
            self.entP2.grid(row=0, column=2, padx=15)
            self.entP3.grid(row=0, column=3, padx=15)
            self.entP4.grid(row=0, column=4, padx=15)
            self.entP5.grid(row=0, column=5, padx=15)
            self.entP6.grid(row=0, column=6, padx=15)
            self.entP7.grid(row=0, column=7, padx=15)
            self.entP8.grid(row=0, column=8, padx=15)
            self.entP9.grid(row=0, column=9, padx=15)
            self.entP10.grid(row=0, column=10, padx=15)
            self.entP1Var.set('{0:.1f}'.format(resP.x[0]))
            self.entP2Var.set('{0:.1f}'.format(resP.x[1]))
            self.entP3Var.set('{0:.1f}'.format(resP.x[2]))
            self.entP4Var.set('{0:.1f}'.format(resP.x[3]))
            self.entP5Var.set('{0:.1f}'.format(resP.x[4]))
            self.entP6Var.set('{0:.1f}'.format(resP.x[5]))
            self.entP7Var.set('{0:.1f}'.format(resP.x[6]))
            self.entP8Var.set('{0:.1f}'.format(resP.x[7]))
            self.entP9Var.set('{0:.1f}'.format(resP.x[8]))
            self.entP10Var.set('{0:.1f}'.format(resP.x[9]))


            self.entK1Var = tk.StringVar()
            self.entK2Var = tk.StringVar()
            self.entK3Var = tk.StringVar()
            self.entK4Var = tk.StringVar()
            self.entK5Var = tk.StringVar()
            self.entK6Var = tk.StringVar()
            self.entK7Var = tk.StringVar()
            self.entK8Var = tk.StringVar()
            self.entK9Var = tk.StringVar()
            self.entK10Var = tk.StringVar()
            self.entK1 = ttk.Label(self.tframe,textvariable=self.entK1Var)
            self.entK2 = ttk.Label(self.tframe,textvariable=self.entK2Var)
            self.entK3 = ttk.Label(self.tframe,textvariable=self.entK3Var)
            self.entK4 = ttk.Label(self.tframe,textvariable=self.entK4Var)
            self.entK5 = ttk.Label(self.tframe,textvariable=self.entK5Var)
            self.entK6 = ttk.Label(self.tframe,textvariable=self.entK6Var)
            self.entK7 = ttk.Label(self.tframe,textvariable=self.entK7Var)
            self.entK8 = ttk.Label(self.tframe,textvariable=self.entK8Var)
            self.entK9 = ttk.Label(self.tframe,textvariable=self.entK9Var)
            self.entK10 = ttk.Label(self.tframe,textvariable=self.entK10Var)
            self.entK1.grid(row=1, column=1, padx=15)
            self.entK2.grid(row=1, column=2, padx=15)
            self.entK3.grid(row=1, column=3, padx=15)
            self.entK4.grid(row=1, column=4, padx=15)
            self.entK5.grid(row=1, column=5, padx=15)
            self.entK6.grid(row=1, column=6, padx=15)
            self.entK7.grid(row=1, column=7, padx=15)
            self.entK8.grid(row=1, column=8, padx=15)
            self.entK9.grid(row=1, column=9, padx=15)
            self.entK10.grid(row=1, column=10, padx=15)
            self.entK1Var.set('{0:.1f}'.format(resK.x[0]))
            self.entK2Var.set('{0:.1f}'.format(resK.x[1]))
            self.entK3Var.set('{0:.1f}'.format(resK.x[2]))
            self.entK4Var.set('{0:.1f}'.format(resK.x[3]))
            self.entK5Var.set('{0:.1f}'.format(resK.x[4]))
            self.entK6Var.set('{0:.1f}'.format(resK.x[5]))
            self.entK7Var.set('{0:.1f}'.format(resK.x[6]))
            self.entK8Var.set('{0:.1f}'.format(resK.x[7]))
            self.entK9Var.set('{0:.1f}'.format(resK.x[8]))
            self.entK10Var.set('{0:.1f}'.format(resK.x[9]))

            self.entS1Var = tk.StringVar()
            self.entS2Var = tk.StringVar()
            self.entS3Var = tk.StringVar()
            self.entS4Var = tk.StringVar()
            self.entS5Var = tk.StringVar()
            self.entS6Var = tk.StringVar()
            self.entS7Var = tk.StringVar()
            self.entS8Var = tk.StringVar()
            self.entS9Var = tk.StringVar()
            self.entS10Var = tk.StringVar()
            self.entS1 = ttk.Label(self.tframe,textvariable=self.entS1Var)
            self.entS2 = ttk.Label(self.tframe,textvariable=self.entS2Var)
            self.entS3 = ttk.Label(self.tframe,textvariable=self.entS3Var)
            self.entS4 = ttk.Label(self.tframe,textvariable=self.entS4Var)
            self.entS5 = ttk.Label(self.tframe,textvariable=self.entS5Var)
            self.entS6 = ttk.Label(self.tframe,textvariable=self.entS6Var)
            self.entS7 = ttk.Label(self.tframe,textvariable=self.entS7Var)
            self.entS8 = ttk.Label(self.tframe,textvariable=self.entS8Var)
            self.entS9 = ttk.Label(self.tframe,textvariable=self.entS9Var)
            self.entS10 = ttk.Label(self.tframe,textvariable=self.entS10Var)
            self.entS1.grid(row=2, column=1, padx=15)
            self.entS2.grid(row=2, column=2, padx=15)
            self.entS3.grid(row=2, column=3, padx=15)
            self.entS4.grid(row=2, column=4, padx=15)
            self.entS5.grid(row=2, column=5, padx=15)
            self.entS6.grid(row=2, column=6, padx=15)
            self.entS7.grid(row=2, column=7, padx=15)
            self.entS8.grid(row=2, column=8, padx=15)
            self.entS9.grid(row=2, column=9, padx=15)
            self.entS10.grid(row=2, column=10, padx=15)
            self.entS1Var.set('{0:.1f}'.format(resS.x[0]))
            self.entS2Var.set('{0:.1f}'.format(resS.x[1]))
            self.entS3Var.set('{0:.1f}'.format(resS.x[2]))
            self.entS4Var.set('{0:.1f}'.format(resS.x[3]))
            self.entS5Var.set('{0:.1f}'.format(resS.x[4]))
            self.entS6Var.set('{0:.1f}'.format(resS.x[5]))
            self.entS7Var.set('{0:.1f}'.format(resS.x[6]))
            self.entS8Var.set('{0:.1f}'.format(resS.x[7]))
            self.entS9Var.set('{0:.1f}'.format(resS.x[8]))
            self.entS10Var.set('{0:.1f}'.format(resS.x[9]))

            labbbP = ttk.Label(self.tframe, text='kg per ha')
            labbbK = ttk.Label(self.tframe, text='kg per ha')
            labbbS = ttk.Label(self.tframe, text='kg per ha')
            labbbP.grid(row=0, column=11, padx=15,sticky='w')
            labbbK.grid(row=1, column=11, padx=15,sticky='w')
            labbbS.grid(row=2, column=11, padx=15,sticky='w')

            PotstockRateP = 100*float(self.stockVar.get())/AoptP0
            PotstockRateK = 100*float(self.stockVar.get())/AoptK0
            PotstockRateS = 100*float(self.stockVar.get())/AoptS0

            PotstockRateUsrP = 100*float(self.stockVar.get())/AusrP0
            PotstockRateUsrK = 100*float(self.stockVar.get())/AusrK0
            PotstockRateUsrS = 100*float(self.stockVar.get())/AusrS0

            PotstockRatezerP = 100*float(self.stockVar.get())/AzerP0
            PotstockRatezerK = 100*float(self.stockVar.get())/AzerK0
            PotstockRatezerS = 100*float(self.stockVar.get())/AzerS0

            PotstockRatemaiP = 100*float(self.stockVar.get())/AmaiP0
            PotstockRatemaiK = 100*float(self.stockVar.get())/AmaiK0
            PotstockRatemaiS = 100*float(self.stockVar.get())/AmaiS0

            costP = float(self.fertPVar.get())
            costK = float(self.fertKVar.get())
            costS = float(self.fertSVar.get())
            costSpread = float(self.fertApVar.get())
            TermP= np.zeros(10)
            TermK=np.zeros(10)
            TermS=np.zeros(10)

            TermUsrP= np.zeros(10)
            TermUsrK= np.zeros(10)
            TermUsrS= np.zeros(10)

            TermZerP= np.zeros(10)
            TermZerK= np.zeros(10)
            TermZerS= np.zeros(10)

            TermMaiP= np.zeros(10)
            TermMaiK= np.zeros(10)
            TermMaiS= np.zeros(10)

            maSS = self.tableFrame.getVal()
            maSSP,maSSK,maSSS=np.zeros(10),np.zeros(10),np.zeros(10)
            for i in range(10):
                maSSP[i] = maSS[1][2*i]+maSS[1][2*i+1]
                maSSK[i] = maSS[2][2*i]+maSS[2][2*i+1]
                maSSS[i] = maSS[3][2*i]+maSS[3][2*i+1]
            for i in range(10):
                if i == 0:
                    TermP[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRateP * AoptP[i]/100 - costP * resP.x[i] - costSpread)
                    TermK[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRateK * AoptK[i]/100 - costK * resK.x[i] - costSpread)
                    TermS[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRateS * AoptS[i]/100 - costS * resS.x[i] - costSpread)
                    TermUsrP[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRateUsrP * AusrP[i]/100 - costP * maSSP[i] - costSpread)
                    TermUsrK[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRateUsrK * AusrK[i]/100 - costK * maSSK[i] - costSpread)
                    TermUsrS[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRateUsrS * AusrS[i]/100 - costS * maSSS[i] - costSpread)
                    TermZerP[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRatezerP * AzerP[i]/100)
                    TermZerK[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRatezerK * AzerK[i]/100)
                    TermZerS[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRatezerS * AzerS[i]/100)
                    TermMaiP[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRatemaiP * AmaiP[i]/100 - costP * mp - costSpread)
                    TermMaiK[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRatemaiK * AmaiK[i]/100 - costK * mk - costSpread)
                    TermMaiS[i] = np.power(alphaE,i) * (alphaE * gmsu * PotstockRatemaiS * AmaiS[i]/100 - costS * ms - costSpread)
                else:
                    TermP[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRateP * AoptP[i]/100 - costP * resP.x[i] - PotstockRateP * (AoptP[i] - AoptP[i-1]) * valueStock/100 - costSpread)
                    TermK[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRateK * AoptK[i]/100 - costK * resK.x[i] - PotstockRateK * (AoptK[i] - AoptK[i-1]) * valueStock/100 - costSpread)
                    TermS[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRateS * AoptS[i]/100 - costS * resS.x[i] - PotstockRateS * (AoptS[i] - AoptS[i-1]) * valueStock/100 - costSpread)
                    TermUsrP[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRateUsrP * AusrP[i]/100 - costP * maSSP[i] - PotstockRateUsrP * (AusrP[i] - AusrP[i-1]) * valueStock/100 - costSpread)
                    TermUsrK[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRateUsrK * AusrK[i]/100 - costK * maSSK[i] - PotstockRateUsrK * (AusrK[i] - AusrK[i-1]) * valueStock/100 - costSpread)
                    TermUsrS[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRateUsrS * AusrS[i]/100 - costS * maSSS[i] - PotstockRateUsrS * (AusrS[i] - AusrS[i-1]) * valueStock/100 - costSpread)
                    TermZerP[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRatezerP * AzerP[i]/100 - PotstockRatezerP * (AzerP[i] - AzerP[i-1]) * valueStock/100)
                    TermZerK[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRatezerK * AzerK[i]/100 - PotstockRatezerK * (AzerK[i] - AzerK[i-1]) * valueStock/100)
                    TermZerS[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRatezerS * AzerS[i]/100 - PotstockRatezerS * (AzerS[i] - AzerS[i-1]) * valueStock/100)
                    TermMaiP[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRatemaiP * AmaiP[i]/100 - costP * mp - PotstockRatemaiP * (AmaiP[i] - AmaiP[i-1]) * valueStock/100 - costSpread)
                    TermMaiK[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRatemaiK * AmaiK[i]/100 - costK * mk - PotstockRatemaiK * (AmaiK[i] - AmaiK[i-1]) * valueStock/100 - costSpread)
                    TermMaiS[i] = np.power(alphaE,i) * alphaE * (gmsu * PotstockRatemaiS * AmaiS[i]/100 - costS * ms - PotstockRatemaiS * (AmaiS[i] - AmaiS[i-1]) * valueStock/100 - costSpread)

            PNPV = np.power(alphaE,10)*(costP*(PoptEnd-15)/par[3] + valueStock*PotstockRateP*AoptP[-1]/100)
            KNPV = np.power(alphaE,10)*(costK*(KoptEnd-2)/par[4] + valueStock*PotstockRateK*AoptK[-1]/100)
            SNPV = np.power(alphaE,10)*(costS*(SoptEnd-2)/par[5] + valueStock*PotstockRateS*AoptS[-1]/100)
            NPV = (sum(TermP)+sum(TermK)+sum(TermS)+PNPV+KNPV+SNPV)/3
            PNPVusr = np.power(alphaE,10)*(costP*(PusrEnd-15)/par[3] + valueStock*PotstockRateUsrP*AusrP[-1]/100)
            KNPVusr = np.power(alphaE,10)*(costK*(KusrEnd-2)/par[4] + valueStock*PotstockRateUsrK*AusrK[-1]/100)
            SNPVusr = np.power(alphaE,10)*(costS*(SusrEnd-2)/par[5] + valueStock*PotstockRateUsrS*AusrS[-1]/100)
            NPVusr = (sum(TermUsrP)+sum(TermUsrK)+sum(TermUsrS)+PNPVusr+SNPVusr+KNPVusr)/3
            PNPVzer = np.power(alphaE,10)*(costP*(PzerEnd-15)/par[3] + valueStock*PotstockRatezerP*AzerP[-1]/100)
            KNPVzer = np.power(alphaE,10)*(costK*(KzerEnd-2)/par[4] + valueStock*PotstockRatezerK*AzerK[-1]/100)
            SNPVzer = np.power(alphaE,10)*(costS*(SzerEnd-2)/par[5] + valueStock*PotstockRatezerS*AzerS[-1]/100)
            NPVzer = (sum(TermZerP)+sum(TermZerK)+sum(TermZerS)+PNPVzer+KNPVzer+SNPVzer)/3
            PNPVmai = np.power(alphaE,10)*(costP*(PmaiEnd-15)/par[3] + valueStock*PotstockRatemaiP*AmaiP[-1]/100)
            KNPVmai = np.power(alphaE,10)*(costK*(KmaiEnd-2)/par[4] + valueStock*PotstockRatemaiK*AmaiK[-1]/100)
            SNPVmai = np.power(alphaE,10)*(costS*(SmaiEnd-2)/par[5] + valueStock*PotstockRatemaiS*AmaiS[-1]/100)
            NPVmai = (sum(TermMaiP)+sum(TermMaiK)+sum(TermMaiS)+PNPVmai+KNPVmai+SNPVmai)/3


            self.labbbUsrVar.set('$'+str(int(NPVusr)))
            self.labbbZerVar.set('$'+str(int(NPVzer)))
            self.labbbMaiVar.set('$'+str(int(NPVmai)))
            self.labbbOptVar.set('$'+str(int(NPV)))

            self.laBBUsrVar.set(str(round(100 * NPV/NPVusr,1))+'  %')
            self.laBBZerVar.set(str(round(100 * NPV/NPVzer,1))+'  %')
            self.laBBMaiVar.set(str(round(100 * NPV/NPVmai,1))+'  %')



            
        self.runOptScenar = ttk.Button(entFrameOpt, text='Run', command=runOPtAlgo)
        self.runOptScenar.grid(row=1,column=0,columnspan=9,pady=3)

        
            

        
app = AgSoft()

app.geometry("1200x720")
app.mainloop()


