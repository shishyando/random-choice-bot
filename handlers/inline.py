from aiogram import types

from loader import dp
from . import refactor


@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="0",
                title="Need an example?",
                description="you will send an example message to see how the bot works",
                input_message_content=types.InputTextMessageContent(
                    message_text="A message: <code>@rnd_choice_bot A B C</code>\n"
                                 "randomly chooses from\n"
                                 "<b>A</b>\n"
                                 "<b>B</b>\n"
                                 "<b>C</b>\n\n"
                                 "The result also shows the chance of choosing that variant\n"
                                 "For more info type /help or /start in PM"

                )
            )
        ],
        switch_pm_text="Get bot info",
        switch_pm_parameter="give_info",
        cache_time=86400
    )


@dp.inline_handler()
async def choice_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="#1: with variants",
                description="all provided variants will be shown",
                input_message_content=types.InputTextMessageContent(
                    message_text=refactor.get_message(query.query, show_variants=True)
                )
            ),
            types.InlineQueryResultArticle(
                id="2",
                title="#2: only result",
                description="only result will be shown",
                input_message_content=types.InputTextMessageContent(
                    message_text=refactor.get_message(query.query, show_variants=False)
                )
            ),
        ],
        cache_time=0
    )
