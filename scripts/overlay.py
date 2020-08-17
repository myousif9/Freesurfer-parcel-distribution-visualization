# from nilearn import plotting 
from glob import glob 
import os
import argparse
from jinja2 import Template

figures = os.listdir(os.path.join(os.getcwd(),'output'))
# fig_name = [fig.replace('.html','') for fig in figures]

# print(figures)

template = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Freesurfer Parcel Distributions</title>
        <style>
        .container {
            display: flex;
            flex-wrap: wrap;
            background-color: DodgerBlue;
        }
        h1 {
            font-family: sans-serif;
        }
        </style>
    </head>
    <body>
    <h1> Freesurfer Parcel Volume Distributions </h1>
    <div class="container">
    {% for fig in figures %}
        <div>
            <iframe src="./output/{{fig}}" width=300 height=300
            style="padding:0; border:0; display: block;
            margin-left: auto; margin-right: auto"></iframe>
        </div>
    {%- endfor %}
    </div>
    </body>
    </html>
    """)

report_html_code = template.render(figures=figures)
    
with open('report.html',"w") as html_file:
    html_file.write(report_html_code)



    # path_dict = dict(zip(overlay_paths,background_paths))

    # print(path_dict)
    
    # overlay = sys.argv[1]
    # background = sys.argv[2]
    # output_dir = sys.argv[3]

    # print(sys.argv[1])                 

    # for path in overlay:
        # sub = [x for x in path.split('/') if 'sub' in x][0]

    # overlay_pattern = sys.argv[3]

    # participants_df = pd.to_csv(os.path.join(overlay_bids_dir,'participants.tsv'),sep='\t')
    # subjects = participants_df.participant_id.tolist()

    

    

