import uvicorn
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route
import yt_dlp
from validators import url as url_validator
import os

try:
    passwords = os.environ.get('ALLES_DLP_PASSWORDS').split(',')
except:
    raise Exception('ALLES_DLP_PASSWORDS not set')

opts = {
    "quiet":    True,
    "simulate": True,
    "forceurl": True,
    # don't download playlists, as it doesn't really work with the ios shortcut
    'noplaylist': True,
    'playlist_items': '1'
}

if os.path.exists('cookies/cookies.txt'):
    opts['cookiefile'] = 'cookies/cookies.txt'
    print('cookies loaded')


async def homepage(request: Request):
    password = request.query_params.get('password')
    if password not in passwords:
        return JSONResponse({'error': 'no'})

    url = request.query_params.get('url')
    if url is None:
        return JSONResponse({'error': 'no url'})

    if not url_validator(url):
        return JSONResponse({'error': 'invalid url'})

    with yt_dlp.YoutubeDL(opts) as ydl:
        try:
            info = ydl.sanitize_info(ydl.extract_info(url, download=False))
            print(info)
            formats = info["formats"]

            viable = []
            if (len(formats) == 1):
                viable = formats
            else:
                for format in formats:
                    vcodec_none = (
                        'vcodec' in format and format['vcodec'] == 'none')
                    video_ext_none = (
                        'video_ext' in format and format['video_ext'] == 'none')

                    if vcodec_none and video_ext_none:
                        format['video_ext'] += " (no video)"

                    # skip anything without audio
                    if 'acodec' in format and format['acodec'] == 'none':
                        continue

                    # skip m3u8
                    if 'protocol' in format and "m3u" in format['protocol']:
                        continue

                    viable.append(format)

            return JSONResponse({"data": viable})
        except Exception as e:
            return JSONResponse({'error': repr(e)})

app = Starlette(debug=not not os.environ.get('ALLES_DLP_DEBUG', False), routes=[
    Route('/', homepage),
])


def start_dev():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("alles_dlp.main:app", host="0.0.0.0", port=8000, reload=True)


def start():
    """Launched with `poetry run start_prod` at root level"""
    uvicorn.run("alles_dlp.main:app", host="0.0.0.0", port=8000)
