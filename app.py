from flask import Flask, render_template
from views import views
import os
# das hier ist einfach alles boiler code. Ändere am besten nichts an den
# Variablenamen oder an den Dateinamen von den Python Dateien, dann gehen bestimmt
# Dinge kaputt.

# die Kommentare auf Englisch sind von mir, als ich das hier das erste mal geschrieben hab

# den Ordner __pychache__ kannst du übrigens ignorieren, den legt Python automatisch
# an, wenn man Dinge hin und her importiert
 
app = Flask(__name__)
img = os.path.join('static', 'medien', 'images_main')
@app.route('/')
def home():
    file = os.path.join(img, 'me.png')
    return render_template('main1.html', me=file)

#img = os.path.join('static', 'medien', 'images_main')
#@app.route('/')
#def home():
#    city = os.path.join(img, 'city_identity.png')
 #   return render_template('main1.html', city_identity=city)

 
#@app.route('/') # ich habe versucht eine Liste fur Fotos erstellen, trotzdem functioniert das nicht
#def index():
 #   images = ['city_identity.png', 'exhibition_catalogue.png', 'wine_packaging_design.png', 'packaging_design.png', 'book_printing.png', 'dvd_box.png']  # Add more filenames as needed
  #  return render_template('main1.html', images=images)

app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)  # automatically reruns the website if code is changed