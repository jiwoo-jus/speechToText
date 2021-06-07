import moviepy.editor as mp


# mp4파일은 프로젝트 폴더 내부에 있어야 함
clip = mp.VideoFileClip("filename.mp4")
clip.audio.write_audiofile("filename.mp3")