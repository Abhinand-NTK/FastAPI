from fastapi import APIRouter
from enum import Enum

class EnumClassName(str,Enum):
    admin = 'admin'
    superadmin = 'superadmin'
    user = 'user'


router = APIRouter()

@router.get("/enums/{enum_name}")
async def get_user_access(enum_name:EnumClassName):
    if enum_name is EnumClassName.admin:
        return {"role": enum_name, "message": "User have Admin privillages"}

    if enum_name is EnumClassName.user:
        return {"role": enum_name, "message": "User have User privillages"}
    
    if enum_name is EnumClassName.superadmin:
        return {"role": enum_name, "message": "User have Superadmin privillages"}