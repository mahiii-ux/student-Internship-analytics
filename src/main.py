import pandas as pd
from dateutil import parser
from sqlalchemy import create_engine, MetaData, Table

df = pd.read_excel("C:\\Users\\Mahi Thakur\\OneDrive\\Documents\\Wide_softech_Data_For_Dashboard\\Cleaned_Data.xlsx")
print(df.head())

# Convert column names to lowercase and replace spaces with underscores
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

# Remove all empty/unnamed columns
df = df.dropna(axis=1, how='all')

# Fill missing values
df = df.fillna({
    "internship_mode": "Not Provided",
    "internship_status": "Not Provided",
    "internship_duration": "Not Provided",
    "internship_domian": "Not Selected",
    "internship_type": "Not Decided",
    "enquiry": "Not Mentioned "
})

# Convert text to number...2025, 2023....
df['pass_out_year'] = pd.to_numeric(df['pass_out_year'], errors='coerce')
df['contect_no'] = pd.to_numeric(df['contect_no'], errors='coerce')

# Check for duplicates before removing them
print("Duplicate contact numbers:")
print(df.duplicated("contect_no").sum())

# Process enquiry_date BEFORE removing duplicates
if "enquiry_date" in df.columns:
    df["enquiry_date"] = df["enquiry_date"].astype(str).str.strip()

    def smart_date(x):
        try:
            # Try automatic powerful parser
            return parser.parse(x, dayfirst=True).date()
        except:
            return pd.NaT

    df["enquiry_date"] = df["enquiry_date"].apply(smart_date)
else:
    print("Warning: 'enquiry_date' column not found in dataframe")
    print("Available columns:", df.columns.tolist())

# NOW remove duplicates (use the same df variable to update it)
df = df.drop_duplicates("contect_no")
print(f"\nDataframe shape after removing duplicates: {df.shape}")
print(df.head())

# Save cleaned output
df.to_excel("cleaned_data.xlsx", index=False)
print("\nCompleted")

# College count analysis
college_count = df.groupby("college_name")["college_name"].count()
print("\nCollege count:")
print(college_count)

# Database connection
# Database login details (NO SPACES inside the quotes!)
username = "root"
password = "tmahi0151"
host = "localhost"  # Database is on our computer
port = "3306"  # MySQL's default port
database = "mydb"  # Our database name

# Create connection (NO SPACES in the f-string!)
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

print("\nDatabase connection successful!")

