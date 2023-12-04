import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("data/Rice_Cammeo_Osmancik.csv")

# Create a profile report
profile = ProfileReport(df, title="Pandas Profiling Report")

profile.to_file("report.html")