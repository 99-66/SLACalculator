from fastapi import APIRouter, status
from pydantic import BaseModel
from starlette.responses import JSONResponse

from core.sla import SLA
from schemas.sla import Response as SLAResponse

router = APIRouter(
    tags=["sla"])


class Message(BaseModel):
    message: str


@router.get("/{percentage}",
            status_code=status.HTTP_200_OK,
            response_model=SLAResponse,
            responses={
                400: {"model": Message},
            })
async def sla_calculator(percentage: float):
    """
    SLA 가동율의 가동 중지 허용시간(downtime)을 계산한다
    """
    # percentage 가 0보다 작거나, 100보다 크다면 에러를 반환한다
    if 0 > percentage > 100:
        return JSONResponse(status_code=400, content={
            'message': 'Bad Request'
        })

    sla = SLA(percentage)

    down_time = sla.downtime()

    return SLAResponse(
        daily=down_time['daily'],
        weekly=down_time['weekly'],
        monthly=down_time['monthly'],
        yearly=down_time['yearly']
    )
