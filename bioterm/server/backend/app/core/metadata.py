import typing
from typing import Any
from typing import Dict
from typing import List


def get_inner_type(field_type):
    if hasattr(field_type, "__origin__"):
        if field_type.__origin__ == typing.Union:
            return next(arg for arg in field_type.__args__ if arg != type(None))
    return field_type


def is_optional(field_type):
    return typing.get_origin(field_type) is typing.Union and type(
        None
    ) in typing.get_args(field_type)


def generate_metadata(pydantic_model: Any) -> List[Dict[str, Any]]:
    metadata = []
    for field_name, field_type in pydantic_model.__annotations__.items():
        meta_info = {
            "label": field_name.capitalize(),
            "model": field_name,
            "autocomplete": False,
        }

        # Determine the field type
        inner_type = get_inner_type(field_type)

        if inner_type == str:
            meta_info["type"] = "text"
        elif inner_type == int:
            meta_info["type"] = "number"
        elif inner_type == bool:
            meta_info["type"] = "boolean"

        # Check if the field is nullable
        is_nullable = is_optional(field_type)
        if is_nullable:
            meta_info["nullable"] = True
        else:
            meta_info["nullable"] = False

        metadata.append(meta_info)
    return metadata
