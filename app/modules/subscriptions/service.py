from sqlalchemy.orm import Session
from fastapi import status, BackgroundTasks, Depends
from fastapi.exceptions import HTTPException

from app.modules.subscriptions.repository import SubscriptionsRepo
from app.core.database.schemas import SubscriberCreate


class SubscriptionsService:
    def __init__(self, subscriptionsRepo: SubscriptionsRepo = Depends()):
        self.subscriptionsRepo = subscriptionsRepo

    async def create_subscriber(self, body: SubscriberCreate, db: Session):
        new_subscriber = self.subscriptionsRepo.fetch_by_email(db, email=body.email)
        if new_subscriber:
            raise HTTPException(status_code=400, detail="Subscriber already exists!")

        return await self.subscriptionsRepo.create(db, body)

    async def get_subscribers(self, email: str, db: Session):
        if email:
            subscriber = self.subscriptionsRepo.fetch_by_email(db, email)
            if not subscriber:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Subscriber Id not found!",
                )
            return subscriber
        else:
            return self.subscriptionsRepo.fetch_all(db)

    async def get_subscriber_by_id(self, _id: int, db: Session):
        db_item = self.subscriptionsRepo.fetch_by_id(db, _id)
        if not db_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Subscriber Id not found!"
            )
        return db_item

    async def get_subscriber_by_email(self, email: str, db: Session):
        db_item = self.subscriptionsRepo.fetch_by_email(db, email)
        if not db_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Subscriber not found!"
            )
        return db_item
