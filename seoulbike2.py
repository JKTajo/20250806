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

# 탭 생성
tab1, tab2, tab3 = st.tabs(["📌 전체 데이터", "🔍 인덱스 조회", "📊 그래프 분석"])

# 1️⃣ 전체 데이터
with tab1:
    st.header("📌 전체 데이터 보기")
    st.dataframe(df)

# 2️⃣ 인덱스 조회
with tab2:
    st.header("🔍 인덱스별 데이터 조회")
    index = st.number_input("인덱스 선택", min_value=0, max_value=len(df)-1, value=0, step=1)
    st.write(df.iloc[[index]])

# 3️⃣ 그래프 분석
with tab3:
    st.header("📊 대여량 히스토그램")

    # 컬럼명 확인 후 공백 제거
    df.columns = df.columns.str.strip()

    index = st.number_input(
        "그래프에 표시할 인덱스",
        min_value=0,
        max_value=len(df)-1,
        value=0,
        step=1,
        key="graph_index"
    )

    # 안전하게 컬럼 불러오기
    if "Rented Bike Count" in df.columns:
        fig, ax = plt.subplots()
        sns.histplot(df["Rented Bike Count"], bins=30, kde=True, ax=ax)
        ax.axvline(
            df.loc[index, "Rented Bike Count"],
            color="red",
            linestyle="--",
            label=f"Index {index}"
        )
        ax.legend()
        st.pyplot(fig)
    else:
        st.error("❌ 'Rented Bike Count' 컬럼을 찾을 수 없습니다. CSV 컬럼명을 확인하세요.")

