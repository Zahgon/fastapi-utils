from typing import Any, Dict, Optional, Tuple

from fastapi import APIRouter, FastAPI

from .cbv import INCLUDE_INIT_PARAMS_KEY, RETURN_TYPES_FUNC_KEY, _cbv


class Resource:
    # raise NotImplementedError
    pass


class Api:
    def __init__(self, app: FastAPI):
        self.app = app

    def add_resource(self, resource: Resource, *urls: str, **kwargs: Any) -> None:
        pass


def take_init_parameters(cls: Any) -> Any:
    setattr(cls, INCLUDE_INIT_PARAMS_KEY, True)
    return cls


def set_responses(
    response: Any, status_code: int = 200, responses: Optional[Dict[str, Any]] = None, **kwargs: Any
) -> Any:
    def decorator(func: Any) -> Any:
        pass

    return decorator
