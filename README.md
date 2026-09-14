# ELECTROGRUP-SA-PYTHON-SCRAPER

[![Oportunitati si Cariere](https://github.com/elenab01234/ELECTROGRUP-SA-PYTHON-SCRAPER/actions/workflows/job-seeker-ro-spider.yml/badge.svg)](https://github.com/elenab01234/ELECTROGRUP-SA-PYTHON-SCRAPER/actions/workflows/job-seeker-ro-spider.yml)
[![Automation Tests](https://github.com/elenab01234/ELECTROGRUP-SA-PYTHON-SCRAPER/actions/workflows/automation-testing.yml/badge.svg)](https://github.com/elenab01234/ELECTROGRUP-SA-PYTHON-SCRAPER/actions/workflows/automation-testing.yml)

**job_seeker_ro_spider** — a Python scraper for ELECTROGRUP S.A. jobs in Romania. It collects the announcements published on the group's [applytojob board](https://electrogrup.applytojob.com) and publishes them to [peviitor.ro](https://peviitor.ro) through the Peviitor API.

> **🌱 Derived scraper.** This repository is derived from the [**Python template**](https://github.com/ale23yfm/e-infra-sa-python-scraper), the reference implementation for Python scrapers in the peviitor.ro ecosystem.

## Overview

The project automates the daily collection of ELECTROGRUP S.A. jobs in Romania, keeping the peviitor.ro board up to date with the latest career opportunities.

## Features

- Extracts jobs from the ELECTROGRUP group applytojob board (`?department=ELECTROGRUP SA` filter)
- Additional ANOFM jobs via CIF
- Validates the company via ANAF (CUI, active/inactive status, full address) with CUIScan fallback
- **ANAF cache** — does not hit the APIs on every scrape
- **Stale cache / config fallback** when ANAF is unavailable
- Cross-validates against the Peviitor API
- Deletes stale jobs (present on the site but not in Peviitor)
- Stores to the Peviitor API (job core + company core)
- Generates `docs/jobs.md` automatically — accessible on GitHub Pages
- **Company identity in a single file** (`scraper/config/company.json`)
- GitHub Actions: daily scrape + automated testing (unit, integration, e2e, consistency)
- Identifies itself through the User-Agent: `job_seeker_ro_spider`

## License

Copyright (c) 2026 Alexandra Ifrim

Licensed under the [MIT License](LICENSE).

## Managed By

This project is managed by [ASOCIATIA OPORTUNITATI SI CARIERE](https://oportunitatisicariere.ro) and used as a web scraper for the [peviitor.ro](https://peviitor.ro) job board project.

## Disclaimer

This scraper is designed for educational purposes and legitimate job data aggregation for the Romanian job market.