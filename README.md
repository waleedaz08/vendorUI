# vendorUI
Create a basic Vendor UI

## Installation

### 1. Install SQLite3
SQLite3 comes pre-installed on most Linux and macOS systems.  
On Windows, you may need to install it manually:

- **Windows**
  1. Download the precompiled binaries from the official SQLite website: https://www.sqlite.org/download.html
  2. Extract the files (e.g., `sqlite3.exe`) into a folder, such as `C:\sqlite`.
  3. Add that folder to your system PATH so you can run `sqlite3` from the Command Prompt.

- **Linux (Debian/Ubuntu)**
  ```bash
  sudo apt update
  sudo apt install sqlite3

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

