import altair as alt
from vega_datasets import data
import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
import pyecharts.options as echarts

# Navigation_bar
# Hide menu
hide_menu = """
<style>
#MainMenu { visibility: hidden;
}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

#Header
st.markdown("""
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #FFFFFF; border-bottom-style: solid;">
    <img src="https://raw.githubusercontent.com/Surllian/SEPM/Tien/logo.png"
              class="img" style="width: 50px; height:50px" alt="MAFOOD">
    <a class="navbar-brand" href="https://mafood-homepage.herokuapp.com/" target="_blank" style="color: #000000;">MAFOOD</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse " id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link disabled" href="#" style="color: #000000;"> Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank" style="color: #000000;">Cuisine</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank" style="color: #000000;">Category</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://localhost:8502" target="_blank" style="color: #000000;">Location</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank" style="color: #000000;">Reccomendation</a>
        </li>
      </ul>
    </div>
  </nav>
""", unsafe_allow_html=True)

# Body
st.title('Cuisine')
st.write('This page allows you to browse the statistical data visualization by cuisine of restaurants in Ho Chi Minh City.'
         ' The data is classified as follows: Japanese, Western, Korean, Italian and so on. However, to make clear the data, Vietnamese cuisine will not be displayed on the bar chart and plot chart.')
st.subheader('Cuisine popularity')
st.write('The chart illustrates the popularity of all types of cuisine whom restaurant topic used. '
         'As the result, the user can choose what type of new cuisine they want to try or those planning to start a restaurant can determine what cuisine they want to utilize in their restaurant to limit competition. ')

sepmall ='https://raw.githubusercontent.com/Surllian/SEPM/main/All_Dis_csv/All_dis_csv.csv'

# dataset
BinhChanh = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/BinhChanh_dataset.csv'
BinhTan = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/BinhTan_dataset.csv'
BinhThanh = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/BinhThanh_dataset.csv'
CuChi = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/CuChi_dataset.csv'
GoVap = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/GoVap_dataset.csv'
NhaBe = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/NhaBe_dataset.csv'
HocMon = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/HocMon_dataset.csv'
PhuNhuan = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/PhuNhuan_dataset.csv'
TanBinh = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/TanBinh_dataset.csv'
TanPhu = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/TanPhu_dataset.csv'
ThuDuc = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/ThuDuc_dataset.csv'
Q1 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis1_data.csv'
Q2 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis2_food_data.csv'
Q3 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis3_food_data.csv'
Q4 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis4_food_data.csv'
Q5 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis5_food_data.csv'
Q6 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis6_food_data.csv'
Q7 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis7_food_data.csv'
Q8 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis8_food_data.csv'
Q9 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis9_food_data.csv'
Q10 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis10_food_data.csv'
Q11 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis11_food_data.csv'
Q12 = 'https://raw.githubusercontent.com/Surllian/SEPM/main/Dataset_500/Dis12_food_data.csv'

# Read csv all data
sepm = pd.read_csv(sepmall)

# Bar_chart
bars = alt.Chart(sepm).mark_bar().encode(
    x=alt.X('count(Cuisine):O',title = "Popularity"),
    y=alt.Y('Cuisine:N'),
    color='Cuisine:N',
    tooltip=['count(Cuisine)']
)

text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='count(Cuisine):O'
)

barchart = (bars + text).properties(height=800, width=800, title = 'Bar chart').interactive()

st.altair_chart(barchart)

# Table bar_chart
table = st.checkbox('Check out the data table')

if table:
    st.subheader('Data table')

    def get_data(filename):
        data = pd.read_csv(filename)
        return data


    with st.sidebar:
        st.subheader("Choose a district to view")
        district_to_view = st.radio("", ("District 1", "District 2", "District 3", "District 4", "District 5", "District 6", "District 7", "District 8", "District 9", "District 10", "District 11", "District 12",
                                         "Binh Thanh","Binh Chanh", "Binh Tan", "Cu Chi","Hoc Mon", "Nha Be", "Nha Be", "Phu Nhuan", "Tan Binh", "Tan Phu", "Thu Duc"))

    if district_to_view == "District 1":
        Q1 = get_data(Q1)
        st.write(Q1)

    if district_to_view == "District 2":
        Q2 = get_data(Q2)
        st.write(Q2)

    if district_to_view == "District 3":
        Q3 = get_data(Q3)
        st.write(Q3)

    if district_to_view == "District 4":
        Q4 = get_data(Q4)
        st.write(Q4)

    if district_to_view == "District 5":
        Q5 = get_data(Q5)
        st.write(Q5)

    if district_to_view == "District 6":
        Q6 = get_data(Q6)
        st.write(Q6)

    if district_to_view == "District 7":
        Q7 = get_data(Q7)
        st.write(Q7)

    if district_to_view == "District 8":
        Q8 = get_data(Q8)
        st.write(Q8)

    if district_to_view == "District 9":
        Q9 = get_data(Q9)
        st.write(Q9)

    if district_to_view == "District 10":
        Q10 = get_data(Q10)
        st.write(Q10)

    if district_to_view == "District 11":
        Q11 = get_data(Q11)
        st.write(Q11)

    if district_to_view == "District 12":
        Q12 = get_data(Q12)
        st.write(Q12)

    if district_to_view == "Cu Chi":
        CuChi = get_data(CuChi)
        st.write(CuChi)

    if district_to_view == "Binh Chanh":
        BinhChanh = get_data(BinhChanh)
        st.write(BinhChanh)

    if district_to_view == "Binh Tan":
        BinhTan = get_data(BinhTan)
        st.write(BinhTan)

    if district_to_view == "Binh Thanh":
        BinhThanh = get_data(BinhThanh)
        st.write(BinhThanh)

    if district_to_view == "Hoc Mon":
        HocMon = get_data(HocMon)
        st.write(HocMon)

    if district_to_view == "Nha Be":
        NhaBe = get_data(NhaBe)
        st.write(NhaBe)

    if district_to_view == "Phu Nhuan":
        PhuNhuan = get_data(PhuNhuan)
        st.write(PhuNhuan)

    if district_to_view == "Tan Binh":
        TanBinh = get_data(TanBinh)
        st.write(TanBinh)

    if district_to_view == "Tan Phu":
        TanPhu = get_data(TanPhu)
        st.write(TanPhu)

    if district_to_view == "Thu Duc":
        ThuDuc = get_data(ThuDuc)
        st.write(ThuDuc)

st.subheader('Rating among the districts categorized by cuisine')
st.write('The chart depicts the overall rating of each restaurant in each district, organized by cuisine.'
        )

# Plot chart

scatter = alt.Chart(sepm).mark_point(filled=True).encode(
        alt.X('Rating',
            scale=alt.Scale(
                domain=(3.0, 4.5),
                clamp=True
            )
        ),
        alt.Y('Cuisine'),
        alt.Size('AveragePrice', scale=alt.Scale(range=[10, 510])),
        alt.OpacityValue(0.6),
        alt.Color('District'),
        tooltip = ['Name', 'Type', 'AveragePrice', 'District']
    ).properties(height=850, width=850, title = 'Plot chart').interactive()
st.altair_chart(scatter)

st.subheader("Tag cloud for cuisine")
data = [
    {"name": name, "value": value}
    for name, value in [
        ("South Vietnamese", "7767"),
        ("North Vietnamese", "3228"),
        ("Central Vietnamese", "4516"),
        ("Highland Vietnamese", "1177"),
        ("Korean", "1244"),
        ("Japanese", "1182"),
        ("Chinses", "1324"),
        ("Thai", "665"),
        ("Taiwanese", "491"),
        ("Italian", "556"),
        ("American", "452"),
        ("International", "931"),
        ("Eastern Europe", "239"),
        ("Australian", "72"),
        ("Middle East", "70"),
        ("Nordic", "63"),
        ("African", "35"),
        ("Singaporean", "336"),
        ("Malaysian", "90"),
        ("Cambodian", "70"),
        ("Philippines", "24"),
        ("Indonesian", "34"),
        ("Indian", "105"),
        ("Iranian", "18"),
        ("French", "324"),
        ("Spanish", "41"),
        ("German", "63"),

    ]
]
wordcloud_option = {"series": [{"type": "wordCloud", "data": data}]}
st_echarts(wordcloud_option)

st.subheader("Category Distribution for the all cuisine")
options = {
    "title": {"text": "Cuisine Distribution Statistic in Total", "subtext": "Data from Foody", "left": "center"},
    "tooltip": {"trigger": "item"},
    "legend": {"orient": "vertical", "left": "left",},
    "series": [
        {
            "name": "pie chart",
            "type": "pie",
            "radius": "50%",
            "data": [

                {"value": 98211, "name": "Vietnamese"},
                {"value": 5865, "name": "Asian"},
                {"value": 1652, "name": "Western"},
                {"value": 376, "name": "Europe / Australian / Middle East / African"},
                {"value": 931, "name": "International"},
                {"value": 452, "name": "American"},

            ],
            "emphasis": {
                "itemStyle": {
                    "shadowBlur": 10,
                    "shadowOffsetX": 0,
                    "shadowColor": "rgba(0, 0, 0, 0.5)",
                }
            },
        }
    ],
}
st_echarts(
    options=options, height="600px",
)

# Footer
st.markdown("""
<nav class="navbar fixed-bottom navbar-expand-xl navbar-dark" style="background-color: #FFFFFF; border-top-style: solid; height: 80px">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse " id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="https://mafood-aboutus.herokuapp.com/" target="_blank" style="color: #000000;">About Us</a>
      </li>
    </ul>
  </div>
  <div style="padding: 100px 80px 50px">Copyright ©2022 TEAM DAVIKO</div>
</nav>
""", unsafe_allow_html=True)