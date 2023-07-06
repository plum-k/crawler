import os

import mysql.connector
import oss2

db = mysql.connector.connect(
    host="rm-wz92cjdff0dv7sc44uo.mysql.rds.aliyuncs.com",
    user="db_user_blog",
    passwd="3s17eHUZ1VJVjm3h",
    database="blog"
)
db_cursor = db.cursor()
access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'LTAI4GDKynjRXzVta2g5UaYr')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'ES7pdWs6xTPT6MbwjgEvUSrGRhfKws')
bucket_name = os.getenv('OSS_TEST_BUCKET', 'nikolas-image')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'oss-cn-chengdu.aliyuncs.com')

bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)


def upload(src_dir):
    for filename in os.listdir(src_dir):
        srcFile = os.path.join(src_dir, filename)
        bucket.put_object_from_file('img_bed/' + filename, srcFile)
        sql = "insert into `img_bed` (url) values (%s)"
        val = ("https://" + bucket_name + "." + endpoint + "/img_bed/" + filename,)
        db_cursor.execute(sql, val)
        db.commit()

upload("./out")
