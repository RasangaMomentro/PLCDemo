import streamlit as st
import json
import requests
from typing import Optional

# Constants from your API code
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "34d17c26-a986-4b87-a228-81e15a1ecc86"
FLOW_ID = "41118164-5374-4bdf-b00b-efa4689337b4"
APPLICATION_TOKEN = "your_application_token_here"  # Replace with your actual token

# Your existing TWEAKS dictionary
TWEAKS = {
    "ChatInput-u4eIz": {},
    "ParseData-0DpNV": {},
    "Prompt-lnk6b": {},
    "OpenAIModel-V4AuE": {},
    "ChatOutput-ZSiwj": {},
    "AstraDB-j2HHt": {},
    "OpenAIEmbeddings-HiZAR": {}
}

def run_flow(message: str,
    endpoint: str = FLOW_ID,
    output_type: str = "chat",
    input_type: str = "chat",
    tweaks: Optional[dict] = TWEAKS) -> dict:
    
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"
    
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    
    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }
    
    if tweaks:
        payload["tweaks"] = tweaks
        
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Remove the ... and add proper indentation for all Streamlit UI code
st.set_page_config(
    page_title="People's Leasing PLC Investment Assistant",
    page_icon="💼",
    layout="centered"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Header
st.title("People's Leasing PLC Investment Assistant")
st.markdown("Ask me anything about People's Leasing PLC's financial performance and investment opportunities.")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = run_flow(prompt)
            if "error" in response:
                st.error(f"Error: {response['error']}")
            else:
                # Extract the actual response text from your Langflow response
                response_text = response.get("output", "No response received")
                st.markdown(response_text)
                st.session_state.messages.append({"role": "assistant", "content": response_text})

# Footer
st.markdown("---")
st.markdown("*Data source: People's Leasing PLC Annual Report FY2024*")

# Optional: Add a button to clear chat history
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()
