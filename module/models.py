from sqlalchemy import Column, Integer, String, Text, BigInteger, DateTime, Float
from module.database import Base, db_session
import datetime

# 세부 항목은 contents 에서 늘어남
class Volatilities_D(Base):
    __tablename__ = 'volatilities_d'
    # login_hash = Column(String(128), primary_key=True)
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(20)) # hist vol , ewma vol 이나 contents에서 category정도로 구분될것들
    yyyymmdd = Column(String(8)) # 20190830
    timestamp = Column(String(30))
    contents = Column(Text)


    def __repr__(self):
        return '<Volatilities_D %r>' % (self.email)

    def __init__(self, category, yyyymmdd, contents, timestamp):
        self.category = category
        self.yyyymmdd = yyyymmdd
        self.contents = contents
        self.timestamp = timestamp


# class Report(Base):
#     __tablename__ = 'reports'
#     key = Column(String(128), primary_key=True)
#     position_token = Column(String(128))
#     results = Column(Text)
#     timestamp = Column(String(30))
#
#     def __repr__(self):
#         return '<Report %r>' % (self.email)
#
#     def __init__(self, key, position_token, results, timestamp):
#         self.key = key
#         self.position_token = position_token
#         self.results = results
#         self.timestamp = timestamp
#
#
# class TradePrice(Base):
#     __tablename__ = 'tradeprices'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     yyyymm = Column(String(6))
#     tradeprice = Column(Float)
#     build_year = Column(Integer)
#     trade_year = Column(Integer)
#     rn = Column(String(60))
#     buldMnnm = Column(Integer)
#     buldSlno = Column(Integer)
#     rnMgtSn1 = Column(Integer)
#     rnMgtSn2 = Column(Integer)
#     apt_name = Column(String(60))
#     trade_month = Column(Integer)
#     trade_days = Column(String(6))  # 1~10 , 11~20 , 21~31 ?
#     private_area = Column(Float)
#     region_code = Column(String(6))
#     floor = Column(Integer)
#     timestamp = Column(String(30))
#
#     def __repr__(self):
#         return '<TradePrice %r>' % (self.id)
#
#     def __init__(self,
#                  yyyymm,
#                  trade_price,
#                  build_year,
#                  trade_year,
#                  rn,
#                  buldMnnm,
#                  buldSlno,
#                  rnMgtSn1,
#                  rnMgtSn2,
#                  apt_name,
#                  trade_month,
#                  trade_days,
#                  private_area,
#                  region_code,
#                  floor,
#                  timestamp):
#         self.yyyymm = yyyymm
#         self.trade_price = trade_price
#         self.build_year = build_year
#         self.trade_year = trade_year
#         self.rn = rn
#         self.buldMnnm = buldMnnm
#         self.buldSlno = buldSlno
#         self.rnMgtSn1 = rnMgtSn1
#         self.rnMgtSn2 = rnMgtSn2
#         self.apt_name = apt_name
#         self.trade_month = trade_month
#         self.trade_days = trade_days
#         self.private_area = private_area
#         self.region_code = region_code
#         self.floor = floor
#
#         self.timestamp = timestamp
#
# def db_data_initialize():
#     pass

