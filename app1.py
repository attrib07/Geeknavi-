import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()

# Configure OpenAI API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the prompt for generating content
system_prompt = """You're an expert YouTube video Notes maker and quiz generator to test if users have watched the video. Your task is to generate concise and informative summaries for YouTube videos based on their transcripts, and create a short quiz to test the viewer's understanding of the content.

Instructions:
1. The transcript will be provided to you with timestamps indicating different sections of the video.
2. If not then sectioning it with time frame.
3. Now take transcript again but this time ask it to summarise one section of time frame.
4. Now repeat this process for all the time Timestamps section one by one.
6. Carefully analyze each section of the transcript and identify the key points, main ideas, and important information.
7. Consolidate the key points from all sections into a concise summary, highlighting the most relevant and valuable information.
8. Keep the summary within 250 words, focusing on the essential details without unnecessary fluff.
9. Based on the transcript, create a short quiz with 5 multiple-choice questions to test the viewer's understanding of the video content.

Your output should be structured as follows:
1. Well-structured and easy-to-understand summary, presented in a bulleted or numbered list format for each section.
2. Quiz with 5 multiple-choice questions and 4 options for each question.

Example input format:
[00:00:00 - 00:02:15] Transcript text for the first section.
[00:02:16 - 00:04:30] Transcript text for the second section.
...

Example output format:
Summary generated after analysing all timestamps and key idea or topic : 
- Point 1: Summary of the first key idea or topic.
- Point 2: Summary of the second key idea or topic.
- ...

Quiz:
1. Question 1?
- a. Option 1
- b. Option 2
- c. Option 3
- d. Option 4

2. Question 2?
...

Remember, your goal is to provide a succinct(with example/code/steps) and informative summary that captures the essence of the video's content, and a 5 Important quiz related to videos content to test the viewer's understanding of the material.
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
def generate_content(transcript_text, generate_summary=True, generate_quiz=False):
    # Create a list of messages with the system prompt and the transcript text
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Transcript: {transcript_text}"},
    ]

    if generate_summary and generate_quiz:
        instruction = "Generate both the summary and the quiz."
    elif generate_summary:
        instruction = "Generate only the summary."
    elif generate_quiz:
        instruction = "Generate only the quiz."
    else:
        return "Please specify whether to generate the summary or the quiz."

    messages.append({"role": "user", "content": instruction})

    # Use the OpenAI API to generate the summary and/or quiz
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Return the generated content
    return chat_completion.choices[0].message.content

# Streamlit app
st.title("YouTube Transcript to Detailed Notes and Quiz Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    if st.button("Get Detailed Notes, Quiz, and Flowchart"):
        
        transcript_text = extract_transcript_details(youtube_link)
        
        if transcript_text == "No transcript available for this video.":
            st.warning("No transcript available for this video.")
    else:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Get Summary Notes"):
                summary = generate_content(transcript_text, generate_summary=True, generate_quiz=False)
                st.markdown("## Summary Notes:")
                st.write(summary)
        with col2:
            if st.button("Get Quiz"):
                quiz = generate_content(transcript_text, generate_summary=False, generate_quiz=True)
                st.markdown("## Quiz:")
                st.write(quiz)
