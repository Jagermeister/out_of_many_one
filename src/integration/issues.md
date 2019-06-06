# Data Integration Issues
Eventually we will provide for applying data fixes to raw data so that:
- We can capture the data fresh again without losing knowledge
- Apply our updates to allow for successful data integration

## Cases

### Michael B Enzi - Annual Report for Calendar 2017 ([link](https://efdsearch.senate.gov/search/view/annual/05d0d25b-5ec2-49f5-acc4-a7aadf5bacd0/))
**Part 4b. Transactions**

Record 4 incorrectly records the date as `02/21/217` instead of `02/21/2017`.
```html
<td> 4</td>
<td>Self</td>
<td><a href="https://finance.yahoo.com/q?s=JALBX" target="_blank">JALBX</a></td>
<td> JHancock Multimanager Lifestyle Bal A </td>
<td>Sale (Full)</td>
<td>02/21/217</td>
<td>$100,001 - $250,000</td>
<td> --</td>
```
