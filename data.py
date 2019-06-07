from scrapy import Spider

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


class Data(Spider):
    name = 'Data'

    start_urls = [
        r'https://data.gov.in/search/site?query=maharajganj&field_search=title%5E2&item=100&exact_match=1'
    ]

    @classmethod
    def check_folder(cls, name):
        folder_path = path.join(getcwd(), name)

        if not path.exists(folder_path):
            print(f'Folder {name} created')

            makedirs(folder_path)

        print(f'Folder {name} already exists')

    @classmethod
    def chrome_options(cls):
        options = webdriver.ChromeOptions()

        Data.check_folder('csv')

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
        driver = webdriver.Chrome(
            executable_path=path.join(getcwd(), 'chromedriver'),
            chrome_options=Data.chrome_options()
        )

        driver.maximize_window()

        for link in links:
            driver.get(link)

            # Click on a CSV link banner
            driver.find_element_by_xpath(
                '//html/body/div[1]/div[1]/div/div[7]/div/div[2]/section/div/div/div/div/div/article/div/div/div[2]/div/div[1]/div/div[2]/div/a'
            ).click()

            # Click on usage type label (non-commercial)
            WebDriverWait(driver, 5).until(
                ec.visibility_of_element_located(
                    (By.XPATH, '/html/body/div[1]/div[1]/div/div[7]/div/div[2]/section/div/div/div/div/div/article/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/form/div/div[4]/div/div[2]/label')
                )
            ).click()

            # Click on purpose label (academia)
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div/div[7]/div/div[2]/section/div/div/div/div/div/article/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/form/div/div[5]/div/div[1]'
            ).click()

            # Click on submit
            driver.find_element_by_xpath('//*[@id=\'edit-submit\']').click()
            
            # Wait the download page loads, if your connection it's fast you can decrease
            # the value below to improve the scrapper speed
            sleep(5)

            # Close opened window
            window_before = driver.window_handles[0]

            window_after = driver.window_handles[1]

            driver.switch_to_window(window_after)

            driver.close()

            driver.switch_to_window(window_before)

        driver.quit()

        # Get JSON, XML, JSONP, XLS or ODS
        # sublinks = response.xpath(
        #     '//a[@class=\'json xml jsonp xls ods\']/@href'
        # ).getall()
