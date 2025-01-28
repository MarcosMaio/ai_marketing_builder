import json
import os
import re

def clean_agent_output(value):
    pattern = r'```json\s*([\s\S]+?)```'
    match = re.search(pattern, value)
    
    if match:
        json_str = match.group(1).strip()
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            pass
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def save_strategy_briefing(
    strategy_briefing_result, output_filename="company_strategy_briefing.json"
):
    try:
        os.makedirs("company_data", exist_ok=True)
        file_path = os.path.join("company_data", output_filename)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(strategy_briefing_result, file, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Error creating directory: {e}")
        

def get_specific_file_data(folder, file):
    try:
        file_path = os.path.join(folder, file)
        if not os.path.exists(file_path):
            return {}

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return content

    except Exception as e:
        print(f"Error get directory data: {e}")
        return {}