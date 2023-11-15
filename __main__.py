import logging

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    filters,
    MessageHandler,
)

from config import TOKEN
from handlers import (
    start_handler,
    help_handler,
    csv_load_handler,
    graph_handler,
    optimized_graph_handler
    )

COMMAND_HANDLERS = {
    "start": start_handler,
    "help": help_handler,
    "graph": graph_handler,
    "optimized_graph": optimized_graph_handler
}

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(MessageHandler(
        filters.Document.ALL, csv_load_handler)
                            )
    for command_name, command_handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_handler))
    application.run_polling()


if __name__ == "__main__":
    main()
