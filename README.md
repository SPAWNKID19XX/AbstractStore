# 🛍️ AbstractStore

**AbstractStore** is a backend platform for an online store built with Python 3.12 and Django REST Framework.

## 🚀 Technology Stack

- **Language:** Python 3.12  
- **Framework:** Django 5.x  
- **REST API:** Django REST Framework  
- **Database:** PostgreSQL  
- **API Documentation:** DRF + Swagger/OpenAPI  
- **Authentication:** JWT / Token / Session (choose as needed)

## 📦 Installation
### Setup Backend

1. Clone the repository:

```aiignore
git clone https://github.com/SPAWNKID19XX/AbstractStore.git
cd abstractstore/server
```

2. Create and activate a Local environment:

```aiignore
python3.12 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies from requirements.txt:

    Navigate to the server folder, where the requirements.txt file containing all necessary dependencies is located.

    To install the dependencies, run the following command:
```aiignore
pip install -r requirements.txt
```
4a. Installing PostgresSQL
   
### Windows

1-Download the PostgresSQL installer from the official website:
https://www.postgresql.org/download/windows/

2-Run the installer and follow the setup steps:

- Choose your installation directory
- Set a password for the postgres user
- Select the default port (5432)
- Complete the installation

3—After installation, open pgAdmin or use the psql command-line tool to connect to your database.


### Linux
    # Update package list
    sudo apt update
    
    # Install PostgreSQL
    sudo apt install postgresql postgresql-contrib
    
    # Start PostgreSQL service
    sudo systemctl start postgresql
    
    # Enable PostgreSQL to start on boot
    sudo systemctl enable postgresql

To switch to the default PostgreSQL user and access the database:

    sudo -i -u postgres
    psql

To exit psql, type \q and press Enter.

## Setup frontend
Before the start you need to make sure to have node.js and npm package.
 Use command 
 
    node -v
    npm -v
    
If node.js doesnt installed, you can get it from oficial site

    https://nodejs.org
    
 A both libraries are included. 
 
 After installations, don't forget to verify by typing 
    
    node -v   # should print something like v18.17.1
    npm -v    # or npm.cmd -v, should print e.g. 10.2.

Before to start local server install frontend dependency witch storage in package.json. Type

    npm install

 While your terminal position into client folder.

 Start frontend server with command 

    npm run dev
    