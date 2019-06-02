""" Interact with web interface to capture local backups of information """

import logging
import json
import time

from bs4 import BeautifulSoup
import requests


EFD_ENDPOINT_ACCESS = 'https://efdsearch.senate.gov/search/home/'
EFD_ENDPOINT_SEARCH = 'https://efdsearch.senate.gov/search/'
EFD_ENDPOINT_DATA = 'https://efdsearch.senate.gov/search/report/data/'
EFD_ENDPOINT_REPORT = 'https://efdsearch.senate.gov/search/view/{}/{}/'

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
        self.is_ready = False
        self.session = requests.Session()
        self.document_type_to_directory = {
            "annual": "annual",
            "periodic transaction report": "ptr",
            "due date extension": "extension-notice/regular"
        }

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
        self.is_ready = True

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

    def annual_reports_search(self):
        """ Search financial disclosures. """
        self.__header_update_token()
        document_links = []

        page_start = 0
        page_end = 100
        is_paging_complete = False
        records_total_count = None
        while not is_paging_complete:
            form_data = {
                'start': page_start,
                'length': page_end,
                'report_types': '[7]',  # Annual Report
                'filter_types': '[1]',  # Senators
                'submitted_start_date': '01/01/2012 00:00:00'
            }
            logging.info(f'Posting for "{page_start}" to "{page_end}" out of "{records_total_count}".')
            response = self.session.post(EFD_ENDPOINT_DATA, data=form_data)
            response = json.loads(response.text)
            document_links.extend(response['data'])
            records_total_count = response['recordsTotal']
            page_start += 100
            page_end += 100
            is_paging_complete = page_start > records_total_count
            if not is_paging_complete: time.sleep(1.25)

        return document_links

    def annual_report_view(self, document_id):
        """ View Electronic Financial Disclosure """
        self.__header_update_token()
        link = EFD_ENDPOINT_REPORT.format('annual', document_id)
        response = self.session.get(link)
        soup = BeautifulSoup(response.text, features='html.parser')
        return soup.find('h1').parent, soup.findAll('section', {'class': 'card mb-2'})
