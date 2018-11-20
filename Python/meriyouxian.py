# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:30:55 2017

@author: admin
"""
import os,time
from hdfs.client import Client

class SelectQuery:

    def __init__(self):
        pass

    def SqlAnalyse(self, sql):
        pass


    def LineHandle(self,cloud_type, line, int_index_list, float_index_list):
        line = line if cloud_type != 'presto' else line.replace('\n','')[1:-1].replace('","','\t')
        line, cc = line.replace('\n','').decode('utf-8').split('\t'), []
        for i in range(len(line)):
            if i in int_index_list:
                try:
                    value_num = int(line[i])
                except:
                    value_num = 0
                cc.append(value_num)
            elif i in float_index_list:
                try:
                    value_num = float(line[i])
                except:
                    value_num = 0
                cc.append(value_num)
            else:
                cc.append(line[i])
        return tuple(cc)


    def SelectQuery(self,cloud_type, command, int_index_list, float_index_list):
        #用于查询出来的结果较多时，返回一个生成器
        f = os.popen(command)
        return (self.LineHandle(cloud_type,x,int_index_list,float_index_list) for x in f)

    def Select(self, cloud_type, sql, int_index_list=[], float_index_list=[]):
        """
        cloud_type:
        hive 提交集群执行hive查询
        spark-sql 单机执行sparksql查询
        presto 分布式sql查询引擎
        """
        if cloud_type == 'hive':
            command = (u'hive -e "%s"'%sql.replace('\n',' ')).encode('utf-8')
        elif cloud_type == 'spark-sql':
            command = (u'spark-sql -e "%s" --conf spark.port.maxRetries=128'%sql.replace('\n',' ')).encode('utf-8')
        elif cloud_type == 'presto':
            command = (u'/usr/local/service/presto-client/presto --server 10.3.4.67:9000 --user hadoop --catalog hive --execute "%s"'%sql.replace('\n',' ')).encode('utf-8')
        else:
            pass
        return self.SelectQuery(cloud_type, command, int_index_list, float_index_list)


    def SparkSQLSubmit(self, result_type, sql, cc, app_name, int_index_list=[], float_index_list=[]):
        """
        result_type:
        save_as_path 结果以文件形式保存到集群，然后再get下来，这里给出hdfs上的路径 result_file_path给的是一个路径
        save_as_print 结果展示在控制台
        cc:
        当result_type=save_as_path时 给的是结果文件的存储路径，当=save_as_print时，给的是展示多少条
        """
        command0 = u'/usr/local/service/spark/bin//spark-submit --deploy-mode client --master yarn --executor-cores 5 --num-executors 2 --executor-memory 6144M --driver-memory=2048M --jars /data/user/litao/MyClass/original-RunSparkSql4Bi2HDFS-{jar_id}.0-SNAPSHOT.jar --class cn.missfresh.RunSql4Bi /data/user/litao/MyClass/original-RunSparkSql4Bi2HDFS-{jar_id}.0-SNAPSHOT.jar "{sql}" {hdfs_path} {appname}'
        cc0 = '/user/bi_user/SparkSql/'+cc if result_type == 'save_as_path' else cc
        jar_id = 2 if result_type == 'save_as_path' else 1
        command = command0.format(jar_id=jar_id, sql=sql.replace('\n',' '), hdfs_path=cc0, appname=app_name).encode('utf-8')
        print(command)
        if result_type == 'save_as_print':
            return self.SelectQuery(result_type,command, int_index_list, float_index_list)
        else:
            os.system('hdfs dfs -rm -r /user/bi_user/SparkSql/' + cc)
            os.system(command)
            result = self.SelectQuery(result_type,'hdfs dfs -cat /user/bi_user/SparkSql/{hdfs_path}/part*'.format(hdfs_path=cc), int_index_list, float_index_list)
            return result

    def SparkSQLSubmit2(self, result_type, sql, cc, app_name, int_index_list=[], float_index_list=[]):
        """
        result_type:
        save_as_path 结果以文件形式保存到集群，然后再get下来，这里给出hdfs上的路径 result_file_path给的是一个路径
        save_as_print 结果展示在控制台
        cc:
        当result_type=save_as_path时 给的是结果文件的存储路径，当=save_as_print时，给的是展示多少条
        """
        command0 = u'/usr/local/service/spark/bin//spark-submit --deploy-mode client --master yarn --executor-cores 5 --num-executors 10 --executor-memory 6144M --driver-memory=3048M --jars /data/user/litao/MyClass/original-RunSparkSql4Bi2HDFS-{jar_id}.0-SNAPSHOT.jar --class cn.missfresh.RunSql4Bi /data/user/litao/MyClass/original-RunSparkSql4Bi2HDFS-{jar_id}.0-SNAPSHOT.jar "{sql}" {hdfs_path} {appname}'
        cc0 = '/user/bi_user/SparkSql/'+cc if result_type == 'save_as_path' else cc
        jar_id = 2 if result_type == 'save_as_path' else 1
        command = command0.format(jar_id=jar_id, sql=sql.replace('\n',' '), hdfs_path=cc0, appname=app_name).encode('utf-8')
        print(command)
        if result_type == 'save_as_print':
            return self.SelectQuery(result_type,command, int_index_list, float_index_list)
        else:
            os.system('hdfs dfs -rm -r /user/bi_user/SparkSql/' + cc)
            os.system(command)
            result = self.SelectQuery(result_type,'hdfs dfs -cat /user/bi_user/SparkSql/{hdfs_path}/part*'.format(hdfs_path=cc), int_index_list, float_index_list)
            return result

    def SubmitClose(self):
        pass


    def InsertM(self, data, table_name, is_overwrite=0, partition='', partition_value=''):
        if is_overwrite == 0:
            self.InsertHive(data, table_name, partition='', partition_value='')
        else:
            self.InsertHive(data, table_name, partition=partition, partition_value=partition_value)

    def InsertF(self, db, table, file_name):
        """
        首先将数据写入文件，再将文件插入hive,会删除原集群文件
        """
        hdfs_path = '/usr/hive/warehouse/{db}.db/{table}/'.format(db=db,table=table)
        os.system('hdfs dfs -rm ' + hdfs_path + '*')
        print('finish truncate table %s.%s at '%(db,table) + time.ctime())
        os.system('hdfs dfs -put ' + file_name + ' ' + hdfs_path)
        print('finish insert into table %s.%s at '%(db,table) + time.ctime())

    def InsertFwithPartition(self, data, table_name, partition='', partition_value=''):
        self.InsertHive(data, table_name, partition=partition, partition_value=partition_value)

    def InsertN(self, data, table_name):
        db, table = table_name.split('.')
        hdfs_path = '/usr/hive/warehouse/{db}.db/{table}/'.format(db=db,table=table)
        os.system('hdfs dfs -rm ' + hdfs_path + '*')
        self.InsertHive(data, table_name)

    def GetInsertData(self, data):
        if len(data) == 0:
            raise Exception("\n++++++++++++++ has no data, please check your SQL ++++++++++++++++++\n")
        words, count, data_len, num = '', 0, len(data), len(data[0])

        for p in data:
            try:
                line = u'\t'.join([u'%s']*num)%tuple(p) + u'\n'
            except:
                print(data_len,count,len(p),num)
                print(p)
                raise Exception("eeeee")
            count += 1
            words += line.encode('utf-8')
        return words

    def InsertHive(self, data, table_name, partition='', partition_value=''):
        insert_type = u'overwrite into' if partition != '' else u'into '
        partition_command = '' if partition == '' else "partition({partition}='{partition_value}')".format(partition=partition, partition_value=partition_value)
        hdfs_path = '/user/bi_user/HiveInsert/'
        data = self.GetInsertData(data)
        client = Client("http://10.3.4.67:4008")
        hive_command = """
        hive -e "load data  inpath '/user/bi_user/HiveInsert/{file_name}' {insert_type} table {table_name} {partition_command}"
        """
        file_name = table_name + str(int(time.time()*1000000))
        os.system('hdfs dfs -touchz ' + hdfs_path + file_name)
        client.write(hdfs_path + file_name, data, overwrite=True, append=False)
        os.system(hive_command.format(file_name=file_name, table_name=table_name, insert_type=insert_type, partition_command=partition_command).replace('\n','').strip())
        os.system('hdfs dfs -rm ' + hdfs_path + file_name)



if __name__=='__main__':
    d = SelectQuery()
    #d.WriteFile([('a','b'),('1','2')],'test')

    sql=u"""
    SELECT 1,'a'
    """
    words = ''
    a = d.SparkSQLSubmit('save_as_path',sql,'test','test')
    print(type(a))
    count=0
    for each in a:
        print(each)
        count+=1
        if count>5:
            break
    print(count)
    d.SubmitClose()
    #a = d.Select('spark-sql',sql,[0])
    #for each in a:
    #    print(each)