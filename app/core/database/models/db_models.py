from sqlalchemy import Column, Integer, String

from app.core.database.services import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(540), nullable=False)

    def __repr__(self):
        return "Subscription(id=%d, email=%s)" % (
            self.id,
            self.email,
        )
