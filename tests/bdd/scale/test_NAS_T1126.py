# coding=utf-8
"""SCALE UI: feature tests."""

import time
from function import (
    wait_on_element,
    is_element_present,
    attribute_value_exist,
)

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/NAS-T1126.feature', 'Create a new dataset with the LDAP user and group permissions')
def test_create_a_new_dataset_with_the_ldap_user_and_group_permissions():
    """Create a new dataset with the LDAP user and group permissions."""


@given('the browser is open, the FreeNAS URL and logged in')
def the_browser_is_open_the_freenas_url_and_logged_in():
    """the browser is open, the FreeNAS URL and logged in."""
    if nas_ip not in driver.current_url:
        driver.get(f"http://{nas_ip}")
        assert wait_on_element(driver, 10, '//input[@data-placeholder="Username"]')
    if not is_element_present(driver, '//mat-list-item[@ix-auto="option__Dashboard"]'):
        assert wait_on_element(driver, 10, '//input[@data-placeholder="Username"]')
        driver.find_element_by_xpath('//input[@data-placeholder="Username"]').clear()
        driver.find_element_by_xpath('//input[@data-placeholder="Username"]').send_keys('root')
        driver.find_element_by_xpath('//input[@data-placeholder="Password"]').clear()
        driver.find_element_by_xpath('//input[@data-placeholder="Password"]').send_keys(root_password)
        assert wait_on_element(driver, 5, '//button[@name="signin_button"]')
        driver.find_element_by_xpath('//button[@name="signin_button"]').click()
    else:
        driver.find_element_by_xpath('//mat-list-item[@ix-auto="option__Dashboard"]').click()


@when('you should be on the dashboard, click on Storage.')
def you_should_be_on_the_dashboard_click_on_storage():
    """you should be on the dashboard, click on Storage.."""
    assert wait_on_element(driver, 10, '//span[contains(.,"Dashboard")]')
    assert wait_on_element(driver, 10, '//mat-list-item[@ix-auto="option__Dashboard"]', 'clickable')
    driver.find_element_by_xpath('//mat-list-item[@ix-auto="option__Dashboard"]').click()
    time.sleep(1)
    assert wait_on_element(driver, 10, '//h1[contains(.,"Dashboard")]')
    assert wait_on_element(driver, 10, '//mat-list-item[@ix-auto="option__Storage"]', 'clickable')
    driver.find_element_by_xpath('//mat-list-item[@ix-auto="option__Storage"]').click()

@then('the storage page should open, then click on the tank three dots button, select Add Dataset')
def the_storage_page_should_open_then_click_on_the_tank_three_dots_button_select_add_dataset():
    """the storage page should open, then click on the tank three dots button, select Add Dataset."""
    raise NotImplementedError
    time.sleep(1)
    assert wait_on_element(driver, 10, '//h1[contains(.,"Storage")]')
    assert wait_on_element(driver, 5, '//tr[contains(.,"tank")]//mat-icon[text()="more_vert"]', 'clickable')
    driver.find_element_by_xpath('//tr[contains(.,"tank")]//mat-icon[text()="more_vert"]').click()
    assert wait_on_element(driver, 4, '//button[normalize-space(text())="Add Dataset"]', 'clickable')
    driver.find_element_by_xpath('//button[normalize-space(text())="Add Dataset"]').click()   



@then(parsers.parse('the Dataset window should open, input dataset name "{dataset_name}" and click save'))
def the_dataset_window_should_open_input_dataset_name_my_ldap_dataset_and_click_save():
    """the Dataset window should open, input dataset name "{dataset_name}" and click save."""
    time.sleep(1)
    assert wait_on_element(driver, 5, '//h3[text()="Add Dataset"]')
    assert wait_on_element(driver, 5, '//input[@ix-auto="input__Name"]', 'inputable')
    driver.find_element_by_xpath('//input[@ix-auto="input__Name"]').clear()
    driver.find_element_by_xpath('//input[@ix-auto="input__Name"]').send_keys(dataset_name)
    assert wait_on_element(driver, 5, '//button[@ix-auto="button__SAVE"]', 'clickable')
    driver.find_element_by_xpath('//button[@ix-auto="button__SAVE"]').click()
    assert wait_on_element_disappear(driver, 20, '//h6[contains(.,"Please wait")]')



@then(parsers.parse('the my_ldap_dataset should be created, click on the "{dataset_name}" three dots button, select Edit Permissions'))
def the_my_ldap_dataset_should_be_created_click_on_the_my_ldap_dataset_three_dots_button_select_edit_permissions():
    """the my_ldap_dataset should be created, click on the "{dataset_name}" three dots button, select Edit Permissions."""
    time.sleep(4)
    assert wait_on_element(driver, 10, f'//div[contains(text(),"{dataset_name}")]')
    time.sleep(1)
    assert wait_on_element(driver, 5, f'//tr[contains(.,"{dataset_name}")]//mat-icon[text()="more_vert"]')
    driver.find_element_by_xpath(f'//tr[contains(.,"{dataset_name}")]//mat-icon[text()="more_vert"]').click()
    assert wait_on_element(driver, 5, '//button[normalize-space(text())="Edit Permissions"]')
    driver.find_element_by_xpath('//button[normalize-space(text())="Edit Permissions"]').click()


@then('the Edit Permissions page should open, select eturgeon for User, click on the Apply User checkbox, then select eturgeon for Group name, click on the Apply Group checkbox, and click the Save button')
def the_edit_permissions_page_should_open_select_eturgeon_for_user_click_on_the_apply_user_checkbox_then_select_eturgeon_for_group_name_click_on_the_apply_group_checkbox_and_click_the_save_button():
    """the Edit Permissions page should open, select eturgeon for User, click on the Apply User checkbox, then select eturgeon for Group name, click on the Apply Group checkbox, and click the Save button."""
    raise NotImplementedError


@then(parsers.parse('on the storage page, click on the "{dataset_name}" three dots button, select Edit Permissions and verify that user and group name is "{user}"'))
def on_the_storage_page_click_on_the_my_ldap_dataset_three_dots_button_select_edit_permissions_and_verify_that_user_and_group_name_is_eturgeon():
    """on the storage page, click on the "{dataset_name}" three dots button, select Edit Permissions and verify that user and group name is "{user}"."""

    assert wait_on_element(driver, 5, '//button[@ix-auto="button__SAVE"]', 'clickable')
    driver.find_element_by_xpath('//button[@ix-auto="button__SAVE"]').click()
    time.sleep(8)
    assert wait_on_element(driver, 10, '//div[contains(text(),"{dataset_name}")]')
    assert wait_on_element(driver, 5, '//input[@data-placeholder="Group"]')
    assert attribute_value_exist(driver, '//input[@data-placeholder="Group"]', 'value', user)


    ## return to dashboard
    assert wait_on_element(driver, 10, '//mat-list-item[@ix-auto="option__Dashboard"]', 'clickable')
    driver.find_element_by_xpath('//mat-list-item[@ix-auto="option__Dashboard"]').click()
    time.sleep(1)

