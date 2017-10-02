import asyncio
import contextlib
import logging

from tapirbot import TapirBot


@contextlib.contextmanager
def setup_logging():
    """Context manager makes things much cleaner"""
    try:
        # Basically __enter__
        logging.getLogger('discord').setLevel(logging.INFO)
        logging.getLogger('discord.http').setLevel(logging.WARNING)

        log = logging.getLogger()
        log.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='tapirbot.log',
                                      encoding='utf-8', mode='w')
        dt_fmt = '%Y-%m-%d %H:%M:%S'
        fmt = logging.Formatter('[{asctime}] [{levelname:<7}] {name}: {message}',
                                dt_fmt, style='{')
        handler.setFormatter(fmt)
        log.addHandler(handler)

        yield
    finally:
        # Basically __exit__
        handlers = log.handlers[:]
        for hdlr in handlers:
            hdlr.close()
            log.removeHandler(hdlr)


def run_bot():
    """The function that actually runs the bot"""
    loop = asyncio.get_event_loop()
    log = logging.getLogger()

    # Should probably put some stuff here later for the database

    bot = TapirBot()
    # More database stuff here probably
    bot.run()

if __name__ == '__main__ ':
    """Starting the bot when this file is ran"""
    loop = asyncio.get_event_loop()
    with setup_logging():
        run_bot()
