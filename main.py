# main.py
import json
import os

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import gspread
from google.oauth2.service_account import Credentials

from gspread.utils import ValueInputOption

from app.constants import DRIVE_API, SHEETS_API, WORKSHEET_NAME, SPREADSHEET_NAME, SPEND_TABLE_RANGE
from app.log import log
from app.constants import GCP_CREDS_JSON, CHART_IMAGE_URL

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

SCOPES = [SHEETS_API, DRIVE_API]
load_dotenv()


def get_credentials():
    creds_json = os.environ[GCP_CREDS_JSON]
    return json.loads(creds_json)


def get_worksheet():
    """
    - Authenticate via service account credentials.
    - Open a specific spreadsheet and worksheet.
    """
    creds = Credentials.from_service_account_info(get_credentials(), scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open(SPREADSHEET_NAME).worksheet(WORKSHEET_NAME)
    return sheet

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Render the HTML form to submit an expense.
    """
    return templates.TemplateResponse("index.html", {"request": request, "active": "add"})


@app.get("/chart-view", response_class=HTMLResponse)
async def show_chart(request: Request):
    return templates.TemplateResponse("chart.html", {"request": request, "active": "chart"})


@app.head("/health", response_class=HTMLResponse)
async def health_check():
    """
    Handle HEAD request to the health check route.
    This is useful for checking if the resource exists without fetching it.
    """
    log.info("Health Check by UptimeRobot")
    return HTMLResponse(status_code=200, content="")


@app.get("/health", response_class=HTMLResponse)
async def health_check():
    """
    Handle GET request to the health check route.
    This is useful for checking if the resource exists without fetching it.
    """
    log.info("Health Check by Uptime")
    return HTMLResponse(status_code=200, content="")


@app.post("/submit")
async def submit_expense(
    date: str = Form(...),
    name: str = Form(...),
    category: str = Form(...),
    priority: str = Form(...),
    amount: int = Form(...),
):
    """
    - Read form data
    - Append a new row to Google Sheets
    - Redirect back to the form (303 redirect for POST->GET)
    """
    try:
        ws = get_worksheet()
        ws.append_row(
            [date, name, category, priority, amount],
            value_input_option=ValueInputOption.user_entered,
            table_range=SPEND_TABLE_RANGE
        )
        log.info(f"Expense submitted: {date}, {name}, {category}, {priority}, {amount}")
        return RedirectResponse(url="/?status=success", status_code=303)
    except Exception as e:
        log.error(f"Error submitting expense: {e}")
        return RedirectResponse(url="/?status=error", status_code=303)


@app.get('/chart')
async def get_chart(request: Request):
    """
    Render the chart page.
    """
    chart_img_url = os.environ.get(CHART_IMAGE_URL)
    async with httpx.AsyncClient() as client:
        resp = await client.get(chart_img_url)
    headers = {
        "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
        "Pragma": "no-cache",
        "Expires": "0",
    }
    return Response(content=resp.content, media_type="image/png", headers=headers)

