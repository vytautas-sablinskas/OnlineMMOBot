from Handlers.DependencyHandler import DependencyHandler
from Bot.Bot import Bot

if __name__ == '__main__':
    DependencyHandler.check_dependencies()
    bot = Bot()
    bot.run_mmo_bot()