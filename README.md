# python3使用scrapy爬取豆瓣电影评论
1. 填写`myspider/spiders/douban_spider.py`中login_param的用户名和密码（不登录只能爬200条）
2. 修改`myspider/spiders/douban_spider.py`中crawl_url为待爬取的目标电影链接
3. 如果需要保存至数据库，修改`myspider/settings.py`中SAVE_TO_DB为True，并填写相关数据库配置
4. 运行`main.py`