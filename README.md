# Simple ChatBot 🤖
 
This project is a simple chatbot powered by Google Generative AI, built using Streamlit. The chatbot is designed to generate responses based on user input using the `gemini-1.5-flash` model from Google's Generative AI API.

## Features

- **User Interface**: A clean and simple user interface built with Streamlit.
- **Chat History**: Displays chat history between the user and the bot.
- **Responsive Design**: The UI is responsive and looks good on different screen sizes.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.9 or higher
- Virtual environment tools (optional but recommended)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install the dependencies:**
    ```bash
   pip install -r requirements.txt
4. **Run the application:**
    ```bash
   streamlit run first_chatbot.py
## Usage
* Once the app is running, you'll see a simple chat interface.
* Enter your message in the input box and click "Send".
* The chatbot will respond based on the input provided.

## Project Structure

    your-repo-name/
    │
    ├── first_chatbot.py           # Main application file
    ├── requirements.txt           # List of dependencies
    ├── .env                       # Environment variables file (not included in the repo)
    ├── .streamlit/
    │   └── config.toml            # Streamlit configuration file (optional)
    └── README.md                  # This readme file
