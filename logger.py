# import logging
#
# # 输出日志  输出在test文件，而不是控制台
# # 实例对象
# logging_hander=logging.FileHandler("test.log",encoding="utf-8")
# stream_hander=logging.StreamHandler()
# log_format="%(asctime)s[%(levelname)s]%(message)s" #日志格式
# time_format="%Y-%m-%d %H:%M:%S"  #时间格式
#
#
#
# # 设置日志等级的配置
# logging.basicConfig(level=logging.DEBUG,format=log_format,datefmt=time_format,handlers=[logging_hander,stream_hander])
# # 调试  最详细的日志等级，用于项目的调试过程
# logging.debug("这是debug等级")
# # 详细程度仅次于debug  记录通常是关键的节点信息
# logging.info("这是info等级")
# # 警告   某些不被期望的错误发生，但是不影响程序运行
# logging.warning("这是warning等级")
# # 严重错误  部分功能不能运行
# logging.error("这是error等级")
# # 严重错误  程序中断
# logging.critical("这是critical等级")