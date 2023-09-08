import os
import sys
import shutil
#import pypandoc
import pandas as pd
from dash import html,dash_table

blast_bin='./ncbi-blast/bin'
blast_db='./ncbi-blast/db/lxsp/lxsp'
def blast_tools(blast_type,filename):
    # query acc.ver（查询序列）
    # subject acc.ver（结果序列）
    # % identity（相似度）
    # alignment length（比对长度）
    # mismatches（错配数）
    # gap opens（起始空位数）
    # q. start（查询序列起始位点）
    # q. end（查询序列终止位点）
    # s. start（结果序列起始位点）
    # s. end（结果序列终止位点）
    # evalue（期望值）
    # bit score（得分）
    #https://www.jianshu.com/p/f93ae396921f

    outname = filename.split('.')[0]
    outfile = outname+'.txt'

    tool_path = os.path.join(blast_bin,blast_type)
    if blast_type == 'blastn':
        os.system(f'{tool_path} -query {filename} -db {blast_db} -out {outfile}') #-evalue 0.2
    elif blast_type == 'blastx':
        os.system(f'{tool_path} -query {filename} -db {blast_db} -out {outfile}')
    elif blast_type == 'blastp':
        os.system(f'{tool_path} -query {filename} -db {blast_db} -out {outfile}')
    elif blast_type == 'psiblast':
        os.system(f'{tool_path} -db {blast_db} -query {filename} -evalue 0.001 -num_iterations 3 -out_ascii_pssm {outfile}')
    elif blast_type == 'phiblast':
        os.system(f'{tool_path} -db {blast_db} -query {filename} -evalue 0.001 -num_iterations 3 -out_ascii_pssm {outfile}')
    elif blast_type == 'tlastx':
        os.system(f'{tool_path} -query {filename} -db {blast_db} -out {outfile}')
    elif blast_type == 'tlastn':
        os.system(f'{tool_path} -query {filename} -db {blast_db} -out {outfile}')
    

    return(outfile)



def predict_tool(predict_type,fasta_file,pssm_file):
    outfiles = []

    new_path = "./TriNet/project/"
    if os.path.exists(new_path):
        for root, dirs, files in os.walk(new_path):
            for file in files:
                os.remove(os.path.join(root, file))

    new_fasta = new_path + 'test.fasta'
    new_pssm = new_path + '1.txt'
    shutil.copy(fasta_file, new_fasta)
    shutil.copy(pssm_file, new_pssm)
    cwd = os.getcwd()
    print(cwd)
    os.chdir(cwd)
    
    if predict_type == 'ACP':
        os.system('python TriNet/TriNet.py --PSSM_file /TriNet/project/ --sequence_file /TriNet/project/test.fasta --output /TriNet/project/result_c.csv --operation_mode sc')
        outfiles.append(f'{cwd}/TriNet/project/result_c.csv')
    elif predict_type == 'AMP':
        os.system('python TriNet/TriNet.py --PSSM_file /TriNet/project/ --sequence_file /TriNet/project/test.fasta --output /TriNet/project/result_m.csv --operation_mode sm')
        outfiles.append(f'{cwd}/TriNet/project/result_m.csv')
    elif predict_type == 'ALL':
        os.system('python TriNet/TriNet.py --PSSM_file /TriNet/project/ --sequence_file /TriNet/project/test.fasta --output /TriNet/project/result_c.csv --operation_mode sc')
        os.system('python TriNet/TriNet.py --PSSM_file /TriNet/project/ --sequence_file /TriNet/project/test.fasta --output /TriNet/project/result_m.csv --operation_mode sm')
        outfiles.append(f'{cwd}/TriNet/project/result_c.csv')
        outfiles.append(f'{cwd}/TriNet/project/result_m.csv')

    return outfiles


def generate_datatable(dataframe, max_rows=30):
    style_cell={
        'font-family': 'Times New Roman',
        'text-align': 'left',
        'minWidth': '100px', 'maxWidth': '200px', 'width': '150px',
    }

    style_header = {
        "backgroundColor": "#0D1A51",#深蓝
        "color": "white",
        "textAlign": "center",
    }

    style_table={
        'height': '200px'
    }

    style_data_conditional=[
        {
            'if': {
                'row_index': 'odd' # 选中行下标为奇数的行
            },
            'background-color': '#0d195161' #浅蓝
        }
    ]
    style_data={
        'font-family': 'Times New Roman',
    }

    return dash_table.DataTable(
        id="data-table",
        columns=[
            {'name': column, 'id': column} for column in dataframe.columns
        ],
        #columns=dataframe.columns,
        data=dataframe.to_dict("records"),
        virtualization=True,
        fixed_rows={'headers': True},
        #editable=True,
        style_header=style_header,
        style_table=style_table,
        style_cell=style_cell,
        style_data_conditional=style_data_conditional,
        style_data=style_data,
        export_format="csv",
        #active_cell={"row": 0, "column": 0},
        #selected_cells=[{"row": 0, "column": 0}],
    )


def read_txt(filename):
    with open (filename, 'r',encoding='UTF-8') as file:
        contents = file.readlines()
    return contents



