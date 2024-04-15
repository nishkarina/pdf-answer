# pdf-answer
You upload a pdf and ask a question it will give you an answer
# Document Understanding with Donut

This project utilizes AI models for document understanding, particularly focusing on the Donut model. It provides functionalities for preprocessing PDFs, PowerPoint slides, and Markdown files, followed by question answering using AllenNLP and OpenAI.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/nishkarina/document-understanding.git
cd document-understanding
pip install -r requirements.txt
python app.py
```

2. **Install dependencies:**
	```bash
    pip install -r requirements.txt```


3. **Run the Flask server:**
    ```bash
    python app.py
    ```

## Usage

1. Upload PDF, DOCX, or other supported document types using the provided web interface.
2. Ask questions related to the Donut document understanding model.
3. Receive answers from the AI assistant based on the uploaded documents.

## Project Structure

- `app.py`: Main Flask application for document upload and question answering.
- `uploads/`: Directory to store uploaded files.

## Acknowledgments

- AllenNLP: Used for question answering.
- OpenAI: Used for conversational question answering.
- Unstructured Client: Used for document preprocessing.
- Chromadb: Used for vector database management.
- Panel: Used for creating the web interface.

