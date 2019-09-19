SCRIPT_DIR=$(cd $(dirname $0); pwd)
cd "$SCRIPT_DIR"
pip3 install -r pip3_freeze.txt
python3 download_html.py https://docs.python.org/ja/3/ "${SCRIPT_DIR%/}/index.html"

