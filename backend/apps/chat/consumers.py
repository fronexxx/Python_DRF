from djangochannelsrestframework.generics import GenericAsyncAPIConsumer


class ChatConsumer(GenericAsyncAPIConsumer):
    async def connect(self):
        if not self.scope['user']:
            return await self.close()
        return await super().connect()