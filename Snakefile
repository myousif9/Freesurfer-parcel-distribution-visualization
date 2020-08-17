from os.path import join
import pandas as pd

configfile: 'config.yaml'

data_df = pd.read_table(config['freesurf_txt'],sep="\t")
# data_df.rename(columns={data_df.columns[0]:'Subject'},inplace=True)
parcels = data_df.columns[1::]

# wildcard_constraints:
#     parcel = "[A-Za-z0-9]+"

rule all:
    input:  
        expand("output/{parcel}.html",parcel=parcels),
        "report.html"
        
rule gen_parcel_boxplot:
    input: config['freesurf_txt']
    output: "output/{parcel}.html"
    script: 'scripts/viz_freesurf.py'

rule html_visualize:
    input: expand("output/{parcel}.html",parcel=parcels)
    output: "report.html"
    script: "scripts/overlay.py"