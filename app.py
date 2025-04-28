import streamlit as st
import yt_dlp

# Function to download the video
def download_video(link, folder):
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'merge_output_format': 'mp4',
        'outtmpl': f'{folder}/%(title)s.%(ext)s',  # Saves the video in the chosen folder
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

# Function to display texts based on the selected language
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

# Streamlit Interface
# Language selection
language = st.selectbox("Select Language", ("pt-BR", "en-US"))

# Get text based on selected language
text = get_text(language)

# App title
st.title(text["title"])

# Description
st.markdown(text["description"])

# Video link input
url = st.text_input(text["video_link"], "")

# Folder input
folder = st.text_input(text["save_folder"], "")

# Button to start downloading
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
