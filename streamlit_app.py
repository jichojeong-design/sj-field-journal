"""Streamlit entry point. Journal records stay in the browser until Google transfer."""
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="SJ 현장일지", page_icon="📋", layout="centered", initial_sidebar_state="collapsed")
st.markdown("""<style>
header[data-testid="stHeader"] {display:none;}
.stMainBlockContainer {max-width:500px;padding:0 0 1rem;}
</style>""", unsafe_allow_html=True)

# Only the bundled application is embedded; no user-supplied HTML is executed.
st.iframe(Path(__file__).with_name("journal.html"), height="content", alt="SJ 현장일지 입력 및 기록 조회")
