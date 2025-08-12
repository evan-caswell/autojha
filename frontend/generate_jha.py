import httpx
import pandas as pd
import streamlit as st

API_URL = "http://localhost:8000/jha/generate"

st.set_page_config("Generate JHA", layout="centered", page_icon="🛠️")

if "task_df" not in st.session_state:
    st.session_state.task_df = pd.DataFrame(
        columns=["task_name", "task_description", "is_indoors"]
    )

st.title("Job Hazard Analysis (JHA) Builder")

with st.expander("Job Info", expanded=True):
    job_name = st.text_input("Job Name")
    jha_date = st.date_input("Job Date", value="today")
    jha_location = st.text_input("Location", placeholder="e.g. Indianapolis, IN")
    jha_conditions = st.text_input(
        "Site Conditions", placeholder="e.g. Muddy, tight quarters"
    )

st.subheader("Add a Task")
with st.form("task_form", clear_on_submit=True):
    task_name = st.text_input("Task Name", value="", key="task_name")
    task_description = st.text_area(
        "Task Description", value="", key="task_description"
    )
    is_indoors = st.checkbox("Indoors", key="is_indoors")
    submitted = st.form_submit_button("Add Task", use_container_width=True)

if submitted:
    if task_name.strip() and task_description.strip():
        new_task = {
            "task_name": task_name.strip(),
            "task_description": task_description.strip(),
            "is_indoors": is_indoors,
        }
        st.session_state.task_df = pd.concat(
            [st.session_state.task_df, pd.DataFrame([new_task])],
            ignore_index=True,
        )
    else:
        st.warning("Task name and description are required.")

if not st.session_state.task_df.empty:
    st.subheader("Current Tasks")
    st.dataframe(
        st.session_state.task_df.rename(
            columns={
                "task_name": "Task",
                "task_description": "Description",
                "is_indoors": "Indoors",
            }
        ),
        use_container_width=True,
    )


# Long timeout as the free tier Gemini can sometimes take awhile to respond.
def send_request(payload: dict) -> str:
    with httpx.Client(timeout=500.0) as client:
        response = client.post(API_URL, json=payload)
        response.raise_for_status()
        # Newline characters in the response are actually "\" + "n" instead of "\n"
        return response.text.replace("\\n", "\n")


st.divider()
if st.button(
    "Generate JHA", disabled=st.session_state.task_df.empty, use_container_width=True
):
    with st.spinner("Generating"):
        try:
            payload = {
                "job_name": job_name,
                "job_date": jha_date.strftime("%Y-%m-%d"),
                "job_location": jha_location,
                "site_conditions": jha_conditions,
                "tasks": st.session_state.task_df.to_dict("records"),
            }
            result = send_request(payload)
            st.success("Complete!")
            # Extra quotations are sent back to the frontend in the response text
            st.markdown(result.strip('"'), unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"Error {e}")
