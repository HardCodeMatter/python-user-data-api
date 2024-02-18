from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title='UserDataAPI',
    version='0.1.0',
)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
