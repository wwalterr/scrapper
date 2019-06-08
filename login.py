import scrapy

__all__ = ['Login']


class Login(scrapy.Spider):
    name = 'Login'

    user_name = 'luisrsporra@gmail.com'

    user_pass = 'Luis123456'

    url = 'https://auth.mygov.in/user/login'

    start_urls = [url]

    def parse(self, response):
        form_build_id = response.css(
            'input[name=\'form_build_id\']::attr(value)'
        ).extract_first()

        yield scrapy.FormRequest(
            url=Login.url,
            formdata={
                'name': Login.user_name,
                'pass': Login.user_pass,
                'form_build_id': form_build_id,
                'form_id': 'user_login',
                'op': 'Log In With Password'
            },
            callback=self.parse_login,
        )

    def parse_login(self, response):
        self.log(response.xpath('//div[@class=\'field-item even\']/text()').getall())