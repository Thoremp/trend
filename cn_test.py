# coding=utf-8

import MySQLdb
from multiprocessing.dummy import Pool
import time
from DBUtils.PooledDB import PooledDB
pool = PooledDB(MySQLdb, 10, host='120.25.103.83',user='root',passwd='Astarmo826@',db='trend',port=3306,charset='utf8') #5为连接


def update_number():
    # 查出basis所有记录
    conn = pool.connection()
    cur = conn.cursor()

    sql = '''
            select id,field from trend_basis where field_number is null
        '''
    count = cur.execute(sql)
    result = cur.fetchmany(count)

    cur.close()
    conn.commit()
    conn.close()

    return result

# update
def update(res):

    id = res[0]
    field = res[1]
    print str(id) + field + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    conn = pool.connection()
    cur = conn.cursor()

    sql = '''
        select field_number,(select field_number from trend_field tf2 where tf2.id=tf.parent_id ) as parent_id
            from trend_field tf where 1=%s and field_name=%s
            '''
    count = cur.execute(sql, (1,field))
    result = cur.fetchmany(count)

    cur.close()
    conn.commit()
    conn.close()

    # 有的职业会找不到编码
    if result:
        res = result[0]
        field_number = res[0]
        parent_number = res[1]

        # 更新 trend_basis 表数据
        conn = pool.connection()
        cur = conn.cursor()

        sql = '''
                update trend_basis set field_number=%s,parent_number=%s where id=%s
            '''
        cur.execute(sql,(field_number,parent_number,id))

        cur.close()
        conn.commit()
        conn.close()


if __name__ == '__main__':
    result = update_number()

    poolThread = Pool()  # 初始化一个实例,4代表四线程,不写参数将使用机器核心数作为参数
    poolThread.map(update, result)
    poolThread.close()
    poolThread.join()  # join()作用:等待爬取完成以后再回到下面一行代码的执行

    print 'success!'