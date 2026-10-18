import re 
from collections import Counter
import streamlit as st

MIN_WORDS = 30

MAX_KEYWORDS = 8

MAX_QUESTIONS = 5

STOPWORDS = {
    "a",
"about",
"after",
"already",
"an",
"and",
"are",
"as",
"at",
"be",
"before",
"body",
"but",
"by",
"called",
"can",
"could",
"for",
"from",
"has",
"have",
"help",
"if",
"in",
"into",
"is",
"it",
"later",
"make",
"more",
"of",
"on",
"only",
"or",
"so",
"some",
"such",
"that",
"the",
"their",
"them",
"these",
"this",
"to",
"use",
"when",
"why",
"with",
}

SAMPLE_PASSAGE = (
    "Artificial intelligence is transforming healthcare by enabling researchers "
    "to analyze large biomedical datasets and identify patterns that were "
    "previously difficult to detect. These advances may improve early disease "
    "detection and support clinical decision-making."
)


def load_sample() -> None:
    """Put the example passage into the study input."""
    st.session_state["passage"] = SAMPLE_PASSAGE

def count_words(text):
    """공백(띄어쓰기, 줄바꿈)을 기준으로 잘라서 단어 개수를 센다"""
    return len(text.split())

def is_mostly_english(text):
    """ 글자(알파벳, 한글 등)중 영어 알파벳이 90% 이상이면 True.
    - ch.isalpha() : 글자이면 True (숫자, 공백, 문자부호는 False)
    - ch.isascii() : 영어 알파벳처럼 기본 키보드 문자이면 True (한글은 False)
    """

    letters = [ch for ch in text if ch.isalpha()]

    if len(letters) == 0:
        return False 
    english = [ch for ch in letters if ch.isascii()]
    return len(english) / len(letters) >= 0.9

def check_passage(text):
    """지문에 문제가 있으면 사용자에게 보여줄 안내 장문을, 없으면 None을 돌려준다
    검사는 위에서부토 차례로 하고, 첫 번째로 걸린 문제만 알려준다.
    """
    if text == "":
        return "The box is empty. Please paste an English passage first "
    if not is_mostly_english(text):
        return "This app only supports English passages for now. Please use an English passage"
    words = count_words(text)
    if words < MIN_WORDS:
        return (
            f"The passage is too short({words}words)."
            f"Please add more detail so it has at least {MIN_WORDS} words"
        )
    return None



st.set_page_config(page_title="HST Guide", page_icon="📚", layout="centered")

st.title("📚 HST Guide")
st.caption("A study space for Health Science and Technology")

st.header("Study")
st.write("Start by pasting an English passage you want to study.")

# st.button("Load sample passage", on_click=load_sample_passage)
passage = st.text_area(
    "English passage",
    key="passage",
    height=240,
    placeholder="Paste an English passage here...",
)

if passage.strip():
    st.caption(f"{len(passage.split())} words")
else:
    st.info("Enter a passage or load the sample passage to get started.")
left,right = st.columns(2)
with left:
    st.button("Use sample passage", on_click = load_sample, width="stretch")
with right: 
    create_clicked = st.button("Create study set", type = "primary", width = "stretch")

if create_clicked:
    passage = st.session_state["passage"].strip()
    problem = check_passage(passage)

    if problem is not None:
        st.warning(problem)
    else: 
        st.success("Your passage is ready!")
        st.metric("Words", count_words(passage))

def tokenize_words(text):
    """ 영어 단어만 뽑아서 모두 소문자로 바꾼 리스트를 만든다.
    절규표현식 [a-zA-Z]+ 는 "영어 알파벳이 1개 이상 이어진 부분"을 뜻한다
    예를 들어 "B cells, T cells."에서는 ["B","cells","T", "cells"]를 찾는다.
    """

    words = re.findall(r"[a-zA-Z]+", text)
    return [word.lower() for word in words]