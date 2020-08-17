import pandas as pd 
import plotly.express as px 
# import plotly.graph_objects as go
from plotly.subplots import make_subplots 

df = pd.read_csv(snakemake.input[0],sep="\t")
df.rename(columns={df.columns[0]:'Subject'},inplace=True)
# df.set_index('Subject',inplace=True)
# names = df.columns[1::]




fig = px.box(df,y=snakemake.wildcards['parcel'],hover_name='Subject',points='all')
fig.write_html(snakemake.output[0])
