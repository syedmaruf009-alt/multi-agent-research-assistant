import streamlit as st
import requests

st.title("Multi-Agent Research Assistant")

question = st.text_input("Ask a question:")

if st.button("Ask"):
    if not question.strip():    #Empty check
        st.warning("Please enter a question.")
    else:
        try:
            #Request to backend Django server
            response = requests.post(
                "http://127.0.0.1:8000/api/ask/",
                json={"question": question},
                timeout=60
            )

            #Status code 200 means success
            st.write("Status code:", response.status_code)

            # Debug: show raw response
            st.write("Raw response:", response.text)

            #Check if response is JSON before parsing
            if response.headers.get("Content-Type", "").startswith("application/json"):
                data = response.json()

                st.subheader("Planner Decision")
                st.write(data.get("plan"))

                st.subheader("Research Result")
                st.write(data.get("research_result"))

                st.subheader("Final Answer")
                st.write(data.get("final_answer"))
            else:
                # If not JSON, show error to user
                st.error("Server did not return JSON.")

        #Network error handling
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")