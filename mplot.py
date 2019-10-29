import pandas as pd
import matplotlib.pyplot as plt
#import descartes
import geopandas as gpd
from shapely.geometry import Point,Polygon
import matplotlib
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import mplcursors
import numpy as np

street_map = gpd.read_file('Admin2.shp')
#street_map.crs
#fig,ax = plt.subplots(figsize = (15,15))
#street_map.plot(ax=ax)
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)
df=pd.read_csv(filename)

if(df is None):
    exit()
Num_cols = len (df.columns)
rows = len(df)

crs = {'init': 'epsg:4326'}
dfcol = df.columns

k=2
n=0
while k<Num_cols:
    df.rename(columns={df.columns[k]:chr(ord('a')+n)},inplace=True)
    k=k+1
    n=n+1
    
print(df.head())
geometry = [Point(xy) for xy in zip(df['longitude'],df['latitude'])]
geometry[:3]
geo_df = gpd.GeoDataFrame(df,crs=crs,geometry=geometry)
print(geo_df.head())

i=3
j=0
k="week "
while i<=Num_cols:
    
    fig,ax = plt.subplots(figsize = (15,15))
    street_map.plot(ax=ax,color='white')
    geo_df[geo_df[chr(ord('a')+j)]<=50].plot(ax=ax,markersize=20,color='white',marker='o',label='Normal')
    geo_df[(geo_df[chr(ord('a')+j)]>50) & (geo_df[chr(ord('a')+j)]<=80)].plot(ax=ax,markersize=15,color='#D6E2FF',marker='o',label="low")
    geo_df[(geo_df[chr(ord('a')+j)]>80) & (geo_df[chr(ord('a')+j)]<=100)].plot(ax=ax,markersize=15,color='#B5C9FF',marker='o',label="low")
    geo_df[(geo_df[chr(ord('a')+j)]>100) & (geo_df[chr(ord('a')+j)]<=120)].plot(ax=ax,markersize=15,color='#7F96FF',marker='o',label="Average")
    geo_df[(geo_df[chr(ord('a')+j)]>120) & (geo_df[chr(ord('a')+j)]<=140)].plot(ax=ax,markersize=15,color='#7285F8',marker='o',label='Average')
    geo_df[(geo_df[chr(ord('a')+j)]>140) & (geo_df[chr(ord('a')+j)]<=160)].plot(ax=ax,markersize=15,color='#009E1E',marker='o',label='Average')
    geo_df[(geo_df[chr(ord('a')+j)]>160) & (geo_df[chr(ord('a')+j)]<=180)].plot(ax=ax,markersize=15,color='#3CBC3D',marker='o',label='high')
    geo_df[(geo_df[chr(ord('a')+j)]>180) & (geo_df[chr(ord('a')+j)]<=200)].plot(ax=ax,markersize=15,color='#B9F96E',marker='o',label='high')
    geo_df[(geo_df[chr(ord('a')+j)]>200) & (geo_df[chr(ord('a')+j)]<=220)].plot(ax=ax,markersize=15,color='#FFF913',marker='o',label='high')
    geo_df[(geo_df[chr(ord('a')+j)]>220) & (geo_df[chr(ord('a')+j)]<=240)].plot(ax=ax,markersize=15,color='#E50000',marker='o',label='very High')
    geo_df[(geo_df[chr(ord('a')+j)]>240) & (geo_df[chr(ord('a')+j)]<=260)].plot(ax=ax,markersize=15,color='#BD0000',marker='o',label='very high')       
    geo_df[geo_df[chr(ord('a')+j)]>260].plot(ax=ax,markersize=15,color='#000000',marker='o',label='Normal')       
    font = {'family' : 'normal',
                        'weight' : 'bold',
                        'size'   : 22,}	
    matplotlib.rc('font', **font)
    i=i+1
    j=j+1
    plt.text(90, 35,k+str(j))
    #plt.figimage(35,20,"D:\photos\Ne\dnt touch\Aura Note 4G_20170422_145225.jpg")
               
mplcursors.cursor(hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(sel.artist.get_label()))
