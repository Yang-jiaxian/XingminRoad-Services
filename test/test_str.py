# -*- coding: utf-8 -*-
# @Author: Yang jiaxian
# @Date  : 2022/11/22
# @Desc  :
# @Email : 499706512@qq.com
import json

aa = "Sector basket stocks"
print(aa.lower().replace(" ", "_").replace("-", "_"))


        #

import json

class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field, ValidationError):
            return {'code': field.code, 'message': field.message}
        else:
            return json.JSONEncoder.default(self, field)


json.dumps(ret,cls=JsonCustomEncoder)