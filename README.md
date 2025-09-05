# vendorUI
Create a basic Vendor UI

## Database Setup

Run the following SQL command in SQLite to create the `vendor` table:

```sql
CREATE TABLE vendor (
    id INTEGER PRIMARY KEY,
    vendor TEXT NOT NULL,
    vendortype TEXT,
    amount REAL NOT NULL,
    duedate TEXT,
    transactiondate TEXT,
    transactiondescription TEXT,
    status TEXT
);

