from pages.add_remove_elements_page import AddRemoveElementsPage

def test_addRemoveElements(browser):
    page = AddRemoveElementsPage(browser)
    page.load()
    #add one element
    page.click_add_button()
    #assert number of delete buttons equals 1
    assert page.number_of_delete_buttons() == 1
    #press delete button
    page.delete_last_element()
    #add 5 more elements and assert delete buttons respectively
    count = 1
    while count < 6:
        page.click_add_button()
        assert page.number_of_delete_buttons() == count
        count += 1
    #delete one by one
    count = 5
    while count > 0:
        page.delete_last_element()
        count -= 1
        assert page.number_of_delete_buttons() == count