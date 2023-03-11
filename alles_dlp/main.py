import uvicorn
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route
import yt_dlp
from validators import url as url_validator
import os

passwords = os.environ.get('ALLES_DLP_PASSWORDS').split(',')

opts = {}
if os.path.exists('cookies/cookies.txt'):
    opts['cookiefile'] = 'cookies/cookies.txt'
    print('cookies loaded')


async def homepage(request: Request):
    password = request.query_params.get('password')
    if password not in passwords:
        return JSONResponse({'error': 'no'})

    url = request.query_params.get('url')
    if url is None:
        return JSONResponse({'error': 'no'})

    if not url_validator(url):
        return JSONResponse({'error': 'invalid url'})

    print(url)
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.sanitize_info(ydl.extract_info(url, download=False))
        formats = (info['formats'])
        viable = []
        if (len(formats) == 1):
            viable = formats
        else:
            viable = list(filter(
                lambda format: ('vcodec' in format and format['vcodec'] != 'none') and (format['acodec'] != 'none' if 'acodec' in format else True), formats))

        return JSONResponse({"data": viable})

app = Starlette(debug=True, routes=[
    Route('/', homepage),
])


def start_dev():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("alles_dlp.main:app", host="0.0.0.0", port=8000, reload=True)


def start():
    """Launched with `poetry run start_prod` at root level"""
    uvicorn.run("alles_dlp.main:app", host="0.0.0.0", port=8000)
