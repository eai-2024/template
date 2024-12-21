import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class Session:
    """
    Сессия для запросов с поддержкой повторных попыток при сбоях.
    """

    def __init__(
        self, base_url: str, timeout: float = 5.0, max_retries: int = 3, backoff_factor: float = 0.3
    ) -> None:
        self.base_url = base_url
        self.timeout = timeout

        retries = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET", "POST"],
        )
        adapter = HTTPAdapter(max_retries=retries)
        self.session = requests.Session()
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.get(f"{self.base_url}/{endpoint}", timeout=self.timeout, **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.post(f"{self.base_url}/{endpoint}", timeout=self.timeout, **kwargs)
