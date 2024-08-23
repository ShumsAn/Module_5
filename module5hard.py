from time import sleep
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password
    def __hash__(self):
        return hash((self.nickname, self.password))
    def __repr__(self):
        return self.nickname
class Video:
    def __init__(self,title,duration,adult_mode = False):
        time_now = 0
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title
    def dict_v(self):
        video_dict = dict.fromkeys(self.title, self.adult_mode)
        return video_dict
class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self,nickname, password):
        if nickname in str(self.users) :
            self.current_user = nickname

    def register(self, nickname, password, age):
        if nickname in str(self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))
            self.dict_u = {nickname: age}
            self.log_in(nickname,password)

    def log_out(self):
        self.current_user = None
        return self.current_user

    def add(self,*args):
        a = ' '.join(self.videos)
        for j in args:
            if (str(j)).upper() not in a.upper():
                    self.videos.append((j))

        return self.videos

    def get_videos(self, get):
        find_list = []
        for j in self.videos:
            if get.lower() in (str(j).lower()):
                find_list.append(j)
                #print(f"Нашел: {j} ")
        return find_list

    def __str__(self):
        return self.videos
    def __repr__(self):
        return self.video()

    def watch_video(self,video):
        if self.current_user == None:
            print( f"Войдите в аккаунт, чтобы смотреть видео")

        elif video in str(self.videos) and self.current_user:
            for i in self.videos:
                if video in i.title and i.adult_mode == True:
                    if self.dict_u[self.current_user] < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        #print(f'Наконецто смотрю : {video}')
                        for duration_ in range(1, i.duration + 1):
                            sleep(1), print(duration_)
                        print('Конец видео')
                elif video in i.title and i.adult_mode == False:
                    for duration_ in range(1, i.duration + 1):
                        sleep(1), print(duration_)
                    print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')





