from typing import List, Any
from fastapi import Body, APIRouter, status, Depends, Query, Path
from fastapi.exceptions import HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from sqlalchemy.orm import Session

from app.core.database.schemas import Subscriber, SubscriberCreate
from app.core.database.services import get_db
from app.modules.subscriptions.service import SubscriptionsService


subscriptions_router = APIRouter(
    tags=["Subscriptions"],
)


@subscriptions_router.post(
    path="/subscriptions",
    response_model=Subscriber,
    response_model_exclude_unset=True,
    status_code=status.HTTP_201_CREATED,
)
async def create_subscription(
    body: SubscriberCreate = Body(...),
    db: Session = Depends(get_db),
    subscriptionsService: SubscriptionsService = Depends(),
):
    """
    Create an User and store it in the database
    """
    try:
        return await subscriptionsService.create_subscriber(body, db)
    except Exception as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@subscriptions_router.get(
    path="/subscriptions",
    response_model=Page[Subscriber],
    response_model_exclude_unset=True,
    status_code=status.HTTP_200_OK,
)
async def get_all_subscriptions(
    email: str = Query(default=None),
    db: Session = Depends(get_db),
    subscriptionsService: SubscriptionsService = Depends(),
):
    """
    Get all the Users stored in database
    """
    try:
        subscriptions = await subscriptionsService.get_subscribers(email, db)
        return paginate(subscriptions)
    except Exception as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@subscriptions_router.get(
    path="/subscriptions/{id}",
    # response_model=Subscriber,
    response_model_exclude_unset=True,
    status_code=status.HTTP_200_OK,
)
async def get_subscription_by_id(
    id: str = Path(...),
    db: Session = Depends(get_db),
    subscriptionsService: SubscriptionsService = Depends(),
):
    """
    Get one Subscriber by ID
    """
    try:
        return await subscriptionsService.get_subscriber_by_id(id, db)
    except Exception as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
