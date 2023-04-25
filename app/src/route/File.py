from flask_restx import Namespace, Resource
import pandas as pd
from flask import *
from werkzeug.utils import secure_filename
import os

api = Namespace(
    'files',
    description='Management alarms notification')

@api.route('/test')
class AlarmsList(Resource):
    def get(self):
        '''Get files'''
        return 'getAll()'

#
# Create and save a file csv
# POST - files/
# body : form_data with a file
@api.route('/')
class AlarmUploadFile(Resource):
    @api.doc('locate_device', responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def post(self):
        f = request.files['file']
        data_filename = secure_filename(f.filename)
        f.save(os.path.join(current_app.config['UPLOAD_FOLDER'],
                            data_filename))    
        return 'File uploaded successfully'
   
#
# Get list alarms
# GET  - files/hired_employees.csv
#
@api.route('/<string:filename>')
class AlarmUploadFile(Resource):
    @api.doc('locate_device', responses={
        200: 'Success',
        400: 'Validation Error'
    })
    def get(self, filename):
       # Uploaded File Path
        data_file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        # read csv
        uploaded_df = pd.read_csv(data_file_path, encoding='unicode_escape', header=None, names=['id', 'name', 'date', 'count', 'age'])
        # Converting to html Table
        uploaded_df_html = uploaded_df.to_dict(orient='records')
        # Save into DB
        return {"data": uploaded_df_html}