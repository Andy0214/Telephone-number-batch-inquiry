#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author = "Andy"
# Date: 2018/7/23

from phone import Phone



if __name__ == "__main__":
    phoneNum = '17613394466'
    info = Phone().find(phoneNum)
    print(info)
    try:
        phone = info['phone']
        province = info['province']
        city = info['city']
        zip_code = info['zip_code']
        area_code = info['area_code']
        phone_type = info['phone_type']
    except:
        print('none')

