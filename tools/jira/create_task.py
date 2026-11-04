import argparse
import os
import sys
import requests
from requests.auth import HTTPBasicAuth

# Đọc cấu hình từ file .env bằng python-dotenv
try:
    from dotenv import load_dotenv
except ImportError:
    print("Lỗi: Thiếu package python-dotenv. Chạy: pip install python-dotenv")
    sys.exit(1)

# Load .env từ tools/jira/.env hoặc fallback sang tools/confluence/.env
ENV_FILE = os.path.join(os.path.dirname(__file__), '.env')
if not os.path.exists(ENV_FILE):
    ENV_FILE = os.path.join(os.path.dirname(__file__), '..', 'confluence', '.env')
load_dotenv(ENV_FILE)


def get_credentials():
    """Đọc credentials từ environment variables (loaded từ .env)."""
    url = os.getenv('JIRA_URL', 'https://jira.vietinvoice.vn')
    username = os.getenv('JIRA_USERNAME', '') or os.getenv('CONFLUENCE_USERNAME', '')
    password = os.getenv('JIRA_PASSWORD', '') or os.getenv('CONFLUENCE_PASSWORD', '')
    return url, username, password


def create_jira_issue(project_key, summary, description, assignee, issuetype, ca_cert=None):
    base_url, username, password = get_credentials()

    if not username or not password:
        print(f"Lỗi: Không tìm thấy thông tin xác thực.")
        print(f"  Kiểm tra file .env tại: {ENV_FILE}")
        print(f"  Hoặc set environment variables: JIRA_USERNAME, JIRA_PASSWORD")
        return False

    api_url = f"{base_url}/rest/api/2/issue"
    auth = HTTPBasicAuth(username, password)

    payload = {
        "fields": {
            "project": {
                "key": project_key
            },
            "summary": summary,
            "description": description,
            "issuetype": {
                "name": issuetype
            }
        }
    }

    if assignee:
        payload["fields"]["assignee"] = {"name": assignee}

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # SSL verification: sử dụng CA bundle nếu cung cấp, mặc định verify=True
    verify = ca_cert if ca_cert else True

    try:
        response = requests.post(
            api_url, json=payload, headers=headers,
            auth=auth, verify=verify, timeout=15
        )
        if response.status_code == 201:
            data = response.json()
            issue_key = data.get('key')
            print(f"Task created successfully.")
            print(f"Key: {issue_key}")
            print(f"URL: {base_url}/browse/{issue_key}")
            return True
        else:
            print(f"Error: HTTP {response.status_code}")
            print(response.text)
            return False
    except requests.exceptions.SSLError as e:
        print(f"SSL Error: {e}")
        print("  Nếu server dùng self-signed cert, sử dụng --ca-cert /path/to/ca-bundle.crt")
        return False
    except Exception as e:
        print(f"Exception: {e}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tạo Jira Task từ command line")
    parser.add_argument('--project', required=True, help="Project Key (VD: XDA, HDDT)")
    parser.add_argument('--summary', required=True, help="Tiêu đề (Summary) của Task")
    parser.add_argument('--description', required=True, help="Mô tả chi tiết")
    parser.add_argument('--assignee', required=False, default="", help="Username người được gán (Assignee)")
    parser.add_argument('--issuetype', required=False, default="Task", help="Loại Issue (mặc định: Task)")
    parser.add_argument('--ca-cert', required=False, default=None,
                        help="Path to CA certificate bundle (cho self-signed cert)")

    args = parser.parse_args()

    ok = create_jira_issue(
        args.project, args.summary, args.description,
        args.assignee, args.issuetype, getattr(args, 'ca_cert', None)
    )
    sys.exit(0 if ok else 1)
