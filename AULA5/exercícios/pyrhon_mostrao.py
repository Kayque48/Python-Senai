import webbrowser

#informe a URL do vídeo aqui:
url = "https://www.youtube.com/watch?si=c1fJpll8BaX9be0T&v=QoAbDOgXBYo&feature=youtu.be"

download = url[:12] + "SS" + url[12:]

webbrowser.open(download)