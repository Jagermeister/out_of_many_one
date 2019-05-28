""" Interact with web interface to capture local backups of information """

import json

from bs4 import BeautifulSoup
import requests


EFD_ENDPOINT_ACCESS = 'https://efdsearch.senate.gov/search/home/'
EFD_ENDPOINT_SEARCH = 'https://efdsearch.senate.gov/search/'
EFD_ENDPOINT_DATA = 'https://efdsearch.senate.gov/search/report/data/'

HTTP_HEADERS = {
    'User-Agent': ' '.join([
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
        'AppleWebKit/537.36 (KHTML, like Gecko)',
        'Chrome/74.0.3729.169 Safari/537.36']),
    'Origin': 'https://efdsearch.senate.gov',
    'Referer': 'https://efdsearch.senate.gov/search/home/',
    'DNT': '1'
}


class EFD():
    """ Manage state for access to Electronic Financial Disclosures """

    def __init__(self):
        self.session = requests.Session()

    @staticmethod
    def __parse_agreement(html):
        """ Produce web token value from agreement HTML.
        Args:
            html: str - Response text from fetching agreement page.
        Raises:
            ValueError: When web token input is not found.
        Returns:
            web_token: str - Value of hidden web token input.
        """
        soup = BeautifulSoup(html, features='html.parser')
        web_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})
        if hasattr(web_token, 'value'):
            return web_token['value']

        raise ValueError('Expected to find web token within HTML.')

    def __fetch_web_token(self):
        """ Return web token from fetching home page. """
        response = self.session.get(EFD_ENDPOINT_SEARCH)
        web_token = EFD.__parse_agreement(response.text)
        return web_token

    @staticmethod
    def __parse_search_form(html):
        """ Return search form input names. """
        soup = BeautifulSoup(html, features='html.parser')
        form_names = [i['name'] for i in soup.find('form').findAll('input')]
        return form_names

    def __post_agreement(self, web_token):
        """ Authenticate by agreement. Allows accessing search form. """
        payload = {
            'prohibition_agreement': 1,
            'csrfmiddlewaretoken': web_token
        }

        self.session.headers.update(HTTP_HEADERS)
        response = self.session.post(EFD_ENDPOINT_ACCESS, data=payload)
        form_names = self.__parse_search_form(response.text)
        return form_names

    def login(self):
        """ Acquire tokens to authenicate and access the Search functionality. """
        web_token = self.__fetch_web_token()
        form_names = self.__post_agreement(web_token)
        assert len(form_names) == 13, 'Login unsuccessful!'

    def __header_update_token(self):
        """ Add required token from cookie to header """
        cookies = self.session.cookies.get_dict()
        self.session.headers.update({
            'Referer': 'https://efdsearch.senate.gov/search/',
            'X-CSRFToken': cookies['csrftoken'],
        })

    def search(self, last_name):
        """ Search financial disclosures. """
        form_data = {
            'start': 0,
            'length': 100,
            'report_types': '[7]',  # Annual Report
            'filter_types': '[1]',  # Senators
            'last_name': last_name,
            'submitted_start_date': '01/01/2012 00:00:00'
        }

        self.__header_update_token()
        response = self.session.post(EFD_ENDPOINT_DATA, data=form_data)
        # draw, recordsTotal, data, recordsFiltered, result
        return json.loads(response.text)
