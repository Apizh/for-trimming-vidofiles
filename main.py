from moviepy.video.io.VideoFileClip import VideoFileClip

# Замените 'input_video.mp4' на путь к вашему видео
input_video = r"C:\Users\admin\Downloads\Array tuples.MP4"
output_video = r'C:\Users\admin\Videos\GeekBrains\Algoritms-Haffman\Hashes.mp4'

start_time = 11 * 60 +30 # Начало обрезки
end_time = 1 * 3600 + 30 * 60 + 30

clip = VideoFileClip(input_video)

# Обрезаем видео
trimmed_clip = clip.subclip(start_time, end_time)

# Сохраняем обрезанное видео с оптимизированными параметрами
trimmed_clip.write_videofile(output_video, codec='libx264', threads=5)

# Закрываем видеофайл
clip.close()