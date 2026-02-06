import argparse
import json


RISKY_OPERATIONS = {"write", "external_claim"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Governance-gated agent MVP")
    parser.add_argument("--mode", default="builder", choices=["chat", "builder", "researcher"])
    parser.add_argument("--approve-risky", default="false")
    parser.add_argument("--operation", default="read", choices=["read", "write", "external_claim"])
    args = parser.parse_args()

    approve_risky = str(args.approve_risky).lower() in {"1", "true", "yes", "on"}
    blocked = args.operation in RISKY_OPERATIONS and not approve_risky

    result = {
        "mode": args.mode,
        "operation": args.operation,
        "approve_risky": approve_risky,
        "allowed": not blocked,
        "reason": "Risky operation blocked without --approve-risky" if blocked else "Allowed by policy",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
