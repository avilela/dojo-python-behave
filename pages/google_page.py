from page_objects import PageObject, PageElement


class GooglePage(PageObject):
    input_field = PageElement(name='q')
    search_button = PageElement(name='btnK')
    result_list = PageElement(id_='res')
    result_count = PageElement(id_='result-stats')
