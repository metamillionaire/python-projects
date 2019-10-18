from pandas import DataFrame

Invoices = {'Date':[20191610,20180103,20111111],'Invoice #':[127,128,129], 'Customer ID':['Webrestaurantstore.com','Poached','GoodFoodJobs.com'], 'Due Date':[201900511,20180202,20111112],'Amount Due':[5000.00,3000.00,1000.00],'Total Paid':[3200.00,1375.00,250.00]}

df = DataFrame(Invoices, columns=['Date','Invoice #','Customer ID','Due Date','Amount Due','Total Paid'])

print(df)

#To export this file to EXCEL, use the follow line of code:

# export_excel = df.to_excel (r'file path location + file name for your EXCEL workbook', index = None, header=True)

#Don't forget to add '.xlsx' at the end of the path

# Then add print(df) like above:

# df = creates the dataframe
# export_excel = next you export it to excel
#print(df)


