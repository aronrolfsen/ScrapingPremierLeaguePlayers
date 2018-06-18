BOT_NAME = 'PLScraper'

SPIDER_MODULES = ['scraper_app.spiders']

USER_AGENT = 'PL (https://www.premierleague.com/players/)'

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'admin',
    'database': 'PLdata'
}

ITEM_PIPELINES = {
    'scraper_app.pipelines.PLdataPipeline': 100
}

