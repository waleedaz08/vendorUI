import pandas as pd
import sqlite3


#create dataframe
df = pd.read_csv(r'vendor_data.csv')

#covert frame to dictionary
array_of_data = df.to_dict('records')

#test read from dictionary
"""i = 0
for r in array_of_data:
    print(r)
    i += 1
    if i == 5:
        break
"""
#create connection to sqllite
conn = sqlite3.connect(r"C:\Users\DELL\Documents\practice.db")

#rename columns
df = df.rename(columns={
    "Vendor": "vendor",
    "Vendor Type": "vendortype",
    "Amount": "amount",
    "Due Date": "duedate",
    "Transaction Date": "transactiondate",
    "Transaction Description": "transactiondescription"
})
#directly insert data from df
df.to_sql(
    name="vendor",
    con=conn,
    if_exists="append",
    index = False
)

#close connection
conn.close()

