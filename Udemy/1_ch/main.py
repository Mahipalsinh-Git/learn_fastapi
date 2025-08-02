from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "hello fast api"}


def main():
    home()


if __name__ == "__main__":
    main()
