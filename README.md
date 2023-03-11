# Alles-DLP

Shortcut for iOS and API for youtube-dlp

## Installation

### Docker

First, build the docker image:

```bash

docker build -t alles_dlp .

```

Then, run the docker container:

for example with: `docker run --env=ALLES_DLP_PASSWORDS=12345,67890 --volume=/Users/elisaado/projects/alles-dlp/cookies:/app/cookies -p 8000:8000 -d alles_dlp:latest`

**Notes**

- The `ALLES_DLP_PASSWORDS` environment variable is a comma-separated list of passwords that will be used to authenticate the API.
- The `cookies` volume is used to store the cookies for the different websites. This is might be necessary for some websites to work properly. The cookies are stored in the folder in a file called cookies.txt, formatted as a Netscape cookie file.

When the container is fully installed, we can move on to setting up the shortcut.

### Shortcut

First, we need to install the shortcut. To do so, we need to download the shortcut from the following link.

https://www.icloud.com/shortcuts/2cd20d4cbe864a31b1b343b5db17388e

Now, some of the values in the shortcut (the URL and the password) need to be edited.

Open and edit the shortcut.

Then, edit the following:

- The first text field is the URL of the API (this is the URL of the docker container).
- The second text field is the password that will be used to authenticate the API.

## Usage

When the shortcut is installed, we can use it to download videos, by simply sharing the link to the video with the shortcut in the iOS or MacOS share sheet.

**Notes**

- The shortcut will only work if the API is running.
- The first time the shortcut is used, it will ask for permission to access certain URLs and your photo library. This is necessary to download and save videos to the camera roll.
