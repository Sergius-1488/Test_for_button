link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

def test_book_shop(browser):
    browser.get(link)
    but=browser.find_element_by_class_name('btn-add-to-basket').tag_name
    assert str(but) == "button"
