import datetime,hashlib,base64,json,requests

class YunTongXin():
    base_url = 'https://app.cloopen.com:8883'

    def __init__(self,accountSid,accountToken,AppID,templateId):
        self.accountSid = accountSid
        self.accountToken = accountToken
        self.AppID = AppID
        self.templateId = templateId
    def get_request_url(self,sig):
        self.url = self.base_url +'/2013-12-26/Accounts/%s/SMS/TemplateSMS?sig=%s'%(self.accountSid,sig)
        return self.url

    def get_timestamp(self):
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        return now_str
    def get_sig(self,timestamp):
        s = self.accountSid + self.accountToken + timestamp
        md5=hashlib.md5()
        md5.update(s.encode())
        return md5.hexdigest().upper()
    def get_request_header(self,timestamp):
        s= self.accountSid+':'+timestamp
        b_s = base64.b64encode(s.encode()).decode()
        return {
            'Accept':'application/json',
            'Content-Type': 'application/json;charset=utf8;',
            'Authorization': b_s
        }

    def get_request_body(self,phone,code):
        data = {
            'to':phone,
            'appId':self.AppID,
            'templateId':self.templateId,
            'datas':[code,'3']
        }
        return data
    def do_request(self,url,header,body):
        res = requests.post(url,headers=header,
                      data = json.dumps(body))
        return res.text

    def run(self,phone,code):
        timestamp = self.get_timestamp()
        sig = self.get_sig(timestamp)
        url = self.get_request_url(sig)

        header = self.get_request_header(timestamp)
        body = self.get_request_body(phone,code)
        res =self.do_request(url,header,body)
        return  res