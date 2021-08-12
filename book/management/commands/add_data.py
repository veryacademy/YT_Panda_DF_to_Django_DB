import pandas as pd
from django.core.management.base import BaseCommand
from book.models import Book
from sqlalchemy import create_engine
from django.conf import settings

class Command(BaseCommand):
  help = "A command to add data from an Excel file to the database"

  def handle(self, *args, **options):

    excel_file = 'books.xlsx'
    df = pd.read_excel(excel_file)
    
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']

    # engine = create_engine('sqlite:///db.sqlite3')
    database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format( user=user,password=password,database_name=database_name,)

    engine = create_engine(database_url, echo=False)

    df.to_sql(Book._meta.db_table, if_exists='replace', con=engine, index=False)
