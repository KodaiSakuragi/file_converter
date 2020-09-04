# coding: utf-8
import subprocess
import glob
import os
import configparser


config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
delete_file = config['common']['delete_file']
wav_folder = 'wav'
avi_folder = 'avi'
bps = config['common']['bps']
wav_data = glob.glob(wav_folder + '/*.wav')
avi_data = glob.glob(avi_folder + '/*.avi')
output_folder = 'output'

# wavのファイル変換
if os.listdir(wav_folder) != '[]':
    for data in wav_data:
        print('start:' + os.path.splitext(os.path.basename(data))[0])
        subprocess.run(['ffmpeg', '-i', data, '-vn', '-ac', '2', '-ar', '44100', '-ab', bps + 'k', '-acodec', 'libmp3lame', '-f', 'mp3', output_folder + '/' + os.path.splitext(os.path.basename(data))[0] + '.mp3'])
        if delete_file == '0':
                os.remove(data)

# aviのファイル変換
if os.listdir(avi_folder) != '[]':
    for data in avi_data:
        print('start:' + os.path.splitext(os.path.basename(data))[0])
        subprocess.run(['ffmpeg', '-i', data, output_folder + '/' + os.path.splitext(os.path.basename(data))[0] + '.mp4'])
        if delete_file == '0':
            os.remove(data)