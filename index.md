# Member Sticker Bot

## What is Member Sticker Bot
Member Sticker Bot is a modular Telegram Bot that automatically return Relevant Thankyou / Greetings Sticker pack.
## Platform
Made with [Python 3](www.python.org), Hosted on [HEROKU](www.heroku.com) Backed By [SQLALCHEMY](www.sqlalchemy.org)
## Configuration
  - Not recommend way

     The prefered version is to use a config.py file, as it makes it easier to see all your settings grouped together. This file should be placed in your tg_bot folder, alongside the __main__.py file . This is where your bot token will be loaded from, as well as your database URI (if you're using a database), and most of your other settings.

     It is recommended to import sample_config and extend the Config class, as this will ensure your config contains all defaults set in the sample_config, hence making it easier to upgrade. 
  - Recommend way
     
      Use Deploy Button For Direct Deployment

## Database

In the case of postgres, this is how you would set up a the database on a debian/ubuntu system. Other distributions may vary.

- install postgresql:

`sudo apt-get update && sudo apt-get install postgresql`

- change to the postgres user:

`sudo su - postgres`

- create a new database user (change YOUR_USER appropriately):

`createuser -P -s -e YOUR_USER`

This will be followed by you needing to input your password.

- create a new database table:

`createdb -O YOUR_USER YOUR_DB_NAME`

Change YOUR_USER and YOUR_DB_NAME appropriately.

- finally:

`psql YOUR_DB_NAME -h YOUR_HOST YOUR_USER`

This will allow you to connect to your database via your terminal.
By default, YOUR_HOST should be 0.0.0.0:5432.

You should now be able to build your database URI. This will be:

`sqldbtype://username:pw@hostname:port/db_name`

Replace sqldbtype with whichever db youre using (eg postgres, mysql, sqllite, etc)
repeat for your username, password, hostname (localhost?), port (5432?), and db name.

**NOTE: IF YOU ARE USING ENV , IT WILL BE AUTOMATICALLY FILLED BY THE HEROKU PLUGGING**
