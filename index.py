from flask import Flask , request

sample = Flask(__name__)

@sample.route("/")
def main():
  return "You are calling me from " + request.remote_addr + "\n"

if __name__ == "__main__":
  sample.run(host="0.0.0.0", port=8080)