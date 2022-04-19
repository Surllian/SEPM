import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import altair as alt
from datetime import datetime
import matplotlib.pyplot as py
import matplotlib.pylab as plt
import seaborn as sns

st.title('Cuisine')
st.write('This page allows you to browse the statistical data visualization by cuisine of restaurants in Ho Chi Minh City. The data is classified as follows: Vietnam, Japanese, Western, Korean, Italian and so on.')
st.subheader('Cuisine popularity')
st.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ')

chart_data = pd.DataFrame(
    np.random.rand(9, 4),
    index=["air","coffee","orange","whitebread","potato","wine","beer","wheatbread","carrot"],
)


to_stream = pd.DataFrame(
    [
        ["CHILDREN", 0.42806248287201976, 0.0],
        ["AMT_TOTAL", 165006, 179357],
        ["SAL", 766582, 703917.0],
        ["ANNUITY", 26851, 28416],
    ],
    columns=("Variable", "Id", "Mean"),
)


plt.rcParams.update({"font.size": 14, "font.weight": "bold"})
dfcols = to_stream.columns.tolist()
fig, ax = plt.subplots(figsize=(12, 8),)
sns.set_style("whitegrid")
to_stream.plot.barh(x="Variable", figsize=(12, 8), width=0.9, ax=ax)
plt.title("Comparer avec la Moyenne Globale", fontsize=24, fontweight="bold")
plt.legend(loc="lower right")
for patch in ax.patches:
    w, h = patch.get_width(), patch.get_height()
    y = patch.get_y()
    ax.text(w + -0.1, h / 2 + y, f"{w:.3f}", va="center")

st.pyplot(fig)