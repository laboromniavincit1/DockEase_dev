from flask import Flask, request, render_template
import subprocess
app = Flask (__name__)
@app.route('/' )
def index():
    return render_template('index.html')
@app.route('/cmd', methods=['GET'])
def cmd():
    data = request.args.get('livecmd')
    print(type(data))
    output = subprocess.getoutput(data)
    return output
@app.route('/run', methods=['GET'])
def run():
    cname = request.args.get('cname')
    cimage= request.args.get('cimage')
    command = "docker run -dit --name " + cname + " " + cimage
    print(type(command))
    output = subprocess.getoutput(command)
    return output
@app.route('/ps', methods=['GET'])
def ps():
    commnad = "docker ps | tail -n +2"
    output = subprocess.getoutput(commnad)
    return output
@app.route('/cpullos', methods=['GET'])
def cpullos():
    image_name = request.args.get('cpullos')
    commnad = "docker pull " + image_name
    output = subprocess.getoutput(commnad)
    return output
@app.route("/allpulledimages", methods=['GET'])
def allpulledimages():
    command = "docker images"
    output = subprocess.getoutput(command)
    return output
@app.route('/del', methods=['GET'])
def delete():
    image_name = request.args.get('cdname')
    command = "docker stop " + image_name
    output = subprocess.getoutput(command)
    return output
@app.route('/deleteall', methods=['GET'])
def deleteall():
    command = "docker rm -f $(docker ps -a -q)"
    output = subprocess.getoutput(command)
    return output
@app.route('/cidelete', methods =['GET'])
def cidelete():
    image_name = request.args.get('cidelete')
    command = "docker rmi -f " + image_name
    output = subprocess.getoutput(command)
    return output
if __name__ == '__main__':
    app.run(debug=True)