from .exts import api
from App.views.test_view import *

api.add_resource(test, '/api/test')

