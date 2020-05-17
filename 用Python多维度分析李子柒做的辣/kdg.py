#!/usr/bin/python
# -*- coding: UTF-8 -*-

import streamlit as st
from PIL import Image


# 起始界面
def status_a():
    image_lx = Image.open('lu_xun.jpg')
    my_placeholder4.image(image_lx, caption='', use_column_width=True)


# 口令错误界面
def status_b(url):
    my_placeholder0.empty()
    my_placeholder1.empty()
    my_placeholder4.empty()
    # 播放搞笑视频
    video_file = open(url, 'rb')
    video_bytes = video_file.read()
    my_placeholder2.video(video_bytes)


# 口令通过界面
def status_c():
    my_placeholder0.title("用Python多维度分析李子柒做的辣酱")
    my_placeholder1.empty()
    my_placeholder2.empty()
    pass




if __name__ == '__main__':
    # 占空符号
    my_placeholder0 = st.empty()
    my_placeholder1 = st.empty()
    my_placeholder2 = st.empty()
    my_placeholder3 = st.empty()
    my_placeholder4 = st.empty()

    # 设置密码
    my_placeholder0.header("您想对对鲁迅说什么？")
    h=my_placeholder1.text_input("")

    # 设置跳转状态量
    status_a()
    if h == '烤地瓜':
        status_b('kdg.mp4')
    if h == '我兄弟':
        status_b('wxd.mp4')


