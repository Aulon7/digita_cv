import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | "
PAGE_ICON = ":wave:"
NAME = "Aulon Morina"
DESCRIPTION = """
Data Enthusiast.
"""

LINKEDIN_URL = "https://www.linkedin.com/in/aulonmorina/"
EMAIL = "aulonmorina@gmail.com"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/Aulon_Morina_CV_2026-02.pdf"
profile_pic_file = "assets/aulon-profile-pic.png"

try:
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic_file)

except FileNotFoundError:
    PDFbyte = b""
    profile_pic = None


# --- PAGE 1: HOME ---
def home_page():
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        if profile_pic:
            st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        if PDFbyte:           
            st.download_button(
                label="📄 Download Resume",
                data=PDFbyte,
                file_name="Aulon-Morina_CV.pdf",
                mime="application/octet-stream",
            )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- ✔️ Experienced in software development, data field (analysis, visualization, engineering).
- ✔️ Skilled in JavaScript (Typescript, React), Python (Pandas, Numpy), GraphQL, REST APIs, SQL.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 👩‍💻 Programming: Javascript, Python, SQL.
- 📊 Data Visualization: PowerBI, Streamlit
- 🗄️ Databases: MySQL, GCP, AWS.
"""
    )

    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Work History")
    st.write("---")

    st.write("🚧", "**Freelance | Prishtina**")
    st.write("09/2023 - 12/2024")
    st.write(
        """
- ► Developed my skills further hence improving my data analysis and engineering skills.
- ► Participated in some mini-projects and collaborated with other developers..
"""
    )

    st.write("\n")
    st.write("🚧", "**Software Developer | Pabau Clinic Software, Prishtina**")
    st.write("07/2022 - 09/2023")
    st.write(
        """
- ► Developed and maintained one of the projects of the product regarding Reports & Analytics.
- ► Implemented GraphQL APIs for data retrieval and integration with other microservices.
- ► Visualized data using customizable dashboards within React ecosystem.
"""
    )

# --- PAGE 2: ABOUT ---
def about_page():
    st.title("About Me")
    st.write("""
    I am a software developer with a strong passion for data science and machine learning,
    from engineering part of creating APIs, data pipelines till interpreting data including feature engineering.(ML) 
    with extensive experience in Javascript (Typescript, Next), GraphQL, Python (FastAPI, Pandas, Numpy), SQL.
    I excel at developing algorithms, building ML pipelines, and crafting robust data solutions. 

    Beside the software development, I am very passionate to fully transition into the data science field.
    I am eager to contribute to the field and explore new opportunities.
    I am always open to learning and exploring new technologies.
    I am also a big fan of gaming especially FPS, MOBA games.
    """)

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")

# --- PAGE 3: PROJECTS ---
def projects_page():
    st.title("Projects")



# --- ROUTING & NAVIGATION ---
pg = st.navigation([
    st.Page(home_page, title="Home", icon=":material/home:", default=True),
    st.Page(about_page, title="About", icon=":material/person:")
])

# Render pages
pg.run()