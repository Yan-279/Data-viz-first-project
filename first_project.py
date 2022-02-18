# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:05:08 2022

@author: Admin
"""
from dash import Dash, dcc, html, dash
import plotly.express as px
import plotly.graph_objs as go
import plotly
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import random
from plotly.offline import plot
import numpy as np

#app = Dash(__name__)
app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



#df = pd.read_csv("C:\\Users\\Admin\\Desktop\\EPITA\\Data visualization\\USA_cars_datasets.csv") 
df = pd.read_csv("USA_cars_datasets.csv") 

#print(df['brand'])

print(df['price'][1])

#fig1 = px.bar(df, x=df['price'][1:5], y=df['brand'][1:5], color=df['brand'][1:5], barmode="group")
#fig1 = px.bar(df, x=df['price'][:30], y=df['brand'][:30], color=df['brand'][:30], barmode="group")

fig1 = px.bar(df['color'][:30])#, color=df['color'][:30])#, barmode="group")

# df['x1'] = df['color']#[df['color']][:30]
# #df['y11'] = 1
# df['y1'] = 1#df['y11'][df['y11']][:30]
# fig1 = px.bar(df, x="x1", y="y1", color="x1", labels={"x1":"Car color", "y1":"Count","x1":"Car color"}, title="Car colors distribution")#, "x1":"Colors"})

fig1.show()

#fig1 = px.bar(df, x=df['price'], y=df['brand'], color=df['brand'], barmode="group")
#fig1 = px.scatter(df, x=df['price'], y=df['brand'], color=df['brand'])#, barmode="group")

brands = []
for i in df['brand']:
    if i not in brands:
        brands.append(i)
        
print("Brands", brands)

brand_dist = df['brand'].value_counts()
print(brand_dist)

fig2 = px.bar(df, x=brands, y=brand_dist, color=brands, barmode="group")

#plt.show(fig2)

#############################################3

states = []
for i in df['state']:
    if i not in states:
        states.append(i)

print("\nStates", states)

# colors = []
# for i in df['color']:
#     if i not in colors:
#         colors.append(i)

# print("\nColors", colors)

state_dist = df['state'].value_counts()
print(state_dist)

#df['sz'] = 50
fig3 = px.bar(df, x=states, y=state_dist, color=states, barmode="group")

#fig3.update_layout(
    #autosize=False,
    #width=500,
    #height=500,
    # yaxis=dict(
    #     title_text="Y-axis Title",
    #     ticktext=["Very long label", "long label", "3", "label"],
    #     tickvals=[1, 2, 3, 4],
    #     tickmode="array",
    #     titlefont=dict(size=30),
    # )
#)

#####################################

# Start with one review:
#text = df.description[0]

test = df.brand

test = ""
for word in df.brand:
    test += " " + str(word)

# Display the generated image:
wordcloud = WordCloud(max_font_size=100, max_words=100, collocations=False, background_color="white").generate(test)


#fig4 = wordcloud

img = wordcloud.to_file("wordcloud-img.png")

plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


#############################################################
df['cars'] = 1
print(df.head())

fig5 = px.treemap(df,
                 path=['state', 'brand'],
                 values='cars')
fig5.update_layout(title="US State/Car brand Distribution",
                  width=1500, height=700,)
#fig5.show()


fig6 = px.treemap(df,
                 path=['brand', 'model'],
                 values='cars')

fig6.update_layout(title="US Car Brand/Model Distribution",
                  width=1500, height=700,)

#fig6.show()

##############################################

a1=0; a2=0; a3=0; a4=0; a5=0
for i in df['price']:
    if (i <= 20000):
        a1 += 1
    elif (i > 20000 and i <= 40000):
        a2 += 1
    elif (i > 40000 and i <= 60000):
        a3 += 1
    elif (i > 60000 and i <= 80000):
        a4 += 1
    elif (i > 80000 and i <= 100000):
        a5 += 1
        
print(a1, a2, a3, a4, a5)
print(a1 + a2 + a3 + a4 + a5)

        
a = [a1,a2,a3,a4,a5]
prices = ['< 20k $', '20k-40k $', '40k-60k $', '60k-80k $', '80k-100k $']

#fig7 = px.pie(df, values='price', name='newname', title='Price range distribution of cars in the US')#, names='country', title='Population of European continent')
#fig7 = px.pie(df, values='year', names='year', title='Price range distribution of cars in the US')#, names='country', title='Population of European continent')
#fig7 = px.pie(df, values='year', names='year', title='')
fig7 = px.pie(values=a, names=prices, title='Price range distribution of Cars in the US')

#fig7.show()

###############################################

#df['sz'] = 3
n8 = 2499
df['x8'] = df['price'][:n8]
df['y8'] = df['mileage'][df['mileage'] <500000][:n8]  #<500000 to remove outliers
df['color8'] = df['year'][:n8]
#df['sz8'] = df['sz'][:n8]
#fig8 = px.scatter(df,x = df['price'][:n8], y = df['mileage'][df['mileage'] <800000][:n8], color = df['year'][:n8], size = df['sz'][:n8], title = "Car Mileage in relation to the price and year bought")

fig8 = px.scatter(df,x = "x8", y = "y8", color = "color8",labels={"x8":"Price", "y8":"Mileage", "color8":"Year bought"}, title = "Car Mileage in relation to the price and year bought")


#fig8.show()



###############################################

app.layout = html.Div(children=[
    html.H1(children='First project'),
    html.Div(children='''
             Graph #1: Pie Chart
             '''),
              dcc.Graph(
                  id='plot7',
                  figure=fig7
                  ),
    html.Div(children='''
             The color distribution of the first 100 cars:
              '''),
              dcc.Graph(
                  id='plot1',
                  figure=fig1
                  ),     
    # html.Div(children='''
    #           The Brand distribution:
    #           '''),
    #           dcc.Graph(
    #               id='plot2',
    #               figure=fig2
    #               ), 
    # html.Div(children='''
    #           The Number of cars per state:
    #           '''),
    #           dcc.Graph(
    #               id='plot3',
    #               figure=fig3
    #               ),
    # html.Div(children='''
    #           The cars brand:
    #           '''),
    #           dcc.Graph(
    #               id='plot4',
    #               figure=fig4
    #               ), 
    html.Div(children='''
              Graph #3: Treemap
              '''),
              dcc.Graph(
                  id='plot6',
                  figure=fig6
                  ),
    html.Div(children='''
              Graph#4: Scatterplot
              '''),
              dcc.Graph(
                  id='plot8',
                  figure=fig8
                  ),
    html.Div(children='''
              Graph #6: Treemap
              '''),
              dcc.Graph(
                  id='plot5',
                  figure=fig5
                  )             
                 
])
             
if __name__ == '__main__':
    app.run_server(debug=True)