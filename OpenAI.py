import streamlit as st
import os
from openai import OpenAI

# .env 는 streamlit으로 배포할 때는 쓸 수 없다
# .streamlit 폴더를 만든 뒤 그 안에 secrets.toml 파일을 생성하고...
# api_key = ... 의 형식으로 입력한다.

os.environ["OPENAI_API_KEY"] = st.secrets["api_key"]
st.title("이미지 생성기입니다.")

with st.form("form"):
    user_input = st.text_input("그리고 싶은 그림은?")
    size = st.selectbox("size", ["1024x1024", "512x512", "256x256"])
    submit = st.form_submit_button("Submit")

# st.button("클릭")


if submit and user_input:
    gpt_prompt = [
        {
            "role": "system",
            "content": "Imagine the detailed appearance of the input. The response should be around 15 words.",
        }
    ]

    gpt_prompt.append({"role": "user", "content": user_input})

    client = OpenAI()

    with st.spinner("Waiting for ChatGPT..."):
        gpt_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt,
        )

    dalle_prompt = gpt_response.choices[0].message.content
    st.write("dall-e prompt:", dalle_prompt)

    with st.spinner("Waiting for DALL-E..."):
        dalle_response = client.images.generate(
            model="dall-e-2", prompt=dalle_prompt, size="1024x1024"
        )

    st.image(dalle_response.data[0].url)
