import os, re, json
from pathlib import Path
import pdfplumber
import pandas as pd
import streamlit as st
import openai
from openai import AzureOpenAI
import datetime
from dotenv import load_dotenv
import utils_async


load_dotenv()

deployement_name=os.getenv("deployement_name")
api_type=os.getenv("api_type")
api_base=os.getenv("api_base")
api_version=os.getenv("api_version")
api_key=os.getenv("api_key")
model=os.getenv("model")

# Set page config
st.set_page_config(page_title="Resume Analyzer", page_icon=":scroll:", layout="wide")

# Configure OpenAI API
openai.api_type = api_type
openai.api_base = api_base
openai.api_version = api_version
openai.api_key = api_key


if __name__ == "__main__":
    utils_async.main()
 