import os

import pydantic as pdtc
import typing as tp

# More Generic Types

    
class Path(pdtc.BaseModel):
    """A class that represents a file."""
    path: str  
    filename: tp.Optional[str] = None  
    dir_path: tp.Optional[str] = None
    

    def __init__(self, path: str, check_exists: bool = False) -> None:
        super().__init__(path=path)
        self.filename = os.path.basename(path)
        self.dir_path = os.path.dirname(path)
        if check_exists:
            self.check_exists()
    
    def exists(self) -> bool:
        return os.path.exists(self.path)
    


    def get_ftype(self) -> str:
        self.check_exists()
        if os.path.isfile(self.path):
            return "file"
        elif os.path.isdir(self.path):
            return "dir"
        else:
            return "other"
    
    def get_abs_path(self) -> str:
        return os.path.abspath(self.path)
    

    
    def is_relative(self) -> bool:
        return not os.path.isabs(self.path)
    
    def is_absolute(self) -> bool:
        return os.path.isabs(self.path)
        

    def check_exists(self) -> None:
        if not self.exists():
            raise FileNotFoundError(f"File {self.path} does not exist.")    
    

