import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from sqlalchemy import select
from config import Parameters

ALL = 'all'
WEEK = 'week'
MONTH = 'month'

class Base(DeclarativeBase):
    pass

class Data(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    value: Mapped[int] = mapped_column(Integer())
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    
    @staticmethod
    def add(name, value):
        this_row = Data(name=name, value=value)
        print(this_row)
        with Session(engine) as session:
            session.add(this_row)
            session.commit()
            
    @staticmethod
    def last(name):
        stmt = select(Data).where(Data.name == name).order_by(Data.created_date.desc())
        with Session(engine) as session:   
            return session.scalars(stmt).first()
        
    @staticmethod
    def history(name=ALL, range=ALL):
        stmt = select(Data)
        # filter for selected name if name is passed
        if name != ALL:
            stmt = stmt.where(Data.name == name)
            
        current_time = datetime.datetime.utcnow()
        
        # filter for selected range if range is passed 
        if(range == WEEK):
            stmt = stmt.where(Data.created_date > current_time - datetime.timedelta(weeks=1))  
        if(range == MONTH):
            stmt = stmt.where(Data.created_date > current_time - datetime.timedelta(days=30))
            
        with Session(engine) as session:   
            return [data for data in session.scalars(stmt)]
        
    @staticmethod
    def all():
        return Data.history()
            
    
    def formatted_date(self) -> str:
        if(self.created_date == None):
            return ""
        return self.created_date.strftime('%A, %d %B %Y %Hh:%M')
    
    def __repr__(self) -> str:
        return f"Parameter(name={self.value!r}, value={self.name!r}, date={self.formatted_date()!r})"
    
    
def initialize_engine(filename):
    return create_engine(f"sqlite+pysqlite:///{filename}", echo=True)


def initialize_tables(engine):
    Base.metadata.create_all(engine)


file_name = "test.db"

engine = initialize_engine(file_name)
initialize_tables(engine)

if __name__ == "__main__":
    Data.add(Parameters.NOX, 9)
    for data in Data.history(name="NOx", range=WEEK):
        print(data)
    print(Data.last(name="CO2"))