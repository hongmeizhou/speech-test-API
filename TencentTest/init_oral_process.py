
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。

from tencentcloud.soe.v20180724 import soe_client, models

from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from addPublicParas import addPublicParameter
import json

def InitOral(text):

	try:
		# 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
		cred = credential.Credential("AKIDb7SivKPjOsM9wYuYufbR6kCd8Yj1dA95", "yWmqsjR1qW0UmzARRfjcQ3byHEoDRZXl")

		# 实例化一个http选项，可选的，没有特殊需求可以跳过。
		httpProfile = HttpProfile()
		httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
		httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
		httpProfile.endpoint = "soe.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)

		# 实例化一个client选项，可选的，没有特殊需求可以跳过。
		clientProfile = ClientProfile()
		clientProfile.signMethod = "HmacSHA256"  # 指定签名算法(默认为HmacSHA256)
		clientProfile.httpProfile = httpProfile

		client = soe_client.SoeClient(cred, "", clientProfile)
		req = models.InitOralProcessRequest()
		req.SessionId = "stress_test_956938"
		req.RefText = "Actually, he has over a million subscribers."
		req.WorkMode = 0
		req.EvalMode = 1
		req.ScoreCoeff = 3.5

		headerDict=addPublicParameter("InitOralProcess")
		headerDict["SessionId"]="zhm1213"
		headerDict["RefText"]=text
		headerDict["WorkMode"]=0
		headerDict["EvalMode"]=1
		headerDict["ScoreCoeff"]=3.5
		strJson=json.dumps(headerDict)
		req.from_json_string(strJson)

		resp = client.InitOralProcess(req)

	# 输出json格式的字符串回包
		print("%s" % resp.to_json_string())

	except TencentCloudSDKException as err:
		print("%s" % err)

