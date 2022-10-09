import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# https://pypi.org/project/Jinja2/


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def hello_world():
    return { 'message': 'hello' }

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

# get the form data from the user
@app.get("/basic", response_class=HTMLResponse)
async def get_basic_form(request: Request):
    return templates.TemplateResponse("basic_form.html", {"request": request})

# post the form data to the server
@app.post("/basic", response_class=HTMLResponse)
async def post_basic_form(request: Request , email: str = Form(...), password: str = Form(...)):
    # print(email, password)
    
    print(f'Email: {email} Password: {password}')
    return templates.TemplateResponse("basic_form.html", {"request": request})



if __name__ == '__main__':
    uvicorn.run(app)