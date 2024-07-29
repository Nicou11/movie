import requests
import os
import pandas as pd
import sys

#dt = sys.argv[1]

def req(load_dt="20120101"):
    url = gen_url(load_dt)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    #print(data)
    return code, data

def gen_url(dt='20120101'):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    # key = "6d73ca55adb7b40c2b042c67db5f37eb"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    return url

def get_key():
    """영화진흥위원회 가입 및 API 키생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def req2list(load_dt='20120101') -> list:
    _, data = req(load_dt)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l

def list2df(load_dt='20120101'):
    l = req2list(load_dt)
    df = pd.DataFrame(l)
    return df

def save2df(load_dt='20120101'):
    """airflow 호출 지점"""
    df = list2df(load_dt)
    df['load_dt'] = '20120101'
    df.to_parquet('~/tmp/test_parquet', partition_cols=['load_dt'])
    print(df.head(5))
    return df
    #df.to_parquet('~/data/parquet/movie/{dt}/{dt}.parquet')
