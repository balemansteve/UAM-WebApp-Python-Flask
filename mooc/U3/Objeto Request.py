request (Request Object)
├── method: str (e.g., 'GET', 'POST')
├── url: str (e.g., 'http://example.com')
├── headers: dict-like
│   ├── 'User-Agent': str (e.g., 'Mozilla/5.0...')
│   ├── 'Host': str (e.g., 'example.com')
│   ├── 'Accept': str (e.g., 'text/html,application/xhtml+xml')
│   └── ...
├── form: dict-like
│   ├── 'username': str
│   ├── 'password': str
│   └── ...
├── args: dict-like (for query parameters)
│   ├── 'search': str (e.g., 'flask')
│   └── ...
├── data: bytes (raw data from the request body)
├── json: dict-like or None (JSON data from request body)
├── cookies: dict-like
│   ├── 'sessionid': str
│   └── ...
├── files: dict-like (for file uploads)
│   ├── 'file1': FileStorage object
│   └── ...
├── remote_addr: str (client IP address)
└── ...

# Métodos comunes:
├── get_data(as_text=False): Devuelve los datos crudos de la solicitud.
├── get_json(silent=False): Devuelve el cuerpo JSON de la solicitud.
├── get_cookie(key): Devuelve el valor de una cookie específica.
└── ...

