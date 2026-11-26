import os
import json
import urllib.request
import urllib.error

def load_env(env_path=None):
    """
    Lightweight zero-dependency .env loader.
    """
    if env_path is None:
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
        env_path = os.path.join(root_dir, ".env")
    
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if key and key not in os.environ:
                        os.environ[key] = val
    return os.environ

def get_typesafe_client():
    """
    Returns API key and endpoint configuration for TypeSafe Jev.
    """
    load_env()
    api_key = os.environ.get("TYPESAFE_API_KEY", "")
    endpoint = os.environ.get("TYPESAFE_ENDPOINT", "https://api.typesafe.ai/v1")
    return {
        "api_key": api_key,
        "endpoint": endpoint,
        "is_configured": bool(api_key.strip())
    }

def call_typesafe_classifier(text_prompt, system_instruction=None, model="jev-fast"):
    """
    Sends a classification/decision request to TypeSafe Jev API.
    """
    config = get_typesafe_client()
    if not config["is_configured"]:
        return {
            "success": False,
            "error": "TYPESAFE_API_KEY is not set in .env. Falling back to local evaluator."
        }
    
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": []
    }
    if system_instruction:
        payload["messages"].append({"role": "system", "content": system_instruction})
    payload["messages"].append({"role": "user", "content": text_prompt})
    
    req = urllib.request.Request(
        f"{config['endpoint']}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {"success": True, "data": data}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        return {"success": False, "status": e.code, "error": err_body}
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    client = get_typesafe_client()
    print("TypeSafe Client Status:")
    print("  Configured:", client["is_configured"])
    print("  Endpoint:  ", client["endpoint"])
    if client["api_key"]:
        masked = client["api_key"][:4] + "..." + client["api_key"][-4:]
        print("  API Key:   ", masked)
    else:
        print("  API Key:    [NOT SET in .env]")
