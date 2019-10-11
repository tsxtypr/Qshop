# from django.utils.deprecation import MiddlewareMixin
# from django.http import HttpResponse
# import time
#
# class MiddlewareTest(MiddlewareMixin):
#     def process_request(self,request):
#         # print(request.META["REMOTE_ADDR"])
#         # ip=request.META["REMOTE_ADDR"]
#         # if ip=='10.10.107.199':
#         #     return HttpResponse("你个大猪头")
#         pass
#
#     # def process_view(self,request,callback,callback_args,callback_kwargs):
#     #     # print("我是process_view")
#     #     # print(callback)
#     #     pass
#
#     # def process_exception(self,request,exception):
#     #     print("我是process_exception")
#     #     print(exception)
#     #     now_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
#     #     content='[%s]:%s \n'%(now_time,exception)
#     #     with open('error.log','a') as f:
#     #         f.write(content)
