@echo off
REM Update the graphify knowledge graph for the whole workspace.
REM AST-only re-extraction: no LLM calls, no API cost.
REM Run after code changes; safe to run anytime.

cd /d "%~dp0"

graphify update .
if errorlevel 1 (
    echo.
    echo [update_graph] graphify update FAILED. If code was deleted or heavily
    echo [update_graph] refactored, retry with: graphify update . --force
    exit /b 1
)

echo.
echo [update_graph] Graph updated: %~dp0graphify-out\graph.json
