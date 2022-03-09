import streamlit as st
import pandas as pd


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


header = st.container()
dataset = st.container()
features = st.container()
modelTrainning = st.container()

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', True)


@st.cache
def get_data(filename):
    covid19_data = pd.read_csv(filename)
    return covid19_data


with header:
    st.title("Welcome to my Data Science project")
    st.text("Test run part 1")

with dataset:
    st.header("Covid_19 datasets")
    st.text("I get this CSV file from: https://www.kaggle.com/imdevskp/corona-virus-report")
    covid19_data = get_data("worldometer_data.csv")
    st.write(covid19_data.head())

    top_cases = pd.DataFrame(covid19_data['TotalCases'].sort_values().head(50))
    st.bar_chart(top_cases)

with features:
    st.header("The features I created")

    st.markdown("I want to create this feature because.....")
    st.markdown("I want to create this feature because......")


with modelTrainning:
    st.header("Time to train model")

    sel_col, disp_col = st.columns(2)

    max_depth = sel_col.slider('What should be the max depth of the model?', min_value=10, max_value=100, value=10)

    n_estimators = sel_col.selectbox("How many trees there should be?", options=[100, 200, 300, "No Limits"], index=0)

    sel_col.text("Here is a list of features in my data")
    sel_col.write(covid19_data.columns)

    input_feature = sel_col.text_input("Which features should be used ad input?", "TotalCases")

    if n_estimators == "No Limits":
        regr = RandomForestRegressor(max_depth=max_depth)
    else:
        regr = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)

    X = covid19_data["TotalCases"]
    y = covid19_data["TotalRecovered"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    X_train = X_train.values.reshape(-1, 1)
    y_train = y_train.values.reshape(-1, 1)
    x_test = X_test.values.reshape(-1, 1)
    y_test = y_test.values.reshape(-1, 1)

    regr.fit(X_train, y_train)

    prediction = regr.predict(y_train)

    disp_col.subheader("Mean absolute error of the model is:")
    disp_col.write(mean_absolute_error(y_train, prediction))

    disp_col.subheader("Mean squared error of the model is:")
    disp_col.write(mean_squared_error(y_train, prediction))

    disp_col.subheader("R squared score of the model is")
    disp_col.write(r2_score(y_train, prediction))
