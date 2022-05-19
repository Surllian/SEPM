import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
import pyecharts.options as echarts
from jmespath import Options
import altair as alt
import numpy as np

from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
import streamlit.components.v1 as components

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
          <a class="nav-link disabled" href="https://mafood-homepage.herokuapp.com/" style="color: #000000;"> Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://mafood-cuisine.herokuapp.com/" target="_blank" style="color: #000000;">Cuisine</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank" style="color: #000000;">Category</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="http://localhost:8502" target="_blank" style="color: #000000;">Location</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://mafood-recommend.herokuapp.com/" target="_blank" style="color: #000000;">Reccomendation</a>
        </li>
      </ul>
    </div>
  </nav>
""", unsafe_allow_html=True)

st.title('Category')
st.caption('This page shows the data by category of restaurants: buffet, cafe, dine out, bar, and pub. It includes distribution charts by type of restaurant, average rating and rating distribution graphs, and graphs showing up to 10 restaurants by category.')

st.subheader("Category distribution for the all category")
options = {
    "title": {"text": "Category Distribution Statistic in Total", "subtext": "Data from Foody", "left": "center"},
    "tooltip": {"trigger": "item"},
    "legend": {"orient": "vertical", "left": "left",},
    "series": [
        {
            "name": "Category",
            "type": "pie",
            "radius": "50%",
            "data": [

                {"value": 173, "name": "Buffet"},
                {"value": 3122, "name": "Restaurant"},
                {"value": 5292, "name": "Street food"},
                {"value": 11562, "name": "Cafe"},
                {"value": 14662, "name": "Bistro"},
                {"value": 305, "name": "Pub / Bar"},

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

st.subheader("Rating distribution for Top 10 restaurants in each category")
st.caption("Based on the rating of the restaurant where has more than 50 reviews (except Pub/bar)")
options = {
    "title": {"text": "Rating"},
    "tooltip": {"trigger": "axis"},
    "legend": {"data": ["Buffet", "Restaurant", "Bistro","Street food", "Cafe", "Pub / Bar"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "toolbox": {"feature": {"saveAsImage": {}}},
    "xAxis": {
        "type": "category",
        "boundaryGap": False,
        "data": ["1", "2", "3", "4", "5", "6","7","8","9","10"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "name": "Buffet",
            "type": "line",
            "stack": "total",
            "data": [4.8, 4.7, 4.4,4.2,4.0,4.0,3.9,3.8,3.75,3.7],
        },
        {
            "name": "Restaurant",
            "type": "line",
            "stack": "total",
            "data": [4.95,4.95, 4.9,4.75,4.7,4.5,4.45,4.4,4.4,4.35],        
            },
                {
            "name": "Bistro",
            "type": "line",
            "stack": "total",
            "data": [4.9,4.85,4.55,4.2,4.2,4.1,4.05,4.0,4.0,3.95],
        },
        {
            "name": "Street food",
            "type": "line",
            "stack": "total",
            "data": [5.0,4.95,4.95, 4.45,4.3,3.95, 3.9,3.9,3.9,3.85,3.85],
        },
        {
            "name": "Cafe",
            "type": "line",
            "stack": "total",
            "data": [4.8,4.45, 4.15,4.05,4.05, 4.05,4.0,3.95,3.95,3.85],
        },
        {
            "name": "Pub / Bar",
            "type": "line",
            "stack": "total",
            "data": [4.8,4.5, 4.45,4.4,4.35,4.35,4.35,4.3,4.3,4.3],
        },
    ],
}
st_echarts(options=options, height="400px")



st.subheader("Best 10 Bistro with average price")
st.caption("Hover over to view the detailed information of best top 10 bistro including name of the bistro, average price, and rating.")
components.html(
        """
        <body style="height: 100%; margin: 0">
    <div id="container" style="height: 500%"></div>

    <script
      type="text/javascript"
      src="https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.min.js"
    ></script>

    <script type="text/javascript">
      var dom = document.getElementById("container");
      var myChart = echarts.init(dom, null, {
        renderer: "canvas",
        useDirtyRect: false,
      });
      var app = {};

      var option;

      const colors = ["#EB5B5B", "#F9C14E", "#EE6666"];

      option = {
        color: colors,

        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
          },
        },
        grid: {
          right: "20%",
        },
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        legend: {
          data: ["Evaporation", "Temperature"],
        },
        xAxis: [
          {
            type: "category",
            axisTick: {
              alignWithLabel: true,
            },

            data: [
              "1 - Ga Nuong A Quan",
              "2 - Han Quoc Quan Lau Ga Nhan Sam & An Vat",
              "3 - Bun Cha Ha Noi Cao Trieu Phat",
              "4 - Ga Ta Thuy Trinh",
              "5 - Lau De Noi Dat Tran Xuan Soan",
              "6 - Ha Cao & Hu Tieu Lam Van Ben",
              "7 - Pham Gia Quan Chuyen Cac Mon Luon",
              "8 - Ramyon Sarang Mi Cay Han Quoc",
              "9 - Be Ba Com Ga Nha Trang Ta Quang Buu",
              "10 - Com Tam Ba Ha Hung Phu",
            ],
          },
        ],
        yAxis: [
          {
            type: "value",
            name: "Average Price",
            position: "right",
            alignTicks: true,
            offset: 0,
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[0],
              },
            },
            axisLabel: {
              formatter: "{value} VND",
            },
          },
          {
            type: "value",
            name: "Rating",
            position: "left",
            alignTicks: true,
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[1],
              },
            },
            axisLabel: {
              formatter: "{value} / 5",
            },
          },
        ],
        series: [
          {
            name: "Average Price",
            type: "bar",
            yAxisIndex: 0,
            data: [
              77000, 125000, 69000,102000 ,270000 , 40000, 80000, 45000, 27500, 27500
            ],
          },
          {
            name: "Rating",
            type: "line",
            yAxisIndex: 1,
            data: [4.9,4.85,4.55,4.2,4.2,4.1,4.05,4.0,4.0,3.95],
          },
        ],
      };

      if (option && typeof option === "object") {
        myChart.setOption(option);
      }

      window.addEventListener("resize", myChart.resize);
    </script>
  </body>
                """
,height=500

)

st.subheader("Best 10 Restaurant with average price")
st.caption("Hover over to view the detailed information of best top 10 restaurants including name of the restaurant, average price, and rating.")
components.html(
        """
        <body style="height: 100%; margin: 0">
    <div id="container" style="height: 500%"></div>

    <script
      type="text/javascript"
      src="https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.min.js"
    ></script>

    <script type="text/javascript">
      var dom = document.getElementById("container");
      var myChart = echarts.init(dom, null, {
        renderer: "canvas",
        useDirtyRect: false,
      });
      var app = {};

      var option;

      const colors = ["#359867", "#91CC75", "#EE6666"];

      option = {
        color: colors,

        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
          },
        },
        grid: {
          right: "20%",
        },
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        legend: {
          data: ["Evaporation", "Temperature"],
        },
        xAxis: [
          {
            type: "category",
            axisTick: {
              alignWithLabel: true,
            },
            data: [
              "1 - Quan Chay Trang Nha",
              "2 - Bova Kitchen Tra Sua & An Vat Phu Dinh",
              "3 - Banh Mi Que 26",
              "4 - Banh Beo Co Thanh Le Loi",
              "5 - Chao Long Chanh Ot",
              "6 - Ca Vien Chien Sinh Vien",
              "7 - Bap Nuong Ba Chieu  Chung Cu My Phuoc",
              "8 - Agechan Restaurant - Com & Mon An Nhat",
              "9 - Bota Tea",
              "10 - Ha Cao & Khoai Lang Lac",
            ],
          },
        ],
        yAxis: [
          {
            type: "value",
            name: "Average Price",
            position: "right",
            alignTicks: true,
            offset: 0,
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[0],
              },
            },
            axisLabel: {
              formatter: "{value} VND",
            },
          },
          {
            type: "value",
            name: "Rating",
            position: "left",
            alignTicks: true,
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[1],
              },
            },
            axisLabel: {
              formatter: "{value} / 5",
            },
          },
        ],
        series: [
          {
            name: "Average Price",
            type: "bar",
            yAxisIndex: 0,
            data: [
              137500, 94000, 12500, 22500, 20000, 40000, 150000, 40000, 25000,
              30000,
            ],
          },
          {
            name: "Rating",
            type: "line",
            yAxisIndex: 1,
            data: [4.95, 4.95, 4.9, 4.75, 4.7, 4.5, 4.45, 4.4, 4.4, 4.35],
          },
        ],
      };

      if (option && typeof option === "object") {
        myChart.setOption(option);
      }

      window.addEventListener("resize", myChart.resize);
    </script>
  </body>
                """
,height=500

)


st.subheader("Best 10 Cafe with average price")
st.caption("Hover over to view the detailed information of best top 10 cafes including name of the cafe, average price, and rating.")
components.html(
        """
        <body style="height: 100%; margin: 0">
    <div id="container" style="height: 500%"></div>

    <script
      type="text/javascript"
      src="https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.min.js"
    ></script>

    <script type="text/javascript">
      var dom = document.getElementById("container");
      var myChart = echarts.init(dom, null, {
        renderer: "canvas",
        useDirtyRect: false,
      });
      var app = {};

      var option;

      const colors = ["#91CC75","#359967",  "#EE6666"];

      option = {
        color: colors,

        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
          },
        },
        grid: {
          right: "20%",
        },
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        legend: {
          data: ["Evaporation", "Temperature"],
        },
        xAxis: [
          {
            type: "category",
            axisTick: {
              alignWithLabel: true,
            },

            data: [
              "1 - Sweetie - Coffee & Milk Tea",
              "2 - YoGun Korean Yogurt - Le Thi Ha",
              "3 - Tra Sua Comebuy - Phan Xich Long",
              "4 - U&ME Coffee & Tea",
              "5 - Quet Diem Coffee",
              "6 - Cafe Khong Gian Xua",
              "7 - Moolcoffee",
              "8 - Bay Coffee",
              "9 - Green House Cafe",
              "10 - Suoi Reo Cafe",
            ],
          },
        ],
        yAxis: [
          {
            type: "value",
            name: "Average Price",
            position: "right",
            alignTicks: true,
            offset: 0,
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[0],
              },
            },
            axisLabel: {
              formatter: "{value} VND",
            },
          },
          {
            type: "value",
            name: "Rating",
            position: "left",
            alignTicks: true,
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[1],
              },
            },
            axisLabel: {
              formatter: "{value} / 5",
            },
          },
        ],
        series: [
          {
            name: "Average Price",
            type: "bar",
            yAxisIndex: 0,
            data: [
              35000, 23000, 48500, 14000, 28500, 39500, 
              22500, 32500, 31000,
              30000,
            ],
          },
          {
            name: "Rating",
            type: "line",
            yAxisIndex: 1,
            data: [4.8,4.45, 4.15,4.05,4.05, 4.05,4.0,3.95,3.95,3.85],
          },
        ],
      };

      if (option && typeof option === "object") {
        myChart.setOption(option);
      }

      window.addEventListener("resize", myChart.resize);
    </script>
  </body>
                """
,height=500

)




st.subheader("Best 10 Pub/Bar with average price")
st.caption("Hover over to view the detailed information of best top 10 cafes including name of the cafe, average price, and rating.")
components.html(
        """
        <body style="height: 100%; margin: 0">
    <div id="container" style="height: 500%"></div>

    <script
      type="text/javascript"
      src="https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.min.js"
    ></script>

    <script type="text/javascript">
      var dom = document.getElementById("container");
      var myChart = echarts.init(dom, null, {
        renderer: "canvas",
        useDirtyRect: false,
      });
      var app = {};

      var option;

      const colors = ["#68B9D9", "#5470C6"];

      option = {
        color: colors,

        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
          },
        },
        grid: {
          right: "20%",
        },
        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },
        legend: {
          data: ["Evaporation", "Temperature"],
        },
        xAxis: [
          {
            type: "category",
            axisTick: {
              alignWithLabel: true,
            },
            data: [4.8,4.5, 4.45,4.4,4.35,
            4.35,4.35,4.3,4.3,4.3],
            data: [
              "1 - Terrace Bar & Cafe",
              "2 - Stand Craft Quan Bia & Fast Food",
             "3 -  Ot Xanh 1  Chao Ech Singapore",
            "4 - Lau Bo Nam Canh Le Van Viet",
              "4 - The Wine Stand By Elsol",
              "6 - O Gai Hue - Quan Nhau Binh Dan",

              "7 - Black Coffee & Beer",
              "8 - HP Ice Lounge",

              "9 - Quan Bia Set So 2 Nguyen Huu Tho",
              "10 - Lau De Thuan Phat",
            ],
          },
        ],
        yAxis: [
          {
            type: "value",
            name: "Average Price",
            position: "right",
            alignTicks: true,
            offset: 0,
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[0],
              },
            },
            axisLabel: {
              formatter: "{value} VND",
            },
          },
          {
            type: "value",
            name: "Rating",
            position: "left",
            alignTicks: true,
            axisLine: {
              show: true,
              lineStyle: {
                color: colors[1],
              },
            },
            axisLabel: {
              formatter: "{value} / 5",
            },
          },
        ],
        series: [
          {
            name: "Average Price",
            type: "bar",
            yAxisIndex: 0,
            data: [
              275000, 169000, 85000, 100000, 117500, 125000, 110000,90000,150000, 40000, 358000,90000
            ],
          },
          {
            name: "Rating",
            type: "line",
            yAxisIndex: 1,
            data: [4.8,4.5, 4.45,4.4,4.35,4.35,4.35,4.3,4.3,4.3],
          },
        ],
      };

      if (option && typeof option === "object") {
        myChart.setOption(option);
      }

      window.addEventListener("resize", myChart.resize);
    </script>
  </body>
                """
,height=500

)


st.subheader("Average price for each category (VND)")
st.caption("Hover over to view the detailed information of the price divided into each category")
components.html(
        """<body style="height: 100%; margin: 0">
  <div id="container" style="height: 500%"></div>

  
  <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5.3.2/dist/echarts.min.js"></script>


  <script type="text/javascript">
    var dom = document.getElementById('container');
    var myChart = echarts.init(dom, null, {
      renderer: 'canvas',
      useDirtyRect: false
    });
    var app = {};
    
    var option;

    option = {
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  xAxis: [
    {
      type: 'category',
      data: ['Bistro','Restaurant',  'Cafe', 'Pub / Bar'],
      axisTick: {
        alignWithLabel: true
      }
    }
  ],
  yAxis: [
    {
      type: 'value'
    }
  ],
  series: [
    {
      name: 'Price',
      type: 'bar',
      barWidth: '60%',
      data: [86300, 57150,30450,170950]
    }
  ]
};

    if (option && typeof option === 'object') {
      myChart.setOption(option);
    }

    window.addEventListener('resize', myChart.resize);
  </script>
</body>
""",height=500
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