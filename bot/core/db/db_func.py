#Copyright 2022-present, Authors: @AbirHasan2005 & 5MysterySD

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from config import Config, LOGGER, USERS_API
from bot.client import Client
from pyrogram.types import Message

class Database:
    def __init__(self, uri, database_name):
        self._client = AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    async def db_load(self):
        all_users = await self._getAllUsers()
        async for user in all_users:
            USERS_API[user['id']] = user['token']
        LOGGER.info('[MongoDB] User Data Imported from Database')

    def _newUser(self, id):
        return dict(
            id=id,
            token=None
        )

    async def _addUser(self, id):
        user = self._newUser(id)
        await self.col.insert_one(user)

    async def _isUserExists(self, id):
        user = await self.col.find_one({'id': int(id)})
        return bool(user)

    async def _totalUsers(self):
        count = await self.col.count_documents({})
        return count

    async def _getAllUsers(self):
        return self.col.find({})

    async def _deleteUser(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def _setUserToken(self, id, Token):
        await self.col.update_one({'id': id}, {'$set': {'token': Token}})

    async def _getUserToken(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('token', None)

    async def _getSingleUserData(self, id) -> dict:
        user = await self.col.find_one({'id': int(id)})
        return user or None

db = Database(Config.MONGODB_URI, "UploadEver-TBot")
asyncio.run(db.db_load())

async def _addNewUserToDB(c: Client, m: Message):
    if not await db._isUserExists(m.from_user.id):
        await db._addUser(m.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await c.send_message(
                int(Config.LOG_CHANNEL),
                f"#NEW_USER: \n\nNew User : {m.from_user.mention}\nUser ID : {m.from_user.id} !!",
                parse_mode=enums.ParseMode.HTML
            )
