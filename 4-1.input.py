# streamlit 라이브러리와 datetime 모듈 불러오기
import streamlit as st
from datetime import datetime  

st.title('Unit 4. Input Widgets')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/widgets')

st.header('### 1. Button')
if st.button('Say hello'):
    st.write('Hello')
else:
    st.write('Goodbye')


st.header('### 2. Radio button')
genre = st.radio('좋아하는 영화 장르를 선택하세요',
                 ('코미디', 'SF', '액션'))

if genre == '코미디':
    st.write('코미디 유쾌하신 분이시군요')
elif genre == 'SF':
    st.write('저도 SF 좋아합니다')
else:
    st.write('멋지십니다.')

    
st.header('### 3. Checkbox')
agree = st.checkbox('I agree')
if agree:
    st.write(':smile:'*10)

    
st.header('### 4. Select box')
option = st.selectbox(
    '어떻게 연락 드릴까요?',
    ('Email', 'Mobile phone', 'Office phone'))
st.write('네', option, '잘 알겠습니다')


st.header('### 5. Multi select')
options = st.multiselect(
          '좋아하는 색을 모두 선택하세요',
          ['Green', 'Yellow', 'Red', 'Blue'],
          ['Yellow', 'Red'])
st.write('선호 색상:')
for i in options:
    st.write(i)


st.header('### 6. Input: Text/Number')
st.subheader('**_text_input_**')
title = st.text_input('write down favorite movie',
                      '신세계')
st.write('Your favorite movie is :', title)


st.subheader('**_number_input_**')
number =  st.number_input('Insert a number(1-10)',
                          min_value=1,
                          max_value=10,
                          value=5,
                          step=1)
st.write('The current number is', number)


st.header('### 7. Date input')
ymd = st.date_input('When is your birthday',
                    datetime(1994, 1, 8))
st.write('Your birthday is:', ymd)


st.header('### 8. Slider')

st.subheader('**_Slider- 이전 구간_**')
age = st.slider('나이가 어떻게 되세요 ? ', 0, 130, 25)
st.write('I m ', age, ' years old')

st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
values = st.slider('값 구간을 선택하세요 ', 0.0, 100.0, (25.0, 75.0))
st.write('Values: ', values)

st.subheader('**_년 월 일 사이 구간_**')

slider_date = st.slider('날짜 구간을 선택하세요',
                        min_value=datetime(2022, 1, 1),
                        max_value=datetime(2022, 12, 31),
                        value=(datetime(2022, 6, 1), datetime(2022, 7, 31)),
                        format='YY/MM/DD')
st.write('구간 날짜:', slider_date)
st.write('min date:', slider_date[0], 'max date:', slider_date[1])


# 년 월 일 시 사이 구간
# slider_time = st.slider(
#     'Select a range of datetime?',
#     datetime(2022, 1, 1, 0, 30), datetime(2022, 12, 31, 0, 30),
#     value=(datetime(2022, 7, 1, 0, 30), datetime(2022, 10, 31, 9, 30)),
#     format='MM/DD/YY - hh:mm')
# st.write('Slider time: ', slider_time)

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\4-1.input.py