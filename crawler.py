import requests
import PyV8
import os
from pyquery import PyQuery as pq
import time
import re


def pswEncode(publicKey, publicTs, psw, Ts):
    jsForEncode = open('11.js')
    strForEncode = jsForEncode.read()
    jsForEncode.close()
    jsForPara = """
    	function encodePsw(){
    		var PublicKey = '%s';
			var RSA = new RSAKey();
			RSA.setPublic(PublicKey, "10001");
			var PublicTs='%s';
			var Res = RSA.encrypt('%s' + '\\n' + '%s' + '\\n');
			return hex2b64(Res);
    	}
		encodePsw();
    """ % ( publicKey, publicTs, psw, Ts)
    strForEncode = strForEncode + jsForPara
    JScript = PyV8.JSContext()
    JScript.enter()
    psw = JScript.eval(strForEncode)
    return psw


def makePayload():
    r = requests.get('https://exmail.qq.com/login')
    d = pq(r.text)
    payload = {
        'sid': '',
        'firstlogin': 'false',
        'domain': 'wallstreetcn.com',
        'aliastype': 'other',
        'errtemplate': 'dm_loginpage',
        'first_step': '',
        'buy_amount': '',
        'year': '',
        'company_name': '',
        'is_get_dp_coupon': '',
        'source': '',
        'qy_code': '',
        'starttime': '',  # 13
        'redirecturl': '',
        'f': 'biz',
        'uin': '',
        'p': '',
        'delegate_url': '',
        'ts': '',  # 10
        'from': '',
        'ppp': '',
        'chg': '0',
        'loginentry': '3',
        's': '',
        'dmtype': 'bizmail',
        'fun': '',
        'inputuin': '',
        'verifycode': '',
    }

    payload['starttime'] = time.time() * 1000
    payload['inputuin'] = raw_input('email,please!>>>>>')
    payload['uin'] = payload['inputuin'][0:payload['inputuin'].find('@')]
    payload['ts'] = d("input[name='ts']").val()
    publicKey = re.search(r'PublicKey = "(.*?)";', r.text).group(1)
    psw = raw_input('psw,please! >>>>>>')
    payload['p'] = pswEncode(publicKey, payload['ts'], psw, payload['ts'])

    return payload


def logIn(payload):
    r = requests.post('https://exmail.qq.com/cgi-bin/login', data=payload)
    print r.text

payload = makePayload()
logIn(payload)
a = raw_input('')
