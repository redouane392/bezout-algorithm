# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:06:49 2020

@author: Redouane
"""

def euc(a,b):
    
    while a%b!=0:
        a,b=b,a%b
    return b

def bez1(a,b):
    x0,x1,y0,y1=1,0,0,1
    while b!=0:
        a0=a
        b0=b
        q=a//b
        z=a%b
        a=b
        b=z
        w=x1
        x1=x0-q*x1
        x0=w
        v=y1
        y1=y0-q*y1
        y0=v
    print( "PGCD :{0}  (u={1})*{2}+(v={3})*{4}={0}".format(euc(a0,b0),x0,a0,y0,b0))
    
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   
    



        
        