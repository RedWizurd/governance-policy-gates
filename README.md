# governance-policy-gates

Enforces governance policies with JSON configs, HITL approval tiers, risky-operation gates, and session-scoped state controls.

## Purpose
Apply strict policy guardrails to agent behavior, especially for high-impact actions, using auditable configuration.

## Features
- JSON-defined governance rules and memory constraints.
- HITL approval tiers for escalating actions.
- Risk flags for sensitive operations (for example: `--approve-risky`).
- Session-scoped state boundaries to minimize retained data.
- Policy checks for writes, external claims, and action classes.

## Config
- `memory_policy.json`: Session state and retention boundaries.
- `approval_policy.json`: HITL tiers and approval requirements.
- `risk_policy.json`: Action risk categories and enforced gates.
- `POLICY_STRICT_MODE`: Enables fail-closed behavior when checks fail.
- `REQUIRE_RISK_APPROVAL_FLAG`: Enforces explicit runtime risk approval flag.

## Quickstart
```bash
cp memory_policy.example.json memory_policy.json
cp approval_policy.example.json approval_policy.json
python3 validate_policies.py
python3 agent.py --mode builder --approve-risky=false
```

## Usage
```bash
make setup
make check
make run
```

## Roadmap
- Add policy decision explainers for operator transparency.
- Add signed policy bundles for deployment integrity.
- Add per-tenant policy overlays.
- Add governance regression test suite.
