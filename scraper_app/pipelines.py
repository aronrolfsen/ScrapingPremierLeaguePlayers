from sqlalchemy.orm import sessionmaker
from scraper_app.models import Players, db_connect, create_players_table

class PLdataPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_players_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self,item,spider):
        session = self.Session()
        player = Players(**item)

        try:
            session.add(player)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item
