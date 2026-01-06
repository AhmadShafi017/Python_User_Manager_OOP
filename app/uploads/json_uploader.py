import json
from uploads.base import UploadBase

class JsonUploader(UploadBase):
    def JSONUploader(UploadBase):
        def read_file(self,filepath):
            with open(filepath,encoding="utf-8") as f:
                return json.load(f)