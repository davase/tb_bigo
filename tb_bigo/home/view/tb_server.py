from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views import View
from home.models import *
import json
from urllib.parse import quote,unquote
import traceback
import requests


class CallBack(View):

    def get(self, request):
        response1 = ''
        try:
            args = request.GET
            code = args.get('code')
            textcontentjson = {}
            # 获取参数
            textcontentjson['code'] = code
            textcontentjson['response'] = ''
            textcontentjson['responsedict'] = ''
            textcontentjson['message'] = ''
            if code:
                # 正常流程
                client_id = '21805942'
                client_secret = 'a90b12c2a9bc72df603e90e7728abda9'
                url = 'https://oauth.taobao.com/token'
                postfields = {'grant_type': 'authorization_code',
                              'client_id': client_id, 'client_secret': client_secret,
                              'code': code, 'redirect_uri': 'http://tb.zen-x.com.cn/hello_world'}
                post_data = '&'.join(['{}={}'.format(k, quote(v)) for k, v in postfields.items()])
                headers = {
                    'content-type': 'application/x-www-form-urlencoded',
                }
                response = requests.post(url, headers=headers, data=post_data)
                rst = response.json()
                textcontentjson['responsedict'] = json.dumps(rst, ensure_ascii=False)
                # 正常流程
                error_description = rst["error_description"] if "error_description" in rst else None
                if not error_description:
                    # 准备数据入数据库
                    tbid = rst["taobao_user_id"] if "taobao_user_id" in rst else  None
                    tbnick = unquote(rst["taobao_user_nick"]) if "taobao_user_nick" in rst else  None
                    token = rst["access_token"] if "access_token" in rst else  None
                    resinfo = json.dumps(rst, ensure_ascii=False)
                    # 判断数据库中是否存在数据，存在刷新，不存在插入
                    if TbserverUserToken.objects.filter(tbid=tbid, tbnick=tbnick).all():
                        # 存在商家数据，更新token信息
                        TbserverUserToken.objects.filter(tbid=tbid, tbnick=tbnick).update(resinfo=resinfo, token=token)
                        textcontentjson['message'] = '更新了token数据'
                        # pass
                    else:
                        # 不存在商家信息，插入数据库
                        print(111111)
                        user_info = TbserverUserToken.objects.create(tbid=tbid, tbnick=tbnick, resinfo=resinfo,
                                                                     token=token)
                        if user_info.id > 0:
                            textcontentjson['message'] = '插入了token数据'
                            pass
                            # 插入数据成功 记录日志文件
                            # message = "添加数据成功"
                        else:
                            textcontentjson['message'] = '插入数据失败'
                            pass
                            # 插入数据失败 记录日志文件
                            # code = -1
                            # message = "添加数据失败"
            textcontentjson['get_info'] = json.dumps(args, ensure_ascii=False)
            response1 = json.dumps(textcontentjson)
            with open('./jsonlog.txt', 'a+', encoding="utf-8") as f:
                f.write(response1 + '\n')
        except Exception as e:
            return HttpResponse('服务器错误')
        return render(request,'callback.html')
