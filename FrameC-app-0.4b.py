import sys
import sys
import getopt
import os
from PIL import Image, ImageDraw #, ImageFont
import ffmpegController as Ffmpeg
import frameCounter as FrameCounter
import graphGenerator as GraphGenerator

# VARIABELS

ffmpeg_path = ''
original_frame_first_name = 'images'
version = '0.4b'
# resize_to = 64
framerate = 30
platform = 'Wii U'
framerate_dot_width = 10

grid_image_global = None
grid_image_frametime_global = None
frametime_grid_width = 200
frametime_grid_height = 80

equal_point_for_compare = 1#3059 #140 nice for 240p PS1  # 480 - nice for 720p 500 #12000 # 10000 # 12000 # 14000

current_frame_name = 'images'
current_frame_extension = '.png'
base_path = ''
seconds = 595
width_frame = 1280
frames_on_screen_line = 120


def print_next_step_info():
    return None


def showTerminalHelp():
    help = "Usage: "
    print help
    exit(2)


try:
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:f:b:t:s:p:w:", ["help", "input=", "output=", "framerate", "bitrate", "temp_dir", "seconds", "platform_name", "width_frame"])
except getopt.GetoptError:
    showTerminalHelp()

for opt, arg in opts:
    if opt in ("-h", "--help"):
        showTerminalHelp()
    if opt in ("-i", "--input"):
        input_file = arg
    if opt in ("-o", "--output"):
        output_file = arg
    if opt in ("-f", "--framerate"):
        framerate = arg
    if opt in ("-b", "--bitrate"):
        bitrate_video = arg
    if opt in ("-t", "--temp_dir"):
        temp_dir = arg
    if opt in ("-s", "--seconds"):
        seconds = arg
    if opt in ("-p", "--platform"):
        platform = arg
    if opt in ("-w", "--width_frame"):
        width_frame = arg

if input_file == '':
    showTerminalHelp()
if output_file == '':
    showTerminalHelp()
if framerate == '':
    showTerminalHelp()
if temp_dir == '':
    showTerminalHelp()
if bitrate_video == '':
    showTerminalHelp()
if seconds == '':
    showTerminalHelp()
if platform == '':
    showTerminalHelp()
if width_frame == '':
    showTerminalHelp()

# endregin


def print_app_info():
    print("FrameC-app v"+version)


def main():
    global original_frame_first_name
    global ffmpeg_path
    path_to_save_file = ffmpeg_path.replace('ffmpeg.exe', '') + 'savefile.json'
    print_app_info()
    print('Now generate frames...')
	#TODO: work with objs!
    Ffmpeg.generate_frames(input_file, framerate, temp_dir, original_frame_first_name, ffmpeg_path)
    print('All frames generated!')
    print('Now counting unique frames...')
    FrameCounter.count_framerate(equal_point_for_compare, temp_dir, framerate, seconds, platform)
    print('All wanted frames counted!')
    print('Now generate frames with graph...')
    GraphGenerator.generate_frames_with_graph(path_to_save_file, temp_dir, width_frame, framerate, original_frame_first_name)
    GraphGenerator.generate_subtitle_from_save(path_to_save_file, platform)


main()