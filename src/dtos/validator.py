from pydantic import BaseModel, ValidationError
from typing import Type, Dict, Any

class Validator:
    @staticmethod
    def parse(data: Dict, dto_class: Type[BaseModel]) -> Any:
        try:
            return dto_class(**data)
        except ValidationError as e:
            raise ValueError(f"Validation error: {e}")