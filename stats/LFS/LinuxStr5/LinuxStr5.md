# Методы управления программным обеспечением в GNU/Linux

[Статьи](../../stats.md) > [Строение GNU/Linux](../LinuxStr.preview.md)

<pre>
<strong>Автор:</strong> <a href="/LinuxSovet/Group/authors.d/Linuxoid85.html">Михаил Краснов</a>
<strong>Дата написания:</strong> 05.07.2021 00:00 (первоначальная версия); 25.02.2022 22:17 (полностью переработанная текущая версия)
</pre>

## Прелюдия

Доброго времени суток! Цикл "Строение GNU/Linux", над которым я начал работать ещё в 2021 году, оказался довольно популярным - видимо, народу было интересно. Этот цикл я представлял себе намного объёмнее, чем сейчас, но что есть, то есть (в любом случае всё впереди, так как работа над циклом статей ещё не закончена). Но, несмотря на это, статьи отсюда, пусть и в довольно модифицированном виде, вошли в руководство "[Linux для себя](https://lx4u.ru)".

Да, этот цикл давно не обновлялся, но это не значит, что он устарел.

Первая версия этой статьи была простым обзором известных пакетных менеджеров, да и к тому же, она содержала очень большое число фактических ошибок и неточностей. Статья с таким содержимым была бы банальна, ведь таких же "творений" - куча, да и использование пакетного менеджера - не единственный метод управления программным обеспечением, поэтому текущую версию статьи разнообразил сведениями о сборке программного обеспечения из исходного кода.

## Введение

Большинство GNU/Linux дистрибутивов не являются source based. Т.е. они поставляют в своём составе уже собранные (бинарные пакеты). Да, есть несколько source based дистрибутивов, таких, как Gentoo, а системы по руководствам [LFS](https://www.linuxfromscratch.org) и [LX4U](https://lx4u.ru) собираются с нуля с использованием *исключительно* исходного кода необходимых пакетов. Так как сейчас в русскоязычном сегменте интернета очень мало годных статей о методах управления как бинарными пакетами, так и пакетами, собранными из исходного кода, то решил написать свою. Не гарантирую того, что у меня получится что-то очень наиболее полное и подробное, но для новичков здесь будет достаточно информации.

## Что такое пакет?

Пакет - это архив с файлами программы и информацией о ней. Информация о пакете включает в себя:

- Имя программы/библиотеки/etc.
- Версия программы
- Описание программы
- Информация о сопровождающем (сборщике) пакета
- Зависимости пакета
- Все файлы, включенные в пакет (используется не во всех ПМ, так как некоторые умеют сами перечислять файлы пакета, а некоторым требуется указать список файлов самостоятельно).

Информация, представленная выше, используется как человеком, так и пакетными менеджерами, созданные для упрощения управления пакетами.

По содержимому, в свою очередь, пакеты можно разделить на две группы:

1. **Бинарные пакеты**. Содержат уже собранные двоичные файлы пакета.
2. **src-пакеты**. Содержат инструкции по сборке. Редки, но иногда можно встретить и их. Сборочные инструкции, как правило, представляют Shell-скрипт, который запускается пакетным менеджером. Просьба ***не путать*** такие src-пакеты, по-сути, "собираемые" пакетным менеджером, с обычными архивами исходного кода требуемого пакета.

## Что такое пакетный менеджер?

Пакетный менеджер - это программа для GNU/Linux (как и многих других
UNIX-систем), в задачи которой входит:

- Установка пакетов;
- Удаление пакетов;
- Просмотр информации о конкретном пакете;
- Ведение базы данных пакетов, установленных в системе;

Кроме того, в большинстве пакетных менеджеров присутствует обработка
зависимостей и отслеживание конфликтов файлов пакетов.

Исходя из всего вышеописанного, пакет - это программа для UNIX-систем,
предназначенная для управления программным обеспечением, а также ведения базы
данных установленных в системе пакетов, обработки зависимостей пакетов, а также
отслеживания конфликтов файлов пакетов.

## Методы управления ПО в GNU/Linux

Грубо говоря, есть два метода управления ПО в GNU/Linux:

1. Установка уже собранных бинарных пакетов;
2. Сборка программного обеспечения из исходного кода.

У каждой программы для GNU/Linux есть *зависимости* - другие пакеты, без которых искомый не сможет работать, либо будет лишён каких-либо функций. Зависимости можно разделить на следующие категории:

- **Обязательные**. Без них пакет не может функционировать вообще. Если какая-то из обязательных зависимостей не будет присутствовать в конкретном дистрибутиве GNU/Linux, то искомый пакет либо не сможет быть собран из исходного кода (произойдёт ошибка либо на этапе конфигурирования, либо на этапе компиляции), а все пакетные менеджеры, в которых присутствует обработка зависимостей (dpkg, apt, apt-get, rpm, dnf, etc.), либо установят эту обязательную зависимость (высокоуровневые пакетные менеджеры, такие как dnf, apt-get, apt, etc.), либо завершат установку с ошибкой - такое поведение характерно низкоуровневым ПМ, таким как dpkg или rpm, которые устанавливают локальные пакеты (т.е. те пакеты, которые находятся на текущем ПК, а не в каких-то удалённых репозиториях).
- **Рекомендуемые**. Эти зависимости рекомендуются сборщиками пакета и/или разработчиками программы, пакет которой собирается, для установки вместе с искомым пакетом. Возможно, без них он не будет работать корректно при выполнении каких-то определённых задач, либо будет лишён какого-то доп. функционала. Этот вид, а также все следующие (за исключением *конфликтующих*) - *необязательные зависимости*.
- **Опциональные**. Ещё один тип необязательных зависимостей. Добавляют какой-то функционал искомому пакету, более охарактеризовать мне нечего.
- **Конфликтующие**. Если в этой секции указан пакет, который установлен в системе, то перед установкой искомого пакета требуется удалить из системы конфликтующий. Возможно, в этих пакетах предоставляются разные версии какой-либо одной библиотеки, либо конфликтуют какие-либо другие файлы. Во избежание ошибок в работе отдельного ПО или всей системы в целом пакетные менеджеры с обработкой зависимостей удаляют перечисленные в этой секции пакеты перед установкой искомого пакета.

---

## Сборка программного обеспечения из исходного кода

Часть дистрибутивов GNU/Linux предлагают не установку бинарных пакетов, а сборку ПО из исходного кода. Самым известным таким дистрибутивом является, конечно же, Gentoo. В книгах/руководствах LFS и LX4U для создания своего дистрибутива GNU/Linux требуется собрать необходимое ПО исключительно из исходного кода. Кроме того, сборка ПО из сорцов может пригодиться тогда, когда для дистрибутива, которым пользуется человек, нет нужного пакета, так как его разработчик не удосужился собрать бинарные пакеты.

> Далее, с вашего позволения, я буду описывать управление пакетами в типичной системе, собранной по LFS или LX4U, так как там как раз-таки и практикуется метод сборки ПО из исходного кода. Кроме того, там нет никаких усложнений, присущих более "продвинутым" системам.

С одной стороны, при использовании пакетного менеджера (ПМ) значительно упрощается управление ПО, так как ПМ позволяет отслеживать установку файлов, делая процесс удаления и/или обновления пакетов значительно проще. Кроме того, ПМ способен следить за конфликтами файлов при установке пакета (например, в пакете `пакет1` и `пакет2` содержатся разные версии одной и той же библиотеки. ПМ должен обнаружить это и, например, прервать установку какого-то из пакетов, дабы избежать всевозможных конфликтов).

Сборка программного обеспечения из исходного кода может оказаться полезной в следующих случаях:

1. Требуется программа, которая распространяется только в виде исходного кода, а подготовленных бинарных пакетов нет. Как правило, это относится к небольшим проектам, где разработчики не могут/не хотят самостоятельно выполнять компиляцию;
2. Требуется некоторая функция программы, добавить которую можно только путём её пересборки. Особенно это могут понять те пользователи, которые знакомы с LFS или LX4U. Те, кто никогда не собирал всю систему с нуля из исходного кода, возможно, не смогут понять этот пункт.
3. Требуется какая-либо оптимизация к железу, на котором программа собиралась. Тут, в принципе, без комментариев.

### Инструментарий для сборки ПО из исходного кода

Сборка ПО из исходного кода выполняется, как правило, с помощью системы сборки GNU Make, но сейчас появились более современные инструменты, такие как `meson` и `ninja`. Их использует, например, рабочее окружение GNOME Shell. Есть и другие системы сборки, но о них сейчас писать не буду (если заинтересованы - то напишите об этом в комментариях).

В большинстве случаев перед выполнением сборки пользователю требуется создать файл с инструкциями для системы сборки (например, `Makefile` для `make`). Это делается с помощью скрипта `configure`. В том случае, если его нет, то нужно создать и его с помощью программ из пакета `autoconf`. Этот пакет обычно поставляется во всех source-based дистрибутивах "из коробки".

### Методы управления пакетами, собранными из исходного кода

Конечно, здесь рассматривается тот случай, когда вся система собрана из исходного кода. Так как в самой обычной системе несколько сотен пакетов, то и управление ими (а, в особенности, их удаление или обновление до новой версии) может быть проблематичным. Ниже рассмотрены основные практики управления таким ПО.

**1. Держать всё в голове.**

Некоторые читатели зададутся вопросом: "А что это за метод такой?". Да, это метод управления ПО. Есть такие пользователи, которым не нужны утилиты для управления пакетами в системе, так как они и сами знают каждый пакет и какой файл к какому пакету принадлежит. Это довольно сложный метод, да и память у человека не резиновая.

Достоинства:
1. Не используется пакетные менеджеры и прочие утилиты для управления ПО. Достаточно сомнительное достоинство. Хотя в минималистичных системах может быть решающим.

Недостатки:
1. Довольно сложный метод, требующий от человека хорошей памяти для того, чтобы помнить версию пакета, его предназначение, зависимости и прочее. И, что самое главное, список файлов, принадлежащих пакету. При использовании большого числа пакетов эта техника становится неуправляемой.

**2. Установка каждого пакета в отдельные директории.**

Что-то подобное реализовано в NixOS (за исключением того, что это не совсем source-based дистрибутив). Метод довольно простой и понятный, использовать его может каждый. К примеру, есть пакет с именем `pkg1`. Он собирается самым обычным методом (`configure`, `make`), а вот устанавливается в отдельную директорию, к примеру, `/usr/pkgs/pkg1`. В этой директории впоследствии будет создана файловая иерархия как в корне (`/bin`, `/sbin`, `/etc` и пр.) и установлен пакет. После чего из `/usr/pkgs/pkg1/` создаются необходимые ссылки в `/` (например, ссылки на бинарные файлы из `/usr/pkgs/pkg1/bin*` в `/bin/`).

Достоинства:
1. Не требуется программа для управления ПО - каждая программа содержится в отдельной директории. Удобно и просто!
2. Очень лёгкое обновление пакета, либо же его удаление. Достаточно удалить директорию с ним!

Недостатки:
1. Переменные окружения `PATH`, `LD_LIBRARY_PATH`, `MATPATH` и прочие приходится расширить, включив в них директорию с пакетом. Как и в предыдущем случае, этот метод может быть неуправляемым в случае, если используется большое число пакетов.

**3. Использование системы портов.**

Система портов - это набор файлов, в котором содержатся инструкции для сборки и установки пакета, информация о пакете, список устанавливаемых файлов и прочее. Это используется, например, в Gentoo Linux (portage). Про *BSD системы писать здесь не буду, так как это не тема статьи, но там тоже это встречается, например, коллекция портов FreeBSD.

Для системы портов легко можно написать утилиту для её управления, в задачи которой входит:

1. Сборка пакета, используя инструкции из системы портов;
2. Ведение базы данных установленных пакетов;
3. Удаление пакетов;
4. Просмотр информации о пакетах;

И другое.

## Процесс сборки пакета из исходного кода

Этот процесс можно разделить на следующие этапы:

1. Загрузка архива(ов) с исходным кодом пакета.
2. Распаковка архива(ов). В результате этого будет распакована директория, в которой содержится сам исходный код.
3. Переход в эту директорию.
4. Конфигурирование пакета. Как правило, это выполняется с помощью запуска скрипта `configure` с переданными ему необходимыми параметрами. В результате чего будет создан `Makefile`. В том случае, если скрипта `configure` не существует, то его нужно создать. Как правило, то выполняется программами из пакета `autoconf`.
5. Компиляция пакета. Как правило это выполняется с помощью `make`.
6. Установка пакета. `make install`.
7. Выход из директории с исходным кодом и её удаление.

К примеру, у нас есть пакет `pkg1`. Архив с исходным кодом находится по адресу `https://www.pkg1.org/pub/pkg1-1.0.tar.xz`. Сборка выполняется посредством `make`.

```bash
# Загрузка:
wget https://www.pkg1.org/pub/pkg1-1.0.tar.xz

# Распаковка:
tar -xf pkg1-1.0.tar.xz

# Переход в директорию с исходным кодом:
cd pkg1-1.0

# Конфигурирование:
./configure --prefix=/usr --localstatedir=/var --disable-static

# Компиляция:
make -j4
# -j4 - указание потоков сборки, например. Использование необязательно.

# Установка:
make install

# Выход из директории с исходным кодом и её удаление:
cd ..
rm -rf pkg1-1.0
```

Кроме того, перед выполнением сборки было бы неплохим почитать содержимое файлов `README` и `INSTALL` - там содержится достаточно информации для того, чтобы понять предназначение пакета и процесс его сборки.

***

## Использование пакетного менеджера как средство управления программным обеспечением

Использование пакетного менеджера (и, соотв., бинарных пакетов) - это самый распространённый метод. Как уже было написано ранее, пакетный менеджер - это утилита для установки, удаления, обновления пакетов, а также просмотра о них информации.

### Типы пакетных менеджеров

Пакетные менеджеры можно разделить на две подгруппы:

- **Низкоуровневые**. `dpkg` из Debian, `rpm` из RHEL.
- **Высокоуровневые**. `apt-get`, `apt`, `aptitude`, `apt-rpm`, `dnf`, `zypper`, `pacman` и пр. Как правило, являются надстройками над низкоуровневыми (кроме `pacman` в этом списке). Но это не обязательно.

Самым главным различием между типами является то, что низкоуровневые ПМ способны устанавливать только локальные пакеты, т.е. те, которые в данный момент находятся на жёстком диске ПК. Высокоуровневые же, наоборот, скачивают пакет с какого-либо репозитория, после чего выполняют его установку.

Кроме того, большинство высокоуровневых ПМ способны выполнять очистку системы от неиспользуемых зависимостей (помнится, `urpmi` из Mandriva Linux, а также графический интерфейс для него (честно говоря, уже забыл название, но что-то вроде `rpmdrake`) называл такие пакеты "сиротскими").

В обоих типах присутствует обработка зависимостей. Но опять же - низкоуровневые ПМ не способны скачивать ПО из репозиториев конкретного дистрибутива, поэтому в случае отсутствия нужной зависимости в системе (т.е. когда эта зависимость или не установлена, или отсутствует в виде пакета в той же директории, в которой содержится искомый пакет) будет выведена ошибка и установка искомого пакета завершится. В случае высокоуровневого ПМ перед установкой искомого пакета будет построено дерево зависимостей, содержащее список необходимых к установке пакетов, а также порядок их установки. По этому дереву впоследствии будут скачаны нужные пакеты, а потом в построенном порядке они будут установлены.

В дереве зависимостей содержатся все пакеты, указанные как обязательные зависимости искомого пакета. Если у какой-то указанной зависимости есть ещё какая(ие)-то зависимость(и), то и она(и) будет добавлена в дерево. Искомый пакет, как правило, в дереве последний.

### Что содержится в пакетах?

В начале этой статьи было дано определение пакета, а сейчас требуется его расширить для более полного понимания, что это такое. Схематично структуру пакета можно изобразить таким образом:

```
some_pkg.txz
|--- файл с информацией о пакете
|--- preinstall-скрипты (опционально)
|--- postinstall-скрипты (опционально)
|--- файлы скомпилированного пакета (должно повторять иерархию директорий в корне):
   |--- /bin
   |--- /etc
   |--- /usr/
      |--- /share/
         |--- /applications/
         |--- /some/
...
```

В файле информации о пакете содержится его имя, версия, описание (краткое и/или полное), информация о сборщике пакета, а также информация о зависимостях пакета. `preinstall`-скрипты выполняются до установки пакета. Как правило это bash-скрипты, предназначенные либо для настройки системы, либо для настройки пакета перед установкой. `postinstall`-скрипты, соответственно, выполняются после установки пакета. Как правило, они используются для настройки пакета после установки. Например, создаёт какие-либо конфигурационные файлы, сервисы systemd, обновляет initramfs и прочее.

## Зоопарк пакетных менеджеров

Для каждого дистрибутива есть какой-либо свой супер-пупер функциональный и ломовейший ПМ, содержащий в себе блекджек и моднейших девушек, но это можно посчитать и за недостаток. Хотя, достоинство в том, что пользователь может выбрать дистрибутив с нужным ему набором ПО, в том числе и нужным ПМ. Честно говоря, мне мало какие ПМ нравятся сейчас. `dnf` допольно медленный, `apt` не очень хорошо может работать с зависимостями, `urpmi` практически нигде не используется... Поэтому я практикую метод сборки ПО из исходного кода, создал для себя систему портов со сборочными инструкциями необходимого мне ПО, написал утилиту для управления этой системой портов ([тык](https://github.com/CalmiraLinux/cport)). Я не программист, и язык Python, на котором написана эта утилита, осваивал буквально на ходу. Зато я доволен результатом.

Но я отвлёкся, ибо речь шла про зоопарк пакетных менеджеров. В нашем сообществе в [ВК](https://www.vk.com/linuxsovet) я, ещё будучи там админом, писал мануалы по наиболее известным пакетным менеджерам (ссылки на эти статьи будут в конце статьи в блоке "Смотрите также"). А сейчас я продублирую информацию оттуда здесь.

Здесь пойдёт речь о НПМ и ВПМ (низкоуровневых/высокоуровневых ПМ) для двух "основных" дистрибутивов: Debian и RHEL.

> **ВНИМАНИЕ!**

> В заголовку кликните на название ПМ - перейдёте на мои старые статьи, в которых я писал о работе с этими ПМ во времена, когда был админом сообщества LinuxSovet в ВК.

### Debian

В этом дистрибутиве есть низкоуровневый `dpkg`, речь о котором шла ниже, а также `apt` - высокоуровневый ПМ, являющийся надстройкой над `dpkg`. Это довольно неплохие ПМ, но и в них иногда могут встречаться проблемы, не без этого. Но в них мне нравится то, что они довольно быстрые.

**1. [`dpkg`](https://vk.com/@linuxsovet-nebolshaya-spravka-po-dpkg)**

Синтаксис `dpkg`:

```bash
dpkg <ключ> <пакет>
```

**Установка пакета:**

* **Установка пакета(ов):** `-i`: `dpkg -i package.deb`
* **Установка пакета(ов) - 2й вариант:** `--install`: `dpkg --install package.deb`
* **Установка всех пакетов из указанной директории и её поддиректорий (рекурсивно):** `-R`: `dpkg -R --install /путь/до/нужной/директории`
* **Распаковка пакета без установки:** `--unpack`: `dpkg --unpack package.deb`
* **Раздельная распаковка и установка пакета:** `--unpack`, `--configure`: `dpkg --unpack package.deb && dpkg --configure package.deb`


**Удаление пакета:**

* **Удаление пакета без зависимостей:** `-r`: `dpkg -r package`
* **Полное удаление пакета:** `-P`: `dpkg -P package`

**Просмотр информации о пакете:**

* **Просмотр содержимого пакета:** `-c`: `dpkg -c package`
* **Проверить, установлен ли пакет:** `-s`: `dpkg -s package`
* **Просмотреть, куда установлены файлы пакета:** `-L`: `dpkg -L package`

**2. [`apt`](https://vk.com/@linuxsovet-nebolshaya-shpargalka-po-advanced-package-tool)**

Синтаксис `apt`:

```bash
apt <действие> <пакет> <ключ>
```

**Установка или обновление пакета:**

* **Установка пакета:** `install`: `apt install package`
* **Обновление списков пакетов:** `update`: `apt update`
* **Обновление пакетов:** `upgrade`, `full-upgrade`: `apt upgrade && apt full-upgrade`

**Удаление пакетов:**

* **Удаление пакета:** `remove`: `apt remove package`
* **Полное удаление пакета:** `purge`: `apt purge package`
* **Удаление брошенных зависимостей, более не используемых никакими пакетами в системе:** `autoremove`: `apt autoremove`

**Информация о пакетах:**

* **Информация о пакете:** `show`: `apt show package`
* **Список всех установленных пакетов:** `list --installed`: `apt list --installed`
* **Список пакетов, требующих обновления:** `list --upgradable`: `apt list --upgradable`

> **Смотрите также:**

> Кроме `apt` в Debian есть ещё один прекрасный ПМ: [`aptitude`](https://vk.com/@linuxsovet-rabota-s-pm-aptitude). Это очень удобный *интерактивный* ПМ. В некоторых случаях он может оказаться более удобным, чем `apt`. Попробуйте!

### RHEL/Fedora

В этих дистрибутивах используется низкоуровневый `rpm`, а также куча надстроек над ним. Например, высокоуровневый ПМ `dnf`.

**1. `rpm`**

Синтаксис `rpm`:

```bash
rpm <ключ> <пакет>
```

**Установка пакетов:**

* **Установка пакета:** `-i`: `rpm -i package.rpm`
* **Установка пакета - 2й вариант:** `--install`: `rpm --install package.rpm`
* **Установка пакета без учёта его зависимостей:** `--nodeps`: `rpm -i --nodeps package.rpm`
* **Обновление пакета:** `-U`: `rpm -U package.rpm`

**Удаление пакетов:**

* **Удаление пакета:** `-e`: `rpm -e package.rpm`
* **Удаление пакета - 2й вариант:** `--erace`: `rpm --erace package.rpm`
* **Удаление пакета без учёта его зависимостей:** `--nodeps`: `rpm -e --nodeps package.rpm`

**2. [`dnf`](https://vk.com/@linuxsovet-kratkii-man-po-yellowdog-updater-modified)** - ссылка для устаревшего `yum`, форком которого является `dnf`. У них одинаковыые синтаксис и основные опции.

Синтаксис `dnf`:

```bash
dnf <действие> <пакет> <ключ>
```

**Установка или обновление пакета:**

* **Установка пакета:** `install`: `dnf install package`
* **Установка группы пакетов:** `groupinstall`: `dnf groupinstall 'название группы'`
* **Проверка обновлений:** `check-update`: `dnf check-update`
* **Установка обновлений:** `update`: `dnf update`
* **Обновление конкретного пакета:** `update`: `dnf update package`
* **Обновление группы пакетов:** `groupupdate`: `dnf groupupdate 'название группы'`
* **Просмотр списка всех доступных групп:** `grouplist`: `dnf grouplist`

![](pic/dnf_groups.png)

*Список доступных групп*

**Удаление пакета:**

* **Удаление одного пакета с его зависимостями:** `remove`: `dnf remove package`
* **Удаление пакетов из определённой группы:** `groupremove`: `dnf groupremove 'имя группы'`

**Информация о пакете:**

* **Поиск определённого пакета по названию и описанию:** `search`: `dnf search package`
* **Список всех пакетов:** `list`: `dnf list`
* **Список всех установленных в системе пакетов:** `list installed`: `dnf list installed`
* **Информация о пакете:** `info`: `dnf info package`

***

## Смотрите также:

- `man dpkg`
- `man apt`
- `man dnf`
- `man zypper`
- `man make`
- Руководство [LFS](https://linuxfromscratch.org/lfs/view/stable), откуда я взял информацию о методах управления ПО, собранного из исходного кода.

Удачи!
