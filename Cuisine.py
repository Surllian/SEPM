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

def get_data(filename):
    data = pd.read_csv(filename)
    return data


with st.sidebar:
    st.subheader("Choose a district to view")
    district_to_view = st.radio("", ("District 1", "District 2", "District 3", "District 4", "District 5", "District 6", "District 7", "District 8", "District 9", "District 10", "District 11", "District 12",
                                     "Cu Chi", "Binh Chanh", "Binh Tan", "Hoc Mon", "Nha Be", "Nha Be", "Phu Nhuan", "Tan Binh", "Tan Phu", "Thu Duc", "Binh Thanh"))

if district_to_view == "District 1":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "District 2":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "District 3":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "District 4":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "District 5":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "District 6":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "District 7":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "District 8":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "District 9":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "District 10":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "District 11":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "District 12":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)


if district_to_view == "Cu Chi":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "Binh Chanh":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "Binh Tan":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "Hoc Mon":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "Nha Be":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "Phu Nhuan":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "Tan Binh":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "Tan Phu":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

if district_to_view == "Thu Duc":
    Cu_Chi = get_data("CuChi.csv")
    st.write(Cu_Chi)

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

