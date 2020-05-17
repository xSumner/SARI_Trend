import streamlit as st
from PIL import Image



def display():
    pass


hero_basic = {"美国队长": {"外文名": "", "身高": "", "体重": "", "": "", "": ""}, "罗宾": {}, "猫女": {}, "闪电侠": {}, "神奇女侠": {}, "鹰眼": {}, "蜘蛛侠": {}}





st.sidebar.title("2019 SuperHero年终总结")
st.sidebar.markdown('''---''')

option = st.sidebar.selectbox("请选择你想要了解的英雄：",
                              ("美国队长", "罗宾", "猫女", "闪电侠", "神奇女侠", "鹰眼", "蜘蛛侠"))

image = Image.open(option + '.png')
st.sidebar.image(image, caption=option, use_column_width=True)


