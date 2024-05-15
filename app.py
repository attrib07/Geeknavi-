import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from plantuml import PlantUML

# Load environment variables
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Define the prompt for generating content
prompt = """You're an expert YouTube video summarizer, quiz generator, and flowchart creator. Your task is to generate concise and informative summaries for YouTube videos based on their transcripts, create a short quiz to test the viewer's understanding of the content, and generate a flowchart representing the key points from the summary.

Instructions:
1. The transcript will be provided to you with timestamps indicating different sections of the video.
2. Carefully analyze each section of the transcript and identify the key points, main ideas, and important information.
3. Consolidate the key points from all sections into a concise summary, highlighting the most relevant and valuable information.
4. Keep the summary within 250 words, focusing on the essential details without unnecessary fluff.
5. Based on the transcript, create a short quiz with 5 multiple-choice questions to test the viewer's understanding of the video content.
6. Generate a flowchart in PlantUML syntax, representing the key points from the summary in a logical flow.

Your output should be structured as follows:
1. Well-structured and easy-to-understand summary, presented in a bulleted or numbered list format.
2. Quiz with 5 multiple-choice questions and 4 options for each question.
3. Flowchart in PlantUML syntax, representing the key points from the Transcript text and summary.

Example input format:
[00:00:00 - 00:02:15] Transcript text for the first section.
[00:02:16 - 00:04:30] Transcript text for the second section.
...

Example output format:
Summary:
- Point 1: Summary of the first key idea or topic.
- Point 2: Summary of the second key idea or topic.
- ...

Quiz:
1. Question 1?
a. Option 1
b. Option 2
c. Option 3
d. Option 4

2. Question 2?
...

Flowchart:
@startuml
[*] --> Point 1
Point 1 --> Point 2
Point 2 --> Point 3
Point 3 --> [*]
@enduml

Remember, your goal is to provide a succinct and informative summary that captures the essence of the video's content, a quiz to test the viewer's understanding of the material, and a flowchart representing the key points in a logical flow.

Transcript: [Transcript text with timestamps will be provided here]
"""

# Function to extract transcript details from a YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        # Attempt to get the transcript
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        # Check if the transcript is empty (no subtitles available)
        if not transcript_text:
            return "No transcript available for this video."
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        return transcript
    except Exception as e:
        raise e

# Function to generate content based on the transcript and prompt
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Function to render PlantUML flowchart
def render_plantuml(plantuml_code):
    server = PlantUML(url="http://www.plantuml.com/plantuml/img/")
    png_bytes = server.processes(plantuml_code)
    return png_bytes

# Streamlit app
st.title("YouTube Transcript to Detailed Notes, Quiz, and Flowchart Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    if st.button("Get Detailed Notes, Quiz, and Flowchart"):
        transcript_text = extract_transcript_details(youtube_link)
        if transcript_text == "No transcript available for this video.":
            st.warning("No transcript available for this video.")
        else:
            summary_quiz_and_flowchart = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Detailed Notes, Quiz, and Flowchart:")
            st.write(summary_quiz_and_flowchart)

            # Render the flowchart
            plantuml_code = summary_quiz_and_flowchart.split("Flowchart:")[1].strip()
            if plantuml_code:
                try:
                    png_bytes = render_plantuml(plantuml_code)
                    st.image(png_bytes, caption="Flowchart")
                except Exception as e:
                    st.warning(f"Failed to render the flowchart: {e}")
