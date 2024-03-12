from models.base_model import BaseModel

class Review(BaseModel):
    """
    Class to manage AirBnB clone reviews
    """
    place_id = ""
    user_id = ""
    text = ""
