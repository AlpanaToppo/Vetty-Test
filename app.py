# app.py

from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def read_file():
    filename = request.args.get('file', 'file1.txt')
    start_line = request.args.get('start_line')
    end_line = request.args.get('end_line')

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if start_line and end_line:
                start_line = int(start_line)
                end_line = int(end_line)
                lines = lines[start_line-1:end_line]
            content = ''.join(lines)
            return render_template('index.html', content=content)
    except FileNotFoundError:
        return render_template('error.html', error='File not found.')
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
