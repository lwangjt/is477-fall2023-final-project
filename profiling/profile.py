import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("data/Rice_Cammeo_Osmancik.csv") 
profile = ProfileReport(df, title="Pandas Profiling Report")