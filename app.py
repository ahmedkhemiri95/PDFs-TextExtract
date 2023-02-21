'''Flask wrapping of the extraction related utilities
'''

import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

from global_common import ports
from global_common import PREFIX
from extraction import extraction
from splitting import splitting

app = Flask(__name__)
port = int(os.environ.get("PORT", ports["data_extraction"]))

path = os.getcwd()

# Project directories defined As follow:

# -data_dir-: data .
data = os.path.join(path, 'data')
if not os.path.isdir(data):
    os.mkdir(data)

# -upload_dir-: contain files uploaded.
uploads = os.path.join(data, 'uploads')
if not os.path.isdir(uploads):
    os.mkdir(uploads)

# -preparation_dir-: contain processed & prepared files.
prepare = os.path.join(data, 'files_preparation')
if not os.path.isdir(prepare):
    os.mkdir(prepare)

# -output_dir-: contain generated text files.
outputs = os.path.join(data, 'outputs')
if not os.path.isdir(outputs):
    os.mkdir(outputs)

# Verify and validate files extensions...
ALLOWED_EXTENSIONS = set(['.pdf'])


def allowed_file(filename):
    '''Assess if the file extension is in the allowed listdir
    '''
    lowercase_extension = os.path.splitext(filename)[1].lower()
    return lowercase_extension in ALLOWED_EXTENSIONS


@app.route(PREFIX + '/upload', methods=['POST'])
def upload():
    '''Upload files to process
    '''
    if request.method != 'POST':
        resp = jsonify({'message': 'Operation not supported'})
        resp.status_code = 500
        return resp

    # check if the post request has the file part
    if 'files[]' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 500
        return resp

    files = request.files.getlist('files[]')

    errors = {}
    success = False

    # check if file allowed or not allowed.
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploads, filename))
            success = True
        else:
            errors[file.filename] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 404
        return resp

    if success:
        resp = jsonify({'message': 'Files successfully uploaded'})
        resp.status_code = 200
        return resp

    resp = jsonify(errors)
    resp.status_code = 404
    return resp


@app.route(PREFIX + '/extraction', methods=['POST'])
def extract_function():
    '''Do extract data from files
    '''
    if request.method == 'POST':  # check request method
        if not os.listdir(uploads):  # if uploads dir is empty return -> error
            resp = jsonify({'message': 'Files not found'})
            resp.status_code = 500
            return resp

        try:

            # splitting : split docs into single pages.
            splitting(uploads, prepare)

            # extraction: extract text from pages.
            extraction(prepare, outputs)

            resp = jsonify({'message': 'Files successfully extracted '})
            resp.status_code = 200
            return resp

        except:

            resp = jsonify({'message': 'error occurs while extraction'})
            resp.status_code = 404
            return resp
    else:

        resp = jsonify({'message': 'Operation not supported'})
        resp.status_code = 500
        return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
