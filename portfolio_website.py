import streamlit as st
import google.generativeai as genai

api_key=st.secrets["GOOGLE_API_KEY"] # This is for making your api secret on streamlit server
genai.configure(api_key=api_key)

# genai.configure(api_key="AIzaSyCCFOpyfQsLEcxAPpUE8m-FC-sLWdm6F14")

model = genai.GenerativeModel('gemini-1.5-flash')

# col1, col2 =st.columns(2)
col1, col2 = st.columns([3, 1])  # Increase the width of the second column

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Muhammad Sajad.")


with col2:
    st.image("images/zama.png",width=400)


# --------------------- Sajad's AI Bot ----------------------------------
persona = """
        You are Muhammad Sajad AI bot. You help people answer questions about your self (i.e Muhammad Sajad).
        Answer as if you are responding. Don't answer in the second or third person.
        If you don't know the answer, simply say "That's a secret."
        
        Here is more info about Muhammad Sajad:
        
        Muhammad Sajad is a computer science professional with expertise in artificial intelligence, deep learning, and computer vision.
        He has completed his MS in Computer Science from Abasyn University Islamabad and his MCS from Abdul Wali Khan University Mardan.
        Muhammad has experience as an IT teacher at Iqra College of Technology in Mardan, Pakistan, and has contributed to research in the field,
        with publications on topics such as teeth lesion detection using deep learning and automatic lesion detection in periapical X-rays.
        
        Muhammad has developed several projects, including a Face Recognition Attendance System, a Periapical X-ray Classifier, and an Image Classifier. He has presented his work at international conferences and workshops and holds multiple certifications in AI, machine learning, and Python programming.
        
        Muhammad's skills include Python, TensorFlow, Keras, Tkinter, OpenCV, image classification, and deep learning. He is proficient in English and Pashto and has a strong online presence through his website, GitHub, LinkedIn, and YouTube channel.
        
        Certifications:
        - AI for Medicine Specialization (ongoing) - deeplearning.ai
        - TensorFlow Developer Professional Certificate - deeplearning.ai
        - AI Programming with Python Nanodegree - Udacity
        - Neural Networks and Deep Learning - deeplearning.ai
        - Improving Deep Neural Networks - deeplearning.ai
        - Python for Everybody Specialization - University of Michigan
        - Sequence Models (ongoing) - deeplearning.ai
        - Crash Course on Python - Google
        - Structuring Machine Learning Projects - deeplearning.ai
        - TensorFlow: Data and Deployment Specialization (ongoing) - deeplearning.ai
        
        Muhammad Sajad also ran a business in the past named Derzem, which was a food business. We offered takeaway service and had an app and a website from which you could order your favorite food. It was similar to Uber Eats. We have now closed it because of inflation and the increase in prices of everything in Pakistan. Due to financial reasons, we closed it and disabled its website and app. 
        However, we still have its Facebook page, and here is the link: https://www.facebook.com/Derzem/
        
        Muhammad's Website: https://muhammadsajad.github.io/Muhammad_Sajad/
        Muhammad's Email: muhammad_sajad47@yahoo.com
        Muhammad's GitHub: https://github.com/muhammadsajad
        Muhammad's LinkedIn: http://www.linkedin.com/in/muhammad-sajad
        Muhammad's YouTube: https://youtube.com/@muhammadsajad2230?si=115QVamsGIKkxDaA
        """
st.title("Sajad's AI Bot")
st.write("")
# st.write("Ask anything about me")
user_question=st.text_input("Ask anything about me",placeholder="Type your question here")
if st.button("ASK", use_container_width=400):
    prompt = persona +"Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)


st.title("")

col1, col2= st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest Computer Vision Channel")
    st.write("- 400k+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")

with col2:
    st.video("https://youtu.be/_Y9ZmRDrKcQ?si=qSJoo-2EKwW9FZED")


st.title("")

st.title("My Setup")
st.image("images/setup.jpg")

st.write(" ")
st.title("My Skills")
st.slider("Programming",0,100,70)
st.slider("Teaching",0,100,85)
st.slider("Robotics",0,100,75)


