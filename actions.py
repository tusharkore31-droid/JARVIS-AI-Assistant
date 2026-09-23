import subprocess
import webbrowser
from urllib.parse import quote


def open_chrome():
    subprocess.Popen("start chrome", shell=True)


def search_youtube(query):
    url = "https://www.youtube.com/results?search_query=" + quote(query)
    webbrowser.open(url)