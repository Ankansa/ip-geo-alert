import requests


def get_ip_location(ip_address: str) -> dict:
    """
    Fetch geolocation info using ip-api.com
    """

    url = f"http://ip-api.com/json/{ip_address}"

    response = requests.get(url, timeout=5)
    data = response.json()

    if data.get("status") != "success":
        return {
            "ip": ip_address,
            "error": data.get("message", "Geo lookup failed"),
        }

    return {
        "ip": data.get("query"),
        "city": data.get("city"),
        "region": data.get("regionName"),
        "country": data.get("country"),
        "lat": data.get("lat"),
        "lon": data.get("lon"),
        "isp": data.get("isp"),
    }
