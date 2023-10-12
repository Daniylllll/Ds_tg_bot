

if __name__ == '__main__':
    from aiogram import executor
    from all_work import dp
    executor.start_polling(dp, skip_updates=True)