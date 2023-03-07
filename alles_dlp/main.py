import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'helloaa': 'world'})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("alles_dlp.main:app", host="0.0.0.0", port=8000, reload=True)

import yt_dlp
import json

# url = "https://www.youtube.com/watch?v=FPKFB0yqLr0"
url = "https://www.instagram.com/reel/CgqamKaLxsM/?igshid=YmMyMTA2M2Y="
with yt_dlp.YoutubeDL({})  as ydl:
  info = ydl.sanitize_info(ydl.extract_info(url, download=False))
  formats = (info['formats'])
  viable = []
  if (len(formats) == 1):
    viable = formats
  else:
    viable = list(filter(lambda format: format['vcodec'] != 'none' and format['acodec'] != 'none', formats))

  print(len(formats))
  print(len(viable))
  print(viable)

  ydl.download(url_list)