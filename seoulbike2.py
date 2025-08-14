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
# 2. 필요한 라이브러리 설치
# ----------------------------------------
!pip install pandas matplotlib seaborn streamlit kaggle

# ----------------------------------------
# 3. Kaggle에서 데이터 다운로드
# ----------------------------------------
!kaggle datasets download -d saurabhshahane/seoul-bike-sharing-demand-prediction -p ./data
!unzip -o ./data/seoul-bike-sharing-demand-prediction.zip -d ./data

# ----------------------------------------
# 4. Streamlit 앱 코드 작성
# ----------------------------------------
app_code = '''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("./data/SeoulBikeData.csv", encoding="ISO-8859-1")
    return df

df = load_data()

# 사이드바 제목
st.sidebar.title("🚲 서울 자전거 수요 분석")

# 탭 구성
tab1, tab2, tab3 = st.tabs(["📄 원본 데이터", "🔍 인덱스 검색", "📊 인덱스 기반 그래프"])

# 📄 첫 번째 탭 - 원본 데이터
with tab1:
    st.header("📄 원본 데이터")
    st.dataframe(df)

# 🔍 두 번째 탭 - 인덱스 검색
with tab2:
    st.header("🔍 인덱스 검색")
    index_input = st.number_input("확인할 인덱스 번호 입력", min_value=0, max_value=len(df)-1, value=0, step=1)
    st.dataframe(df.iloc[[int(index_input)]])

# 📊 세 번째 탭 - 인덱스 기반 그래프
with tab3:
    st.header("📊 인덱스 기반 그래프")
    index_input_graph = st.number_input("그래프를 그릴 인덱스 번호 입력", min_value=0, max_value=len(df)-1, value=0, step=1)
    row_data = df.iloc[int(index_input_graph)]

    # 예시: 대여량, 온도, 습도, 풍속 시각화
    features = ["Rented Bike Count", "Temperature(°C)", "Humidity(%)", "Wind speed (m/s)"]
    available_features = [f for f in features if f in df.columns]

    if available_features:
        fig, ax = plt.subplots()
        sns.barplot(x=available_features, y=row_data[available_features], ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("그래프를 그릴 수 있는 수치형 컬럼이 없습니다.")
'''

with open("app.py", "w") as f:
    f.write(app_code)

# ----------------------------------------
# 5. requirements.txt 작성
# ----------------------------------------
reqs = '''
streamlit
pandas
matplotlib
seaborn
kaggle
'''
with open("requirements.txt", "w") as f:
    f.write(reqs)

print("✅ app.py와 requirements.txt 생성 완료")
