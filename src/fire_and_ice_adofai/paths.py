from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def external_root() -> Path:
    root = project_root()
    nested = root / "fire_and_ice_adofai_project" / "external"
    if nested.exists():
        return nested
    return root / "external"


def llamafactory_path() -> Path:
    return external_root() / "LLaMA-Factory"


def mug_diffusion_path() -> Path:
    return external_root() / "Mug-Diffusion"
