from pytube import YouTube

url = input("url: ") #colocar a url

video = YouTube(url) 
entry = YouTube(url).title #título do video

opcao = int(input("Digite [1] para vídeo; [2] para aúdio \nResposta: "))
if opcao == 1:
    video_download = video.streams.get_highest_resolution()
    print(f"Baixando vídeo {entry}...")
    video_download.download(filename=f"{entry}.mp4")
elif opcao == 2:
    audio_download = video.streams.get_audio_only()
    print(f"Baixando o aúdio do vídeo {entry}...")
    audio_download.download(filename=f"{entry}.mp3")
print("Programa concluído.")

#Exemplo: https://www.youtube.com/watch?v=TgqAoAUZWfA&list=OLAK5uy_nhRgkGJitsDzUTi_0o-75mSfA1aGSo4k8&index=1
# https://www.youtube.com/watch?v=ZtFPexrxt4g