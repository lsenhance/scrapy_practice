# scrapy practice

对scrapy的学习做个记录

parctice_one 网址：看妹子
流程：
    get总网址，获得总网址中的目标地址列表                       start_requests()
    对列表中的每个元素提交一次request，获得各个详情页的response  start_parse()
    从各个详情页response中提取各个页的地址，提交request         parse()
    用上一步得来的response填充item对象                         img_urls()
    提交item，pipeline进行download
知识点：
    主要使用了imagepipeline和item这两个内容
    创建保存数据的item，在parse中提交item，在pipeline中对item进行处理
    imagepipeline重写了file_path,get_media_requests,item_completed方法
    在setting中启用imagepipeline和image_store
存在的问题：
    对链接的追踪解析方面还存在一些问题，逻辑不够清晰