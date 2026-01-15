# ip-geo-alert

Lightweight IP geolocation alert package for FastAPI.

## Features
- Proxy-aware IP detection
- Uses ip-api.com
- User-defined email sender
- Route-level execution

## Install
pip install ip-geo-alert

## Usage
python
from ip_geo_alert import process_request


## 🔐 Production Notes (Important)

- ip-api free tier → **45 requests/min**
- Do NOT store IPs without consent (DPDP/GDPR)

