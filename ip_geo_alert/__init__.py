from fastapi import Request
from .detector import extract_client_ip
from .geo import get_ip_location
from .notifier import notify_via_email
from .rules import EndpointRuleEngine

LOCAL_IPS = {"127.0.0.1", "::1", "localhost", "unknown"}


async def process_request(
    request: Request,
    send_mail_func,
    rule_engine: EndpointRuleEngine,
):
    """
    Main entry point.
    Triggers mail ONLY if endpoint rule matches.
    """

    if not rule_engine.should_trigger(request):
        return {
            "triggered": False,
            "reason": "Endpoint not configured",
        }

    ip = extract_client_ip(request)

    if ip in LOCAL_IPS:
        return {
            "triggered": False,
            "ip": ip,
            "reason": "Local or unknown IP",
        }

    geo_data = get_ip_location(ip)

    await notify_via_email(geo_data, send_mail_func)

    return {
        "triggered": True,
        "geo": geo_data,
    }
