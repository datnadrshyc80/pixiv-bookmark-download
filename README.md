A simple Python script to download Pixiv favorites to local using RSSHub.

Use the command `pip install -r requirements.txt` to install the required Python packages.

Login to your Pixiv personal page, copy the numerical ID from the URL and paste it at the end of `RSS_URL = 'https://rsshub.app/pixiv/user/bookmarks/'`.

Run `python main.py` to start downloading images from your Pixiv favorites. The downloaded images will be saved in the `downloaded_images` folder by default, and the URLs of the downloaded images will be automatically stored in the `downloaded_images.txt` file to avoid duplicate downloads.