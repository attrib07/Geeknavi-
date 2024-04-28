# Geeknavi : Automatically summarize lectures and create a quiz to test your learning

Geeknavi app that automatically summarizes lecture recordings and create a quiz to test your learning from the lecture. 

> The architecture involves interacting with various services such as Google API, OpenAI, Baseten, and Backblaze B2 to transcribe audio, generate notes, and create quiz questions.

You can check out a demo of the app [here- updating soon]) or Test out with public Link and code : code [here](https://huggingface.co/spaces/Rishabh12j/AI_Powered_Teaching_Assistant).

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
