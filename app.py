from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():

    #!Titre
    title = "LINFO1002 - Projet 2 : Visualisation de données"
    
    #!Liste des paragraphes
    paragraph = ["Groupe Ralph Abona,Igor Bertrand,Romain Carlier"]
    


    return render_template("index.html", title = title, paragraph = paragraph)
    
    
@app.route('/about')
def aboutpage():

    title = "A propos de ce projet"
    paragraph = ["bla bla bla bla bla bla bla bla bla bla"]
    
    pageType = 'doc'
    
    return render_template("index.html", title = title, paragraph = paragraph, pageType = pageType)
    

@app.route('/about/documentation')
def docPage():

    title = "A propos de ce projet"
    paragraph = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius massa eu tempor commodo. Aliquam dapibus ligula in tortor venenatis, id porttitor tellus tempus. Nullam maximus est et turpis aliquet tristique. Etiam et sapien condimentum ex posuere lacinia. Aliquam erat volutpat. Vestibulum quis lorem pulvinar, vestibulum turpis eget, vestibulum ipsum. Donec hendrerit, mi et pretium vestibulum, sem felis commodo sem, quis varius est lorem eget erat. Donec euismod risus sed justo ultrices, id consectetur mi tempor. Curabitur elementum eget risus quis gravida. Etiam consectetur tortor quis diam sollicitudin auctor. Nulla vel faucibus purus, volutpat viverra massa. Fusce orci tortor, elementum.",
    "Praesent vehicula elit vitae luctus finibus. In et facilisis lectus, id pharetra metus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam viverra pellentesque arcu, vitae molestie nulla. Integer et dictum quam. Ut elit metus, pellentesque ac ex vitae, fermentum vestibulum mauris. Donec ullamcorper erat."
    ]
    
    pageType = 'about'
    
    return render_template("index.html", title = title, paragraph = paragraph, pageType = pageType)
 
if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
