from app import application


DEV_PORT = 5000
PRO_PORT = 80

DEV_HOST = "localhost"
PRO_HOST = "0.0.0.0"

#mode = "production"
mode = "development"


if __name__ == "__main__":
    if mode == "production":
        application.run(port=PRO_HOST, host=DEV_HOST)
    else:
        application.run(port=DEV_PORT, host=DEV_HOST, debug=True)