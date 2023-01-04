# -*- coding: utf-8 -*-
# @Author: Yang jiaxian
# @Date  : 2022/9/19
# @Desc  : 启动文件
# @Email : 499706512@qq.com

import uvicorn

if __name__ == '__main__':
    uvicorn.run(app='src.main:app', host='localhost', port=8000, workers=1, reload=True)
