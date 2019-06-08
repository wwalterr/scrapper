from scrapy import Spider, Request

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By

from os import getcwd, path, makedirs

from time import sleep

__all__ = ['Data']

# It is also possible to download the files through the id
# of the document, present in the body tag, and the URL:
#
# https://data.gov.in/node/id/download
#
# Try to don't resize the window in a way that Selenium
# can't scroll, e.g extreme small in the vertical axis
#
# If the IP its blocked, there are 3 main ways to fix this
# issue:
#
# 1. Configure the network to change its external IP
#
# 2. Configure the Requests package, before make any request https://stackoverflow.com/questions/23013220/max-retries-exceeded-with-url-in-requests
#
# 3. Change the IP dynamically using the Scrapy and a Proxy https://stackoverflow.com/questions/28852057/change-ip-address-dynamically


class Data(Spider):
    name = 'Data'

    start_urls = [
        r'https://data.gov.in/search/site?query=maharajganj&field_search=title%5E2&item=10&exact_match=1'
    ]

    base = 'https://data.gov.in'

    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=path.join(getcwd(), 'chromedriver'),
            chrome_options=Data.chrome_options()
        )

    @classmethod
    def check_folder(cls, name):
        folder_path = path.join(getcwd(), name)

        if not path.exists(folder_path):
            makedirs(folder_path)

            print(f'Folder {name} created')

            return

        print(f'Folder {name} already exists')

    @classmethod
    def chrome_options(cls):
        Data.check_folder('csv')

        options = webdriver.ChromeOptions()

        preferences = {
            # Define the folder to save file (s)
            'download.default_directory': path.join(getcwd(), 'csv'),
            # Disable image (s) download
            'profile.managed_default_content_settings.images': 2,
            # Enable disk cache
            'profile.managed_default_content_settings.images': 2,
            # Set disk cache size
            'disk-cache-size': 4096
        }

        options.add_experimental_option('prefs', preferences)

        return options

    def parse(self, response):
        links = response.xpath('//div[@class=\'row\']//h3//a/@href').getall()

        # Get CSV files
        for link in links:
            self.driver.get(link)

            sleep(1)

            # Click on CSV banner
            self.driver.find_element_by_xpath(
                '//html/body/div[1]/div[1]/div/div[7]/div/div[2]/section/div/div/div/div/div/article/div/div/div[2]/div/div[1]/div/div[2]/div/a'
            ).click()

            # Click on usage type (non-commercial)
            WebDriverWait(self.driver, 5).until(
                ec.visibility_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div[7]/div/div[2]/section/div/div/div/div/div/article/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/form/div/div[4]/div/div[2]/label')
                )
            ).click()

            # Click on purpose (academia)
            self.driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[7]/div/div[2]/section/div/div/div/div/div/article/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/form/div/div[5]/div/div[1]'
            ).click()

            # Click on submit
            self.driver.find_element_by_xpath(
                '//*[@id=\'edit-submit\']'
            ).click()

            # Wait the download page to load. Decrease the value if your internet its fast
            sleep(3)

            # Close opened window
            if len(self.driver.window_handles) > 1:
                window_before = self.driver.window_handles[0]

                window_after = self.driver.window_handles[1]

                self.driver.switch_to_window(window_after)

                self.driver.close()

                self.driver.switch_to_window(window_before)

        # Go to next page
        next_page = response.xpath(
            '/html/body/div[1]/div[1]/div/div[7]/div[1]/div/section/div/div/div/div/div/div/div[3]/div/ul/li/a[@class=\'pager-item-next\']/@href'
        ).getall()[-1]

        if next_page:
            next_page_url = Data.base + next_page

            yield Request(next_page_url, dont_filter=True)
        
        # Quit the driver
        driver.quit()