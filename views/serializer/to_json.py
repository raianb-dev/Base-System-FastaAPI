from fastapi import Response
import datetime, json


def build_toJson(status=400, content=None, token=None, alert=None):
    data = {}
    data["message"] = "Procedure performed successfully"
    data["time_request"] = str(datetime.datetime.now())
    data["status"] = status
    data["content"] = content
    
    if (token):
        data["access_token"] = token
    if (alert):
        data["alert"] = alert
        
    data["footer"] = "Api/v1 Version"
    data["info"] = "App build with FastAPI"
    data["author"] = "https://github.com/raianb-dev"    
    return Response(
        json.dumps(data),
        status_code=status,
        media_type="aplication/json"
    )