from pages.checkboxes_page import CheckboxesPage

def test_Checkboxes(browser):
    page = CheckboxesPage(browser)
    page.load()
    page.maximize()

    #find which checkbox is already selected and print
    i = 1
    for _ in page.checkboxes():
        if page.checkbox_selected(i-1):
            print("Checkbox", i, "is selected")
        else:
            print("Checkbox", i, "is not selected")
        i += 1

    # check all checkboxes and validate
    i = 0
    for _ in page.checkboxes():
        if page.checkbox_selected(i) == False:
            page.click_checkbox(i)
        assert page.checkbox_selected(i)
        i += 1

    # uncheck all checkboxes and validate
    i = 0
    for _ in page.checkboxes():
        if page.checkbox_selected(i) == True:
            page.click_checkbox(i)
        assert not page.checkbox_selected(i)
        i += 1