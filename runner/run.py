#!/usr/bin/python3
import sys
import glob
import os
import re
from pathlib import Path
from datetime import date, datetime

FILES = sys.argv[1]

HOME = Path.home()
CWD = os.getcwd()

PROJECT = f'{CWD}'
SRC_PATH = f'{PROJECT}/src/entidades'
PROC_PATH = f'{PROJECT}/data/notebooks'
DATA_PATH = f'{PROJECT}/data/process'
HTML_WEB = f'{PROJECT}/data/notebooks'
JSON_WEB = f'{PROJECT}/docs/_data/series'
LOG_FILE = f'{PROJECT}/data/log'
LOG_WEB = f'{PROJECT}/docs/_docs/updates/logs.md'
HTML_HEADER = f'{PROJECT}/runner/header_notebooks.md'

TEST = False

print(f'env - HOME: {HOME} *CWD: {CWD} SRC: {SRC_PATH}')

def update_log(msg, status):
    """ update logs

    Args:
        msg (string): log message
        status (string|array): result (number os result)
    """
    append_line(LOG_FILE, f'{datetime.now()} | {msg} | {status}\n')

def replace_in_file(file_name, r_search, r_replace):
    """ replace a line 

    Args:
        file_name (string): file name where works
        r_search (regexp): reg search
        r_replace (regexp): replace
    """
    print(f'f:{file_name} s:{r_search} r:{r_replace}')
    with open(file_name, "r") as fd:
        lines = fd.readlines()
    with open(file_name, "w") as fd:
        for line in lines:
            fd.write(re.sub(r_search, r_replace, line))

def update_log_web(file_name, status):
    """ update a log that is shown in our web

    Args:
        file_name (string): filename with path where is the ipynb 
        status (string|array): result (number os result)
    """
    file_name = os.path.basename(file_name)
    sts = 'OK' if status == 0 else f'Error {status}'
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sub = f'{file_name} | {now} | {sts}'
    replace_in_file(LOG_WEB, rf'^{file_name}.*', sub)

def exec_notebook(file_name,entity):
    """ execute ipynb

    Args:
        file_name (string): filename with path where is the ipynb 
        dst_path (string, optional): output path. Defaults to PROC_PATH.
        entity (string): entity
    """
    dst_path=f'{PROC_PATH}/{entity}'
    cmd = f'''jupyter nbconvert \
              --to notebook \
              --execute {file_name} \
              --ExecutePreprocessor.kernel_name='python3' \
              --output-dir={dst_path}'''
    cmd = re.sub(" +", " ", cmd)
    print(f'{cmd}')
    #os.system(f'cd {dst_path}')
    status = 0 if TEST else exec(cmd)
    update_log('exec_notebook', status)
    update_log(cmd, 0)
    update_log_web(file_name, status)
    result_file = f'{dst_path}/{os.path.splitext(os.path.basename(file_name))[0]}.ipynb'
    return result_file    
    
def convert_notebook(file_name, entity):
    """ convert notebook to html and ensure that there
        is a html copy on the ipynb source

    Args:
        file_name (string): full path of source notebook
        entity (string): entity

    Returns:
        string: file name in output path
    """
    #--HTMLExporter.theme=dark \
    cmd = f'''jupyter nbconvert \
                {file_name} \
                --to html \
                --output-dir {HTML_WEB}/{entity}'''
    cmd = re.sub(" +", " ", cmd)
    status = 0 if False else exec(cmd)
    update_log('convert_notebook', status)
    update_log(cmd, 0)

    file_base = f'{os.path.splitext(os.path.basename(file_name))[0]}'    
    html_base = f'{file_base}.html'
    html_file = f'{HTML_WEB}/{entity}/{html_base}'
    ensure_src_html(html_base, html_file, entity)

    return html_file

def ensure_src_html(html_base, html_file, entity):
    """ ensure there is a html file as is the ipynb at begining

    Args:
        html_base (string): html file name without path
        html_file (string): full file path with the html processed 
        entity (string): entity
    """
    src_html = f'{SRC_PATH}/{entity}/{html_base}'
    if (not os.path.isfile(src_html)):
        cmd = f"cp -vfr {html_file} {src_html}"
        status = 0 if False else exec(cmd)
        update_log('initial html src notebook', status)

# not used
def prepend_line(file_name, line):
    with open(file_name, 'r+') as fd:
        lines = fp.readlines()
        lines.insert(0, line)
        fd.seek(0)
        fd.writelines(lines)

# not used
def process_header(file_header, file_name, entity, entity_name):
    with open(file_header, 'r') as fd:
        lines = fd.readlines()
    file = f'{os.path.splitext(os.path.basename(file_name))[0]}'
    title = file.replace('_',' ')
    file = f'{SRC_PATH}/{entity}/{file}.ipynb'
    lines = [re.sub(r'_file_', file, l) for l in lines]
    lines = [re.sub(r'_title_', title, l) for l in lines]
    lines = [re.sub(r'_entity_', entity, l) for l in lines]
    lines = [re.sub(r'_entityname_', entity_name, l) for l in lines]
    lines = [re.sub(r'_date_', f'{datetime.now()}', l) for l in lines]
    return lines

# not used
def change_header(file_name, file_header, entity, entity_name):
    print(f'Addin header to - {file_name}')
    add = process_header(file_header,
                         file_name, 
                         entity, 
                         entity_name)
    with open(file_name, 'r') as fd:
        lines = fd.readlines()                         
    with open(file_name, 'w+') as fd:
        lines.insert(0, ''.join(add))
        fd.seek(0)
        fd.writelines(lines)

def append_line(file_name, line):
    """ append a line at the end of file name

    Args:
        file_name (string): full fil name where works
        line (string): text to append
    """
    with open(file_name, "a+") as fd:
        fd.write(line)

def move_results_and_clean(entity):
    """ move processed data to data path and clean 
    temporary files and dirs


    Args:
        entity (string): entity
    """
    print(f"cp -vfr {SRC_PATH}/{entity}/data/process/{entity}/* {DATA_PATH}/{entity}")
    process_path = f'{SRC_PATH}/{entity}/serhi'
    status = [
        exec(f"cp -vfr {process_path}/data/process/{entity}/* {DATA_PATH}/{entity}"), 
        exec(f'rm -vfr {process_path}'),
    ]
    update_log('move_results_and_clean',status)

def copy_files(src,dst):
    """copy files from src to dst

    Args:
        src (string): source path
        dst (string): destination path
    """
    status = [exec(f'mkdir -p {dst}; cp -pv {f} {dst}/') for f in src]
    update_log('copy_files',status)

def exec(cmd):
    os.system(f'echo {cmd}')
    return os.system(cmd)

# MAIN

def main():
    lines = open(FILES, 'r').readlines()
    count = 0
    update_log('*** RUNNER ***', 0)
    for i, line in enumerate(lines):
        [entity, entity_name, ipynb] = line.strip().split(':')
        print(f'\nEntity -> {entity} - {entity_name} - {ipynb}')
        # execute notebooks
        process_path = f'{SRC_PATH}/{entity}/*'
        files_to_process = glob.glob(f'{process_path}.ipynb')
        print(f'{files_to_process}')
        # generate new ipynb executed 
        files_to_convert = [exec_notebook(f,entity) for f in files_to_process]
        
        # generate html files
        html_files = [convert_notebook(f, entity) for f in files_to_convert]
        
        # copy documents (json) to jekyll
        files_to_process = glob.glob(f'{process_path}.json')
        copy_files(files_to_process,JSON_WEB)

if __name__ == "__main__":
    main()    