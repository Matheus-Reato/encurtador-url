from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database import Base
from sqlalchemy import Text

class Url(Base):
    __tablename__ = "url"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(Text, unique=True)
    url_encurtada: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())