from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
      song = request.form["song"]

      songs_file = open("songs.txt", "a")
      songs_file.write(song + "\n")
      songs_file.close()
      
      return render_template("index.html", song=song)
    else:
      songs_file = open("songs.txt", "r")
      songs = songs_file.readlines()
      songs_file.close()
      return render_template("index.html", songs=songs)

app.run(host='0.0.0.0', port=81)
