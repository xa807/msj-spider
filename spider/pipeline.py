import sqlite3
from threading import Thread


class ItemPipeline(Thread):
    def __init__(self, itemQueue):
        super().__init__()
        self.queue = itemQueue

    def save(self,conn, **values):
        sql = "INSERT INTO t_food(%s) VALUES(%s)"
        fields = ','.join([key for key in values])
        # field_placeholders = ','.join(['%%(%s)s' % key for key in values])
        field_values = ','.join(["'%s'" % value for value in values.values()])
        c = conn.cursor()
        insert_sql = sql % (fields, field_values)
        c.execute(insert_sql)
        conn.commit()
        print('保存OK', values)

    def run(self):
        db_name = '/Users/apple/PycharmProjects/swiper/swiper.db'
        conn = sqlite3.connect(db_name)

        while True:
            try:
                item = self.queue.get(timeout=60)
                self.save(conn, **item)
            except:
                break

        conn.close()
