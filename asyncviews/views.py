import asyncio
import httpx
from django.http import HttpResponse
from time import sleep

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

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)

def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")

def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")

def home_view(request):
    return HttpResponse("<br> Aula 5: Views Assincronas com Django Async Views OK <br> 127.0.0.1:8000/ home_view pagina inicial OK<br>127.0.0.1:8000/api/ Non-blocking HTTP request OK <br>127.0.0.1:8000/sync/ Blocking HTTP request OK ")
