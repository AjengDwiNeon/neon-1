import json
from fastapi import APIRouter, Body, Response
from apps.controllers.AdetController import ControllerAdet as adet

router = APIRouter()

example_input_cifno = json.dumps({
    "cif": "1",
}, indent=2)

@router.post("/get_loan_by_cif_created_by_adet")
async def get_loan_by_cif_created_by_adet(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = adet.get_loan_by_cif_created_by_adet(input_data=input_data)
    response.status_code = result.status
    return result

@router.post("/get_loan_by_cif_debug_created_by_adet")
async def get_loan_by_cif_debug_created_by_adet(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = adet.get_loan_by_cif_debug_created_by_adet(input_data=input_data)
    response.status_code = result.status
    return result