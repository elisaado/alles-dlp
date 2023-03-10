# Alles-DLP

Shortcut for iOS and API for youtube-dlp

## Installation

### Docker

Run the docker container. The image is built for linux/amd64 and linux/arm64.

```bash
docker run --env=ALLES_DLP_PASSWORDS=12345,67890 --volume=/Users/elisaado/projects/alles-dlp/cookies:/app/cookies -p 8000:8000 -d ghcr.io/elisaado/alles-dlp:master
```

- The `ALLES_DLP_PASSWORDS` environment variable is a comma-separated list of passwords that will be used to authenticate access to the webserver.
- The `cookies` volume is used to store the cookies for the different websites. This is might be necessary for some websites to work properly. The cookies are stored in the folder in a file called cookies.txt, formatted as a Netscape cookie file.

### Shortcut

First, we need to install the shortcut. To do so, we need to download the shortcut from [here](https://www.icloud.com/shortcuts/2cd20d4cbe864a31b1b343b5db17388e).

Open and edit the shortcut. We need to change the following parameters:

- The first text field is the URL of the API (this is the URL of the docker container).
- The second text field is the password that will be used to authenticate the API.

## Usage

When the shortcut is installed, we can use it to download videos, by simply sharing the link to the video with the shortcut in the iOS or MacOS share sheet.

- The shortcut will only work if the API is running.
- The first time the shortcut is used, it will ask for permission to access certain URLs and your photo library. This is necessary to download and save videos to the camera roll.
