import csv
from uploads.base import UploadBase

class CSVUploader(UploadBase):
    def read_file(self,filepath):
        with open(filepath, newline="",encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)