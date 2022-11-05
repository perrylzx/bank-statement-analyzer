# Bank statement analyzer

This program helps people track their finances using their bank statement. I created this because I found that keeping track of your finances manually is a hassle and prone to inaccuracies, either by way of forgetting to input your transactions or making mistakes when you input them. You also have to continuously maintain this otherwise you might get off track. By creating a program to analyze your bank statement, you solve all of these issues.

Currently, you're able to group each transaction under a category that you define yourself. An example of a transaction in a bank statement looks like this:


Transaction Date,Reference,Debit Amount,Credit Amount,Transaction Ref1,Transaction Ref2,Transaction Ref3

02 Nov 2022,MST,11.39,,SHOPEE SINGAPORE SI NG 29OCT,4628-4500-5663-9207,,

The program lets you group all future expenses under SHOPEE SINGAPORE under a user defined category. That's what's great about this - you teach the program what future transactions will fall under. So the more you use the program the easier it more accurate it gets.

## Roadmap

- [x] Create gui that displays statement in table
- [ ] Allow uploading of csv
- [ ] Add ability to add categories (food, transport, etc)
- [ ] Add ability to group transactions under categories
- [ ] Some statistics from the data
