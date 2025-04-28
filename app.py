import streamlit as st
import yt_dlp
import os

# Function to download the video
def download_video(link, folder):
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'merge_output_format': 'mp4',
        'outtmpl': f'{folder}/%(title)s.%(ext)s',  # Saves the video in the chosen folder
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        filename = ydl.prepare_filename(info)
        if filename.endswith('.webm'):
            filename = filename.replace('.webm', '.mp4')  # Adjust filename if necessary
        return filename

# Function to display texts based on the selected language
def get_text(language):
    if language == "en-US":
        return {
            "title": "YouTube Video Downloader",
            "description": "Enter the YouTube video link and the folder where you want to save the file.",
            "video_link": "Video Link",
            "save_folder": "Folder to Save (optional when online)",
            "download_button": "Download Video",
            "downloading": "Downloading video...",
            "success": "Video successfully downloaded!",
            "error": "Error downloading the video:",
            "provide_info": "Please provide the video link."
        }
    else:  # pt-BR
        return {
            "title": "Downloader de Vídeo do YouTube",
            "description": "Informe o link do vídeo do YouTube e a pasta onde deseja salvar o arquivo.",
            "video_link": "Link do Vídeo",
            "save_folder": "Pasta para Salvar (opcional se estiver online)",
            "download_button": "Baixar Vídeo",
            "downloading": "Baixando vídeo...",
            "success": "Vídeo baixado com sucesso!",
            "error": "Erro ao baixar o vídeo:",
            "provide_info": "Por favor, forneça o link do vídeo."
        }

# Streamlit Interface
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
    if url:
        try:
            st.write(text["downloading"])

            # Define local folder or fallback
            save_folder = folder if folder else "."

            # Download video
            downloaded_file_path = download_video(url, save_folder)

            # Show success message
            st.success(f"{text['success']}")

            # Offer download if file exists
            if os.path.exists(downloaded_file_path):
                with open(downloaded_file_path, "rb") as f:
                    st.download_button(
                        label="Clique aqui para baixar o vídeo",
                        data=f,
                        file_name=os.path.basename(downloaded_file_path),
                        mime="video/mp4"
                    )

        except Exception as e:
            st.error(f"{text['error']} {e}")
    else:
        st.error(text["provide_info"])

