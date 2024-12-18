# PDF_Q&A-System: Unlock Insights from Your PDFs

This application allows you to extract key information from PDF documents and ask questions about their content using a natural, conversational interface powered by OpenAI and other AI libraries.

## Table of Contents

1.  [Features](#features)
2.  [Requirements](#requirements)
3.  [Installation](#installation)
4.  [Setup](#setup)
5.  [Usage](#usage)
6.  [Disclaimer](#disclaimer)
7.  [Further Enhancements](#further-enhancements)
8. [Contributing](#contributing)
9. [License](#license)

---

## Features

-   **AI-powered Information Extraction:** Uses advanced NLP techniques to extract text, tables, and other relevant data from PDF documents.
-   **Conversational Interface:** Enables users to ask questions about PDF content in a natural, conversational manner, maintaining context across multiple questions.
-   **Streamlit User Interface:** Provides a smooth and intuitive user experience for uploading PDF files and interacting with the application.

---

## Requirements

-   Python 3.8 or higher
-   Streamlit (`pip install streamlit`)
-   OpenAI API Key (see [Setup](#setup))
-   Langchain Libraries (This includes `langchain`, `tiktoken`, and other related packages used to integrate different models)
-   PyPDF2 (`pip install pypdf2`)
-   Other libraries are listed in `requirements.txt`.

---

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Kshitij10000/PDF-Question-Answering-System.git
    ```
2.  **Create a Virtual Environment:** (Highly recommended to isolate dependencies)
    ```bash
    python -m venv venv
    ```
3.  **Activate the Virtual Environment:**
    *   Linux/macOS: `source venv/bin/activate`
    *   Windows: `venv\Scripts\activate.bat`
4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Setup

1.  **Obtain Your OpenAI API Key:**
    *   Visit the OpenAI website (https://openai.com/api/) and create an account or log in. Then, create a new API key.
2.  **Create a `.env` File:**
    *   In the root directory of the project, create a file named `.env`. This file is used to store your API key securely. Add the following line, replacing `YOUR_OPENAI_API_KEY` with your actual key:
        ```
        OPENAI_API_KEY=YOUR_OPENAI_API_KEY
        ```
        *Note: Ensure the `.env` is added to your `.gitignore` file if not already included*

---

## Usage

1.  **Run the Application:**
    ```bash
    streamlit run main.py
    ```
2.  **Access the Streamlit Interface:** The application will open in your default web browser.
3.  **Upload Your PDF:** Use the file upload option to upload your PDF document.
4.  **Ask Questions:** Enter your questions in the provided input box. The system will use the AI to interpret your questions and provide answers based on the content of the PDF.

---

## Disclaimer

This project provides a basic implementation of a PDF Q&A system. It serves as a starting point for users wishing to explore the capabilities of LLMs and PDF processing. For a more comprehensive and production-ready solution, consider further development and enhancements.

---

## Further Enhancements

This is a list of potential improvements and directions to explore:

-   **Advanced NLP Techniques:** Investigate more advanced NLP techniques, such as named entity recognition, sentiment analysis, and topic modeling, for enhanced information extraction.
-   **Pre-trained Models:** Explore the integration of pre-trained language models for improved performance and accuracy.
-   **Expanded Question Answering:** Implement more sophisticated question-answering capabilities, such as handling multi-part questions and complex queries.
-   **Data Visualization:** Integrate data visualization techniques to display extracted information in a clear and insightful way.
-   **Summarization:** Add the functionality to generate summaries of PDF content.
-   **Database Storage:** Implement database storage of processed data for easy retrieval and further analysis.

---

## Contributing
We welcome contributions to the project. To contribute, please follow these steps:
1.  Fork the repository.
2.  Create a new branch.
3.  Make your changes
4.  Submit a Pull Request.

---

## License

This project is licensed under the MIT License.
