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




st.title('Category')
st.caption('This page shows the data by category of restaurants: buffet, cafe, dine out, bar, and pub. It includes distribution charts by type of restaurant, average rating and rating distribution graphs, and graphs showing up to 10 restaurants by category.')

st.subheader("Category Distribution for the all category")
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
            "data": [9.6, 9.4, 8.8,8.4,8.0,8.0,7.8,7.6,7.5,7.4],
        },
        {
            "name": "Restaurant",
            "type": "line",
            "stack": "total",
            "data": [9.9,9.9, 9.8,9.5,9.4,9.0,8.9,8.8,8.8,8.7],
        },
                {
            "name": "Bistro",
            "type": "line",
            "stack": "total",
            "data": [9.8,9.7,9.1,8.4,8.4,8.2,8.1,8.0,8.0,7.9],
        },
        {
            "name": "Street food",
            "type": "line",
            "stack": "total",
            "data": [10.0,9.9,9.9, 8.9,8.6,7.8, 7.9,7.8,7.8,7.7,7.7],
        },
        {
            "name": "Cafe",
            "type": "line",
            "stack": "total",
            "data": [9.6,8.9, 8.3,8.1,8.1, 8.1,8.0,7.9,7.9,7.7],
        },
        {
            "name": "Pub / Bar",
            "type": "line",
            "stack": "total",
            "data": [9.6,9.0, 8.9,8.8,8.7,8.7,8.7,8.6,8.6,8.6],
        },
    ],
}
st_echarts(options=options, height="400px")




st.subheader("Best 10 Buffet with average price")

options = {
  "tooltip": { "trigger": "axis",
    "axisPointer": {
      "type": "shadow"
    }
  },
  "grid": {
    "left": "3%",
    "right": "4%",
    "bottom": "3%",
    "containLabel": True
  },
  "xAxis": [
    {
      "type": "category",
      "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Su"],
      "axisTick": {
       " alignWithLabel": True
      }
    }
  ],
  "yAxis": [
    {
      "type": "value"
    }
  ],
  "series": [
    {
      "name": "Direct",
     " type": "bar",
     " barWidth": "60%",
      "data": [10, 52, 200, 334, 390, 330, 220]
    }
  ]
};
st_echarts(
  options=options, height="400px")

st.subheader("Best 10 Restaurant with average price")
st.subheader("Best 10 Street food with average price")
st.subheader("Best 10 Cafe with average price")
st.subheader("Best 10 Pub/Bar with average price")










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
