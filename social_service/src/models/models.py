from pydantic import BaseModel, Field 
from typing import Optional

# region Publication

class PublicationModel(BaseModel):
    publication_id: str = None
    post_text: str = Field(..., max_length=500)
    reply_post_id: str = None

# endregion


