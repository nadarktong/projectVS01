import streamlit as st
import pandas as pd

st.image('img/g2.jpg')
st.header("การนำเสนอสถิติการเกิดอุบัติเหตุของประเทศไทย")

col1,col2=st.columns(2)

with col1:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write("2,5600")
with col2:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write("2,5600")

dt=pd.read_excel('data/opendata-rtddi-54-66-9month.xlsx')

NumM=dt[dt['Sex']=='ชาย'].count()
Numโ=dt[dt['Sex']=='หญิง'].count()

dtSex=[NumM,NumF]
dtSex=pd.DataFrame(dtSex)
st.bar_chart(dtsexb)