from time import sleep
class User:
    """Класс пользователей для инициализации """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return self.nickname
class Video:
    """Класс для инициализации видео хранящий в себе параметры видео :
    Наименование , длительность, и возрастное ограничение
    """
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


class UrTube:
    """Класс просмотра для просмотра видео содежащий методы :
    log_in , register , log_out , add , get_videos , log_out , watch_video ,
     """

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self,nickname, password):
        """Метод входа в профиль"""
        if nickname in str(self.users):                   #Если пользователь существует в списке пользователей
            for find_user in self.users:                  #Считываем логин и пароль пользователя из существующих
                # Сравниваем логин и пароль по хэш
                if hash(password) == find_user.password and nickname == find_user.nickname:
                    self.current_user = nickname
                    #print(f'Добро пожаловать {nickname}')
                elif hash(password) != find_user.password and nickname == find_user.nickname:
                    print('Пароль не правильный')
        else:
            print('Такого пользователя нет!')



    def register(self, nickname, password, age):

        """Метод регистрации  с последующим входом в профиль"""

        if nickname in str(self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))  # Добавление пользователя в список зарегестрированных
                                                                # пользователей
            #print('зарегался')
            self.log_in(nickname,password)       # Передаем значения в метод входа в профиль


    def log_out(self):
        """Метод выхода из профиля"""
        print(f'Досвидания {self.current_user}')
        self.current_user = None


    def add(self,*args):
        """Метод добавления видео """

        for k in args:   # Перебираем значения аргс и сравниваем по титулу с нижним регистром с существующим списком 
            if k.title.lower() not in (str(self.videos)).lower(): 
                self.videos.append(k)

        return self.videos

    def get_videos(self, search_value):
        """Метод поиска видео по совпадению строк без учета регистра"""

        find_list = []   # Cоздали список видео который должен возвратить по итогу поиска
        for j in self.videos:    # Перебираем существующие видео и в случае совпадений добавляем в find list
            if search_value.lower() in (str(j).lower()):
                find_list.append(j)
        return find_list

    def __str__(self):
        return self.videos
    def __repr__(self):
        return self.video()

    def watch_video(self,video):

        """Метод просмотра видео в корый передается точное наименование видео
         если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр"""

        if self.current_user == None: # Проверка на вход в аккаунт
            print( f"Войдите в аккаунт, чтобы смотреть видео")

        elif video in str(self.videos) and self.current_user: # Если существующее видео найдено и юзер залогинился
            for i in self.videos:                             # Перебираем список видео для определения его параметров
                if video in i.title and i.adult_mode == True:  # Исключаем видео по имени и возрастному ограничению
                    for user in self.users:
                        if user.nickname == self.current_user and user.age < 18: # Если тек. юзеру меньше 18 лет
                                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        elif user.nickname == self.current_user and user.age >= 18: # Если ему больше либо 18 лет
                            for duration_ in range(1, i.duration + 1):
                                sleep(1), print(duration_)          # Пользуемся методом sleep из библиотеки time
                            print('Конец видео')

                elif video in i.title and i.adult_mode == False:  #Если у видео нет возрастных ограничений
                    for duration_ in range(1, i.duration + 1):
                        sleep(1), print(duration_)
                    print('Конец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# Добавление видео
ur.add(v1, v2,v3)
ur.add(v3)
print(ur.videos)

#Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
# print(ur.users[vasya_pupkin].age)
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

#Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

#Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')





