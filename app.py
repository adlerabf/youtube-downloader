import streamlit as st
import yt_dlp

# Função para baixar o vídeo
def download_video(link, folder):
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'merge_output_format': 'mp4',
        'outtmpl': f'{folder}/%(title)s.%(ext)s',  # Salva o vídeo na pasta escolhida
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

# Função para exibir textos com base no idioma escolhido
def get_text(language):
    if language == "en-US":
        return {
            "title": "YouTube Video Downloader",
            "description": "Enter the YouTube video link and the folder where you want to save the file.",
            "video_link": "Video Link",
            "save_folder": "Folder to Save",
            "download_button": "Download Video",
            "downloading": "Downloading video...",
            "success": "Video successfully downloaded to",
            "error": "Error downloading the video:",
            "provide_info": "Please provide both the video link and the folder to save."
        }
    else:  # pt-BR
        return {
            "title": "Downloader de Vídeo do YouTube",
            "description": "Informe o link do vídeo do YouTube e a pasta onde deseja salvar o arquivo.",
            "video_link": "Link do Vídeo",
            "save_folder": "Pasta para Salvar",
            "download_button": "Baixar Vídeo",
            "downloading": "Baixando vídeo...",
            "success": "Vídeo baixado com sucesso para",
            "error": "Erro ao baixar o vídeo:",
            "provide_info": "Por favor, forneça tanto o link do vídeo quanto a pasta para salvar."
        }

# Interface Streamlit
# Escolha do idioma
language = st.selectbox("Select Language", ("pt-BR", "en-US"))

# Obter o texto de acordo com o idioma selecionado
text = get_text(language)

# Título do aplicativo
st.title(text["title"])

# Descrição
st.markdown(text["description"])

# Input de link
url = st.text_input(text["video_link"], "")

# Input de diretório
folder = st.text_input(text["save_folder"], "")

# Botão para iniciar o download
if st.button(text["download_button"]):
    if url and folder:
        try:
            st.write(text["downloading"])
            download_video(url, folder)
            st.success(f'{text["success"]} {folder}')
        except Exception as e:
            st.error(f"{text['error']} {e}")
    else:
        st.error(text["provide_info"])
