---

# AI Nutritionist Health App

## Introduction

The AI Nutritionist Health App is a Streamlit-based web application that leverages Google Gemini Pro Vision API and LangSmith tracing to provide nutritional analysis of food items from images. Users can upload images of food, and the app will return the total calories and proteins, along with details for each food item.

## Features

- Upload images of food items for nutritional analysis.
- Utilizes Google Gemini Pro Vision API for content generation.
- Integration with LangSmith for tracing and debugging.
- Provides detailed nutritional information including calories and protein content for each food item in the image.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.10
- Conda (Anaconda or Miniconda)

### Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/AI-Nutritionist-Health-App.git
   cd AI-Nutritionist-Health-App
   ```

2. Create a virtual environment using Conda:

   ```sh
   conda create -p venv python==3.10 -y
   ```

3. Activate the virtual environment:

   ```sh
   conda activate ./venv
   ```

4. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

5. Set up your environment variables:

   Create a `.env` file in the root directory of your project and add your Google API Key and LangChain API Key:

   ```sh
   GOOGLE_API_KEY=your_google_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   ```

## Usage

1. Run the Streamlit application:

   ```sh
   streamlit run health.py
   ```

2. In the browser, you will see the AI Nutritionist Health App interface.

3. Upload an image file (`jpg`, `jpeg`, `png`) containing food items.

4. Click the "Tell me the total calories and Proteins" button to get the nutritional analysis.

## Code Overview

### health.py

The main application file contains the following key components:

- **Environment Setup**: Loads API keys from environment variables using `dotenv`.
- **Google Gemini Pro Vision API Configuration**: Configures the Generative AI model with the provided API key.
- **LangSmith Integration**: Utilizes LangSmith's `@traceable` decorator for tracing the function `get_gemini_repsonse`.
- **Streamlit Interface**: Handles file upload and displays the image and nutritional analysis results.

### Example Function: get_gemini_repsonse

```python
@traceable
def get_gemini_repsonse(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])
    return response.text
```

### LangSmith Integration

LangSmith is integrated for tracing and debugging purposes. It helps in tracking the function calls and their execution, making it easier to debug and understand the workflow. For more details on LangSmith, visit [LangSmith Documentation](https://www.langchain.com/langsmith).

## Requirements

Refer to the `requirements.txt` file for the list of required packages:

```
streamlit
google-generativeai
python-dotenv
langchain
PyPDF2
chromadb
pdf2image
faiss-cpu
langchain_google_genai
langsmith
```

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License.

---
