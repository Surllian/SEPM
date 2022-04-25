import altair as alt
import streamlit as st
import pandas as pd

st.title('Cuisine')
st.write('This page allows you to browse the statistical data visualization by cuisine of restaurants in Ho Chi Minh City.'
         ' The data is classified as follows: Vietnam, Japanese, Western, Korean, Italian and so on.')
st.subheader('Cuisine popularity')
st.write('The chart illustrates the popularity of all types of cuisine whom restaurant topic used. '
         'As the result, the user can choose what type of new cuisine they want to try or for who having intention to open a restaurant will decide what cuisine they want to used in their restaurnt in order to reduce to compete. ')

sepmall ='https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_20/CuChi.csv'
sepm = pd.read_csv(sepmall)

# Bar_chart
barchart = alt.Chart(sepm).mark_bar().encode(
    x=alt.X('count(Cuisine):O',title = "Popularity"),
    y=alt.Y('Cuisine:N'),
    color='Cuisine:N'
)

st.altair_chart(barchart)

# Table bar_chart

st.subheader('Average price and popularity by cuisine')
st.write('The chart illustrates the popularity  and average price of all types of cuisine whom restaurant topic used. '
         'This can help anyone who are going to set themselves up in food business can choose the appropriate price for their restaurant theme. ')

# Plot chart
plotchart = alt.Chart(sepm).mark_circle().encode(
    y=alt.Y('average(Average):O',type='quantitative'),
    x=alt.X('count(Cuisine):O', title="Popularity"),
    color='Cuisine:N'
)

st.altair_chart(plotchart)

# Table Plot_chart
