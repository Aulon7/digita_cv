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
        st.image("assets/project_assets/azure/azure_databricks.png", width='content')
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
        st.image("assets/project_assets/azure/data-model.png", width='content')
        st.markdown("##### Power BI")
        st.image("assets/project_assets/azure/overview-page.png", width='content')
        st.image("assets/project_assets/azure/time-based-page.png", width='content')

    st.divider()

    # --- PROJECT TWO ---
    with st.container(border=True, width=1000, gap="small"):
        st.header("NYC Taxi ETL (GCP)")
        st.write("""
        End-to-end data pipeline for NYC Yellow Taxi 2024 (official data) data using Spark, GCP, dbt, Airflow and PowerBI.
        """)
        st.markdown("#### 🏗️ Project Architecture & Summary")
        st.image("assets/project_assets/gcp/gcp-pipeline.png", width='content')
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
        st.image("assets/project_assets/gcp/data-model.png", width='content')
        st.markdown("##### Power BI")
        st.image("assets/project_assets/gcp/executive-summary.png", width='content')
        st.image("assets/project_assets/gcp/financial-insights.png", width='content')

    st.divider()

      # --- PROJECT THREE ---
    with st.container(border=True, width=1000, gap="small"):
        st.header("- CarePlus Data Pipeline (AWS)")
        st.write("""
        This project moves support logs and support tickets through ingestion, transformation, and analytics on AWS.
        """)
        st.markdown("#### 🏗️ Project Architecture & Summary")
        st.image("assets/project_assets/aws/aws-pipeline.png", width='content')
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
        st.image("assets/project_assets/aws/support-logs-quicksight.png", width='content')
        st.image("assets/project_assets/aws/support-tickets-quicksight.png", width='content')

def lectures_12_page():
    st.title("Intro to SQL, Database, Data Modeling, Types of Data Repositories")
    st.markdown(
        "This lecture provides a wide, practical overview of SQL fundamentals, database categories, "
        "data modeling concepts and strategies, and modern data repository patterns used in analytics."
    )

    # Section 1 — Introduction to SQL
    st.header("Introduction to SQL")
    with st.container(border=True, width=1000, gap="small"):
        st.write(
            "Summary: SQL (Structured Query Language) is the primary language for working with "
            "relational data. It covers defining schemas, manipulating rows, querying results, "
            "and managing access and transactions. Modern data platforms often extend SQL with "
            "procedural features, window functions, and analytical constructs."
        )

        st.image("assets/project_assets/sql.png", width='content')
        st.subheader("Core Pillars")
        st.markdown(
            """
            - **DDL:** `CREATE`, `ALTER`, `DROP` — defines and evolves schema.
            - **DML:** `SELECT`, `INSERT`, `UPDATE`, `DELETE` — reads and modifies data.
            - **DCL:** `GRANT`, `REVOKE` — manages access and permissions.
            - **TCL:** `BEGIN`, `COMMIT`, `ROLLBACK`, `SAVEPOINT` — controls transaction boundaries.
            """
        )
        st.subheader("Normalization & Design Trade-offs")
        st.write(
            "Normalization (1NF → 2NF → 3NF → BCNF) reduces redundancy and update anomalies and is ideal for transactional systems. "
            "However, denormalization and dimensional models are often preferred for analytics because they simplify queries and improve read performance."
        )

        st.divider()

        st.subheader("Databases and Their Types")
        st.write(
            "Summary: Databases are optimized for different data models and workloads (OLTP vs OLAP vs specialized workloads). "
            "Choosing the right type depends on consistency needs, query patterns, latency, scale, and schema flexibility."
        )
        st.markdown(
            """
            - Relational (RDBMS): Strong schema, ACID, joins and transactions. Good for OLTP and trusted consistency (Postgres, MySQL, SQL Server).
            - Document stores: Schema-flexible JSON documents suited for hierarchical or evolving data (MongoDB, Couchbase).
            - Key-Value stores: Extremely fast lookups and caching scenarios (Redis, DynamoDB in KV mode).
            - Wide-column stores: Highly scalable, suited for time-series or event data at scale (Cassandra, HBase).
            - Graph databases: Optimized for relationship-rich queries (Neo4j, TigerGraph).
            """
        )
        st.write("Considerations: replication models, consistency (strong vs eventual), partitioning/sharding, and operational complexity.")

    st.divider()

    st.header("Data Modeling")
    with st.container(border=True, width=1000, gap="small"):
        st.write(
            "Summary: Data modeling spans conceptual, logical, and physical levels and guides how source data becomes analytics-ready. "
            "Good modeling balances query performance, maintainability, and governance."
        )
        st.image("assets/project_assets/data-modeling.jpg", width='content')
        st.subheader("Modeling Levels")
        st.markdown(
            """
            - **Conceptual:** High-level business entities and relationships (stakeholder view).
            - **Logical:** Detailed entity definitions, normalized relationships, attributes and business keys (DB-agnostic).
            - **Physical:** Concrete tables, column types, indexes, partitions and storage layout optimized for a specific engine.
            """
        )
        st.subheader("Key Modeling Concepts")
        st.markdown(
            """
            - **Grain:** Define the atomic level of a fact table clearly (e.g. one row = one order line). Grain determines aggregation and joins.
            - **Surrogate keys:** Use synthetic keys for dimensions to isolate analytic models from changing source keys.
            - **Conformed dimensions:** Shared dimensions used across multiple facts to enable consistent analysis.
            - **Slowly Changing Dimensions:** Handle changing attributes with Type 1 (overwrite), Type 2 (history rows), or Type 3 (limited history).
            """
        )
        st.subheader("Warehousing Philosophies")
        st.markdown(
            """
            - **Kimball (bottom-up):** Build dimensional data marts (star/snowflake schemas) for business processes then integrate via conformed dimensions — fast to deliver analytic use-cases.
            - **Inmon (top-down):** Create an enterprise data warehouse (normalized) as single source of truth, with downstream marts for reporting — emphasizes integration and consistency.
            - **Data Vault:** Hub-Link-Satellite architecture focused on auditability, historization and flexible ingestion — useful for large, rapidly changing sources and rigorous lineage.
            """
        )
        st.write("Choosing an approach depends on delivery cadence, governance needs, reporting complexity, and change velocity of source systems.")


    st.header("Types of Data Repositories")
    with st.container(border=True, width=1000, gap="small"):
        st.write(
            "Summary: Repositories are chosen by purpose: operational DBs handle transactions, warehouses power analytics, lakes store raw/varied data, and lakehouses attempt to combine both."
        )
        st.image("assets/project_assets/data-repos.png", width='content')
        st.markdown(
            """
            - **Operational Database (OLTP):** Designed for fast, consistent transactions with normalized schemas (e.g., customer systems, order entry).
            - **Data Warehouse (OLAP):** Modeled for analytics and reporting with schema-on-write and performance features (Snowflake, BigQuery, Redshift).
            - **Data Lake:** Low-cost object storage for raw structured and unstructured data; favors schema-on-read and flexible ingestion (S3, ADLS).
            - **Lakehouse:** Brings ACID, schema management and performant query capabilities to lake storage (Delta Lake, Apache Iceberg, Hudi) enabling BI & ML workflows on open storage.
            """
        )
        st.subheader("Trade-offs & Patterns")
        st.write(
            "Key trade-offs include schema-on-write vs schema-on-read, cost vs performance, governance and cataloging needs, and how easily downstream tools (BI/ML) can consume data. "
            "Modern architectures often use a hybrid approach: operational systems → ingestion layer → lake (raw) → transformation (ETL/ELT) → warehouse/lakehouse for consumption."
        )

# --- ROUTING & NAVIGATION ---
pg = st.navigation({
    "": [
        st.Page(home_page, title="🏡 Home", default=True),
        st.Page(about_page, title="🙎‍♂️ About"),
        st.Page(projects_page, title="💼 Projects"),
    ],
    "📚 Lessons": [
        st.Page(lectures_12_page, title="📝 Lecture 12"),
    ]
})

pg.run()