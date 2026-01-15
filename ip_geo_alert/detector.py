from fastapi import Request


def extract_client_ip(request: Request) -> str:
    """
    Extract real client IP from request headers.
    """

    x_forwarded_for = request.headers.get("x-forwarded-for")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()

    x_real_ip = request.headers.get("x-real-ip")
    if x_real_ip:
        return x_real_ip.strip()

    if request.client:
        return request.client.host

    return "unknown"
