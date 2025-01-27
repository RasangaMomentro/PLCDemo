# First these imports at the very top
import streamlit as st
import json
import requests
from typing import Optional

# Then all the constants
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "34d17c26-a986-4b87-a228-81e15a1ecc86"
FLOW_ID = "41118164-5374-4bdf-b00b-efa4689337b4"
APPLICATION_TOKEN = "your_application_token_here"  # Replace with your actual token

# Then the TWEAKS dictionary
TWEAKS = {
    "ChatInput-u4eIz": {},
    "ParseData-0DpNV": {},
    "Prompt-lnk6b": {},
    "OpenAIModel-V4AuE": {},
    "ChatOutput-ZSiwj": {},
    "AstraDB-j2HHt": {},
    "OpenAIEmbeddings-HiZAR": {}
}

# Then the run_flow function
def run_flow(message: str,
    endpoint: str = FLOW_ID,
    output_type: str = "chat",
    input_type: str = "chat",
    tweaks: Optional[dict] = TWEAKS) -> dict:
    # ... rest of the function ...

# Finally all the Streamlit UI code
st.set_page_config(...)
# ... rest of the Streamlit code ...
