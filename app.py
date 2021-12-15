import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

from eda_app import run_eda_app

def main():
    
    #제목
    st.title('자동차 가격 예측')

    #사이드바 메뉴
    menu = ['home','EDA','ML']
    choice = st.sidebar.selectbox('메뉴',menu)

    #사이드바 설정
    if choice == 'home':
        st.write('이 앱은 고객데이터와 자동차 구매에 대한 내용입니다. 고객의 정보를 입력하면, 얼마정도의 차량을 구매할 수 있는지 예측해줍니다.')
        st.write('왼쪽의 사이드바에서 선택하세요.')
    #새로운 py파일에 함수를 만들어주고 온다
    elif choice =='EDA':
        run_eda_app()
    #
    #
    #
    #
    #
    #
    #
    #






















if __name__ == '__main__':
    main()