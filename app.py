import streamlit as st
from os.path import exists
import pandas as pd
from datetime import datetime
import os


version_date = '2023-27-02'
__version__ = '0.0.1'
__author_email__ = 'lcalmbach@gmail.com'
__author__ = 'Lukas Calmbach'
git_repo = 'https://github.com/lcalmbach/digitial-mailbox-admin'

saved_files = []
s3_bucket = 'lc-opendata01'
s3_path = r's3://lc-opendata01/'
local_path = './data/'
LOG_FILE_REMOTE = 'https://lc-opendata01.s3.amazonaws.com/versand.csv'
log_file_local = 'versand.csv'

APP_INFO = f"""<div style="background-color:powderblue; padding: 10px;border-radius: 15px;">
    <small>App created by <a href="mailto:{__author_email__}">{__author__}</a><br>
    version: {__version__} ({version_date})<br>
    <a href="{git_repo}">git-repo</a>
    """
MAIL_LISTE_DATEI = './mail-liste.csv'
CODE_LEN = 20

def get_filename(filename:str):
    fn = filename
    files_exists = exists(local_path + fn)
    version = 0
    while (files_exists):
        version +=1
        postfix = f"_{version}.xlsx"
        fn = fn = filename.replace('.xlsx', postfix)
        files_exists = exists(local_path + fn)
    return fn

def get_fs():
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    pass

def init_mail_verteiler():
    df = pd.read_csv(MAIL_LISTE_DATEI, sep=';')
    for index,row in df.iterrows():
        pass # df['code'] = tools.randomword(CODE_LEN)
    df.to_csv('./mail-liste.csv', index=False, sep=';')

def send_invitation():
    pass
    

def verify_code(code):
    df = pd.read_csv(MAIL_LISTE_DATEI, sep = ';')
    df = df[df['code'] == code]
    if len(df) > 0:
        return dict(df.iloc[0])
    else:
        st.warning("Dieser Code ist nicht korrekt, bitte copy/pasten sie den Code aus der Mail-Einladung des Statistischen Amts oder kontaktieren sie stata@bs.ch für einen neuen Code.")
        return False

def create_mail_list():
    st.info("To come soon :rocket:...")

def empty_mailbox():
    options_show = ['Alle', 'Neue']
    show = st.radio('Show', options=options_show)
    log_df = pd.read_csv(LOG_FILE_REMOTE, sep=';')
    if show == options_show[0]:
        st.write(log_df)
    else:
        st.write(log_df[log_df['status']=='ungelesen'])
    if st.button("Ungelesene Dateien Herunterladen"):
        st.info("To come soon :rocket:...")

def main():
    st.set_page_config(page_title='digiMail-admin', page_icon = '📬', layout = 'wide')
    fs = get_fs()
    st.markdown("### Digitale Mailbox📬 Administration")
    st.markdown("**Statistisches Amt des Kantons Basel-Stadt**")
    menu = ['Briefkasten Leeren', 'Versandliste Erstellen']
    action = st.sidebar.selectbox('Menu', options=menu)
    if action == menu[0]:
        empty_mailbox()
    else:
        create_mail_list()
    
    st.sidebar.markdown(APP_INFO, unsafe_allow_html=True)
    

if __name__ == '__main__':
    main()