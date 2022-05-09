import streamlit as st
import pandas as pd
from streamlit_echarts import st_echarts
from pyecharts import options as opts


st.title('Category')
st.caption('This page shows the data by category of restaurants: buffet, cafe, dine out, bar, and pub. It includes distribution charts by type of restaurant, average rating and rating distribution graphs, and graphs showing up to 10 restaurants by category.')

st.subheader("Category Distribution")


option = {
    "legend": {"top": "bottom"},
    "toolbox": {
        "show": True,
        "feature": {
            "mark": {"show": True},
            "dataView": {"show": True, "readOnly": False},
            "restore": {"show": True},
            "saveAsImage": {"show": True},
        },
    },
    "series": [
        {
            "name": "Restaurant Distribution Statistic",
            "type": "pie",
            "radius": [50, 250],
            "center": ["50%", "50%"],
            "roseType": "area",
            "itemStyle": {"borderRadius": 8},
            "data": [
                {"value": 40, "name": "rose 1"},
                {"value": 38, "name": "rose 2"},
                {"value": 32, "name": "rose 3"},
                {"value": 30, "name": "rose 4"},
                {"value": 28, "name": "rose 5"},
                {"value": 26, "name": "rose 6"},
                {"value": 22, "name": "rose 7"},
                {"value": 18, "name": "rose 8"},
            ],
        }
    ],
}
st_echarts(
    options=option, height="600px",
)