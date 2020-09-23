class Album:
    # Инициализируем класс
    def __init__(self, title, group, track_list):
        self.title = title
        self.group = group
        self.track_list = track_list

    # Функция возвращает инфо по всем трекам в альбоме
    def get_tracks(self):
        return self.title, self.group, self.track_list

    # Функция добавляет трек в альбом
    def add_track(self, track_list):
        self.track_list += track_list

    # Функция считает длинну всех треков в альбоме
    def get_duration(self):
        return 'Длинна первого альбома: ', round(song_1.duration + \
        song_2.duration + song_3.duration, 2) , ' Длинна второго альбома: ', \
        song_4.duration + song_5.duration + song_6.duration

class Track:
    # Инициализируем класс
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    # Возвращает название и длительность
    def show(self):
        return self.name, self.duration

# Создаем треки к первому альбому
song_1 = Track('die', float(3.45))
song_2 = Track('depression', float(1.25))
song_3 = Track('pain', float(5.17))

# Создаем треки ко второму альбому
song_4 = Track('beautiful', float(1.45))
song_5 = Track('nice', float(2.25))
song_6 = Track('baby', float(4.55))

# Создаем первый альбом
album_1 = Album('painfull', 'killfuck', [[song_1.name, song_1.duration], \
 [song_2.name, song_2.duration], [song_3.name, song_3.duration]] )

# Создаем второй альбом
album_2 = Album('princess', 'lady', [[song_4.name, song_4.duration], \
[song_5.name, song_5.duration], [song_6.name, song_6.duration]] )

# Метод show выводящий информацию по трекам
print('Информация по трекам: ')
print(song_1.show(), song_2.show(), song_3.show())
print(song_4.show(), song_5.show(), song_6.show())

# Добавляем новые треки в альбом
album_1.add_track([['suffering', 7.77]])
album_2.add_track([['pussy', 2.22]])

# Выводим всю информацию альбома
print('\nИнформация по всем трекам в альбоме: ')
print(album_1.get_tracks())
print(album_2.get_tracks())

# Выводим длину треков в альбоме
print('\nДлина альбомов: ')
print(album_1.get_duration())
