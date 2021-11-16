#encoding: utf-8

'''
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
 '''

import requests
import sys, os


def getanime():
	logo = "                   /\                                 \n               _  / |            .-.                  \n              (  /  |  .. ,';.   -' . ,';.,';.  .-.  \n               /.|_.';;  ;;  ;'   ;;  ;;  ;;.;.-'  \n           .:' /    |  ';  ;;_.;:._.';  ;;  ';  `:::' \n          (.'     `-';    .     _;        -'      \n   .-.                               .;                          \n  (_) )-.                           .;'           .'             \n    .:   \   .-.  ;     .-. ,';.  .;  .-.   .-..'  .-.   .;.::. \n   .:'    \ ;   ;';  ;   ; ;;  ;; ::  ;   ;':   ; .;.-'   .;     \n .-:.      );;'  .' .' ';  ;;_;;_.-;;'  :::'.:::'.;'      \n(_/  ----'               ;    .                                \n\t\t\tBy:4D3358 | https://libregit.org/m3x/\n\n"
	print logo

	while True:
		url = raw_input('Informe o link do anime: ')
		if "https://animesonline.cc/" not in url:
			print "[!] Informe um link valido\nEx: https://animesonline.cc/anime/sora-no-otoshimono/"
			print "[!] Apenas anime da pagina https://animesonline.cc"
		else:
			break

	html = requests.get(url)

	list = str(html.text.encode('UTF-8')).split('Temporadas e Episodios')[1]
	temporadas = list.split('<span class="title">Temporada')
	print "-"*10
	nome = str(html.text.encode('UTF-8')).split('Todos os Episodios Online')[0].split('<title>')[1]

	if nome[-1] == ' ':
		nome = nome[:-1]

	if os.path.isdir(nome) == False:
		os.mkdir(nome)

	print "Anime:",nome
	print "Temporadas:",len(temporadas) - 1
	print "-"*10,"\n"




	while True:
		if len(temporadas) - 1 == 1:
			temp = 1
			break

		try:
			temp = int(raw_input('Iniciar download apartir da temporada: '))

			if temp > len(temporadas) - 1 or temp <= 0:
				print "[!] Numero de temporadas invalido"

			else:
				break
		except:
			print "[!] Você deve inserir o numero referente a temporada"

	print '[!] Iniciando Download'
	idtemp = 1

	download(idtemp, temp, temporadas, nome)

def download(idtemp, temp, temporadas, nome):
	for temporada in temporadas:
		if temp > idtemp:
			idtemp += 1
			pass

		if len(temporada.split('<div class="numerando">Ep -')) - 1 != 0:
			print "[INFO] Baixando temporada",idtemp
			episodios = temporada.split('<div class="numerando">Ep -')
			print '[INFO]',len(episodios) - 1,"Episodios"
			idep = 1
			for episodio in episodios:
				try:
					print "[!] Baixando Ep "+str(idep)
					linkep = temporada.split('<div class="numerando">Ep - '+str(idep)+'</div>')[1].split('<a href="')[1].split('"')[0]
	#				print linkep
					ephtml = requests.get(linkep)
					for line in str(ephtml.text.encode('UTF-8')).split('"'):
						if 'https://www.blogger.com/video.g' in line:
							newurl = line
							gettingvideo = requests.get(newurl)
							pastat = "Temporada "+str(idtemp)
							if os.path.isdir(nome+'/'+pastat) == False:
								os.mkdir(nome+'/'+pastat)

							linkvideo = gettingvideo.text.split('"play_url":"')[1].split('"')[0]
							file_name = nome+"/"+pastat+'/Episodio '+str(idep)+".mp4"
							os.system('wget "'+linkvideo+'" -q --show-progress -O "'+str(file_name+'"'))
					idep += 1
				except:
					None

			idtemp += 1

getanime()
