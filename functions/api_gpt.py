import aiohttp


class ConnectGPT:

    """
    Данный класс необходим для подключения к серверу ChatGPT
    """

    URL = r'https://ask.chadgpt.ru/api/public/gpt-4o-mini'


    def __init__(self, gpt_token: str) -> None:
        self.GPT_TOKEN = gpt_token


    async def send_query_gpt(self, query: str, history: list[dict] = []) -> dict | None:
        
        """
        Данный метод отправляет запрос на сервер Чата GPT.
        """

        query_json = {
            'message': query,
            'api_key': self.GPT_TOKEN,
            "history": history
        }

        async with aiohttp.ClientSession() as session:
            response = await session.post(url=self.URL, json=query_json)

        if response.status == 200:
            return await response.json()
        