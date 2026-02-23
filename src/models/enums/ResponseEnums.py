from enum import Enum



class responesSignal(Enum):


    
    FILE_TYPE_NOT_SUPPORTED = 'Error! file type is not supported.'
    FILE_SIZE_EXCEEDED = 'Error! file size is too large.'
    FILE_UPLOAD_SUCCESS = 'File uploaded successfully.'
    FILE_UPLOAD_FAILED = 'File uploaded failed.'