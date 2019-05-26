# Capturing Electronic Filings
Disclosures may be submitted electronically or by paper, resulting in dramatically different displays. Due to the systematic formatting of electronic filings, we will look to build a local data cache for our personal use.

<table>
    <tr>
        <td>Electronic</td>
        <td>Paper Submission resulting in Image</td>
    </tr>
    <tr>
        <td><img src="./Booker_Electronic.PNG"></td>
        <td><img src="./Booker_Paper.PNG"></td>
    </tr>
</table>

We will use a combination of [Requests](https://github.com/kennethreitz/requests) for downloading and [BeautifulSoup4]() for parsing documents. First we should explore the website and understand the network activity taking place.

## Manual Network Review
https://efdsearch.senate.gov/search/

<table style="max-width: 800px">
    <tr>
        <td><img src="./Process_01_Access.PNG"/></td>
        <td><img src="./Process_01_Search.PNG"/></td>
    </tr>
</table>

We can use Chrome's DevTools (Ctrl+Shirt+i) to review requests that occur when the `Search Reports` button is pressed. We are looking for POST requests that may contain the search results. Often times the data is returned embedded within the HTML (we will see this later with the eletronic filing details), but in this case we see there is a separate response.

<table style="max-width: 800px">
    <tr>
        <td width="45%">1. Reviewing Network Responses</td>
        <td>3. Copy Request</td>
    </tr>
    <tr>
        <td><img src="./Process_01_Network.PNG"/></td>
        <td rowspan="3"><img src="./Process_01_Request.PNG"/></td>
    </tr>
    <tr><td>2. Preview Reponse Data</td></tr>
    <tr><td><img src="./Process_01_Data.PNG"/></td></tr>
    <tr><td colspan="2">4. Replay Request and Response</td></tr>
    <tr><td colspan="2" style="text-align: center;"><img src="./Process_01_CURL.PNG"/></td></tr>
</table>

## Python Request and Session
Let's try to duplicate our manual efforts above now that we know what we are looking for. Starting all the way back at agreeing to the prohibitions on obtaining and use of financial disclosure reports. When we use the Network tab with DevTools we can see what form data is sent along when a user checks the agreement box and is allowed to search.

![Access Post](./Process_01_Access_Post.PNG)


We need to grab the form input elements to append to our post.
```html
    <form action="" method="POST" id="agreement_form">
        <div class="checkbox">
            <label>
                <input type="checkbox" id="agree_statement" value="1" name="prohibition_agreement" />
                I understand the prohibitions on obtaining and use of financial disclosure reports.
            </label>
        </div>
        <input type="hidden" name="csrfmiddlewaretoken" value="{TOKEN_WEB_FORM}">
    </form>
```

### Fetch the Access page, and parse the web tokens.
```python
from bs4 import BeautifulSoup
import requests

EFD_ENDPOINT_SEARCH = 'https://efdsearch.senate.gov/search/'

session = requests.Session()
response = session.get(EFD_ENDPOINT_SEARCH)

soup = BeautifulSoup(response.text, features='html.parser')
csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})

print(csrf_token)
```

```html
<input name="csrfmiddlewaretoken" type="hidden" value="{TOKEN_WEB_FORM}"/>
```

### Post the web token and agreement form
```python
headers = {
    'User-Agent': '{USER_AGENT_STRING}',
    'Origin': 'https://efdsearch.senate.gov',
    'Referer': 'https://efdsearch.senate.gov/search/home/'
}

payload = {
    'prohibition_agreement': 1,
    'csrfmiddlewaretoken': csrf_token['value']
}

session.headers.update(headers)
response = session.post(EFD_ENDPOINT_ACCESS, data=payload)
soup = BeautifulSoup(response.text, features='html.parser')

form_names = [i['name'] for i in soup.find('form').findAll('input')]
print(form_names)
```
```python
[
    'first_name', 'last_name',
    'filer_type', 'filer_type', 'filer_type',
    'report_type', 'report_type', 'report_type', 'report_type', 'report_type',
    'submitted_start_date', 'submitted_end_date',
    'csrfmiddlewaretoken'
]
```

We have made it to the search page with all the form elements. 

![Search Form](./Process_01_Search.PNG)
