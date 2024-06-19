import streamlit as st
from PIL import Image


# 사이드 바 화면 구성
st.sidebar.title('Streamlit Sidebar')
st.sidebar.header('텍스트 입력 사용 예')
user_id = st.sidebar.text_input("ID 입력", value='streamlit', max_chars=15)
user_password = st.sidebar.text_input("Password 입력", value='abce', type="password")

st.sidebar.header('셀렉트박스 사용 예')
selectbox_options = ['진주 귀걸이를 한 소녀 ', '별이 빛나는 밤', '절규']

your_option = st.sidebar.selectbox("좋아하는 작품은?", selectbox_options)

st.sidebar.write('**당신의 선택**:', your_option)

# 메인 화면 구성
folder = './data/'
image_files = ['https://github.com/songhannaa/streamlit/blob/main/sidebar/data/Vermeer.png?raw=true',
                'https://github.com/songhannaa/streamlit/blob/main/sidebar/data/Gogh.png?raw=true',
                'https://github.com/songhannaa/streamlit/blob/main/sidebar/data/Munch.png?raw=true',
                'https://github.com/songhannaa/streamlit/blob/main/sidebar/data/ShinYoonbok.png?raw=true']
                
selectbox_options_index = selectbox_options.index(your_option)

image_file=image_files[selectbox_options_index]
image_local = Image.open(folder + image_file)
st.image(image_local, caption=your_option)
