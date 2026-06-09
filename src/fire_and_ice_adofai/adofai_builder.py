import json


def build_adofai_dict(angle_data, bpm, offset, song):
    return {"angleData": angle_data, "settings": {"version": 15, "song": song, "bpm": bpm, "offset": int(offset * 1000)}, "actions": []}


def write_adofai(path, angle_data, bpm, offset, song):
    data = build_adofai_dict(angle_data, bpm, offset, song)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
