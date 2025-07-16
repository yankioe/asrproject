# Author: Yanki Öztürk
# Automatic Speech Recognition, Summer Semester 2025
# scripts for prepping Common Voice data into input files for MFA

import pandas as pd
import shutil

def create_sent_folder(filepath, src_folder, dest_folder):
    """
    Creates a folder of eligible sentences based on sentence metadata.

    filepath (str): path to file that contains metadata
    src_folder (str): path to folder that contains all sound clips
    dest_folder (str): path to folder that the selected sound files will be moved to 
    """
    print('Copying eligible sentences. . .')
    with open(filepath, 'r', encoding='utf-8') as f:
        sentences = pd.read_csv(f, sep='\t')
    for sent_path in sentences['path']:
        srcpath = src_folder + sent_path
        destpath = dest_folder + sent_path
        shutil.copyfile(srcpath, destpath)
    print('Created sentence folder.')

def create_transacription_files(filepath, dest_folder):
    """
    Creates .TextGrid transcription files with matching file names as the source .mp3 files.

    filepath (str): path to file that contains metadata
    dest_folder (str): path to folder that the transcription files will be created in
    """
    print('Creating TextGrids. . .')
    with open(filepath, 'r', encoding='utf-8') as f:
        sentences = pd.read_csv(f, sep='\t')
    for index, row in sentences.iterrows():
        old_path, transcription = row[0], row[1]
        new_path = old_path.split('.')[0] + '.txt'
        textgrid = open(dest_folder + new_path, 'w', encoding='utf-8')
        textgrid.write(transcription)
        textgrid.close()
    print('Created TextGrids.')

def get_speaker(filepath, sent_path):
    """
    Gets speaker information of given .mp3 or .TextGrid file.

    filepath (str): path to file that contains metadata
    sent_path (str): path to folder that contains all sound clips

    speaker_info (dict): dictionary that contains speaker id, gender (if available), 
    age (if available), accent (if available)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        sentences = pd.read_csv(f, sep='\t')  
    row = sentences.loc[sentences['path'] == sent_path]
    speaker_info = {'client_id': None, 'gender': None, 'age': None, 'accents': None}
    for info in speaker_info.keys():
        speaker_info[info] = row[info][0]
    return speaker_info