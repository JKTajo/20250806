{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNMY/Q1aQ64z4Vkp0pq1eRr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JKTajo/20250806/blob/main/Seoulbike.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "wC3bH50cJNma",
        "outputId": "a7190539-cd0c-4637-cc69-1ca85e3fd3a8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipython-input-4270648171.py:10: DeprecationWarning: load_dataset is deprecated and will be removed in a future version.\n",
            "  df = kagglehub.load_dataset(\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "First 5 records:          Date  Rented Bike Count  Hour  Temperature(°C)  Humidity(%)  \\\n",
            "0  01/12/2017                254     0             -5.2           37   \n",
            "1  01/12/2017                204     1             -5.5           38   \n",
            "2  01/12/2017                173     2             -6.0           39   \n",
            "3  01/12/2017                107     3             -6.2           40   \n",
            "4  01/12/2017                 78     4             -6.0           36   \n",
            "\n",
            "   Wind speed (m/s)  Visibility (10m)  Dew point temperature(°C)  \\\n",
            "0               2.2              2000                      -17.6   \n",
            "1               0.8              2000                      -17.6   \n",
            "2               1.0              2000                      -17.7   \n",
            "3               0.9              2000                      -17.6   \n",
            "4               2.3              2000                      -18.6   \n",
            "\n",
            "   Solar Radiation (MJ/m2)  Rainfall(mm)  Snowfall (cm) Seasons     Holiday  \\\n",
            "0                      0.0           0.0            0.0  Winter  No Holiday   \n",
            "1                      0.0           0.0            0.0  Winter  No Holiday   \n",
            "2                      0.0           0.0            0.0  Winter  No Holiday   \n",
            "3                      0.0           0.0            0.0  Winter  No Holiday   \n",
            "4                      0.0           0.0            0.0  Winter  No Holiday   \n",
            "\n",
            "  Functioning Day  \n",
            "0             Yes  \n",
            "1             Yes  \n",
            "2             Yes  \n",
            "3             Yes  \n",
            "4             Yes  \n"
          ]
        }
      ],
      "source": [
        "# Install dependencies as needed:\n",
        "# pip install kagglehub[pandas-datasets]\n",
        "import kagglehub\n",
        "from kagglehub import KaggleDatasetAdapter\n",
        "\n",
        "# Set the path to the file you'd like to load\n",
        "file_path = \"SeoulBikeData.csv\"\n",
        "\n",
        "# Load the latest version\n",
        "df = kagglehub.load_dataset(\n",
        "  KaggleDatasetAdapter.PANDAS,\n",
        "  \"saurabhshahane/seoul-bike-sharing-demand-prediction\",\n",
        "  file_path,\n",
        "  pandas_kwargs={'encoding': 'ISO-8859-1'}\n",
        "  # Provide any additional arguments like\n",
        "  # sql_query or pandas_kwargs. See the\n",
        "  # documenation for more information:\n",
        "  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas\n",
        ")\n",
        "\n",
        "print(\"First 5 records:\", df.head())"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4c1ced7c",
        "outputId": "fc3654bf-723f-4d5b-d33e-459520295227"
      },
      "source": [
        "!pip install streamlit -q\n",
        "!pip install pyngrok"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.9/9.9 MB\u001b[0m \u001b[31m2.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m4.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m4.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pyngrok\n",
            "  Downloading pyngrok-7.3.0-py3-none-any.whl.metadata (8.1 kB)\n",
            "Requirement already satisfied: PyYAML>=5.1 in /usr/local/lib/python3.11/dist-packages (from pyngrok) (6.0.2)\n",
            "Downloading pyngrok-7.3.0-py3-none-any.whl (25 kB)\n",
            "Installing collected packages: pyngrok\n",
            "Successfully installed pyngrok-7.3.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 585
        },
        "id": "1e051889",
        "outputId": "41a881dd-a4d0-4cd4-a4bf-45ce77f6d500"
      },
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "# Terminate open tunnels if any\n",
        "ngrok.kill()\n",
        "\n",
        "# Setting the authtoken (optional)\n",
        "# Get your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken\n",
        "NGROK_AUTH_TOKEN = \"YOUR_NGROK_AUTH_TOKEN\"  #@param {type:\"string\"}\n",
        "ngrok.set_auth_token(NGROK_AUTH_TOKEN)\n",
        "\n",
        "# Open a http tunnel on the default port 8501\n",
        "public_url = ngrok.connect(8501)\n",
        "print(f\"Streamlit app is running at: {public_url}\")"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": []
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "ERROR:pyngrok.process.ngrok:t=2025-08-06T05:59:26+0000 lvl=eror msg=\"failed to reconnect session\" obj=tunnels.session err=\"authentication failed: Usage of ngrok requires a verified account and authtoken.\\n\\nSign up for an account: https://dashboard.ngrok.com/signup\\nInstall your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken\\r\\n\\r\\nERR_NGROK_4018\\r\\n\"\n",
            "ERROR:pyngrok.process.ngrok:t=2025-08-06T05:59:26+0000 lvl=eror msg=\"session closing\" obj=tunnels.session err=\"authentication failed: Usage of ngrok requires a verified account and authtoken.\\n\\nSign up for an account: https://dashboard.ngrok.com/signup\\nInstall your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken\\r\\n\\r\\nERR_NGROK_4018\\r\\n\"\n",
            "ERROR:pyngrok.process.ngrok:t=2025-08-06T05:59:26+0000 lvl=eror msg=\"terminating with error\" obj=app err=\"authentication failed: Usage of ngrok requires a verified account and authtoken.\\n\\nSign up for an account: https://dashboard.ngrok.com/signup\\nInstall your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken\\r\\n\\r\\nERR_NGROK_4018\\r\\n\"\n",
            "CRITICAL:pyngrok.process.ngrok:t=2025-08-06T05:59:26+0000 lvl=crit msg=\"command failed\" err=\"authentication failed: Usage of ngrok requires a verified account and authtoken.\\n\\nSign up for an account: https://dashboard.ngrok.com/signup\\nInstall your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken\\r\\n\\r\\nERR_NGROK_4018\\r\\n\"\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "PyngrokNgrokError",
          "evalue": "The ngrok process errored on start: authentication failed: Usage of ngrok requires a verified account and authtoken.\\n\\nSign up for an account: https://dashboard.ngrok.com/signup\\nInstall your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken\\r\\n\\r\\nERR_NGROK_4018\\r\\n.",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mPyngrokNgrokError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-474601746.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     10\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0;31m# Open a http tunnel on the default port 8501\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 12\u001b[0;31m \u001b[0mpublic_url\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mngrok\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m8501\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     13\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Streamlit app is running at: {public_url}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pyngrok/ngrok.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(addr, proto, name, pyngrok_config, **options)\u001b[0m\n\u001b[1;32m    383\u001b[0m     \u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minfo\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Opening tunnel named: {name}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    384\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 385\u001b[0;31m     \u001b[0mapi_url\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mget_ngrok_process\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpyngrok_config\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mapi_url\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    386\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    387\u001b[0m     \u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Creating tunnel with options: {options}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pyngrok/ngrok.py\u001b[0m in \u001b[0;36mget_ngrok_process\u001b[0;34m(pyngrok_config)\u001b[0m\n\u001b[1;32m    201\u001b[0m     \u001b[0minstall_ngrok\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpyngrok_config\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    202\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 203\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mprocess\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_process\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpyngrok_config\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    204\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    205\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pyngrok/process.py\u001b[0m in \u001b[0;36mget_process\u001b[0;34m(pyngrok_config)\u001b[0m\n\u001b[1;32m    269\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0m_current_processes\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mpyngrok_config\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mngrok_path\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    270\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 271\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0m_start_process\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpyngrok_config\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    272\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    273\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/pyngrok/process.py\u001b[0m in \u001b[0;36m_start_process\u001b[0;34m(pyngrok_config)\u001b[0m\n\u001b[1;32m    445\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    446\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mngrok_process\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstartup_error\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 447\u001b[0;31m             raise PyngrokNgrokError(f\"The ngrok process errored on start: {ngrok_process.startup_error}.\",\n\u001b[0m\u001b[1;32m    448\u001b[0m                                     \u001b[0mngrok_process\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlogs\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    449\u001b[0m                                     ngrok_process.startup_error)\n",
            "\u001b[0;31mPyngrokNgrokError\u001b[0m: The ngrok process errored on start: authentication failed: Usage of ngrok requires a verified account and authtoken.\\n\\nSign up for an account: https://dashboard.ngrok.com/signup\\nInstall your authtoken: https://dashboard.ngrok.com/get-started/your-authtoken\\r\\n\\r\\nERR_NGROK_4018\\r\\n."
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7170c635"
      },
      "source": [
        "# Colab에서 app.py 파일로 저장하기\n",
        "code = '''\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from kagglehub import load_dataset, KaggleDatasetAdapter\n",
        "\n",
        "# ✅ KaggleHub로 데이터 불러오기\n",
        "@st.cache_data\n",
        "def load_data():\n",
        "    df = load_dataset(\n",
        "        adapter=KaggleDatasetAdapter.PANDAS,\n",
        "        dataset=\"saurabhshahane/seoul-bike-sharing-demand-prediction\",\n",
        "        file=\"SeoulBikeData.csv\",\n",
        "        pandas_kwargs={\"encoding\": \"ISO-8859-1\"}\n",
        "    )\n",
        "    return df\n",
        "\n",
        "df = load_data()\n",
        "\n",
        "# ✅ 사이드바\n",
        "st.sidebar.title(\"🚲 서울 자전거 수요 예측\")\n",
        "st.sidebar.subheader(\"Kaggle 데이터 기반\")\n",
        "st.sidebar.markdown(\n",
        "    \"\"\"\n",
        "    이 앱은 서울의 자전거 대여 수요 데이터를 시각화하고,\n",
        "    사용자 입력에 따라 특정 인덱스 데이터를 확인할 수 있는 기능을 제공합니다.\n",
        "    \"\"\"\n",
        ")\n",
        "\n",
        "# ✅ 탭\n",
        "tab1, tab2, tab3 = st.tabs([\"📌 요약\", \"📊 전체 데이터 보기\", \"🔍 인덱스별 분석\"])\n",
        "\n",
        "# 📌 Tab 1: 요약\n",
        "with tab1:\n",
        "    st.header(\"📌 데이터 요약\")\n",
        "    st.dataframe(df.head())\n",
        "    st.dataframe(df.describe())\n",
        "\n",
        "# 📊 Tab 2: 전체 데이터 보기\n",
        "with tab2:\n",
        "    st.header(\"📊 전체 데이터 보기\")\n",
        "    st.dataframe(df)\n",
        "\n",
        "# 🔍 Tab 3: 인덱스 분석\n",
        "with tab3:\n",
        "    st.header(\"🔍 인덱스별 분석 및 시각화\")\n",
        "    sort_column = st.selectbox(\"정렬할 컬럼을 선택하세요\", df.columns)\n",
        "    ascending = st.radio(\"정렬 방식\", (\"오름차순\", \"내림차순\")) == \"오름차순\"\n",
        "    sorted_df = df.sort_values(by=sort_column, ascending=ascending)\n",
        "\n",
        "    st.subheader(\"🎯 대여량 히스토그램\")\n",
        "    if 'Rented Bike Count' in df.columns:\n",
        "        fig, ax = plt.subplots()\n",
        "        sns.histplot(sorted_df['Rented Bike Count'], bins=30, kde=True, ax=ax)\n",
        "        st.pyplot(fig)\n",
        "    else:\n",
        "        st.warning(\"'Rented Bike Count' 컬럼이 존재하지 않습니다.\")\n",
        "\n",
        "    index_input = st.number_input(\"확인할 인덱스를 입력하세요\", min_value=0, max_value=len(df)-1, value=0, step=1)\n",
        "    st.dataframe(sorted_df.iloc[[int(index_input)]])\n",
        "'''\n",
        "\n",
        "with open(\"app.py\", \"w\") as f:\n",
        "    f.write(code)"
      ],
      "execution_count": 15,
      "outputs": []
    }
  ]
}
