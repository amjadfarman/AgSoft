
import numpy as np
from scipy.optimize import minimize


def u(x):
    if np.size(x) == 1 and x < 0:
        return 0
    elif np.size(x) == 1 and x==0:
        return 0.5
    elif np.size(x) == 1 and x > 0:
        return 1
    elif np.size(x) > 1:
        out = np.zeros(np.shape(x))
        for i in range(0, np.size(x)):
            if x[i] < 0:
                out[i] = 0.
            elif x[i] == 0:
                out[i] = 0.5
            elif x[i] > 0:
                out[i] = 1.0
        return out

def backGfunc(c, m, t, T, alpha):
    return c * m * u(t - T) * np.exp(-alpha * (t - T))


def f(t, P0, alpha, c, m, T1, period):
    secs = int((t[-1] - T1)/period) + 1
    a0 = P0 * np.exp(-alpha * (t - t[0]))
    a = np.zeros((secs, np.size(t)))
    for i in np.arange(0, secs):
        a[i, :] = backGfunc(c, m[i], t - t[0], T1 + i * period - t[0], alpha)
    return a0 + np.sum(a, axis=0)

def ff(t, P0, alpha, c, m, T0, TFert):
    a0 = P0 * np.exp(-alpha * (t - T0))
    a = np.zeros((np.size(TFert), np.size(t)))
    for i in np.arange(0, np.size(TFert)):
        a[i, :] = backGfunc(c, m[i], t - T0, TFert[i] - T0, alpha)
    return a0 + np.sum(a, axis=0)


def rYieldFunc(t, Nutrient, yConsts):
    a = yConsts[0]
    k1 = yConsts[1]
    k2 = yConsts[2]
    Yield = a * (k1 + Nutrient) / (k2 + Nutrient)
    return Yield.clip(max=100)


def alphaPfunc():
    alphaPData=[]
    alphaPLines = open('data/alphaP.txt', 'r').read()
    alphaPList = alphaPLines.split('\n')
    for line in alphaPList:
        if len(line) > 1.5:
            alphaPData.append(float(line))
    return alphaPData


alphaPData = alphaPfunc()

medianAlpha = np.percentile(alphaPData,50)
lowAlpha = min(alphaPData)
highAlpha = max(alphaPData)
alphaPQ1 = np.percentile(alphaPData,25)
alphaPQ3 = np.percentile(alphaPData,75)

aaP = (lowAlpha,alphaPQ1,medianAlpha,alphaPQ3,highAlpha)

def alphaKfunc():
    alphaKData=[]
    alphaKLines = open('data/alphaK.txt', 'r').read()
    alphaKList = alphaKLines.split('\n')
    for line in alphaKList:
        if len(line) > 1.5:
            alphaKData.append(float(line))
    return alphaKData


alphaKData = alphaKfunc()
medianAlphaK = np.percentile(alphaKData,50)
lowAlphaK = min(alphaKData)
highAlphaK = max(alphaKData)
alphaKQ1 = np.percentile(alphaKData,25)
alphaKQ3 = np.percentile(alphaKData,75)

aaK = (lowAlphaK,alphaKQ1,medianAlphaK,alphaKQ3,highAlphaK)

def alphaSfunc():
    alphaSData=[]
    alphaSLines = open('data/alphaS.txt', 'r').read()
    alphaSList = alphaSLines.split('\n')
    for line in alphaSList:
        if len(line) > 1.5:
            alphaSData.append(float(line))
    return alphaSData


alphaSData = alphaSfunc()

medianAlphaS = np.percentile(alphaSData,50)
lowAlphaS = min(alphaSData)
highAlphaS = max(alphaSData)
alphaSQ1 = np.percentile(alphaSData,25)
alphaSQ3 = np.percentile(alphaSData,75)

aaS = (lowAlphaS,alphaSQ1,medianAlphaS,alphaSQ3,highAlphaS)


def cPfunc():
    cPData=[]
    cPLines = open('data/cP.txt', 'r').read()
    cPList = cPLines.split('\n')
    for line in cPList:
        if len(line) > 1.5:
            cPData.append(float(line))
    return cPData

cPData = cPfunc()

medianc = np.percentile(cPData,50)
lowc = min(cPData)
highc = max(cPData)
cPQ1 = np.percentile(cPData,25)
cPQ3 = np.percentile(cPData,75)

ccP = (lowc,cPQ1,medianc,cPQ3,highc)

def cKfunc():
    cKData=[]
    cKLines = open('data/cK.txt', 'r').read()
    cKList = cKLines.split('\n')
    for line in cKList:
        if len(line) > 1.5:
            cKData.append(float(line))
    return cKData

cKData = cKfunc()

mediancK = np.percentile(cKData,50)
lowcK = min(cKData)
highcK = max(cKData)
cKQ1 = np.percentile(cKData,25)
cKQ3 = np.percentile(cKData,75)

ccK = (lowcK,cKQ1,mediancK,cKQ3,highcK)


def cSfunc():
    cSData=[]
    cSLines = open('data/cS.txt', 'r').read()
    cSList = cSLines.split('\n')
    for line in cSList:
        if len(line) > 1.5:
            cSData.append(float(line))
    return cSData

cSData = cSfunc()

mediancS = np.percentile(cSData,50)
lowcS = min(cSData)
highcS = max(cSData)
cSQ1 = np.percentile(cSData,25)
cSQ3 = np.percentile(cSData,75)

ccS = (lowcS,cSQ1,mediancS,cSQ3,highcS)


def PKP(TObs, Obs, TFert, Mass):
    try:
        if np.shape(Obs)[1] == 2:
            resX = PK2(TObs, Obs[:,0], Obs[:,1], TFert, Mass[:,0], Mass[:,1], 1)
        elif np.shape(Obs)[1] == 3:
            resX = PK3(TObs, Obs[:,0], Obs[:,1], Obs[:,2], TFert, Mass[:,0], Mass[:,1], Mass[:,2], 1)
        elif np.shape(Obs)[1] == 4:
            resX = PK4(TObs, Obs[:,0], Obs[:,1], Obs[:,2], Obs[:,3], TFert, Mass[:,0], Mass[:,1], Mass[:,2], Mass[:,3], 1)
        elif np.shape(Obs)[1] == 5:
            resX = PK5(TObs, Obs[:,0], Obs[:,1], Obs[:,2], Obs[:,3], Obs[:,4], TFert, Mass[:,0], Mass[:,1], Mass[:,2], Mass[:,3], Mass[:,4], 1)
        elif np.shape(Obs)[1] == 6:
            resX = PK6(TObs, Obs[:,0], Obs[:,1], Obs[:,2], Obs[:,3], Obs[:,4], Obs[:,5], TFert, Mass[:,0], Mass[:,1], Mass[:,2], Mass[:,3], Mass[:,4], Mass[:,5], 1)
    except IndexError:
        resX = PK1(TObs, Obs, TFert, Mass, 1)
    return resX

def PKK(TObs, Obs, TFert, Mass):
    try:
        if np.shape(Obs)[1] == 2:
            resX = PK2(TObs, Obs[:,0], Obs[:,1], TFert, Mass[:,0], Mass[:,1], 2)
        elif np.shape(Obs)[1] == 3:
            resX = PK3(TObs, Obs[:,0], Obs[:,1], Obs[:,2], TFert, Mass[:,0], Mass[:,1], Mass[:,2], 2)
        elif np.shape(Obs)[1] == 4:
            resX = PK4(TObs, Obs[:,0], Obs[:,1], Obs[:,2], Obs[:,3], TFert, Mass[:,0], Mass[:,1], Mass[:,2], Mass[:,3], 2)
        elif np.shape(Obs)[1] == 5:
            resX = PK5(TObs, Obs[:,0], Obs[:,1], Obs[:,2], Obs[:,3], Obs[:,4], TFert, Mass[:,0], Mass[:,1], Mass[:,2], Mass[:,3], Mass[:,4], 2)
        elif np.shape(Obs)[1] == 6:
            resX = PK6(TObs, Obs[:,0], Obs[:,1], Obs[:,2], Obs[:,3], Obs[:,4], Obs[:,5], TFert, Mass[:,0], Mass[:,1], Mass[:,2], Mass[:,3], Mass[:,4], Mass[:,5], 2)
    except IndexError:
        resX = PK1(TObs, Obs, TFert, Mass, 2)
    return resX

def PKS(TObs, Obs, TFert, Mass):
    try:
        if np.shape(Obs)[1] == 2:
            resX = PK2(TObs, Obs[:,0], Obs[:,1], TFert, Mass[:,0], Mass[:,1], 3)
        elif np.shape(Obs)[1] == 3:
            resX = PK3(TObs, Obs[:,0], Obs[:,1], Obs[:,2], TFert, Mass[:,0], Mass[:,1], Mass[:,2], 3)
        elif np.shape(Obs)[1] == 4:
            resX = PK4(TObs, Obs[:,0], Obs[:,1], Obs[:,2], Obs[:,3], TFert, Mass[:,0], Mass[:,1], Mass[:,2], Mass[:,3], 3)
        elif np.shape(Obs)[1] == 5:
            resX = PK5(TObs, Obs[:,0], Obs[:,1], Obs[:,2], Obs[:,3], Obs[:,4], TFert, Mass[:,0], Mass[:,1], Mass[:,2], Mass[:,3], Mass[:,4], 3)
        elif np.shape(Obs)[1] == 6:
            resX = PK6(TObs, Obs[:,0], Obs[:,1], Obs[:,2], Obs[:,3], Obs[:,4], Obs[:,5], TFert, Mass[:,0], Mass[:,1], Mass[:,2], Mass[:,3], Mass[:,4], Mass[:,5], 3)
    except IndexError:
        resX = PK1(TObs, Obs, TFert, Mass, 3)
    return resX



def PK1(TObs, Obs, Tfert, Mass, key):
    x0 = np.array([Obs[0], medianAlpha, medianc])
    def PK11(t, x):
        a0 = x[0] * np.exp(-x[1] * (t-TObs[0]))
        a = np.zeros((np.size(Tfert), np.size(t)))
        for i in np.arange(0, len(Tfert)):
            a[i, :] = backGfunc(x[2],Mass[i],t - TObs[0],Tfert[i]-TObs[0],x[1])
        return a0 + np.sum(a, axis=0)
    def f11(x):
        Y = PK11(TObs, x)
        y = sum(np.power(Y - Obs, 2))
        return y
    if key == 1:
        mybounds = [(1, None), (lowAlpha, highAlpha), (lowc, highc)]
    elif key == 2:
        mybounds = [(1, None), (10e-6, 10e-3), (0.005, 0.3)]
    elif key == 3:
        mybounds = [(1, None), (10e-6, 10e-3), (0.005, 0.3)]
    res = minimize(f11, x0, method='L-BFGS-B',bounds=mybounds)
    return res.x

def PK2(TObs, Obs1, Obs2, Tfert, Mass1, Mass2, key):
    x0 = np.array([(Obs1[0]+Obs2[0])/2, medianAlpha, medianc])
    def PK21(t, Mass, x):
        a0 = x[0] * np.exp(-x[1] * (t-TObs[0]))
        a = np.zeros((np.size(Tfert), np.size(t)))
        for i in np.arange(0, len(Tfert)):
            a[i, :] = backGfunc(x[2],Mass[i],t - TObs[0],Tfert[i] - TObs[0], x[1])
        return a0 + np.sum(a, axis=0)
    def f21(x):
        Y1 = PK21(TObs, Mass1, x)
        Y2 = PK21(TObs, Mass2, x)
        y = sum(np.power(Y1 - Obs1, 2)) + sum(np.power(Y2 - Obs2, 2))
        return y
    if key == 1:
        mybounds = [(1, None), (lowAlpha, highAlpha), (lowc, highc)]
    elif key == 2:
        mybounds = [(1, None), (10e-6, 10e-3), (0.005, 0.3)]
    elif key == 3:
        mybounds = [(1, None), (10e-6, 10e-3), (0.005, 0.3)]
    res = minimize(f21, x0, method='L-BFGS-B', bounds=mybounds)
    return res.x

def PK3(TObs, Obs1, Obs2, Obs3, Tfert, Mass1, Mass2, Mass3, key):
    x0 = np.array([(Obs1[0]+Obs2[0] + Obs3[0])/3, 4e-05, .01])
    def PK31(t, Mass, x):
        a0 = x[0] * np.exp(-x[1] * (t-TObs[0]))
        a = np.zeros((np.size(Tfert), np.size(t)))
        for i in np.arange(0, len(Tfert)):
            a[i, :] = backGfunc(x[2],Mass[i],t - TObs[0],Tfert[i] - TObs[0], x[1])
        return a0 + np.sum(a, axis=0)
    def f31(x):
        Y1 = PK31(TObs, Mass1, x)
        Y2 = PK31(TObs, Mass2, x)
        Y3 = PK31(TObs, Mass3, x)
        y = sum(np.power(Y1 - Obs1, 2)) + sum(np.power(Y2 - Obs2, 2)) + sum(np.power(Y3 - Obs3, 2))
        return y
    if key == 1:
        mybounds = [(1, None), (lowAlpha, highAlpha), (lowc, highc)]
    elif key == 2:
        mybounds = [(1, None),  (10e-6, 10e-3), (0.005, 0.3)]
    elif key == 3:
        mybounds = [(1, None), (10e-6, 10e-3), (0.005, 0.3)]
    res = minimize(f31, x0, method='L-BFGS-B', bounds=mybounds)
    return res.x

def PK4(TObs, Obs1, Obs2, Obs3, Obs4, Tfert, Mass1, Mass2, Mass3, Mass4, key):
    x0 = np.array([(Obs1[0]+Obs2[0] + Obs3[0] + Obs4[0])/4, 4e-05, .01])
    def PK41(t, Mass, x):
        a0 = x[0] * np.exp(-x[1] * (t-TObs[0]))
        a = np.zeros((np.size(Tfert), np.size(t)))
        for i in np.arange(0, len(Tfert)):
            a[i, :] = backGfunc(x[2],Mass[i],t - TObs[0],Tfert[i] - TObs[0], x[1])
        return a0 + np.sum(a, axis=0)
    def f41(x):
        Y1 = PK41(TObs, Mass1, x)
        Y2 = PK41(TObs, Mass2, x)
        Y3 = PK41(TObs, Mass3, x)
        Y4 = PK41(TObs, Mass4, x)
        y = sum(np.power(Y1 - Obs1, 2)) + sum(np.power(Y2 - Obs2, 2)) + sum(np.power(Y3 - Obs3, 2)) + sum(np.power(Y4 - Obs4, 2))
        return y
    if key == 1:
        mybounds = [(1, None), (lowAlpha, highAlpha), (lowc, highc)]
    elif key == 2:
        mybounds = [(1, None), (10e-6, 10e-3), (0.005, 0.3)]
    elif key == 3:
        mybounds = [(1, None), (10e-6, 10e-3), (0.005, 0.3)]
    res = minimize(f41, x0, method='L-BFGS-B', bounds=mybounds)
    return res.x

def PK5(TObs, Obs1, Obs2, Obs3, Obs4, Obs5, Tfert, Mass1, Mass2, Mass3, Mass4, Mass5, key):
    x0 = np.array([(Obs1[0]+Obs2[0] + Obs3[0] + Obs4[0] + Obs5[0])/5, 4e-05, .01])
    def PK51(t, Mass, x):
        a0 = x[0] * np.exp(-x[1] * (t-TObs[0]))
        a = np.zeros((np.size(Tfert), np.size(t)))
        for i in np.arange(0, len(Tfert)):
            a[i, :] = backGfunc(x[2],Mass[i],t - TObs[0],Tfert[i] - TObs[0], x[1])
        return a0 + np.sum(a, axis=0)
    def f51(x):
        Y1 = PK51(TObs, Mass1, x)
        Y2 = PK51(TObs, Mass2, x)
        Y3 = PK51(TObs, Mass3, x)
        Y4 = PK51(TObs, Mass4, x)
        Y5 = PK51(TObs, Mass5, x)
        y = sum(np.power(Y1 - Obs1, 2)) + sum(np.power(Y2 - Obs2, 2)) + sum(np.power(Y3 - Obs3, 2)) + sum(np.power(Y4 - Obs4, 2)) + sum(np.power(Y5 - Obs5, 2))
        return y
    if key == 1:
        mybounds = [(1, None), (lowAlpha, highAlpha), (lowc, highc)]
    elif key == 2:
        mybounds = [(1, None), (10e-6, 10e-3), (0.005, 0.3)]
    elif key == 3:
        mybounds = [(1, None), (10e-6, 10e-3), (0.005, 0.3)]
    res = minimize(f51, x0, method='L-BFGS-B', bounds=mybounds)
    return res.x

def PK6(TObs, Obs1, Obs2, Obs3, Obs4, Obs5, Obs6, Tfert, Mass1, Mass2, Mass3, Mass4, Mass5, Mass6, key):
    x0 = np.array([(Obs1[0]+Obs2[0] + Obs3[0] + Obs4[0] + Obs5[0] + Obs6[0])/6, 4e-05, .01])
    def PK61(t, Mass, x):
        a0 = x[0] * np.exp(-x[1] * (t-TObs[0]))
        a = np.zeros((np.size(Tfert), np.size(t)))
        for i in np.arange(0, len(Tfert)):
            a[i, :] = backGfunc(x[2],Mass[i],t - TObs[0],Tfert[i] - TObs[0], x[1])
        return a0 + np.sum(a, axis=0)
    def f61(x):
        Y1 = PK61(TObs, Mass1, x)
        Y2 = PK61(TObs, Mass2, x)
        Y3 = PK61(TObs, Mass3, x)
        Y4 = PK61(TObs, Mass4, x)
        Y5 = PK61(TObs, Mass5, x)
        Y6 = PK61(TObs, Mass6, x)
        y = sum(np.power(Y1 - Obs1, 2)) + sum(np.power(Y2 - Obs2, 2)) + sum(np.power(Y3 - Obs3, 2)) + sum(np.power(Y4 - Obs4, 2)) + sum(np.power(Y5 - Obs5, 2)) + sum(np.power(Y6 - Obs6, 2))
        return y
    if key == 1:
        mybounds = [(1, None), (lowAlpha, highAlpha), (lowc, highc)]
    elif key == 2:
        mybounds = [(1, None), (10e-6, 10e-3), (0.005, 0.3)]
    elif key == 3:
        mybounds = [(1, None), (10e-6, 10e-3), (0.005, 0.3)]
    res = minimize(f61, x0, method='L-BFGS-B', bounds=mybounds)
    return res.x
