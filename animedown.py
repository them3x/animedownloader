#encoding: utf-8
import requests
import sys, os

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

if os.path.isdir(nome) == False:
	os.mkdir(nome)

print "Anime:",nome
print "Temporadas:",len(temporadas) - 1
print "-"*10,"\n"
#	print("Houve um problema, talvez o link para o anime esteja incorreto")
#	print(erro)
#	exit(0)


while True:
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
'''
for line in str(html.text.encode('UTF-8')).split('"'):
	if "https://www.blogger.com/video.g" in line:
		newurl = line
'''

