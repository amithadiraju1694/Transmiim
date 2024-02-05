from typing import Union, List
from fastapi import FastAPI, File, UploadFile,Request
from typing_extensions import Annotated
from fastapi.responses import HTMLResponse
from src.inference.preprocess_image import load_image_into_numpy_array
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="./src/templates")
app.mount("/src/templates", StaticFiles(directory="./src/templates"), name="templates")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/translate")
async def Translate_Image(
    files: Annotated[
        UploadFile, File(description="Upload a file into memory")
    ]):  
    
    if files is None:
        return {"error": "Could not take in file, please try and upload again !"}
    
    
    if "image" in files.content_type:
        image = load_image_into_numpy_array(await files.read())
        # text_from_im = extract_text_from_img(image)
        # if len(text_from_im) == 0:
        #   return Warning
        # else:
        #   translated_text = translate_to_english(text_form_im)
        #   clean_translated_text = supress_curse_words(translated_text)
        #   ensure not None and send response back
        return {"filenames": files.filename, "filetypes": files.content_type, "image size": image.shape}
    
    return {"error": " We don't support non image files for translation, please upload images ony"}




@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(
        name="index.html", context={'request': request}
    )




