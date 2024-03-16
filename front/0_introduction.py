import logging
import sys
import streamlit as st
import webbrowser
import requests

sys.path.append("./")
sys.path.append("./back")
from back.config import *   #IP, PORT 얻어오기 위해 import

# 로거 초기화
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# 페이지 제목 및 설명
st.title('안녕자비스 - 면접 챗봇 서비스')
st.markdown('## 언제든 면접 연습을 할 수 있는 인공지능 면접 챗봇 서비스입니다.')

# 시작하기 버튼
if st.button('시작하기'):
    url = f"http://{OUTSIDE_IP}:{PORT}/kakao"
    response = requests.get(url)
    if response.status_code == 200:
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={url}">', unsafe_allow_html=True)
        st.stop()  # 현재 페이지 중지
    else:
        st.error('리디렉션 실패')
    
# 비회원 버튼
if st.button('GUEST'):
    url = f"http://{OUTSIDE_IP}:{PORT}/launch_streamlit_app"
    response = requests.get(url)
    if response.status_code == 200:
        st.markdown(f'<meta http-equiv="refresh" content="0;URL={url}">', unsafe_allow_html=True)
        st.stop()  # 현재 페이지 중지
    else:
        st.error('리디렉션 실패')
