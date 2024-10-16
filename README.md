# Video Trimmer

## Описание

Video Trimmer — это простой и эффективный скрипт на Python, позволяющий обрезать видеофайлы с помощью библиотеки `moviepy`. Этот инструмент идеально подходит для пользователей, которым нужно быстро выделить нужные фрагменты из длинных видео без сложных настроек и дополнительных инструментов.

## Основные функции

- **Легкость в использовании**: всего несколько строк кода для обрезки видео.
- **Поддержка различных форматов**: работает с популярными видеоформатами, такими как MP4, AVI и другими.
- **Гибкость**: возможность указания времени начала и окончания обрезки, что позволяет точно настроить нужный фрагмент.

## Установка

Для работы скрипта вам потребуется установить библиотеку `moviepy`. Вы можете сделать это, выполнив команду:

```bash
pip install moviepy
```

## Пример использования

Скрипт позволяет обрезать видеофайл, указав время начала и окончания. Пример кода:

```python
from moviepy.video.io.VideoFileClip import VideoFileClip

# Загрузите видео
video = VideoFileClip("input_video.mp4")

# Установите время начала и окончания (в секундах)
start_time = 10  # время начала обрезки
end_time = 20    # время окончания обрезки

# Обрежьте видео
trimmed_video = video.subclip(start_time, end_time)

# Сохраните обрезанное видео
trimmed_video.write_videofile("output_video.mp4")
```

## Примечания

- Убедитесь, что указанные времена находятся в пределах длины видео.
- Скрипт может быть легко адаптирован для обработки нескольких видеофайлов одновременно.

Пользуйтесь Video Trimmer для упрощения процесса редактирования видео и наслаждайтесь созданием уникальных видеороликов!
