def check_element_exists(element):
    try:
        if element.is_displayed():
            return True
    except:
        return False
