# ----------------------------------------
# 1. Kaggle API Key 설정
# ----------------------------------------
import os

os.makedirs("/root/.kaggle", exist_ok=True)

# Kaggle API 키 저장
with open("/root/.kaggle/kaggle.json", "w") as f:
    f.write('{"username":"jk3571","key":"93ef00e30dac8d800b648ba7ed8bc597"}')

os.chmod("/root/.kaggle/kaggle.json", 600)



# ----------------------------------------
# 4. Streamlit 앱 코드 작성
# ----------------------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
@st.cache_data
def load_data():
    return pd.read_csv("SeoulBikeData.csv", encoding="ISO-8859-1")

df = load_data()

# 사이드바
st.sidebar.title("🚲 서울 자전거 데이터 분석")
st.sidebar.markdown("Kaggle 데이터 기반 웹앱")

# 탭
tab1, tab2, tab3 = st.tabs(["📌 전체 데이터", "🔍 인덱스 조회", "📊 그래프 분석"])

# 1️⃣ 전체 데이터
with tab1:
    st.header("📌 전체 데이터")
    st.dataframe(df)

# 2️⃣ 인덱스 조회
with tab2:
    st.header("🔍 인덱스 조회")
    index = st.number_input("인덱스 선택", min_value=0, max_value=len(df)-1, value=0, step=1)
    st.write(df.iloc[[index]])

# 3️⃣ 그래프 분석
with tab3:
    st.header("📊 대여량 히스토그램")
    index = st.number_input("그래프에 표시할 인덱스", min_value=0, max_value=len(df)-1, value=0, step=1, key="graph_index")
    fig, ax = plt.subplots()
    sns.histplot(df["Rented Bike Count"], bins=30, kde=True, ax=ax)
    ax.axvline(df.loc[index, "Rented Bike Count"], color="red", linestyle="--", label=f"Index {index}")
    ax.legend()
    st.pyplot(fig)
