from transformers import pipeline
import streamlit as st

st.title("감성분류기")
input = st.text_input("당신의 기분을 입력하세요.")
st.button("클릭")

sentiment_analysis = pipeline(
    "sentiment-analysis", model="monologg/koelectra-base-finetuned-nsmc"
)

result = sentiment_analysis(input)[0]["label"]

with st.spinner():  # 로딩 시 회전 애니메이션
    if result == "positive":
        st.write("-----" * 30)
        st.write("입력값:", input)
        st.info("자네 생각이 건강하구만")
    else:
        st.write("-----" * 30)
        st.write("입력값:", input)
        st.info("뭐래? 힘내야지")
