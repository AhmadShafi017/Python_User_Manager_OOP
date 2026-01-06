from app.services.search_service import SearchService
from app.ui.search_menu import SearchMenu
from app.services.update_service import UpdateService
from app.ui.update_menu import UpdateMenu

elif current_page == SEARCH:
    search_service = SearchService(db)
    menu = SearchMenu(search_service)
    menu.show(stack)

elif current_page == UPDATE:
    sevice = UpdateService(db)
    menu = UpdateMenu(sevice)
    menu.show(stack)