# coding: utf-8
import subprocess
import glob
import os
import configparser

# config設定
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
delete_file = config['common']['delete_file']
music_extension = config['common']['music_extension']
video_extension = config['common']['video_extension']
bps = config['common']['bps']

# 各フォルダ指定
music_folder = 'music'
video_folder = 'video'
output_folder = 'output'

# configで設定した拡張子のファイルのみを抽出
music_data = glob.glob(music_folder + '/*.' + music_extension)
video_data = glob.glob(video_folder + '/*.' + video_extension)

# musicフォルダの動画をmp3ファイルに変換
if os.listdir(music_folder) != '[]':
    for data in music_data:
        print('start:' + os.path.splitext(os.path.basename(data))[0])
        subprocess.run(['ffmpeg', '-i', data, '-vn', '-ac', '2', '-ar', '44100', '-ab', bps + 'k', '-acodec', 'libmp3lame', '-f', 'mp3', output_folder + '/' + os.path.splitext(os.path.basename(data))[0] + '.mp3'])
        if delete_file == '0':
            os.remove(data)

# videoフォルダの動画をmp4ファイルに変換
if os.listdir(video_folder) != '[]':
    for data in video_data:
        print('start:' + os.path.splitext(os.path.basename(data))[0])
        subprocess.run(['ffmpeg', '-i', data, output_folder + '/' + os.path.splitext(os.path.basename(data))[0] + '.mp4'])
        if delete_file == '0':
            os.remove(data)