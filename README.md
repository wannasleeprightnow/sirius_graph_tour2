# sirius-map-telegram-bot

## Наше понимание кейса

Избыточными мы решили считать те вершины, которые имеют только 2 связи => являются промежуточными. Также возможна реализация определения избычточных вершин методом анализа угла между смежными путями при помощи теоремы косинусов определения длины вектора.

Теорема косинусов:
![](https://github.com/wannasleeprightnow/sirius_graph_tour2/raw/main/images/cosine_theorem.png)

Длина вектора:
![](https://github.com/wannasleeprightnow/sirius_graph_tour2/raw/main/images/vector_length.png)

## Команды бота
- /start - начинает работу с ботом.
- /help - описание функциональности бота.
- /graph - отправляет картинку с построенным графом.
- /opimized_graph - отпраляет картинку с оптимизированным пстроенным графом.

## Запуск

Требуется Python3.12.

Инструкция для запуска на linux:

Клонирование репозитория:

```bash
git clone https://github.com/wannasleeprightnow/sirius_graph_tour2
cd sirius_graph_tour2/
```

Создание и активация виртуального окружения:

```bash
python3 -m venv venv
source venv/bin/activate
```

Токен нужно получить у @BotFather и подставить его в значение TOKEN.

```bash
echo "TELEGRAM_TOKEN = """ > .env
```

Обновление pip, установка зависимостей и запуск:
```bash
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 __main__.py
```
