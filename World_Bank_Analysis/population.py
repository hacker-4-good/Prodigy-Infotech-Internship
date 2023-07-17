#   Import Library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

#   Functions

def search(arr: list, x:str) -> int:
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

#   Data Analysis Code  

data = pd.read_csv('World_Bank_Analysis/world_bank.csv')
data = data.drop(columns=['Indicator Name','Indicator Code','2022', 'Unnamed: 67'])
for i in range(1960, 2022):
    data[str(i)] = data[str(i)].fillna(np.mean(data[str(i)]))

work = np.transpose(data)

#   Streamlit app code

import streamlit as st

st.title("Population Graph Visualization")
select = st.selectbox('Select the Option',options=list(data['Country Name']))

if st.button('Plot'):
    my_bar = st.progress(0, 'Operation in Progress')
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, 'Operation in Progress')
    index = search(list(data['Country Name']), select)
    fig = plt.figure(figsize=(30,6))
    plt.xlabel('Years', fontsize=20)
    plt.title(f'{select}', fontsize=30)
    sns.barplot(x=work.index[2:], y=work[2:][index])
    st.pyplot(fig)

st.title("Population Data of Country")
country = st.selectbox('Select the Country',options=list(data['Country Name']))
year = st.slider("Enter the year", min_value=1960, max_value=2021)

if st.button('Show'):
    my_bar = st.progress(0, 'Operation in Progress')
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, 'Operation in Progress')
    ans = int(data[data['Country Name']==country][str(year)])
    temp = list(str(ans))[::-1]
    value = ''
    count = 0
    flag1,flag2 = True,False
    for i in range(len(temp)):
        if count==3 and flag1:
            count = 0
            flag1 = False
            flag2 = True
            value += ','
        if count%2==0 and count>0 and flag2:
            value += ','
        value += temp[i]
        count += 1
    value = value[::-1]
    st.text(f'The population in {country} in the year {year}: {value}')
