from flask_restx import Api, Resource

from .File import api as File

api = Api(title='Pixki Alert API', version='1.0', description='API for create files')
api.add_namespace(File)