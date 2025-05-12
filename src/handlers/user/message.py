from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from src.utils.db import MongoDbClient
from fluentogram import TranslatorRunner


router = Router()

@router.message(Command("start"))
async def _(message: Message, bot: Bot, db: MongoDbClient, locale: TranslatorRunner):
    await message.answer(locale.welcome_text())