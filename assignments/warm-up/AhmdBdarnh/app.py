from mangum import Mangum
from main import app

lambda_handler = Mangum(app)
