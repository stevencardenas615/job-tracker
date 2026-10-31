from datetime import date, datetime
from enum import Enum
from pydantic import BaseModel

class Status(str, Enum):
    SAVED = "saved"
    APPLIED = "applied"
    INTERVIEWING = "interviewing"
    OFFER = "offer"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"

class Source(str, Enum):
    MANUAL = "manual"
    IMPORT = "import"
    AGENT = "agent"

class ApplicationCreate(BaseModel):
    company: str
    role: str
    location: str
    url: str
    source: Source = Source.MANUAL
    deadline: date | None = None
    notes: str | None = None

class Application(ApplicationCreate):
    application_id: int
    status: Status
    applied_at: datetime | None = None
    created_at: datetime
    updated_at: datetime
