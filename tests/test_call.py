from mov.api.call import gen_url, req, get_key, req2dataframe

def test_비밀키숨기기():
    key = get_key()
    assert key
    

#def test_유알엘테스트():
    #url = gen_url()
    #assert "http" in url
    #assert "kobis" in url

def test_req():
    code, data = req()
    assert code == 200


def test_req2():
    l = req2dataframe()
    v = l[2]
    assert len(l) > 0
    assert 'rnum' in v.keys()
    assert v['rankInten'] == '-1'
