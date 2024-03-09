from models.engine.file_storage import FileStorage
#from file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()

b_model = BaseModel()

__all__ = ['storage', 'b_model']
