# wechat
微信公众号爬虫
## 需求
Windows环境  
python2 BeautifulSoup selenium  
Fiddler  
微信电脑客户端
## 步骤
首先打开Fiddler，在微信上点开某公众号的历史纪录
在Fiddler上获取该页面的临时url
并利用crawl_wechat_copy.py 爬到该公众号所有文章的链接
接下来再用 test_all.py 爬每个文章的内容
思路来自于 https://github.com/fst034356/crawler/blob/master/python%E7%88%AC%E5%8F%96%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7%E5%8E%86%E5%8F%B2%E6%96%87%E7%AB%A0%E9%93%BE%E6%8E%A5%E6%80%9D%E8%B7%AF.md
