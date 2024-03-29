from dotenv import find_dotenv, load_dotenv


ALLOWED_UPDATES = {'message', 'edited_message', 'callback_query'}
load_dotenv(find_dotenv())