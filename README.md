# Energy Map

Energy Map identifies energy-hungry software modules by combining:

- energy measurements (RAPL)
- testcase execution
- static analysis (AST)

## Current Scope

1. Run testcases
2. Measure energy consumption
3. Map testcases to modules
4. Compute energy statistics per module

## Architecture

Backend:
- energy measurement
- test runner
- static analysis
- aggregation

Frontend:
- visualization dashboard