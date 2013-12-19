# -*- coding: utf-8 -*-

from bottle import Bottle, run, view, static_file
import json


app = Bottle()
 

config_file = open( 'config.json' )
config = json.loads( config_file.read())

config['WIKI_VERSION'] = 'BlazeKiss 0.1';

# Load configuration from a json file
# with open('config.json') as fp:
#     app.config.load_dict(json.load(fp))

@app.route('/')
def home():
	return "Salut Coco"

@app.route('/toto')
@view('test1.tpl')
def toto():
	return {'titre' : 'toto'}


@app.route('/:mon_id')
@view('template.tpl')
#@view('t.tpl')
def hello(mon_id):
	config['WIKI_TITLE_BRUT'] = mon_id;

	return config
 
@app.route('/static/<filename:path>')
def server_static(filename):
    """
        Sert les fichiers statiques tel que .js, .css, .jpeg, etc...
    """
    return static_file(filename, root='.')

run(app, host='localhost', port=8080, reloader=True)