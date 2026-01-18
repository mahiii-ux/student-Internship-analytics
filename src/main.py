import pandas as pd
from dateutil import parser
df = pd.read_excel("C:\\Users\\Mahi Thakur\\OneDrive\\Documents\\Wide_softech_Data_For_Dashboard\\Cleaned_Data.xlsx")
print(df.head())
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")

# Remove all empty/unnamed columns
df = df.dropna(axis=1, how='all')


df = df.fillna({
    "internship_mode": "Not Provided",
    "internship_status": "Not Provided",
    "internship_duration": "Not Provided",
    "internship_domian": "Not Selected",
    "internship_type": "Not Decided",
    "enquiry": "Not Mentioned "
})


# convert text to number...2025,2023....
df['pass_out_year'] = pd.to_numeric(df['pass_out_year'], errors='coerce')
df['contect_no'] = pd.to_numeric(df['contect_no'], errors='coerce')
D_duplicate= df.drop_duplicates ("contect_no")

print(df.duplicated("contect_no") )
print(D_duplicate)




df["enquiry_date"] = df["enquiry_date"].astype(str).str.strip()

def smart_date(x):
    try:
        # Try automatic powerful parser
        return parser.parse(x, dayfirst=True).date()
    except:
        return pd.NaT

df["enquiry_date"] = df["enquiry_date"].apply(smart_date)

# Save cleaned output
df.to_excel("cleaned_data.xlsx", index=False)
print("Completed")
college_count=df.groupby("college_name")["college_name"].count()
print(college_count)
