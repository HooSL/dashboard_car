from seaborn.axisgrid import pairplot
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app():
    #서브헤더
    st.subheader('EDA화면 입니다.')

    #1. csv파일 가져오기
    df = pd.read_csv('data/Car_purchasing_Data.csv',encoding='ISO-8859-1')

    #2. 3개중 하나 선택하는 동그란 버튼 설정
    radio_menu = ['데이터 프레임','통계치']
    selected_radio = st.radio('선택하세요.',radio_menu)

    #2-1. 데이터 프레임 체크할때
    if selected_radio == '데이터 프레임' :
        st.dataframe(df)
    #2-2. 통계치 체크할때
    elif selected_radio == '통계치':
        st.dataframe(df.describe())

    #3. 컬럼을 선택하면 해당 컬럼들만 데이터프레임 표시하는 화면
    selected_columns = st.multiselect('컬럼을 선택하세요.', df.columns)

    #3-1. 0라는건 유저가 선택을 안했다는 뜻이지만 선택을 했을 경우 !=
    if len(selected_columns) != 0:
        st.dataframe(df[selected_columns])

    #3-2. 유저가 컬럼을 선택 안했을 경우
    else:
        st.write('선택한 컬럼이 없습니다.')

    #4. 상관계수 분석을 위한, 상관계수 보여주는 화면 개발
    st.subheader('상관계수')
    #st.dataframe(df.corr()) #문자열도 다나오기 떄문제 주석처리

    #4-1. 숫자만 처리하자
    df_corr = df.iloc[ : , 3 : ]
    selected_corr = st.multiselect('상관계수 컬럼 선택',df_corr.columns)

    #4-2. 유저가 1개라도 선택했을 경우
    if len(selected_corr)>0:
        st.dataframe(df_corr[selected_corr].corr())

        #4-3. 상관계수를 수치로도 구하고, 차트로도 표시해라
        fig1 = sns.pairplot(data = df_corr[selected_corr])
        st.pyplot(fig1)

    #4-3. 유저가 컬럼을 선택하지 않은 경우
    else :
        st.write('선택한 컬럼이 없습니다.')


    #5. 유저가 컬럼을 선택하면 해당 컬럼의 min과 max에 해당하는 사람이 누구인지 그 사람의 데이터를 화면에 보여주는 기능 개발
    st.subheader('최소,최대값')

    #5-1. 문자열 데이터가 아닌 컬럼들만 가여오는 코드
    # 컬럼중 문자열이 아닌걸 True, False 로 출력: print(df.dtypes != object)
    #위 추려낸 컬럼을 컬럼들로 출력: print(df.columns[df.dtypes != object])
    number_colums = df.columns[df.dtypes != object]
    selected_minmax_columes = st.selectbox('최소,최대값 컬럼 선택',number_colums)

    #5-2. 선택한 컬럼의 최소값에 해당되는 사람의 데이터 출력
    min_data = df.loc[df[selected_minmax_columes] == df[selected_minmax_columes].min(),]
    st.dataframe(min_data)

    #5-3. 선택한 컬럼의 최대값에 해당되는 사람의 데이터 출력
    max_data = df.loc[df[selected_minmax_columes] == df[selected_minmax_columes].max(),]
    st.dataframe(max_data)

    #6. 고객의 이름을 검색할 수 있는 기능 개발
    st.subheader('사람 검색')

    #6-1. 유저에게 검색어를 입력 받습니다.
    word = st.text_input('검색어를 입력하세요')
    word.lower() #검색을 위해 소문자로 바꾼다

    #6-2. 검색어를 데이터 프레임의 Customer Name컬럼에서 검색해서 가져온다
    df_search = df.loc[df['Customer Name'].str.lower().str.contains(word),]

    #6-3. 화면에 결과를 보여준다.
    st.dataframe(df_search)











