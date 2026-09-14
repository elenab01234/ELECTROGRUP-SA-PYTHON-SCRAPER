# Contributing

Thank you for your interest in contributing to the ELECTROGRUP S.A. Python
Scraper. This project is part of the peviitor.ro ecosystem and follows its
conventions.

## How to contribute

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Run the fast test suite (no network required):

   ```bash
   python3 -m pytest tests/unit tests/consistency
   ```

5. Commit and push, then open a pull request.

## What to work on

- Bug fixes and improvements to the scraper logic in `scraper/index.py`.
- Location/workmode normalization improvements.
- Additional test coverage.
- Documentation updates.

## Do NOT

- Modify the shared template modules: `scraper/api.py`, `scraper/anaf.py`,
  `scraper/company.py`, `scraper/job_validator.py`,
  `scraper/markdown_generator.py`, `scraper/validate_jobs.py`.
- Commit generated artifacts (`scraper/jobs.json`, `scraper/anaf_cache.json`).
- Commit any secrets or credentials.