from models.base_model import BaseModel

class User(BaseModel):
    """
    Class to manage AirBnB clone users
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
