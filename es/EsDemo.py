from elasticsearch import Elasticsearch

esUrl = 'http://localhost:9200'

es = Elasticsearch(esUrl)

index = 'users'

# 创建索引
print(es.indices.exists(index))
if (es.indices.exists(index) == False):
    mapping = {
        'dynamic':'',#自动创建索引
        'properties': {
            'title': {
                'type': 'text',
                'analyzer': 'ik_max_word',
                'search_analyzer': 'ik_max_word'
            },
            'url': {
                'type': 'string'
            },
            'date': {
                'type': 'date'
            }
        }
    }
    result = es.indices.create(index)
    es.indices.analyze(index, body=mapping)
datas = [
    {
        'title': '美国留给伊拉克的是个烂摊子吗',
        'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
        'date': '2011-12-16',
    }, {
        'title': '公安部：各地校车将享最高路权',
        'url': 'http://www.chinanews.com/gn/2011/12-16/3536077.shtml',
        'date': '2011-12-16',
    }, {
        'title': '中韩渔警冲突调查：韩警平均每天扣1艘中国渔船',
        'url': 'https://news.qq.com/a/20111216/001044.htm',
        'date': '2011-12-17',
    }, {
        'title': '中国驻洛杉矶领事馆遭亚裔男子枪击嫌犯已自首',
        'url': 'http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml',
        'date': '2011-12-18',
    }
]
for k, row in enumerate(datas):
    print("K",k,"row",row)
    es.index(index, body=row, doc_type='user', id=(k + 1))

search = {
    'query': {
        'match': {
            'title': '各地校车 将享'
        }
    },
    'highlight': {
        'fields': {
            'title': {}
        }
    }
}


result = es.search(index="users", body={"query":{"match_all":{}}})
print(result)