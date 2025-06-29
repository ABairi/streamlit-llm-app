from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 【条件】

# 「app.py」にコードを記述してください。
# 画面に入力フォームを1つ用意し、入力フォームから送信したテキストをLangChainを使ってLLMにプロンプトとして渡し、回答結果が画面上に表示されるようにしてください。なお、当コースのLesson8を参考にLangChainのコードを記述してください。
# ラジオボタンでLLMに振る舞わせる専門家の種類を選択できるようにし、Aを選択した場合はAの領域の専門家として、またBを選択した場合はBの領域の専門家としてLLMに振る舞わせるよう、選択値に応じてLLMに渡すプロンプトのシステムメッセージを変えてください。また用意する専門家の種類はご自身で考えてください。
# 「入力テキスト」と「ラジオボタンでの選択値」を引数として受け取り、LLMからの回答を戻り値として返す関数を定義し、利用してください。
# Webアプリの概要や操作方法をユーザーに明示するためのテキストを表示してください。
# Streamlit Community Cloudにデプロイする際、Pythonのバージョンは「3.11」としてください。

def get_expert_response(input_text: str, expert_type: str) -> str:
    # LLMの初期化
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    # システムメッセージの設定
    if expert_type == "AIアシスタント":
        system_message = SystemMessage(content="あなたはAIアシスタントの専門家です。")
    elif expert_type == "データサイエンティスト":
        system_message = SystemMessage(content="あなたはデータサイエンティストの専門家です。")

    # ユーザーメッセージの設定
    user_message = HumanMessage(content=input_text)

    # メッセージのリストを作成
    messages = [system_message, user_message]

    # LLMにプロンプトを渡して応答を取得
    response = llm(messages)

    return response.content

# Streamlitアプリの設定
st.title("専門家に質問するアプリ")
st.write("このアプリでは、専門家に質問を投げかけることができます。以下のフォームに質問を入力し、専門家の種類を選択してください。") 
expert_type = st.radio(
    "専門家の種類を選択してください:",
    ("AIアシスタント", "データサイエンティスト")
)

input_text = st.text_area("質問を入力してください:")

if st.button("送信"):
    response = get_expert_response(input_text, expert_type)
    st.write("専門家の回答:")
    st.write(response)