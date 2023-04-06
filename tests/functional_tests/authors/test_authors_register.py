from .base import AuthorsBaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AuthorsRegisterTest(AuthorsBaseTest):

    def get_by_name(self, container, element, name):
        return container.find_element(By.XPATH, f'//{element}[@name="{name}"]')
    
    def fill_form_dummy_data(self, form):

        fields = form.find_elements(By.TAG_NAME, 'input')
        for field in fields: 
            if field.is_displayed() and field.accessible_name != 'E-mail':
                field.send_keys(" "*20)

    def get_form(self):
        return self.browser.find_element(By.XPATH, '/html/body/main/div[2]/form')
        
    def form_field_test_with_callback(self, callback):           

        self.browser.get(self.live_server_url + "/authors/register")
        form = self.get_form()

        self.fill_form_dummy_data(form)
        form.find_element(By.NAME,  'email').send_keys('dummy@dummy.com')
        
        callback(form)
        return form

    def test_empty_first_name_error_message(self):

        def callback(form):
            first_name_field = self.get_by_name(form, "input", 'first_name')
            first_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Write your first name', form.text)
            self.sleep(10)

        self.form_field_test_with_callback(callback)
