# Author: Yanki Öztürk

# scripts for prepping Common Voice data into input files for MFA
# using only validated sentences

import pandas as pd
import shutil

with open('validated.tsv', 'r', encoding='utf-8') as f:
    sentences = pd.read_csv(f, sep='\t', usecols=['path', 'sentence'])

srcfolder = 'SOURCE FOLDER PATH'
destfolder = 'DESTINATOIN FOLDER PATH'

def getsentences():
    pass

def gettranscriptions():
    pass


    """for sent_path in sentences['path']:
        srcpath = srcfolder + sent_path
        destpath = destfolder + sent_path
        shutil.copyfile(srcpath, destpath)

    for index, row in sentences.iterrows():
        pathold, transcription = row[0], row[1]
        pathnew = pathold.split('.')[0] + '.txt'
        textgrid = open(destfolder+pathnew, 'w', encoding='utf-8')
        textgrid.write(transcription)
        textgrid.close()"""