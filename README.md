# Creepy Crawly

Creepy Crawly is a rather simple financial analytics tool for exchange traded assets. 
It collects various parameters for a given product. The data is kept in a database. 
Based on the collected data a user can define financial events. When such an event occurs, it can trigger tasks that, 
for example, notify a person about a certain market condition.

The database in the background requires MySQL - make sure you have a MySQL database running somewhere

## Installation

1. Make sure Python 3.4 is installed and the executable is included in the path.
1. Run the command `pip install beautifulsoup4` which installs the screen scraper framework.
1. Run the command `pip install requests` which installs the requests framework.
1. Run the command `pip install SQLAlchemy` which installs the ORM.
1. Install the MySQL/Python Connector from: [https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html] - if you
want to use a different connector, check out the list of available ones here: [http://docs.sqlalchemy.org/en/rel_1_0/dialects/mysql.html]

## Database setup

The database can be automatically set up using the ORM SQLAlchemy. The description of the database tables is
in the file 'model.py'. A helper file to set up the database is the file 'database_setup.py'. To actually set
up the database, follow the steps below.

1. Change the file `settings.properties` to reflect your database connection details.
1. Go to the folder `<install_dir>/database`.
1. Run `python dtaabase_setup.py` which drops all tables in the schema and creates all required tables.

## Usage

1. Got to your installation folder and run `python creepycrawly.py`.
1. Next, open your favourite browser and navigate to [http://localhost:5000]() and enjoy.

## Contributing

1. Fork it!
1. Create your feature branch: `git checkout -b my-new-feature`
1. Commit your changes: `git commit -am 'Add some feature'`
1. Push to the branch: `git push origin my-new-feature`
1. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

TODO: Write license