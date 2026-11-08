import re 
from collections import Counter
import streamlit as st

MIN_WORDS = 30

MAX_KEYWORDS = 8



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
    "Vaccines help the immune system learn to recognize a virus before a real infection happens."
    "A vaccine contains a weakened virus, an inactive virus, or only a small piece of the virus, such as a protein."
    "When the vaccine enters the body, immune cells called B cells detect the protein and start to make antibodies."
    "Antibodies are proteins that attach to the virus and stop it from entering healthy cells. "
    "Other immune cells, called T cells, destroy cells that are already infected. After the response ends, some B cells and T cells stay in the body as memory cells."
    "If the real virus appears later, these memory cells recognize it quickly, so the immune system can make antibodies much faster."
    "This is why vaccines can prevent serious disease without causing the illness itself."
)


def load_sample():
    """Put the example passage into the study input."""
    st.session_state["passage"] = SAMPLE_PASSAGE

def count_words(text):
    """Count the number of words by splitting the text based on whitespace (spaces and line breaks)."""
    return len(text.split())

def is_mostly_english(text):
    """ If 90% or more of the characters (letters such as English and Korean) are English alphabet characters, return True.
        ch.isalpha(): Returns True if the character is a letter (returns False for numbers, whitespace, and punctuation).
        ch.isascii(): Returns True if the character is an ASCII character (basic keyboard characters, including English letters, numbers, and symbols; returns False for Korean characters)
    """

    letters = [ch for ch in text if ch.isalpha()]

    if len(letters) == 0:
        return False 
    english = [ch for ch in letters if ch.isascii()]
    return len(english) / len(letters) >= 0.9

def check_passage(text):
    """If there is an issue with the passage, return a detailed message to display to the user. If there are no issues, return None.
    Perform the checks in the order listed above and report only the first issue detected.
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

def tokenize_words(text):
    """ Extract only the English words and create a list with all words converted to lowercase. 
        The regular expression [a-zA-Z]+ matches one or more consecutive English alphabet characters.
        For example, in "B cells, T cells.", it finds ["B", "cells", "T", "cells"].
        The final lowercase list would be ["b", "cells", "t", "cells"].
    """

    words = re.findall(r"[a-zA-Z]+", text)
    return [word.lower() for word in words]

def find_important_words(text, max_words=MAX_KEYWORDS):
    """find the most commonly used word, remove any stopwords or 3 letter words, counter counts how many times each words appears
    ex) if cells appeared 10times it would be (cells, 10)
    """
    candidates = [word for word in tokenize_words(text) if len(word) >= 3 and word not in STOPWORDS]
    return Counter(candidates).most_common(max_words)


st.set_page_config(page_title="HST Guide", page_icon="", layout="centered")

st.title(" HST Guide")
st.caption("A study space for Health Science and Technology")

st.header("Study")
st.write("Start by pasting an English passage you want to study.")


passage = st.text_area(
    "English passage",
    key="passage",
    height=240,
    placeholder="Paste an English passage here...",
)

if passage.strip():
    st.caption(f"{count_words((passage))} words")
else:
    st.info("Enter a passage or load the sample passage to get started.")
left,right = st.columns(2)
with left:
    st.button("Use sample passage", on_click = load_sample, width="stretch")
with right: 
    create_clicked = st.button("Analyze passage", type = "primary", width = "stretch")

if create_clicked:
    passage = st.session_state["passage"].strip()
    problem = check_passage(passage)

    if problem is not None:
        st.warning(problem)
    else: 
        st.success("Your passage is ready!")
        st.metric("Words", count_words(passage))

        important_words = find_important_words(passage)
        print(important_words)
        st.subheader("Important words")
        if len(important_words) == 0: 
            st.info("No important words were found. Try a longer HST passage")
        else:
            st.table([{"Word": word, "Count": count} for word, count in important_words])


