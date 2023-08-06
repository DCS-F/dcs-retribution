from dataclasses import dataclass, field
from typing import Any, Optional

from .optiondescription import OptionDescription, SETTING_DESCRIPTION_KEY


def string_option(
    text: str,
    page: str,
    section: str,
    default: int,
    detail: Optional[str] = None,
    tooltip: Optional[str] = None,
    causes_expensive_game_update: bool = False,
    **kwargs: Any,
) -> str:
    return field(
        metadata={
            SETTING_DESCRIPTION_KEY: OptionDescription(
                page,
                section,
                text,
                detail,
                tooltip,
                causes_expensive_game_update,
            )
        },
        default=default,
        **kwargs,
    )
