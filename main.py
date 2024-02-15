import streamlit as st
import plotly.express as px

st.title("Weather forecast for the Next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {str(days)} days in {place}")


def get_data(input_days):
    dates = ["2023-10-25", "2023-10-26", "2023-10-27"]
    temperatures = [10, 11, 15]
    temperatures = [input_days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)
