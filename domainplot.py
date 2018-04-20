#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl 

domainType = [8248, 116, 230, 2289]
thissum = sum(domainType)
for m in range(0, 4):
    domainType[m] = domainType[m] / thissum


def draw_pie_4(labels,quants):  
    # make a square figure  
    plt.figure(1, figsize=(6,6))  
    # For China, make the piece explode a bit  
    expl = [0,0.3,0.2,0.1]   #第二块即China离开圆心0.1  
    # Colors used. Recycle if not enough.  
    colors  = ["blue","red","coral","green"]  #设置颜色（循环显示）  
    # Pie Plot  
    # autopct: format of "percent" string;百分数格式  
    plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%',pctdistance=0.8, shadow=True)  
    plt.title('IPv6 and DNSSEC Situation of .net Domains ', bbox={'facecolor':'0.8', 'pad':5})  
    plt.show()  
    plt.savefig("comtype.jpg") 
    plt.close()

def draw_pie_11(labels,quants):  
    # make a square figure  
    plt.figure(1, figsize=(6,6))  
    # For China, make the piece explode a bit  
    expl = [0,0,0,0,0.1,0.2,0.3,0.2,0.1,0,0]   #第二块即China离开圆心0.1  
    # Colors used. Recycle if not enough.  
    colors  = ["blue","red","coral","green","yellow","orange"]  #设置颜色（循环显示）  
    # Pie Plot 
    # autopct: format of "percent" string;百分数格式  
    plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%',pctdistance=0.8, shadow=True)  
    plt.title('TLD of Top 10k Domains ', bbox={'facecolor':'0.8', 'pad':5})  
    plt.show() 
    plt.savefig("tld.jpg") 
    plt.close()


def draw_pie(labels,quants):  
    # make a square figure  
    plt.figure(1, figsize=(8,8))  
    # For China, make the piece explode a bit  
    expl = [0,0.1,0,0,0,0,0,0,0,0]   #第二块即China离开圆心0.1  
    # Colors used. Recycle if not enough.  
    colors  = ["blue","red","coral","green","yellow","orange"]  #设置颜色（循环显示）  
    # Pie Plot  
    # autopct: format of "percent" string;百分数格式  
    plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%',pctdistance=0.8, shadow=True)  
    plt.title('Top 10 GDP Countries', bbox={'facecolor':'0.8', 'pad':5})  
    plt.show()  
    plt.savefig("pie.jpg") 
    plt.close()  
  
# quants: GDP  
  
# labels: country name  
  
# labels   = ['USA', 'China', 'India', 'Japan', 'Germany', 'Russia', 'Brazil', 'UK', 'France', 'Italy']  
  
# quants   = [15094025.0, 11299967.0, 4457784.0, 4440376.0, 3099080.0, 2383402.0, 2293954.0, 2260803.0, 2217900.0, 1846950.0]  

labels = ['None', 'IPv6 & DNSSEC', 'DNSSEC Only', 'IPv6 Only']
# quants = [4474, 43, 78, 1152]

# draw_pie_4(labels,domainType) 

b = ['com', 'net', 'org', 'ru', 'in', 'jp', 'cn', 'br', 'de', 'edu', 'others']
c = [5747, 525, 384, 336, 193, 188, 161, 151, 147, 145, 2906]

for m in range(0, 11):
    c[m] = c[m] / 10883

# draw_pie_11(b, c)

labels = ['None', 'IPv6 & DNSSEC', 'DNSSEC Only', 'IPv6 Only']
quants = [359, 6, 11, 149]
for m in range(0,4):
    quants[m] = quants[m] / c[1]

draw_pie_4(labels,quants) 