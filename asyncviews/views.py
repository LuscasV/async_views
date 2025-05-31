import asyncio
import httpx
from django.http import HttpResponse

# Função assíncrona que realiza uma contagem e uma requisição HTTP
async def new_http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)  # Pausa a execução por 1 segundo
        print(num)  # Imprime o número atual
    async with httpx.AsyncClient() as client:
        r = await client.get("https://jsonplaceholder.typicode.com/posts")  # Faz uma requisição GET
        print(r)  # Imprime a resposta da requisição

# Nova view assíncrona que chama a função acima
async def new_async_view(request):
    loop = asyncio.get_event_loop()  # Obtém o loop de eventos atual
    loop.create_task(new_http_call_async())  # Cria uma tarefa assíncrona
    return HttpResponse('Non-blocking HTTP request from new_async_view')  # Retorna uma resposta HTTP
