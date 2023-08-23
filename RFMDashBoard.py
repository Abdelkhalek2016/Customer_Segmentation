import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('rfm_table_data.csv')
df_raw=pd.read_csv('transaction_data.csv')
st.set_page_config(page_title='Customer Segmentation by RFM Analysis',layout='wide')
st.header("Customer Segmentation by RFM Analysis")

## Side Bar
show_table_box=st.sidebar.checkbox("Show Sample of Row Data")
show_statistics=st.sidebar.checkbox("Show Statistics Analysis on Data")
show_rfm_table=st.sidebar.checkbox("Show RFM Score Table")
selected_customer=st.sidebar.multiselect( "Select Type of Customer", df['My_Segmentation'].unique() )
all_options = st.sidebar.checkbox("Select all options",value=True)
if all_options:
    selected_customer = list(df['My_Segmentation'].unique())

selected_customer2=st.sidebar.multiselect("Select Type of Customer",df["customer_segmentation"].unique())
all_options2 = st.sidebar.checkbox("Select all types",value=True)
if all_options2:
    selected_customer2 = list(df['customer_segmentation'].unique())

if show_table_box:
    st.header("Raw DataSet Sample")
    st.dataframe(df_raw.sample(10),hide_index=True)
if show_statistics:
    st.header("Statistics Analysis on Raw DataSet")
    st.dataframe(df_raw.describe())
if show_rfm_table:
    st.header("Sample of RFM Scroe Table")
    st.dataframe(df.sample(10),hide_index=True)
    
## Body
col1, col2 = st.columns(2,gap='medium')

with col1:
    new_df=df[df['My_Segmentation'].isin(selected_customer)]
    fig=px.histogram(new_df,x=new_df["My_Segmentation"],title="Customer Segmentation",color='My_Segmentation')
    fig.update_xaxes(tickangle=45)
    fig.update_yaxes(title="Count Of Customers")
    st.plotly_chart(fig,use_container_width=True)
with col2:
    new_df=df[df['customer_segmentation'].isin(selected_customer2)]
    fig=px.histogram(new_df,new_df['customer_segmentation'],title='Customer Segmentation2',color='customer_segmentation')
    fig.update_xaxes(title="Type Of Customer")
    fig.update_yaxes(title="Count of Customers")
    st.plotly_chart(fig,use_container_width=True)

    
