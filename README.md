# LinuxSovet

## Разделы
[Новости сообщества](Group/news.md) | [Статьи](stats/stats.md) | [Правила](Group/rules.md) | [Скачать Calmira Linux](Group/calmira.md)

Доброго времени суток! Ты попал в скромное сообщество GNU/Linux. Здесь ты узнаешь многое об ОС GNU/Linux.

## Основная тематика сообщества:
- новости
- подсказки (помощь новичку)
- советы (помощь новичку)

На данном сайте находятся самые длинные и сложные статьи, которые потом вы читаете в ВК и Telegram ;).

Не стесняйся задавать вопросы, ведь самый простой способ найти ответ — совет опытного пользователя. Взаимопомощь и общение — традиция в мире GNU/Linux. Всегда можно обратиться за помощью к сообществу пользователей и разработчиков GNU/Linux. Большинство вопросов повторяются, поэтому для начала стоит поискать ответ на свой вопрос в документации, затем в сети Интернет. Если вы не нашли ответа в перечисленных источниках, не стесняйтесь, пишите нам в [чат](Group/chats.md) или на [стену](Group/chats.md) [сообщества](https://vk.com/linuxsovet). Так, как писали бы своим друзьям, и вам обязательно помогут. С уважением, с чувством, с толком и с расстановкой.


## Полезные статьи:
* [Python. Отдельные статьи](stats/programming/python/README.md)
* [Получение значений переменных bash в Python](stats/programming/python/environ.md)
* [Пример работы с файлами в C++](stats/programming/cpp/fstream.md)
* [Обзор грядущей Calmira LX4 1.1](stats/blog/calmira_lx4_1.1)
* [Программирование с использованием GTK4 (перевод официальной статьи)](stats/GTK/README.md)
* [Настройка клавиатуры в LFS - часть 2](stats/LFS/keyboard-lfs.md)
* [Строение GNU/Linux:](stats/LFS/LinuxStr.prewiew.md)
	* [Часть 1 - общие понятия](stats/LFS/LinuxStr.md)
	* [Часть 2 - принцип "всё есть файл"](stats/LFS/LinuxStr2/LinuxStr2.md)
	* [Часть 3 - права доступа к файлам](stats/LFS/LinuxStr3/LinuxStr3.md)
	* [Часть 4 - строение ELF файла](stats/LFS/LinuxStr4/LinuxStr4.md)
* [Оперативная память и подкачка](stats/RAM/ram.md)

> Не забывай подписываться на наше [сообщество](https://vk.com/linuxsovet) в ВК, а так же [канал](https://t.me/linuxsovet) и [чат](https://t.me/linuxsovet_chat) в Telegram!

## Новости

* Добавлен раздел со статьями о рабочем окружении [GNOME](stats/GNOME/README.md)! 

Больше новостей [здесь](Group/news.md).

## Поддержка
У сообщества работает неплохая поддержка. При чём делится решением проблем абсолютно безвозмездно. Хотя и не факт, что помогут, но на решение наведут.

* [Чат](https://t.me/linuxsovet_chat)
* [Канал](https://t.me/linuxsovet)
* [Сообщество ВКонтакте](https://vk.com/linuxsovet)

## Программное обеспечение
Помимо написания статей и прочего материала, мы ещё и производим некоторый софт. На данный момент, написаны:

| Название | Версия | ЯП | Ссылка для скачивания |
|:---------|:-------|:---|:----------------------|
| Helper   | 0.06.1.2020 (разработка окончена) | Bash | [deb-пакет](https://github.com/Linuxoid85/helper/releases/download/0.06.2.2020/Helper.deb), [tar архив](https://github.com/Linuxoid85/helper/releases/download/0.06.2.2020/Helper.tar) |
| Calmira GNU/Linux | LX4 1.1 Test build 2 | some langs | [Base](https://github.com/CalmiraLinux/CalmiraLinux/releases/download/v1.1rc2/calmira-1.1_test2.sfs) [Остальные релизы](https://github.com/CalmiraLinux/CalmiraLinux/releases/tag/v1.1rc2) |

### Calmira Linux
Это легковесный независимый дистрибутив со своей пакетной базой.

Главная особенность дистрибутива - его малый размер и неприхотливость. Для работы ему будет достаточно процессора Intel Atom, оперативной памяти объёмом от 30 Мб и жёсткого диска от 2-3 Гб.

Пакетный менеджер `cpkg` (релиз Calmira 2021.2), пришедший на смену `cpkg-tools` из релиза Calmira 2021.1, содержит множество изменений. Тут и более стабильная работа, и хорошая работа с добавлением пакета в свою БД, а так же меньшая разрозненность. Установка и удаление ПО теперь следует одним и тем же правилам.

Однако основной упор делается на сборку пакетов из исходного кода. В релиз LX4 1.1 войдёт система портов, автоматизирующая сборку ПО. В неё войдут все пакеты из базовой системы, а так же несколько дополнительных. В первую очередь, система портов предназначена для автоматизированной сборки новых релизов дистрибутива.

### Идеология, следование принципам
Дистрибутив старается следовать стандартам FHS и LSB в первую очередь. Помимо этого, дистрибутив "проповедует" KISS.

### Скачивание
Текущий билд вы можете скачать из таблицы выше. А так же зайдите на [GitHub](https://github.com/Linuxoid85/CalmiraLinux) проекта, чтобы следить за последними новостями.

## Сотрудничество
Нам требуются авторы! Пишите статьи о строении, настройке и работе с GNU/Linux, если вы хотите, чтобы сообщество развивалось быстрее! О сотрудничестве читайте [здесь](Group/authors.md).

***

В декабре 2020 нам исполнился год!

![Аватарка группы](ava.jpg "Логотип сообщества")

***
(C) 2019-2021 [Linuxoid85](https://www.vk.com/linuxoid85). При копировании материалов с сайта указание первоисточника **обязательно**!

Репозиторий был создан 25 апреля 2021 года для публикования разных заметок о Linux, наблюдений и прочего, что многим не будет интересно :). Используется GitHub Pages. Тема: Hacker. Простая тема, хотя некоторым может показаться страшной.
