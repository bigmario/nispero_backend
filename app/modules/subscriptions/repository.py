import bcrypt
from sqlalchemy.orm import Session

import app.core.database.models.db_models as models
import app.core.database.schemas.db_schemas as schemas


class SubscriptionsRepo:
    async def create(self, db: Session, subscriber: schemas.SubscriberCreate):

        db_subscriber = models.Subscription(
            email=subscriber.email,
        )
        db.add(db_subscriber)
        db.commit()
        db.refresh(db_subscriber)
        return db_subscriber

    def fetch_by_id(self, db: Session, _id: int):
        return (
            db.query(models.Subscription).filter(models.Subscription.id == _id).first()
        )

    def fetch_by_email(self, db: Session, email: str):
        return (
            db.query(models.Subscription)
            .filter(models.Subscription.email.contains(email))
            .all()
        )

    def fetch_all(self, db: Session, skip: int = 0, limit: int = 100):
        result = db.query(models.Subscription).offset(skip).limit(limit).all()
        return result
