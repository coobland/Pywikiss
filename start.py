# -*- coding: utf-8 -*-

from bottle import Bottle, run, view, static_file, redirect
import json
import markdown
import os


app = Bottle()
 

# Chargement du fichier de config.
config_file = open( 'config.json' )
config = json.loads( config_file.read())

config['WIKI_VERSION'] = 'BlazeKiss 0.1';


@app.route('/')
def home():
	return redirect("/Accueil")

@app.route('/static/<filename:path>')
def server_static(filename):
    """
        Sert les fichiers statiques tel que .js, .css, .jpeg, etc...
    """
    return static_file(filename, root='.')

@app.route('/:mon_id')
@view('template.tpl')
def hello(mon_id):
	config['PAGE_TITLE_BRUT'] = mon_id;

	file_path = "./pages/" + mon_id + ".txt"
	
	print(" -- Chemin du ficheir " + file_path)

	content = ''
	if os.path.exists(file_path):

		print " -- le fichier exist"
		# Ouverture d'un fichier en *lecture*:
		fichier = open(file_path, "r")	 
		toutesleslignes = fichier.readlines()
		content = markdown.markdown(''.join(toutesleslignes))

		# content = markdown.markdownFromFile(fichier)
		
		fichier.close()

		print ' ----  ### CONTENT ### '
		print content


	if len(content) > 0:
		config['CONTENT'] = content
	else:
		config['CONTENT'] = ''
		print " -- Pas de contenu"

	return config
 
# Lancement du serveur sur le port 8080
run(app, host='localhost', port=8080, reloader=True)