# importações:

from pytube import exceptions
from pytube import YouTube
from pytube import Playlist
import os

num = input('Quantos links?')

caminho = os.getcwd()
file = caminho + r"\coisas baixadas(pytube)"

try:
    for baixar in range(int(num)):
        links = str(input('Coloque o link'))
        tipo = str(input('Tipo (MP3/MP4)')).lower()

        if 'playlist' in links:
            try:
                p = Playlist(f'{links}')

            except exceptions.RegexMatchError:
                print(f'LINK NÃO ACEITO, VOCÊ ESCREVEU: {links}')
                break

            print(f'Baixando playlist "{p.title}":')

            for video in p.videos:
                if tipo == 'mp4':
                    video.streams.filter(res='720p').first().download(output_path=file)
                    print(f'{video.title}.{tipo} baixado')
                if tipo == 'mp3':
                    video.streams.filter(only_audio=True).first().download(output_path=file)
                    print(f'{video.title}.{tipo} baixado')
                elif tipo != 'mp4' and tipo != 'mp3':
                    print(f'ESCREVA MP3 OU MP4, VOCÊ ESCREVEU: {tipo}')

        

        else:
            try:
                yt = YouTube(links)
                
            except exceptions.RegexMatchError:
                print(f'LINK NÃO ACEITO, VOCÊ ESCREVEU: {links}')
                break

            if tipo == 'mp4':
                yt.streams.filter(res='720p').first().download(output_path=file)
                print(f'{yt.title}.{tipo} baixado')
            elif tipo == 'mp3':
                yt.streams.filter(only_audio=True).first().download(output_path=file)
                print(f'{yt.title}.{tipo} baixado')           
            elif tipo != 'mp4' and tipo != 'mp3':
                print(f'ESCREVA MP3 OU MP4, VOCÊ ESCREVEU: {tipo}')

except ValueError:
    print(f'NÚMERO DE LINKS NÃO ACEITO, VOCÊ ESCREVEU: {num}')
    pass

except KeyError:
    print(f'O LINK DIRECIONA A ALGO PRIVADO, COLOQUE-O EM NÃO LISTADO PARA CONSEGUIR BAIXAR!!!')
    pass

print('\n')
print('-PROGRAMA FINALIZADO-\n'*2)