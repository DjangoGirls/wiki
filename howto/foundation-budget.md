# How to update Foundation's budget

1. Find budget spreadsheet in our Drive folder -> Foundation folder.

## CAFBank

2. Login to CAFBank
3. Click on "View activity"
4. Click on "Search and export activity"
5. Select date range since latest update to now
6. Export activity to CSV
7. Run [`cafbank.py` script](../scripts/cafbank.py) like this: `python cafbank.py path_to_exported_csv.csv`
8. Upload newly generated CSV to Budget spreadsheet, ad as new sheet
9. Copy data from new sheet and paste it to "Items" sheet in Budget ad the end. 
10. Sort Items sheet by day, Z-A. 
11. Manually update "Item" and "Category" columns.
12. Balance of CAFBank (in Balance sheet) should check out with the Balance on the actual account.

## PayPal

13. Go to [Download history](https://history.paypal.com/cgi-bin/webscr?cmd=_history-download)
14. Select date range since latest update to now
15. File Types for Download: Comma Delimited - All activity
16. Hit "Download history"
17. Run [`paypal..py` script](../scripts/paypal.py) like this: `python paypal.py path_to_exported_csv.csv`
18. Upload newly generated CSV to Budget spreadsheet, ad as new sheet
19. Copy data from new sheet and paste it to "Items" sheet in Budget ad the end. 
20. Sort Items sheet by day, Z-A. 
21. Manually update "Item" and "Category" columns.
22. Balance of PayPal (in Balance sheet) should check out with the Balance on the actual account.

