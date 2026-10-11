import streamlit as st


SAMPLE_PASSAGE = (
    "Artificial intelligence is transforming healthcare by enabling researchers "
    "to analyze large biomedical datasets and identify patterns that were "
    "previously difficult to detect. These advances may improve early disease "
    "detection and support clinical decision-making."
)


def load_sample_passage() -> None:
    """Put the example passage into the study input."""
    st.session_state["passage"] = SAMPLE_PASSAGE


st.set_page_config(page_title="HST Guide", page_icon="📚", layout="centered")

st.title("📚 HST Guide")
st.caption("A study space for Health Science and Technology")

st.header("Study")
st.write("Start by pasting an English passage you want to study.")

st.button("Load sample passage", on_click=load_sample_passage)
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
