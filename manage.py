# -*- coding: utf-8 -*-
# @Author: Yang jiaxian
# @Date  : 2022/9/19
# @Desc  : 启动文件
# @Email : 499706512@qq.com

import uvicorn

if __name__ == '__main__':
    # 生成日志文件夹

    uvicorn.run(app='src.main:app', host='0.0.0.0', port=8000, reload=True, workers=1)
