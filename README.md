# Geeknavi : Automatically summarize lectures and quiz to test your learning.

Geeknavi app that automatically summarizes lecture recordings and create a quiz to test your learning from the lecture. 

> The architecture involves interacting with various services such as Google  Gemini API, OpenAI/Groq API, Baseten, and Backblaze B2 to transcribe audio, generate notes, and create quiz questions.

![Geeknavi-architecture](https://github.com/attrib07/Geeknavi-/assets/44226488/23d1f2e2-96a8-45c1-8f84-18be9c0ee4e1)

You can check out a demo of the app [here- updating soon]) or Test out with public Link and code : [here](https://huggingface.co/spaces/Rishabh12j/AI_Powered_Teaching_Assistant).

The application was tested with **Python 3.10.11**

## Prerequisites
You must have:
1. [Python](https://www.python.org/) installed
2. [pip](https://pip.pypa.io/en/stable/installation/) installed
3. An [Google_API_Key](https://ai.google.dev/)
4. An [OPEN_API_KEY](https://console.groq.com/)
5. An [baseten_API-Optional](https://www.baseten.co/)
6. An [Backblaze_B2_API_KEY-Optional](https://www.backblaze.com/)

## Setup

1. Clone this repository and cd into it
    ```bash
    git clone https://github.com/users/geeknavi-lecture-summarizer.git
    cd geeknavi-lecture-summarizer
    ```

2. Create and activate a virtual environment (optional)

    MacOS/Linux:
    ```bash
    python -m venv venv  # you may need to use `python3` instead
    source ./venv/bin/activate
    ```

    Windows:
    ```bash
    python -m venv venv  # you may need to use `python3` instead
    .\venv\Scripts\activate.bat
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```
    
4. Set your All your API Key (optional)

    In the ".env" file, add all your API's key, which you can copy by visiting the official pages. Here is a Format :
    ```bash
    GOOGLE_API_KEY = ''
    OPENAI_API_KEY = ''
    bucket_name = ''
    API_key_baseten = ''
    model_id_whisper = ""
    application_key_id_blackblaze = ''
    application_key_blackblaze = ''
    ```

## Run the application

1. Start the app
```bash
gradio run app.py
```

2. Open the app
Click the link output in the terminal by the last command - the default is http://localhost:8501/

## Use the application

0. To test **geeknavi**, open this [link](https://huggingface.co/spaces/Rishabh12j/AI_Powered_Teaching_Assistant) 

1. Select the lecture file or youtube link.

    You can use either an audio or video file, and the file can be locally stored, remotely stored (and publicly accessibly), or on YouTube.

    ![Geeknavi-Interface](https://github.com/attrib07/Geeknavi-/assets/44226488/3b212637-690b-482c-9ef6-f227ebc979fa)


3. View the results

    Click **Sent** and wait for the results.

    Processing time will depend on the length of the file - hour long lectures may take several minutes to process.

Future Plans : Comming Soon

- Allow you to ask questions about the course material to get specific answers tailored to the lecture content. 
- Allow you to create Diagrams of course/module (flowchat and sequences)
- New UI for Geeknavi 
    - Optional : Upload chat.txt 
    - Optional : Add referance for a compehensive note
    - Optional : Upload Ppt
- Share on x

## Team - Gen4

Name |Discord Name with Email]
-- | --
Rishabh Jain | [b0rn2clutch](rishabh12j@gmail.com)
Sai Amith Chillamcherla | [amith98](amith.ch@outlook.com)
Aman Hanspal | [hanspaa2017108](amanhanspal05@gmail.com)
Vicky Kumar | [resetvicky01](vickykumar07vikram@gmail.om)
