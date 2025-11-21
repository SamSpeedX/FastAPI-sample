from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.routes.user_route import router as UserRouter
# from pydantic import BaseModel

app = FastAPI()

app.include_router(UserRouter, prefix="/users", tags=["Users"])
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "msg": "Welcome SAM OCHU!"})


@app.post("/register", response_class=HTMLResponse)
def register(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
            "msg": f"User {username} registered successfully!",
            "username": username,
            "email": email
        }
    )