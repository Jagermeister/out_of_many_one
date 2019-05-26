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
