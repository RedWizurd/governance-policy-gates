import json
from pathlib import Path


def require_keys(path: Path, keys: set[str]) -> None:
    data = json.loads(path.read_text())
    missing = keys - set(data.keys())
    if missing:
        raise ValueError(f"{path.name} missing keys: {sorted(missing)}")


def main() -> None:
    require_keys(Path("memory_policy.json"), {"session_scope", "retention", "max_events"})
    require_keys(Path("approval_policy.json"), {"tiers"})
    require_keys(Path("risk_policy.json"), {"risky_actions", "require_flag", "flag_name"})
    print("Policy files valid")


if __name__ == "__main__":
    main()
