import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Interview Assistant', layout='centered')
st.title('AI Interview Assistant🤖')
st.caption('Practice interview with AI-generated questions and constructive feedback.')
st.caption('Developed by:NIDA IRAM👩‍💻')
try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write("API connection is successful✅")
except (KeyError, FileNotFoundError):
  st.error('GROQ_API_KEY is missing , add it to streamlit cloud -> app settings secrets')
  st.stop()

role = st.selectbox("Select Job Role",[
                    "Python Developer",
                    "Java Developer",
                    "Data Analyst",
                    "Machine Learning Engineer",
                    "Software Engineer",
                    "HR Executive"
                    ])
diff = st.selectbox("Select Difficulty level",[
                     "Beginner",
                     "Intermediate",
                     "Advanced"])
  
if st.button("Generate Interview Questions"):
  prompt = "Generate 5 Interview Questions for the role of " + role + "with" + diff + "difficulty"
  response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
         {"role": "system", "content": "You are an expert technical Interviewer"},
      {"role": "user", "content": prompt}
    ]
  )
  output = response.choices[0].message.content
  st.write(output)
