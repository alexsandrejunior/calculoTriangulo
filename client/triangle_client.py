import os

import requests


def main() -> None:
    base_url = os.environ.get("BASE_URL", "http://127.0.0.1:8000")
    url = f"{base_url}/api/v1/triangle/area"

    base_str = input("Base: ").strip()
    height_str = input("Altura: ").strip()

    try:
        payload = {"base": float(base_str), "height": float(height_str)}
    except ValueError:
        print("Erro: base e altura precisam ser números.")
        return

    r = requests.post(url, json=payload, timeout=15)
    if r.ok:
        data = r.json()
        print(f"Area do triangulo = {data['area']}")
        return

    try:
        detail = r.json().get("detail")
    except ValueError:
        detail = None
    print(f"Erro ({r.status_code}): {detail or r.text}")


if __name__ == "__main__":
    main()

