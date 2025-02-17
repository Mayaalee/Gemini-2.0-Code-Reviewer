import streamlit as st
import google.generativeai as genai

# Streamlit UI
st.title("Code Reviewer with Gemini-2.0 🤖")
st.write("Hi there! I'm ready to help you with code reviewing. Write your code below:")

# Secure API Key Input (Blurred)
API_KEY = st.text_input("🔑 Enter your Google API Key:", type="password")

if API_KEY:
    try:
        # Configure Gemini AI with the provided API key
        genai.configure(api_key=API_KEY)

        # System instruction for AI
        system_prompt = """You are an AI-powered Code Reviewer. Your task is to analyze code submitted by the user, detect any potential bugs, and provide a fixed version of the code. 
        
        Ensure your response follows this structure:

        Bug/Error Identification
        - Identify the programming language used.
        - Clearly explain any errors or bugs found in the provided code.
        - Provide a very detailed explanation of all mistakes in the code, as well as coding best practices.

        Suggested Fixes/Optimizations
        - Offer potential fixes for the identified issues.
        - Suggest optimizations or corrections following best practices.
        - Provide a corrected version of the code. 

        Corrected Code
        - Provide the corrected version of the code, ensuring that the syntax and logic are valid and functional.
        - The corrected code should be fully functional, without errors, and ready to run.
        - Finally, provide an explanation of changes in the fixed code.

        Note:
        - Highlight headings and important terms in the response.
        - If the query is unrelated to code review, bug fixing, or code analysis, politely decline with the following message:
          "I can only assist with reviewing code, identifying bugs/errors, suggesting fixes/optimizations, and providing corrected code. Please provide a code snippet for review."
        """

        # Initialize Gemini AI
        gemini = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            system_instruction=system_prompt
        )

        # Text input for user
        user_prompt = st.text_area("📌 Enter your Python code:", height=250)

        # Button to process the code
        if st.button("🔍 Review Code"):
            if user_prompt.strip():
                with st.spinner("Reviewing your code... ⏳"):
                    try:
                        # Generate content from Gemini AI
                        response = gemini.generate_content(user_prompt)

                        # Display AI Review
                        st.subheader("✅ AI Review:")
                        st.write(response.text)  # Assuming response.text contains the full review

                    except Exception as e:
                        st.error(f"❌ An error occurred while reviewing the code: {e}")
            else:
                st.warning("⚠️ Please enter a Python code snippet first.")
    except Exception as e:
        st.error("⚠️ Invalid API Key or configuration error. Please check your key and try again.")
else:
    st.warning("🔑 Please enter your Google API Key to proceed.")
