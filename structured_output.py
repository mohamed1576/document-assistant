from pydantic import BaseModel , ValidationError , Field
from typing import Literal

class Ticket(BaseModel):   
        category: str
        priority:Literal["low" , "medium" , "high"]
        confidence: float = Field(ge=0 , le=1)

try :
        ticket = Ticket(
                category="order_problem",
                priority="high",
                confidence=.8

        )
except ValidationError as error:
        print("validation failed")
        print(error)