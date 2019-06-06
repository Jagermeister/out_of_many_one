""" SQL used to apply hotfixes to data after capturing """

michael_b_enzi__annual_report_2017 = '''
update report_annual_raw set part_four_b_transactions = '<section class="card mb-2">
<div class="card-body">
<h3 class="h4">Part 4b. Transactions

                        </h3>
<p>
                                Did you, your spouse, or dependent child buy, sell, or exchange an asset that exceeded $1,000?
                                <strong>

                                                Yes

                                </strong>
</p>
</div>
<div class="table-responsive">
<table class="table table-striped">
<caption class="sr-only">List of transactions added to this report</caption>
<thead>
<tr class="header">
<th scope="col"></th>
<th scope="col">#</th>
<th scope="col">Owner</th>
<th scope="col">Ticker</th>
<th scope="col">Asset Name</th>
<th scope="col">Transaction Type</th>
<th scope="col">Transaction Date</th>
<th scope="col">Amount</th>
<th scope="col">Comment</th>
</tr>
</thead>
<tbody>
<tr class="nowrap">
<td>
</td>
<td>
                                                                1</td>
<td>Joint</td>
<td>
<a href="https://finance.yahoo.com/q?s=JALGX" target="_blank">JALGX</a>
</td>
<td>

                                    JHancock Multimanager Lifestyle Gr A

                            </td>
<td>Purchase</td>
<td>02/21/2017</td>
<td>$100,001 - $250,000</td>
<td>
                                                                --</td>
</tr>
<tr class="nowrap">
<td>
</td>
<td>
                                                                2</td>
<td>Joint</td>
<td>
<a href="https://finance.yahoo.com/q?s=JALBX" target="_blank">JALBX</a>
</td>
<td>

                                    JHancock Multimanager Lifestyle Bal A

                            </td>
<td>Sale (Full)</td>
<td>02/21/2017</td>
<td>$100,001 - $250,000</td>
<td>
                                                                --</td>
</tr>
<tr class="nowrap">
<td>
</td>
<td>
                                                                3</td>
<td>Self</td>
<td>
<a href="https://finance.yahoo.com/q?s=JALGX" target="_blank">JALGX</a>
</td>
<td>

                                    JHancock Multimanager Lifestyle Gr A

                            </td>
<td>Purchase</td>
<td>02/21/2017</td>
<td>$100,001 - $250,000</td>
<td>
                                                                --</td>
</tr>
<tr class="nowrap">
<td>
</td>
<td>
                                                                4</td>
<td>Self</td>
<td>
<a href="https://finance.yahoo.com/q?s=JALBX" target="_blank">JALBX</a>
</td>
<td>

                                    JHancock Multimanager Lifestyle Bal A

                            </td>
<td>Sale (Full)</td>
<td>02/21/2017</td>
<td>$100,001 - $250,000</td>
<td>
                                                                --</td>
</tr>
<tr class="nowrap">
<td>
</td>
<td>
                                                                5</td>
<td>Spouse</td>
<td>
<a href="https://finance.yahoo.com/q?s=JALGX" target="_blank">JALGX</a>
</td>
<td>

                                    JHancock Multimanager Lifestyle Gr A

                            </td>
<td>Purchase</td>
<td>02/21/2017</td>
<td>$1,001 - $15,000</td>
<td>
                                                                --</td>
</tr>
<tr class="nowrap">
<td>
</td>
<td>
                                                                6</td>
<td>Spouse</td>
<td>
<a href="https://finance.yahoo.com/q?s=JALBX" target="_blank">JALBX</a>
</td>
<td>

                                    JHancock Multimanager Lifestyle Bal A

                            </td>
<td>Sale (Full)</td>
<td>02/21/2017</td>
<td>$1,001 - $15,000</td>
<td>
                                                                --</td>
</tr>
</tbody>
</table>
</div>
</section>' where report_annual_raw_key = 287;'''