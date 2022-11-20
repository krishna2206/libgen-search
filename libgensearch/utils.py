class Util:
    @staticmethod
    def filter_result(result: dict, filters: dict) -> bool:
        outcome = True
        for key in filters:
            if not filters[key] in result[key]:
                outcome = False
        return outcome

    @staticmethod
    def raise_error(status_code: int, resp: str) -> None:
        raise ConnectionError(
            f'{status_code}: {resp}')
