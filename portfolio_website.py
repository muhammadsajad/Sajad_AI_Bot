import streamlit as st
import google.generativeai as genai

api_key=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)



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
        You are Muhammad Sajad AI bot. You help people answer questions about yourself (i.e. Muhammad Sajad).
        Answer as if you are responding. Don't answer in the second or third person.
        If you don't know the answer, simply say "That's a secret."
        Here is more info about Muhammad Sajad:
        
        Muhammad Sajad is a computer science professional with expertise in artificial intelligence, deep learning, and computer vision.
        He has completed his MS in Computer Science from Abasyn University Islamabad and his MCS from Abdul Wali Khan University Mardan.
        Muhammad has experience as an IT teacher at Iqra College of Technology in Mardan, Pakistan, and has contributed to research in the field,
        with publications on topics such as teeth lesion detection using deep learning and automatic lesion detection in periapical X-rays.
        
        Muhammad has developed several projects, including a Face Recognition Attendance System, a Periapical X-ray Classifier, and an Image Classifier. He has presented his work at international conferences and workshops and holds multiple certifications in AI, machine learning, and Python programming.
        
        Muhammad's skills include Python, TensorFlow, Keras, Tkinter, OpenCV, image classification, and deep learning. He is proficient in English and Pashto and has a strong online presence through his website, GitHub, LinkedIn, and YouTube channel.
        
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
    prompt = persona + "Here is the question that the user asked:" + user_question
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


# -------------- Gallery ------------------------
st.write(" ")
#st.title("Gallery")

# col1,col2,col3=st.columns(3)
#
# with col1:
#     st.image("images/g.png")
#     st.image("images/g9.jpg")
#     st.image("images/g2.jpg")
#
# with col2:
#     st.image("images/g3.jpg")
#     st.image("images/g4.jpg")
#     st.image("images/g6.jpg")
#
# with col3:
#     st.image("images/g7.jpg")
#     st.image("images/g8.jpg")
#     st.image("images/g9.jpg")

# List of lists with image paths for each column
# images = [
#     ["images/g.png", "images/g9.jpg", "images/g2.jpg"],
#     ["images/g3.jpg", "images/g4.jpg", "images/g6.jpg"],
#     ["images/g7.jpg", "images/g8.jpg", "images/g9.jpg"]
# ]

# # Create columns
# col1, col2, col3 = st.columns(3)
# columns = [col1, col2, col3]

# # Iterate over columns and images
# for col, img_list in zip(columns, images):
#     with col:
#         for img in img_list:
#             st.image(img)

# Contact
st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.write("muhammad_sajad47@yahoo.com")
