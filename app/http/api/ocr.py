from fastapi import APIRouter, Depends, FastAPI, HTTPException, UploadFile

from app.http.deps import get_db
from app.models.user import User
from app.services.auth import hashing
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import time
import openai
import requests
import json
from PyPDF2 import PdfReader
import docx
import asyncio
import json
import paddlehub as hub
import cv2
from paddleocr import PaddleOCR,draw_ocr

router = APIRouter(
    prefix="/ocr"
)


@router.get("/")
async def index():
    return "ocr index"


async def ImageErrorCorrection(file):
    # 读取上传的文件
    imgBytes = file.file.read()
    imgName = file.filename
    # 判断上传文件类型
    imgType = imgName.split(".")[-1]
    if imgType != "png" and imgType != "jpg" and imgType != "jpeg":
        raise HTTPException(status_code=406, detail=str(
            "请求失败，上传图片格式不正确！请上传jpg或png图片！"))
    try:
        now_time = int(time.mktime(time.localtime(time.time())))
        # 拼接生成随机文件名，注意名称不能包含中文否则后面读取出错
        imgPath = "storage/image/" + str(now_time) + "_image." + imgType
        print(imgPath)
        fout = open(imgPath, 'wb')
        fout.write(imgBytes)
        fout.close()
        print("文件上传成功！")
        # ocr = hub.Module(name="chinese_ocr_db_crnn_server", enable_mkldnn=True)       # mkldnn加速仅在CPU下有效
        # result = ocr.recognize_text(images=[cv2.imread(imgPath)])
        # text_list = []
        # for item in result:
        #     for data in item['data']:
        #         text_list.append(data['text'])
        # text_str = ' '.join(text_list)
        # print(text_str)
        # need to run only once to download and load model into memory
        ocr = PaddleOCR(use_angle_cls=True, lang='ch')
        result = ocr.ocr(imgPath, cls=True)
        txts = [detection[1][0] for line in result for detection in line] # Nested loop added
        all_context = " ".join(txts)
        print(all_context)
        # 接口结果返回
        results1 = {"message": "success",
                    "orcResult": "str(ocr_image_results[0])", "correctionResults": all_context}
        return results1
    # 异常处理
    except Exception as e:
        print("异常信息：", e)
        raise HTTPException(status_code=500, detail=str(
            "请求失败，服务器端发生异常！异常信息提示：" + str(e)))


# 定义路径操作装饰器：POST方法 + API接口路径

# 文本识别接口

# 图片识别接口
@router.post("/crn/", status_code=200)
# 定义路径操作函数，当接口被访问将调用该函数
async def handle_request(file: UploadFile):
    # 创建一个事件循环
    loop = asyncio.get_running_loop()
    print('创建事件循环成功')
    # 创建一个协程，用于处理当前请求
    coroutine = ImageErrorCorrection(file)
    print('创建协程成功')
    # 并行处理当前请求
    result = await asyncio.gather(coroutine, return_exceptions=True)
    print('并行处理当前请求成功')
    print(result)
    return result[0]
