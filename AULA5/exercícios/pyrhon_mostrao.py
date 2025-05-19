import webbrowser

#informe a URL do vídeo aqui:
url = "https://www.youtube.com/watch?v=vTjHa5PumZE"

download = url[:12] + "SS" + url[12:]

webbrowser.open(download)