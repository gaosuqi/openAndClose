# -*- coding: UTF-8 -*-
import pandas as pd
import streamlit as st

from main import main


def transform(x, length):
    day = [0] * length
    for i in x:
        day[i] = 1
    return day


def int2str(x):
    for i in range(len(x)):
        if x[i] == 0:
            x[i] = "关"
        else:
            x[i] = "开"
    return x


def show():
    st.title("开关井策略")
    with st.form("my_form"):
        amount = st.text_input(
            "请输入目标产量"
        )
        submitted = st.form_submit_button("生成策略")
        if submitted:
            amount = int(amount)
            if amount <= 0 or amount > 1200:
                st.write("请输入合法数据（大于0小于1200）")
            else:

                order, one_strategy, two_strategy, three_strategy, four_strategy, five_strategy, six_strategy, seven_strategy = \
                    main(amount)
                length = len(order)
                first_day = int2str(transform(one_strategy, length))
                second_day = int2str(transform(two_strategy, length))
                third_day = int2str(transform(three_strategy, length))
                fourth_day = int2str(transform(four_strategy, length))
                fifth_day = int2str(transform(five_strategy, length))
                sixth_day = int2str(transform(six_strategy, length))
                seventh_day = int2str(transform(seven_strategy, length))
                first_day_df = pd.DataFrame({
                    "Date": ["2022-08-09"] * length, "Well Name": order, "Status": first_day
                })
                second_day_df = pd.DataFrame({
                    "Date": ["2022-08-10"] * length, "Well Name": order, "Status": second_day
                })
                third_day_df = pd.DataFrame({
                    "Date": ["2022-08-11"] * length, "Well Name": order, "Status": third_day
                })
                fourth_day_df = pd.DataFrame({
                    "Date": ["2022-08-12"] * length, "Well Name": order, "Status": fourth_day
                })
                fifth_day_df = pd.DataFrame({
                    "Date": ["2022-08-13"] * length, "Well Name": order, "Status": fifth_day
                })
                sixth_day_df = pd.DataFrame({
                    "Date": ["2022-08-14"] * length, "Well Name": order, "Status": sixth_day
                })
                seventh_day_df = pd.DataFrame({
                    "Date": ["2022-08-15"] * length, "Well Name": order, "Status": seventh_day
                })
                df = pd.concat(
                    [first_day_df, second_day_df, third_day_df, fourth_day_df, fifth_day_df, sixth_day_df, seventh_day_df])
                st.table(df)


if __name__ == '__main__':
    show()

