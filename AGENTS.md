# Repository Guidelines

## Project Structure & Module Organization
The Rust core lives in `src/`, where `lib.rs` registers the Python module and `exposure.rs` implements the atomic types exported to Python. Type hints for downstream users sit in `atomicx.pyi`; update this stub alongside any API changes. Python-facing regression tests reside in `tests/`, driven by `pytest`. Packaging and release metadata is split between `Cargo.toml` for the Rust crate and `pyproject.toml` for the maturin build backend. Reference usage notes in `DOCS.md` when adjusting behavior or examples.

## Build, Test, and Development Commands
- `maturin develop --release`: build the extension and install it into the active virtualenv for local iteration.
- `maturin build --release`: produce distributable wheels; run before publishing.
- `pytest tests -q`: execute the Python interoperability suite; use `-k` to target specific atom types during triage.
- `cargo fmt` / `cargo clippy --all-targets -- -D warnings`: enforce Rust formatting and lint the CDylib before opening a PR.

## Coding Style & Naming Conventions
Rust follows edition 2021 defaults: 4-space indentation, `snake_case` for functions, and `CamelCase` for PyO3 classes. Prefer explicit `SeqCst` ordering for new atomic operations to match existing semantics. Keep docstrings and Python examples concise and in imperative mood. When updating APIs, mirror signatures and docstrings in `atomicx.pyi` and ensure public methods stay annotated.

## Testing Guidelines
Add new scenarios under `tests/` using `test_*` functions or `Test*` classes so `pytest` auto-discovers them. Cover both happy paths and contention cases; stress concurrent behavior with thread pools when feasible. Run `pytest -n auto` (via `pytest-xdist`, optional) to validate thread-safety under parallel scheduling. When touching Rust internals, add targeted unit tests or assert-based checks in Python to capture regressions in atomic semantics.

## Commit & Pull Request Guidelines
Keep commits small and present-tense, echoing the existing history (`add float div guard`, `bump version`). Reference related issues in the commit body if context is non-obvious. PRs should include: a concise summary of the change surface, verification notes (`pytest`, `maturin develop`), and any relevant benchmarks or screenshots from docs. Request review once CI passes and the branch rebases cleanly on `main`.
