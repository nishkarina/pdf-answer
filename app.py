from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
from PyPDF2 import PdfReader
import docx
from transformers import pipeline

app = Flask(__name__, template_folder='.')

# Define upload directory and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

# Create the uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the question answering pipeline
qa_pipeline = pipeline("question-answering")

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Endpoint to handle file upload and question submission
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        question = request.form['question']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Process uploaded file and answer question
            if filename.endswith('.pdf'):
                with open(file_path, 'rb') as f:
                    reader = PdfReader(f)
                    text = ''
                    for page in reader.pages:
                        text += page.extract_text()
            elif filename.endswith('.docx'):
                doc = docx.Document(file_path)
                text = '\n'.join([para.text for para in doc.paragraphs])
            else:
                return jsonify({'error': 'Unsupported file format'}), 400

            # Use the question answering pipeline for answering questions
            result = qa_pipeline(question=question, context=text)
            answer = result['answer']
            
            return render_template('upload.html', answer=answer)
        else:
            return jsonify({'error': 'Invalid file extension'}), 400
    else:
        return render_template('upload.html', answer=None)

if __name__ == '__main__':
    app.run(debug=True)
