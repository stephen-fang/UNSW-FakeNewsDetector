# 短文本相似度api by Harry

'''
这个是百度的
这个网站介绍！ https://ai.baidu.com/docs#/NLP-Python-SDK/top
'''
from aip import AipNlp

# 免费次数有限，大佬们用自己的申请各种key呀！！！！！！！！！！！！！！！
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# 小小的相似度分析demo
text1 = '我秃顶了'
text2 = '我光头了'
options = {}
options["model"] = "CNN"
res = client.simnet(text1, text2, options) # option默认为"BOW"，可选"BOW"、"CNN"与"GRNN"
print('相似度为:', res["score"])



'''
这个是腾讯的
腾讯nlp接口公测期间（2019年7月1日至2019年11月1日）提供免费服务！用到就是赚到！
这个网站介绍！ https://cloud.tencent.com/document/product/271/35486
'''

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.nlp.v20190408 import nlp_client, models
import json

# 小小的腾讯demo
try: 
    cred = credential.Credential("", "") #填大佬们申请的key
    httpProfile = HttpProfile()
    httpProfile.endpoint = "nlp.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile) #别改地区！！！

    req = models.SentenceSimilarityRequest()
    # 对比文字
    params = '''{
        "SrcText": "你好美丽",
        "TargetText": "你好可爱"
    }'''
    req.from_json_string(params)

    resp = client.SentenceSimilarity(req)
    print('相似度为:', json.loads(resp.to_json_string())['Similarity'])

except TencentCloudSDKException as err: 
    print(err) 

