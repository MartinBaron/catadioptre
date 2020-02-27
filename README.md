# photo-palourde

##COMMENT IMPORTER UN NOUVEL ALBUM ?

* **Etape 1** : exporter les photos de l'album en qualité maximale raisonnable dans le dossier input (vérifier qu'il est bien vide avant cela)
* **Etape 1bis** : *FACULTATIF* Pour avoir un ordre spécial des photos dans l'album, les renommer dans l'ordre alphabétique souhaité.
* **Etape 2** : ouvrir le terminal (Applications -> Terminal). On doit se trouver dans le dossier Laura, de là faire la commande *cd rob_work/catadioptre*
* **Etape 3** : maintenant qu'on est dans le même dossier que import_album.py, on peut faire la commande *python3 import_album.py* Plusieurs questions vont être posées, bien mettre le nom de l'album tel qu'il apparaîtra sur le site et choisir la photo de couverture de l'album. La date doit être entrée au format MM/AAAA exemple (02/2019)
* **Etape 4** : une fois l'import terminé, aller dans le dossier output et double cliquer sur index.html. Cela va ouvrir le site dans Firefox. Se balader sur le site pour vérifier que tout est ok avec le nouvel album.
* **Etape 4bis** : *FACULTATIF* Si jamais il y a eu un problème avec l'import et qu'on veut recommencer, alors supprimer le dossier du nouvel album dans le dossier output/albums. Ouvrir le fichier albums.csv et supprimer la ligne de l'album qu'on vient d'ajouter. Prendre garde à bien laisser une ligne vide à la fin. Si malgré cela, le site est toujours cassé, alors copier le contenu de output/backup dans le dossier output, pour revenir au site tel qu'il était au début de la manip.
* **Etape 5** : si tout est ok, alors on peut publier le site sur le serveur à l'aide de la commande : *scp -r ./output/* photo-palourde@buddha.all2all.org:./public/* Un mot de passe sera demandé pour exécuter la commande.


