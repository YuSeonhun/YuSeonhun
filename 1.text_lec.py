import streamlit as st
import pandas as pd

st.markdown('# Unit 1. Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')

# title, header, subheader, caption
st.markdown('## 1. Title, Header, Subheader, Caption')

st.title('this is the title')
st.header('this is the header')
st.subheader('this is the subheader')
st.text('this is the text')
st.caption('Caption in small font')

st.text('■ item 1\n'
            '   ◆ item 1.1\n'
            '   ◆ item 1.2\n'
            '      - item 1.2.1\n'
            '■ item 2')

st.text('1. item 1\n'
        '   1.1 item 1.1\n'
        '   1.2 item 1.2\n'
        '      1.2.1 item 1.2.1\n'
        '2. item 2')

# Markdown 
st.markdown('## 2. Markdown')

st.markdown('# This is a Markdown title')
st.markdown('## This is a Markdown header')
st.markdown('### This is a Markdown subheader')
st.markdown('This is the markdown')
st.markdown('This is **the markdown 진하게**')
st.markdown('This is _the markdown 기울임_')
st.markdown('This is **_the markdown 진하고 기울임_** ')

st.markdown('- item 1\n'
            '   - item 1.1\n'
            '   - item 1.2\n'
            '      - item 1.2.1\n'
            '- item 2')

st.markdown('1. item 1\n'
            '   1. item 1.1\n'
            '   2. item 1.2\n'
            '      1. item 1.2.1\n'
            '2. item 2')

st.title('_who made it!_')
st.subheader('it was stunning~')
st.caption('## i need a hand')
code = '''Hello streamlit'''
st.code(code, language='python')

# code, latex-수학식 표현
st.markdown('## 3. Code, Latex')

st.code('x=2021')
st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right) ''') 

# String, data_frame, chart, graph, LaTex 등의 objects를 App에  출력할 수 있다.
# st.markdown('## 4. Write')
st.title('write')
st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')

st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')
# st.write('this is a string write')
# st.write('Hello, *World!* 😎')

df = pd.DataFrame({'이;름': ['홍길동', '김사랑', '이지매', '이루리'],'수준': ['금', '동', '은', '은']})
st.write('딕셔너리를 판다스의 데이터프레임으로 바꿔서:', df, '스트림릿의 write함수로 표현')

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\1.text_lec.py