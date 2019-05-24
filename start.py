from spider.msj_spider import MsjSpider
from spider.pipeline import ItemPipeline
from queue import Queue

if __name__ == '__main__':
    q = Queue()
    itemQueue = Queue()
    q.put('https://www.meishij.net/chufang/diy/')

    pipeline = ItemPipeline(itemQueue)
    pipeline.start()

    spider = MsjSpider(q, itemQueue)
    spider.start()

    spider.join()
    pipeline.join()
    print('--Close Spider---')