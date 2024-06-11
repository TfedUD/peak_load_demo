import plotly as plt
import plotly.express as px
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout="wide", 
                   page_title='Sensitivity Study',
                   page_icon='8100464.png')

st.markdown('''For this study a PNNL prototype building was selected ''')

df = pd.read_csv('data.csv')

df = df.rename(columns={'in:Shade_Count':'Shade Count',
                        'in:Shade_Depth':'Shade Depth',
                        'in:Shade_Vertical':'Is Shade Vertical',
                        'in:Angle':'Angle',
                        'out:Cooling Energy Kwh': 'Cooling Energy Kwh',
                        'out:Heating Energy Kwh': 'Heating Energy Kwh'})
df['Is Shade Vertical'] = df['Is Shade Vertical'].astype(int)

fig = px.parallel_coordinates(df, color='Cooling Energy Kwh', color_continuous_scale='Portland')
st.plotly_chart(fig, use_container_width=True)




col1,col2,col3,col4 = st.columns(4)

with col1:
    fig1 = px.scatter(df, x='Shade Count', y='Cooling Energy Kwh')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(df, x='Shade Depth', y='Cooling Energy Kwh')
    st.plotly_chart(fig2, use_container_width=True)
    
with col3:
    fig3 = px.scatter(df, x='Is Shade Vertical', y='Cooling Energy Kwh') 
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    fig4 = px.scatter(df, x='Angle', y='Cooling Energy Kwh')
    st.plotly_chart(fig4, use_container_width=True)
    
    
col11,col12,col13,col14 = st.columns(4)

with col11:
    fig11 = px.scatter(df, x='Shade Count', y='Heating Energy Kwh', color_discrete_sequence=['red'])
    st.plotly_chart(fig11, use_container_width=True)
    
with col12:
    fig12 = px.scatter(df, x='Shade Depth', y='Heating Energy Kwh', color_discrete_sequence=['red'])
    st.plotly_chart(fig12, use_container_width=True)
    
with col13:
    fig13 = px.scatter(df, x='Is Shade Vertical', y='Heating Energy Kwh', color_discrete_sequence=['red'])
    st.plotly_chart(fig13, use_container_width=True)
    
with col14:
    fig14 = px.scatter(df, x='Angle', y='Heating Energy Kwh', color_discrete_sequence=['red'])
    st.plotly_chart(fig14, use_container_width=True)