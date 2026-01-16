async def notify_via_email(geo_data: dict, send_mail_func):
    """
    Calls user-provided mail function.
    """

    subject = f"🚨 API Access Alert from {geo_data.get('country', 'Unknown')}"

    body = f"""
IP Address: {geo_data.get('ip')}
City: {geo_data.get('city')}
Region: {geo_data.get('region')}
Country: {geo_data.get('country')}
ISP: {geo_data.get('isp')}
Latitude: {geo_data.get('lat')}
Longitude: {geo_data.get('lon')}
"""

    await send_mail_func(subject.strip(), body.strip())
