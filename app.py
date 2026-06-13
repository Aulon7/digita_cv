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

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

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
    st.divider()

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

    # --- PROJECT ONE ---
    with st.container(border=True, width=1000, gap="small"):
        st.header("E-Commerce Analytics (Azure)")
        st.write("""
        A modern data pipeline for e-commerce analytics using Azure Databricks, Delta Lake, and Power BI.
        """)
        st.markdown("#### 🏗️ Project Architecture & Summary")
        st.image("assets/project_assets/azure/azure_databricks.png", use_container_width=True)
        st.write("""
        - **Medallion Architecture:** Raw streaming from ADLS Gen2 via Auto Loader **(Bronze)**, transformed and deduplicated via MERGE **(Silver)**, and structured into an analytical star schema **(Gold)**.
        - **Key Features:** End-to-end data lineage, explicit schema enforcement, and an optimized hybrid framework of incremental and batch processing.
        """)

        st.markdown("#### 📊 Data modeling and visualization")
        st.write("""
        - **Star Schema Model:** High-performance analytical design featuring granular transaction fact (`Fact_Order_Items`) and dimensions tables (`Products`, `Customers`, `Date`).
        - **BI Visualization:** Clean, Power BI-ready tables optimized to reduce join depth, ensuring lightning-fast dashboard queries and seamless reporting.
        """)
        st.markdown("##### Data Modeling")
        st.image("assets/project_assets/azure/data-model.png", use_container_width=True)
        st.markdown("##### Power BI")
        st.image("assets/project_assets/azure/overview-page.png", use_container_width=True)
        st.image("assets/project_assets/azure/time-based-page.png", use_container_width=True)

    st.divider()

    # --- PROJECT TWO ---
    with st.container(border=True, width=1000, gap="small"):
        st.header("NYC Taxi ETL (GCP)")
        st.write("""
        End-to-end data pipeline for NYC Yellow Taxi 2024 (official data) data using Spark, GCP, dbt, Airflow and PowerBI.
        """)
        st.image("assets/project_assets/gcp/gcp-pipeline.png", use_container_width=True)
        st.markdown("#### 🏗️ Project Architecture & Summary")
        st.write("""
        - **Orchestration & Ingestion (E & L):** **Apache Airflow** manages scheduled orchestration for **GCP Dataproc (Spark)** jobs. Spark extracts raw files from **Cloud Storage**, processes them, and writes partitioned Parquet files directly into **BigQuery**.
        - **Transformation & Modeling (T):** **dbt** executes transformation logic inside BigQuery, running quality tests and modeling staging layers into clean, production-ready Star Schema Data Marts.
        - **Visualization & Deployment:** **Power BI** connects directly to BigQuery for real-time querying, while the entire local environment is containerized via **Docker Compose**.
        """)

        st.markdown("#### 📊 Data modeling and visualization")
        st.write("""
        - **Star Schema Model:** Built optimized analytical layers consisting of granular fact tables paired with descriptive dimension tables, designed to drastically reduce join depth.
        - **BI Visualization:** Connected Power BI to the modeled BigQuery gold tables, enabling responsive semantic performance, direct data drill-downs, and clean dashboard layout visualization.
        """)
        st.markdown("##### Data Modeling")
        st.image("assets/project_assets/gcp/data-model.png", use_container_width=True)
        st.markdown("##### Power BI")
        st.image("assets/project_assets/gcp/executive-summary.png", use_container_width=True)
        st.image("assets/project_assets/gcp/financial-insights.png", use_container_width=True)

    st.divider()

      # --- PROJECT THREE ---
    with st.container(border=True, width=1000, gap="small"):
        st.header("- CarePlus Data Pipeline (AWS)")
        st.write("""
        This project moves support logs and support tickets through ingestion, transformation, and analytics on AWS.
        """)
        st.markdown("#### 🏗️ Project Architecture & Summary")
        st.image("assets/project_assets/aws/aws-pipeline.png", use_container_width=True)
        st.write("""
        - **Data Ingestion (E & L):** Automated multi-source ingestion handling transactional data and streaming application logs, pushing raw datasets directly into dedicated **Amazon S3** landing zones.
        - **Serverless Transformation (T):** Orchestrates decoupled processing pipelines using an **AWS Lambda** function to parse and convert raw logs into optimized Parquet formats, paired with a Lambda trigger that initiates an **AWS Glue ETL** job for ticket cleaning.
        - **Pipeline Infrastructure:** Centrally controlled configurations utilizing environment secrets, ensuring secure connectivity for data extraction from an external **MySQL** database.
        """)
        st.markdown("#### 📊 Data modeling and visualization")
        st.write("""
        - **Processed Storage Layer:** Transformed datasets are partitioned and stored in Amazon S3 (`processed-data/`), optimized for high-performance schema discovery and low-cost analytical queries.
        - **BI Visualization:** Standardized data outputs are engineered to integrate seamlessly into QuickSight for visualizations over consolidated support logs and tickets.
        """)
        st.markdown("##### QuickSight")
        st.image("assets/project_assets/aws/support-logs-quicksight.png", use_container_width=True)
        st.image("assets/project_assets/aws/support-tickets-quicksight.png", use_container_width=True)

# --- ROUTING & NAVIGATION ---
pg = st.navigation([
    st.Page(home_page, title="Home", icon=":material/home:", default=True),
    st.Page(about_page, title="About", icon=":material/person:"),
    st.Page(projects_page, title="Projects", icon=":material/work:")
])

# Render pages
pg.run()