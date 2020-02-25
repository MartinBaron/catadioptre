#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import unidecode
import string
import shutil
import imghdr

try:
    from PIL import Image
    import hitherdither
    enabled = True
except:
    logging.warning("Unable to load PIL or hitherdither, disabling thumbnailer")
    enabled = False

DEFAULT_DITHER_PALETTE = [(25,25,25), (75,75,75),(125,125,125),(175,175,175),(225,225,225),(250,250,250)] # 6 tone palette\
DEFAULT_THRESHOLD = [96, 96, 96]
DEFAULT_MAX_SIZE = (500,500)
DEFAULT_MAX_SIZE_ORIGINAL = (200,200)

def create_folders(album_name):
	cur = os.getcwd()
	if not os.path.exists("./output/albums/" + album_name + '/'):
		os.makedirs("./output/albums/" + album_name + '/')
	if not os.path.exists("./output/albums/" + album_name + '/photo/'):
		os.makedirs("./output/albums/" + album_name + '/photo/')
	if not os.path.exists("./output/albums/" + album_name + '/photo_page/'):
		os.makedirs("./output/albums/" + album_name + '/photo_page/')
	if not os.path.exists("./output/albums/" + album_name + '/photo_vignette/'):
		os.makedirs("./output/albums/" + album_name + '/photo_vignette/')



def rename_photos(input, album_name):
	dst = os.getcwd() + '/output/albums/' + album_name + '/photo/'
	photos = os.listdir(input)
	photos = sorted(photos)
	photo_counter = 1
	for p in photos :
		if p=='.DS_Store':
			continue
		if photo_counter < 10 :
			new_name = '0' + str(photo_counter) + '.jpg'
		else:
			new_name = str(photo_counter) + '.jpg'
		print("La photo "+ p + " a été importée et renommée en " +new_name)
		#os.rename(os.getcwd() + '/input/'+p, os.getcwd() + '/output/albums/'+ album_name + '/photo/'+ new_name)
		os.rename(os.getcwd() + '/input/'+p, os.getcwd() + '/input/'+ new_name)
		shutil.copy2(os.getcwd() + '/input/'+new_name,dst)
		photo_counter = photo_counter + 1




def dither_photos(album_name):
	featured_photo = input("Quel est le numéro de la photo qui sera la couverture de l'album ? (ex : 01, 11, 24) /!\\ merci de choisir une photo en paysage. ")
	if not os.path.exists("./output/albums/" + album_name + '/'):
		print("La création du dossier a échoué...\n")
		return
	else:
		filename = featured_photo+'.jpg'
		fn= os.path.join("./output/albums/"+album_name+'/photo/',filename)
		of = os.path.join("./output/albums/"+album_name+"/", filename.replace('.jpg','.png'))
		img= Image.open(fn).convert('RGB')
		image_size =DEFAULT_MAX_SIZE
		img.thumbnail(image_size, Image.LANCZOS)
		palette = hitherdither.palette.Palette(DEFAULT_DITHER_PALETTE)            
		threshold = DEFAULT_THRESHOLD   
		img_dithered = hitherdither.ordered.bayer.bayer_dithering(img, palette, threshold, order=8) #see hither dither documentation for different dithering algos
		img_dithered.save(of, optimize=True)



def resize_photos(album_name):
	indirname =  "./output/albums/" + album_name + '/photo/'
	outdirname = "./output/albums/" + album_name + '/photo_vignette/'
	if not os.path.exists(indirname) or not os.path.exists(outdirname):
		print("La création du dossier a échoué...\n")
		return
	else:
		for p in os.listdir(dirname):



def create_html():
	return


def main():
	print("*P*H*O*T*O*P*A*L*O*U*R*D*E*","\n")
	print("Importons un nouvel album !")
	print("************************")
	album_name_display = input("Comment s'appelle ce nouvel album ? \n")
	album_date = input("Quelle est la date de cet album ? (Mois AAAA, commme Mars 2020 par exemple) \n")
	#create the folder name
	album_name = unidecode.unidecode(album_name_display.replace(" ", "_").lower().translate(str.maketrans('', '', string.punctuation)))
	print(album_date)
	print(album_name_display)
	print(album_name)
	create_folders(album_name)
	#rename_photos("input/", album_name)
	dither_photos(album_name)
	#resize_photos()
	#create_html(album_name, album_name_display, album_date)
exc = main()

