from selenium.common.exceptions import NoSuchElementException

link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

def test_book_shop(browser):
    browser.get(link)
    try:
        browser.find_element_by_class_name('btn-add-to-basketы').tag_name
        result = True
    except NoSuchElementException:
        result = False
    assert result == True, "Element not found"
    
 
