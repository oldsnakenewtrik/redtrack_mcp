"""
RedTrack FastMCP Python Server

Expose selected RedTrack API endpoints as MCP tools using FastMCP.
- Default transport: stdio (python mcp_server.py)
- Optional HTTP transport: set FASTMCP_TRANSPORT=http to run as HTTP server

Environment:
- REDTRACK_API_KEY: your RedTrack API key
- REDTRACK_BASE_URL (optional): default https://api.redtrack.io
"""
from __future__ import annotations

import os
import sys
from datetime import datetime
from typing import Any, Dict, Optional

try:
    import httpx
except Exception as e:  # pragma: no cover
    # Defer hard failure until tool call for better DX
    httpx = None  # type: ignore

try:
    from fastmcp import FastMCP
except Exception as e:
    print("Error: fastmcp is not installed. Install with: pip install fastmcp", file=sys.stderr)
    raise


def _require_httpx():
    global httpx
    if httpx is None:
        raise RuntimeError("httpx is not installed. Install with: pip install httpx")
    return httpx


def _validate_date(date_str: str, param_name: str) -> None:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"{param_name} must be YYYY-MM-DD (got: {date_str})") from e


class RedTrackClient:
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("REDTRACK_API_KEY")
        if not self.api_key:
            raise RuntimeError(
                "Missing REDTRACK_API_KEY. Set env var or pass api_key explicitly to the tool."
            )
        self.base_url = (base_url or os.getenv("REDTRACK_BASE_URL") or "https://api.redtrack.io").rstrip("/")

    def _get(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        hx = _require_httpx()
        url = f"{self.base_url}{path}"
        # Ensure api_key is always present as query parameter
        merged = {"api_key": self.api_key}
        merged.update({k: v for k, v in params.items() if v is not None and v != ""})
        with hx.Client(timeout=60) as client:
            resp = client.get(url, params=merged)
            try:
                resp.raise_for_status()
            except Exception as e:
                # Attempt to include server-provided error details
                detail = None
                try:
                    detail = resp.json()
                except Exception:
                    detail = resp.text
                raise RuntimeError(f"RedTrack GET {path} failed: {resp.status_code} {detail}") from e
            try:
                data = resp.json()
            except Exception:
                return {"status": resp.status_code, "text": resp.text}
            # FastMCP tools must return a dict; wrap list responses
            if isinstance(data, list):
                return {"items": data, "count": len(data)}
            return data


mcp = FastMCP("RedTrack MCP Server")


@mcp.tool
def redtrack_tracks(
    date_from: str,
    date_to: str,
    campaign_id: Optional[str] = None,
    source_id: Optional[str] = None,
    offer_id: Optional[str] = None,
    page: int = 1,
    per: int = 1000,
    time_interval: Optional[str] = None,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Fetch clicks log from RedTrack (/tracks).

    Required:
    - date_from, date_to: YYYY-MM-DD

    Optional filters:
    - campaign_id, source_id, offer_id
    - page (default 1), per (default 1000)
    - time_interval (e.g., hour)
    - api_key/base_url: override env values for this call
    """
    _validate_date(date_from, "date_from")
    _validate_date(date_to, "date_to")

    client = RedTrackClient(api_key=api_key, base_url=base_url)
    params: Dict[str, Any] = {
        "date_from": date_from,
        "date_to": date_to,
        "campaign_id": campaign_id,
        "source_id": source_id,
        "offer_id": offer_id,
        "page": page,
        "per": per,
        "time_interval": time_interval,
    }
    return client._get("/tracks", params)


@mcp.tool
def redtrack_conversions(
    date_from: str,
    date_to: str,
    campaign_id: Optional[str] = None,
    source_id: Optional[str] = None,
    offer_id: Optional[str] = None,
    page: int = 1,
    per: int = 1000,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Fetch conversions log from RedTrack (/conversions). Same params pattern as tracks.
    """
    _validate_date(date_from, "date_from")
    _validate_date(date_to, "date_to")

    client = RedTrackClient(api_key=api_key, base_url=base_url)
    params: Dict[str, Any] = {
        "date_from": date_from,
        "date_to": date_to,
        "campaign_id": campaign_id,
        "source_id": source_id,
        "offer_id": offer_id,
        "page": page,
        "per": per,
    }
    return client._get("/conversions", params)


@mcp.tool
def redtrack_countries(api_key: Optional[str] = None, base_url: Optional[str] = None) -> Dict[str, Any]:
    """Get countries dictionary (/countries)."""
    client = RedTrackClient(api_key=api_key, base_url=base_url)
    return client._get("/countries", {})


@mcp.tool
def redtrack_report(
    date_from: str,
    date_to: str,
    group_by: Optional[str] = None,
    campaign_id: Optional[str] = None,
    source_id: Optional[str] = None,
    offer_id: Optional[str] = None,
    time_interval: Optional[str] = None,
    page: int = 1,
    per: int = 1000,
    filters: Optional[Dict[str, Any]] = None,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Call RedTrack /report endpoint.

    You can pass common filters directly (campaign_id, source_id, offer_id, time_interval),
    or provide any additional query params via `filters`.
    """
    _validate_date(date_from, "date_from")
    _validate_date(date_to, "date_to")

    client = RedTrackClient(api_key=api_key, base_url=base_url)
    params: Dict[str, Any] = {
        "date_from": date_from,
        "date_to": date_to,
        "group_by": group_by,
        "page": page,
        "per": per,
        "campaign_id": campaign_id,
        "source_id": source_id,
        "offer_id": offer_id,
        "time_interval": time_interval,
    }
    if filters:
        params.update(filters)
    return client._get("/report", params)


@mcp.tool
def redtrack_report_summary(
    date_from: str,
    date_to: str,
    group_by: Optional[str] = None,
    campaign_id: Optional[str] = None,
    source_id: Optional[str] = None,
    offer_id: Optional[str] = None,
    time_interval: Optional[str] = None,
    page: int = 1,
    per: int = 1000,
    top_n: Optional[int] = None,
    sort_by: str = "revenue",
    filters: Optional[Dict[str, Any]] = None,
    api_key: Optional[str] = None,
    base_url: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Convenience tool: fetch /report and return compact totals + optional breakdown.

    - Returns: { summary: {...}, breakdown: [...], count }
    - summary includes clicks, conversions, cost, revenue, profit, roi, roas
    - breakdown rows include the same metrics plus a label for grouping
    """
    _validate_date(date_from, "date_from")
    _validate_date(date_to, "date_to")

    # Reuse the report tool to build params consistently
    resp = redtrack_report(
        date_from=date_from,
        date_to=date_to,
        group_by=group_by,
        campaign_id=campaign_id,
        source_id=source_id,
        offer_id=offer_id,
        time_interval=time_interval,
        page=page,
        per=per,
        filters=filters,
        api_key=api_key,
        base_url=base_url,
    )

    # Normalize rows
    rows: list[dict[str, Any]]
    if isinstance(resp, dict) and "items" in resp and isinstance(resp["items"], list):
        rows = resp["items"]
    elif isinstance(resp, list):
        rows = resp
    elif isinstance(resp, dict):
        rows = [resp]
    else:
        rows = []

    def get_num(d: dict, *keys: str) -> float:
        for k in keys:
            if k in d and isinstance(d[k], (int, float)):
                return float(d[k])
        return 0.0

    # Compute totals
    totals = {
        "clicks": 0.0,
        "conversions": 0.0,
        "cost": 0.0,
        "revenue": 0.0,
        "profit": 0.0,
    }
    for r in rows:
        totals["clicks"] += get_num(r, "clicks")
        totals["conversions"] += get_num(r, "total_conversions", "conversions")
        revenue_r = get_num(r, "total_revenue", "revenue")
        cost_r = get_num(r, "cost")
        profit_r = get_num(r, "profit")
        totals["revenue"] += revenue_r
        totals["cost"] += cost_r
        # Use explicit profit if present, else imply
        totals["profit"] += profit_r if profit_r else (revenue_r - cost_r)

    roi = (totals["revenue"] - totals["cost"]) / totals["cost"] if totals["cost"] else None
    roas = totals["revenue"] / totals["cost"] if totals["cost"] else None

    summary = {
        "clicks": int(totals["clicks"]),
        "conversions": int(totals["conversions"]),
        "cost": round(totals["cost"], 4),
        "revenue": round(totals["revenue"], 4),
        "profit": round(totals["profit"], 4),
        "roi": round(roi, 4) if roi is not None else None,
        "roas": round(roas, 4) if roas is not None else None,
    }

    # Optional breakdown (only if multiple rows or grouping requested)
    breakdown: list[dict[str, Any]] = []
    if rows:
        for r in rows:
            label = None
            if group_by:
                label = r.get(group_by) or r.get(f"{group_by}_id")
            if label is None:
                label = r.get("date")
            b_rev = get_num(r, "total_revenue", "revenue")
            b_cost = get_num(r, "cost")
            b_roi = ((b_rev - b_cost) / b_cost) if b_cost else None
            b_roas = (b_rev / b_cost) if b_cost else None
            breakdown.append({
                "label": label,
                "clicks": int(get_num(r, "clicks")),
                "conversions": int(get_num(r, "total_conversions", "conversions")),
                "cost": round(b_cost, 4),
                "revenue": round(b_rev, 4),
                "profit": round(get_num(r, "profit") or (b_rev - b_cost), 4),
                "roi": round(b_roi, 4) if b_roi is not None else None,
                "roas": round(b_roas, 4) if b_roas is not None else None,
            })

    # Sort and slice breakdown if requested
    if breakdown:
        key = (sort_by or "revenue").lower()
        breakdown.sort(key=lambda x: x.get(key) or 0, reverse=True)
        if top_n is not None and top_n > 0:
            breakdown = breakdown[:top_n]

    return {"summary": summary, "breakdown": breakdown, "count": len(rows)}



if __name__ == "__main__":
    # Choose transport via env var for convenience
    transport = os.getenv("FASTMCP_TRANSPORT", "stdio").lower()
    if transport == "http":
        host = os.getenv("FASTMCP_HOST", "127.0.0.1")
        port = int(os.getenv("FASTMCP_PORT", "8000"))
        print(f"Starting RedTrack MCP (HTTP) on http://{host}:{port}/mcp/")
        mcp.run(transport="http", host=host, port=port)
    else:
        # stdio is the default and is what MCP clients expect
        mcp.run()

