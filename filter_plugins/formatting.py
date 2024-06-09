from ansible.plugins.filter import AnsibleJinja2Filter
from ansible.module_utils.common.text import converters

from typing import Any


class FilterModule(AnsibleJinja2Filter):

    def __init__(self) -> None:
        pass

    def filters(self) -> dict[str, object]:
        return {'yesno': self.yesno}

    def yesno(self, obj: Any) -> str:
        result: str = "yes" if obj else "no"
        return converters.to_text(result)
