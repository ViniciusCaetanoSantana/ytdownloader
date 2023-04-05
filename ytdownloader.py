# importações:

from pytube import exceptions
from pytube import YouTube
from pytube import Playlist
import os

num = input('Quantos links?')
caminho = os.getcwd()
arquivo = caminho + r"\coisas baixadas(pytube)"

links_download = []
tipo_download=[]
try:
    for baixar in range(int(num)):

        links = str(input('Coloque o link'))
        links_download.append(links)

        tipo = str(input('Tipo (MP3/MP4)')).lower()
        tipo_download.append(tipo)

    for i, videoss in enumerate(links_download):
            
        if 'playlist' in videoss:
            try:
                p = Playlist(videoss)
                    
            except exceptions.RegexMatchError:
                print(f'LINK NÃO ACEITO, VOCÊ ESCREVEU: {videoss}')
                break

            print(f'Baixando playlist "{p.title}":')
            for video in p.videos:

                if tipo_download[i] == 'mp4':
                    video.streams.filter(res='720p').first().download(output_path=arquivo)
                    print(f'{video.title}.{tipo_download[i]} na lista de download')


                if tipo_download[i] == 'mp3':
                    video.streams.filter(only_audio=True).first().download(output_path=arquivo)
                    print(f'{video.title}.{tipo_download[i]} na lista de download')


        
                elif tipo_download[i] != 'mp4' and tipo_download[i] != 'mp3':
                    print(f'ESCREVA MP3 OU MP4, VOCÊ ESCREVEU: {tipo_download[i]}')

            

        else:
            try:
                yt = YouTube(videoss)

            except exceptions.RegexMatchError:
                print(f'LINK NÃO ACEITO, VOCÊ ESCREVEU: {videoss}')
                break

            if tipo_download[i] == 'mp4':
                videos = yt.streams.filter(res='720p')
                print(f'{yt.title}.{tipo_download[i]} na lista de download')
                videos.first().download(output_path=arquivo)

            elif tipo_download[i] == 'mp3':
                videos = yt.streams.filter(only_audio=True)
                print(f'{yt.title}.{tipo_download[i]} na lista de download')
                videos.first().download(output_path=arquivo)   

            elif tipo_download[i] != 'mp4' and tipo_download[i] != 'mp3':
                print(f'ESCREVA MP3 OU MP4, VOCÊ ESCREVEU: {tipo_download[i]}')


except ValueError:
    print(f'NÚMERO DE LINKS NÃO ACEITO, VOCÊ ESCREVEU: {num}')
    pass

except KeyError:
    print(f'O LINK DIRECIONA A ALGO PRIVADO, COLOQUE-O EM NÃO LISTADO PARA CONSEGUIR BAIXAR!!!')
    pass


print('\nDOWNLOAD FEITO!!')
print('\n')
print('-PROGRAMA FINALIZADO-\n'*2)