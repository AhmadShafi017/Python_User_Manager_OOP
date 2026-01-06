from uploads.csv_uploader import CSVUploader
from uploads.json_uploader import JsonUploader
from uploads.excel_uploader import ExcelUploader

def upload_menu(user_service):
    choice = input(
        "1 - CSV \n" \
        "2 - JSON \n" \
        "3 - Excel \n" \
        "0 - Back \n"
    )

    if choice == "1":
        uploader = CSVUploader(user_service)
        uploader.upload("user_50.csv")

    elif choice == "2":
        uploader = JsonUploader(user_service)
        uploader.upload("user_50.json")

    elif choice == "3":
        uploader = ExcelUploader(user_service)
        uploader.upload("user_50.json")