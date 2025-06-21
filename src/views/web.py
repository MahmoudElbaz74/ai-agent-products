from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from src.controllers.agent import ask_question

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

html = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>الوكيل الذكي للمنتجات</title>
</head>
<body style="text-align:right; direction:rtl; font-family:Tahoma;">
    <h2>اسأل عن منتجاتنا</h2>
    <form method="post" action="/ask">
        <input type="text" name="question" placeholder="ما الذي تريد معرفته؟" style="width:300px;" required>
        <button type="submit">إرسال</button>
    </form>
    <hr>
    <div>{response}</div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def form_get():
    return html.format(response="")

@app.post("/ask", response_class=HTMLResponse)
async def form_post(question: str = Form(...)):
    answer = ask_question(question)
    return html.format(response=answer)