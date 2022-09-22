#Copyright 2022-present, Authors: @AbirHasan2005 & 5MysterySD

import datetime
import motor.motor_asyncio
from configs import Config, LOGGER


class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

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
        dbData = self.col.find({})
        LOGGER.info(dbData)
        return dbData

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
