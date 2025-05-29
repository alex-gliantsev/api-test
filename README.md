# API Test Automation project

## 1. Introduction
This repository contains a lightweight Python-based API test automation project built with pytest and requests. It demonstrates core concepts and best practices of API testing, including structured test organization, reusable request handlers, and response validation.

The project targets the demo service at [restful-api.dev](https://api.restful-api.dev/) and covers typical CRUD (Create, Read, Update, Delete) operations. It is intended as a practical showcase of API test automation skills and a starting point for extending into more complex scenarios.

## 2. Project Goal
The primary objective is to showcase foundational abilities in API test automation, including:
*   Designing and implementing automated API tests.
*   Structuring a test project logically.
*   Utilizing common testing libraries and patterns.
*   Implementing schema validation and data management.
*   Generating clear test reports.

## 3. Key Features
*   **CRUD Operations Coverage:** Tests for POST, GET, PUT, PATCH, and DELETE endpoints.
*   **Schema Validation:** Ensures API responses adhere to expected JSON structures.
*   **Reusable API Clients:** Modular design with a base API client and specific endpoint handlers.
*   **Pytest Fixtures:** Manages test setup (e.g., creating test data) and teardown (e.g., cleanup).
*   **Dynamic Data Handling:** Uses helpers for payload generation and unique ID generation for negative testing.
*   **Allure Reporting:** Integrated for clear and interactive test execution reports.

## 4. Technologies Used
*   **Python 3.x**
*   **Pytest:** Core testing framework.
*   **Requests:** For HTTP API interactions.
*   **jsonschema:** For response schema validation.
*   **Allure Pytest:** For report generation.

## 5. Running Tests & Viewing Reports
Tests are executed using Pytest. After test execution, Allure can be used to generate and view an HTML report.

**pytest.ini configuration includes:**
`addopts = -s -v -ra --tb=short --colour=yes --alluredir=./allure-results --clean-alluredir`

This configuration enables verbose output, short tracebacks, colored output, and specifies the Allure results directory, ensuring it's cleaned before each run.
