# Pywikiss

Pywikiss is a Wiki developed with KISS (**K**eep **I**t **S**imple **S**tupid) principe. 
It is strongly inspired by [Blazekiss](http://projet.idleman.fr/blazekiss/) but written in python.
It use the micro framework [bottle](http://bottlepy.org). 
Pywikiss use the markdown syntax.

## Install it

* No needs to get bottle, it given with sources. 

* Need python-markdown

    pip install markdown

* Download and decompress Pywikiss archive
* Edit and modify config.json at your convenience, don't forget to change the password
* Make sure the Pywikiss directory and all subdirectories are writable and readable,  if this is not the case, do a chmod 775

## Run it

    python start.py

## Use it

* Click on ***Edit***, at the bottom of the page, to modify the page. Use the password defined in ***config.json*** to validate your modifications.
* Pywikiss is made to use the markdown syntax. I add the following specific syntax to make a reference at a page in the wiki : [[A page]].
* To create a new page, just type the name of the page in the address bar : [http://127.0.0.1/My new page].
* To edit the menu, change the [[Menu]] page. 

## TODO List 

* ~~Manage menu~~
* Manage pages backup  
* Manage toc 
* enregistrer le mot de passe en md5 dans le cookie.
* ~~FIXME : problème d'authentification sur les nouvelles pages.~~
* ~~FIXME : gestion des liens vers les pages un peu douteuse.~~
* FIXME : mauvaise gestion des caractères accentués.
