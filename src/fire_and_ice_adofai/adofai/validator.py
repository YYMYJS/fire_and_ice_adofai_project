import json


def validate_adofai(path: str) -> list[str]:
    try:
        data = json.loads(open(path, encoding="utf-8-sig").read())
    except Exception as exc:
        return ["invalid json: " + str(exc)]
    angles = data.get("angleData")
    if not isinstance(angles, list):
        return ["missing angleData list"]
    for angle in angles:
        if not isinstance(angle, (int, float)):
            return ["angleData contains non-number"]
    return []
