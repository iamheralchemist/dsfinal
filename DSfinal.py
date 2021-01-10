#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import pyecharts
import pyecharts.options as opts
from pyecharts.charts import Line, Grid
import pandas_datareader as pdr
import matplotlib.pyplot as plt #plt.style.use('seaborn-darkgrid')
import numpy as np


# In[3]:


world_data = pd.read_csv('world_covid.csv')
death = world_data[['Country','deaths_cumulative_total']][world_data['deaths_cumulative_total']>20000]
rank = death[['Country','deaths_cumulative_total']].sort_values(by='deaths_cumulative_total',ascending=False).values


# In[4]:


from pyecharts.charts import Pie

pie = Pie().add("Total Deaths", 
                rank, 
                radius = ["20%", "80%"],  
                center = ["60%", "60%"],  
                rosetype = "radius")   


# In[5]:


pie.set_global_opts(title_opts = opts.TitleOpts(title="COVID-19 Cumulative Death Cases by Countries on 2021/01/09",  
                                                pos_right = '30%'),  
                    legend_opts = opts.LegendOpts( 
                                                orient='vertical', 
                                                pos_right="0.001%", 
                                                pos_top="0.001%"))

pie.set_series_opts(label_opts = opts.LabelOpts(formatter="{b} : {d}%"))     
pie.render_notebook()


# In[6]:


stock=pd.read_csv('stock.csv')
stock


# In[7]:


usa=pd.read_csv('national_history.csv')
import warnings
warnings.filterwarnings('ignore')


# In[8]:


usa_data=usa[['date','positiveIncrease']]


# In[9]:


l1 = Line().add_xaxis(# Set x axis
                      xaxis_data = usa_data['date'].values  #input x
                      )


l1.add_yaxis(# Set y axis
             series_name = "Positive cases Increased",  # Name y
             y_axis = usa_data['positiveIncrease'].values.tolist(),  # input y value
             symbol_size = 1, # control sizes of points
             label_opts = opts.LabelOpts(is_show=False), # set labels
             linestyle_opts = opts.LineStyleOpts(width=1.5, type_='dotted'), # set width of line
             is_smooth = True, # make line smooth
             )

l1.set_global_opts(title_opts = opts.TitleOpts(title = "Positive Cases Increased between 2020/11 and 2021/1", 
                                               pos_left = "center"), # set title
                   axispointer_opts = opts.AxisPointerOpts(is_show = True, 
                                                           link = [{"xAxisIndex": "all"}]),  # coordinate operation 
                   xaxis_opts = opts.AxisOpts(type_ = "category",
                                              boundary_gap = True), 
                   yaxis_opts = opts.AxisOpts(name = "IncreasedPositive"),  
                   legend_opts = opts.LegendOpts(pos_left  ='3%') 
                   )


# In[10]:


l2 = Line().add_xaxis(xaxis_data = usa_data['date'].values)

l2.add_yaxis(series_name = "Pfizer",
             y_axis = stock['PFE'].values, 
             symbol_size = 1,
             label_opts = opts.LabelOpts(is_show = False),
             linestyle_opts = opts.LineStyleOpts(width = 1.5),
             is_smooth = True)

l2.add_yaxis(series_name = "Moderna",
             y_axis = stock['MRNA'].values,
             symbol_size = 1,
             label_opts = opts.LabelOpts(is_show = False),
             linestyle_opts = opts.LineStyleOpts(width = 1.5),
             is_smooth = True)

l2.set_global_opts(axispointer_opts = opts.AxisPointerOpts(  
                                                           is_show = True, 
                                                           link = [{"xAxisIndex": "all"}]),  
                   xaxis_opts = opts.AxisOpts(grid_index = 1,  
                                             type_ = "category", 
                                             boundary_gap = True,
                                             position = "top", 
                                             axisline_opts = opts.AxisLineOpts(is_on_zero=True)),  
                   yaxis_opts = opts.AxisOpts(is_inverse = False, name = "Value",name_gap = 25), 
                   legend_opts = opts.LegendOpts(pos_bottom = '10%',pos_right = '50') 
                   )


# In[11]:


grid = Grid(init_opts = opts.InitOpts(width = "1024px", height = "768px")) 

grid.add(chart=l1,  
         grid_opts = opts.GridOpts(pos_left = 50, pos_right = 50, height = "35%"))  
grid.add(chart = l2, 
         grid_opts = opts.GridOpts(pos_left = 50, pos_right = 50, pos_top = "55%", height = "35%"))
grid.render_notebook()


# In[12]:


# get_data_yahoo(inst_ticker, start_date, end_date)
sp = pdr.get_data_yahoo('^GSPC', '17-Nov-19')
ns = pdr.get_data_yahoo('^IXIC', '17-Nov-19')
nk = pdr.get_data_yahoo('^N225', '17-Nov-19')
# Calculate the percentage change
pc_1 = sp.Close.pct_change()
pc_2 =ns.Close.pct_change()
pc_3 =nk.Close.pct_change()
 # Plot
pc_1.plot(figsize=(10, 7), grid=True)
pc_2.plot(figsize=(10, 7), grid=True)
pc_3.plot(figsize=(10, 7), grid=True)
plt.axvline('30-Jan-20')
plt.show()


# In[ ]:




