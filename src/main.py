#  main
from logging import Logger
import utils.config as config
import utils.api_utils as api 
# from processing import 
# from translation import 
# from evaluation import

try:
    api.test_all_auth()
    print("APIs Authenthicated.")
except Exception as e:
    Logger.error("One or more APIs failed: ", e)