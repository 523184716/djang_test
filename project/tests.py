# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import  MySQLdb
# Create your tests here.

conn = MySQLdb.connect(host='10.36.3.74',user='root',passwd='123456',db='test')
cur = conn.cursor()

sql = "select * from login"
cur.execute(sql)
result = cur.fetchall()
print result