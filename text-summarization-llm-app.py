import boto3
import json
import streamlit as st

bedrock = boto3.client(service_name="bedrock-runtime", region_name='us-east-1')

prompt = """

[INST]You are a summarization system that can provide a summary with a confidence score. In clear and concise language 600 words or less provide a short summary of the following text, along with a confidence score. Do not provide explanations.[/INST]

{Composition}

"""

modelId = "mistral.mistral-large-2402-v1:0"

accept = "application/json"
contentType = "application/json"


def streamlit_ui():
    st.set_page_config("Text Summarization LLM Application")

    st.markdown("""
        <style>
            .reportview-container {
                margin-top: -2em;
            }
            #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
            footer {visibility: hidden;}
            #stDecoration {display:none;}
        </style>
    """, unsafe_allow_html=True)

    st.header("Text Summarization LLM Application")

    user_input = st.text_area("Text to summarize.", height=300)

    if st.button("Summarize Now") or user_input:
        if not user_input:
            st.error("Please provide text to summarize.")
            return
        with st.spinner("Summarizing..."):
            completed_prompt = prompt.format(Composition=user_input)
            body = json.dumps({
                "prompt": completed_prompt,
                "max_tokens": 3072,
                "top_p": 0.8,
                "temperature": 0.5,
            })
            response = bedrock.invoke_model(
                body=body,
                modelId=modelId,
                accept=accept,
                contentType=contentType
            )
            response_json = json.loads(response["body"].read())
            text = response_json['outputs'][0]['text']
            st.write(text)
            st.success('Summary Completed!')


if __name__ == "__main__":
    streamlit_ui()
