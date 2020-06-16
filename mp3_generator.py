# coding: utf-8
import subprocess
import glob
import os

# data/aviSourceに格納されているaviファイルを、configのsourceFolderに指定したフォルダに格納する

wav_folder = 'wav'
source_data = glob.glob(wav_folder + '/*.wav')
output_folder = 'output'

for data in source_data:
    print('start:' + os.path.splitext(os.path.basename(data))[0])
    subprocess.run(['ffmpeg', '-i', data, '-vn', '-ac', '2', '-ar', '44100', '-ab', '256k', '-acodec', 'libmp3lame', '-f', 'mp3', output_folder + '/' + os.path.splitext(os.path.basename(data))[0] + '.mp3'])