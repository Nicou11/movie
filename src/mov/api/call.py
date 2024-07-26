def req(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"

    key = "6d73ca55adb7b40c2b042c67db5f37eb"

    url = f"{base_url}?key={key}&targetDt={dt}"
    print(url)

