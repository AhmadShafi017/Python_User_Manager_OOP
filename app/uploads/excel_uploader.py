import pandas as pd
from uploads.base import UploadBase

class ExcelUploader(UploadBase):
    def read_file(self,filepath):
        df = pd.read_excel(filepath)
        return df.to_dict(orient='records')