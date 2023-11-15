from telegram import Update
from telegram.ext import ContextTypes

from graph import with_algorithm, without_algorithm


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        """Привет! Я умею строить графы по точкам из файла формата .csv, а также оптимизировать их. Чтобы подробнее узнать про функционал, введите команду /help."""
    )


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        """Прежде всего необходимо загрузить файл в формате .csv, для этого просто отправьте его боту.
/graph - построить граф.
/optimized_graph - построить оптимизированный граф.

csv-файл должен быть следующего формата:
edges
name_of_point1,name_of_point2
# ребра
positions
name_of_point,x,y
# точки


Пример csv-файла и результата с ним:

edges
name_of_point1,name_of_point2
лекторий,спорт-зал
столовка,спорт-зал
лекторий,кофепоинт
матеша,спорт-зал
positions
name_of_point,x,y
кофепоинт,2,10
лекторий,3,3
спорт-зал,6,6
столовка,9,9
матеша,6,12

"""
    )
    await update.message.reply_text("С командой /graph")
    without_algorithm("example_data.csv", "graph.png")
    photo = open("graph.png", "rb")
    await update.message.reply_photo(photo)
    photo.close()
    await update.message.reply_text("С командой /optimazed_graph")
    with_algorithm("example_data.csv", "graph.png")
    photo = open("graph.png", "rb")
    await update.message.reply_photo(photo)
    photo.close()


async def csv_load_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = await context.bot.get_file(update.message.document)
    await file.download_to_drive("data.csv")
    await update.message.reply_text("Файл успешно загружен.")


async def graph_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        without_algorithm("data.csv", "graph.png")
        photo = open("graph.png", "rb")
        await update.message.reply_photo(photo)
        photo.close()
    except FileNotFoundError:
        await update.message.reply_text("Вы не загрузили файл.")


async def optimized_graph_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    try:
        with_algorithm("data.csv", "graph.png")
        photo = open("graph.png", "rb")
        await update.message.reply_photo(photo)
        photo.close()
    except FileNotFoundError:
        await update.message.reply_text("Вы не загрузили файл.")
