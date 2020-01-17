# vol 을 계산해서 넣음

import time, datetime, json
from  module.models import Volatilities_D
from  module.database import db_session

# start_job_time = '09:00'
# update_frequency = '1D'

def main_job():
    print("volatilities working...")

    data = {'test' : 10}

    category = 'test_category'
    yyyymmdd = '20190830'
    contents = json.dumps(data)

    timestamp = str(datetime.datetime.utcnow())

    p = Volatilities_D.query.filter(Volatilities_D.category == category and Volatilities_D.yyyymmdd == yyyymmdd).first()

    if p is None:
        p = Volatilities_D(category, yyyymmdd, contents, timestamp)
        db_session.add(p)
        print("volatilities added...")
    else:
        p.category = category
        p.yyyymmdd = yyyymmdd
        p.contents = contents
        p.timestamp = timestamp
        print("volatilities updated...")

    db_session.commit()

def main_job2():
    print("volatilities working...")

    # get data from upbit
    data = dict()

    # calculate vol
    result_data = dict()
    result_data['BTC'] = {
                            'price': 0.0,
                            'vol': 0.0
                          }

    result_data['ETH'] = [0.0]

    # save or update
    ref_date_time = time.time()

if __name__ == '__main__':
    main_job()
