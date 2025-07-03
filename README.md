
# Product Description Generator with Marketing Angle

## Table of Contents
- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Goal](#goal)
- [Features](#features)
- [Inputs & Outputs](#inputs--outputs)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
- [Author](#author)

## Project Overview
This project provides a Streamlit-based web application that leverages Large Language Models (LLMs) via Langchain's `SequentialChain` to generate creative product titles, compelling marketing-optimized product descriptions, and relevant social media captions. It aims to automate and streamline content creation for e-commerce businesses.

## Problem Statement
[cite_start]E-commerce businesses frequently encounter difficulties in crafting engaging and SEO-friendly product descriptions that resonate with their intended audience[cite: 1]. [cite_start]Manually generating these descriptions for a large volume of products is both time-consuming and often leads to inconsistencies in tone[cite: 2].

## Goal
The primary objective of this project is to develop a tool that accepts a basic product name and its key features as input. It then automatically generates a creative product title, followed by a marketing-optimized product description. [cite_start]An additional third chain is included to generate social media captions[cite: 3, 7]. This is achieved using a `SequentialChain` to ensure a coherent flow of content generation.

## Features
The tool utilizes a `SequentialChain` with the following steps:
1.  [cite_start]**Step 1 (Chain 1): Product Title Generation** [cite: 4]
    * Generates a creative and catchy product title based on the input product name and features.
2.  [cite_start]**Step 2 (Chain 2): Product Description Generation** [cite: 5]
    * Uses the previously generated product title to create a compelling, marketing-toned product description.
3.  [cite_start]**Step 3 (Chain 3): Social Media Caption Generation** [cite: 7]
    * Generates social media captions, incorporating an SEO keyword or tone modifier, based on the product title and description.

## Inputs & Outputs
[cite_start]The application takes the following inputs and produces the specified outputs[cite: 6]:

**Inputs:**
* `product_name`: e.g., "Wireless Earbuds"
* `features`: e.g., "Noise cancellation, 12-hour battery life, Bluetooth 5.3"
* `seo_keyword`: A key term to enhance search visibility for social media captions.
* `tone`: A desired tone/style for the social media caption (e.g., "bold," "luxurious," "elegant").
* `platform`: The target social media platform (e.g., "Instagram", "LinkedIn").

**Outputs:**
* `title`: e.g., "SilentBeats: The Next-Gen Wireless Sound"
* `description`: e.g., "Experience crystal-clear sound like never before. With SilentBeats, Immerse yourself in music thanks to advanced noise cancellation, seamless Bluetooth 5.3 connectivity, and a 12-hour battery that powers your day."
* `caption`: A generated social media caption tailored to the inputs.

## Technologies Used
* **Python:** The core programming language.
* **Streamlit:** For creating the interactive web application interface.
* **Langchain:** Framework for developing applications powered by language models, specifically using `LLMChain` and `SequentialChain`.
* **Groq API:** Utilized as the Large Language Model provider (`ChatGroq` with `deepseek-r1-distill-llama-70b` model).
* **python-dotenv:** For securely loading environment variables (like API keys) from a `.env` file.
* **UUID:** For generating unique IDs for interactive elements.
* **HTML:** For custom styling and interactive components within Streamlit.

## Setup and Installation

Follow these steps to get the project up and running on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/TanyaKumari/ProductDescriptionGenerator.git](https://github.com/TanyaKumari/ProductDescriptionGenerator.git)
    cd ProductDescriptionGenerator
    ```
    *(Note: Replace `TanyaKumari` with your actual GitHub username if different)*

2.  **Create a Virtual Environment:**
    It's highly recommended to use a virtual environment to manage dependencies.
    ```bash
    python -m venv genai-env
    ```

3.  **Activate the Virtual Environment:**
    * **On Windows:**
        ```bash
        .\genai-env\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source genai-env/bin/activate
        ```

4.  **Install Dependencies:**
    You'll need to create a `requirements.txt` file first.
    Create a file named `requirements.txt` in your project root with the following content:
    ```
    streamlit
    dotenv
    langchain
    langchain-core
    langchain-groq
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set Up Environment Variables:**
    Create a file named `.env` in the root directory of your project.
    Add your Groq API key to this file:
    ```
    GROQ_API_KEY="your_groq_api_key_here"
    ```
    Replace `"your_groq_api_key_here"` with your actual API key obtained from [Groq](https://console.groq.com/keys).

## Usage

1.  **Run the Streamlit Application:**
    Ensure your virtual environment is active.
    ```bash
    streamlit run index.py
    ```
2.  Your browser should automatically open to the Streamlit application (usually at `http://localhost:8501`).
3.  Enter the required product information in the form fields.
4.  Click the "Generate Content" button to get your product title, description, and social media caption.
5.  Use the copy buttons next to each generated output to easily copy the text.

## Project Structure

ProductDescriptionGenerator/

├── .env                  # Environment variables 

├── .gitignore            # Specifies intentionally untracked files to ignore

├── genai-env/            # Python virtual environment 

├── index.py              # Main Streamlit application and LLM chain logic

├── LICENSE               # Project license file

├── ProblemStatement.txt  # Defines the project's problem, goal, and steps

├── README.md             # This readme file

├── requirements.txt      # Lists Python dependencies

└── solution.ipynb        # Jupyter Notebook for testing chain components


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Tanya Kumari
*©2025 Tanya Kumari*

