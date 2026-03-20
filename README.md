# DepressionResearch

## Overview

DepressionResearch is a project focused on building a research-ready dataset from public CDC NHANES data in order to study associations between depression-related questionnaire responses and biological, chemical, and laboratory measurements.

The current goal is to identify, download, organize, and prepare public NHANES datasets that can be linked at the participant level for later statistical analysis.

## Current Work

At this stage, the project is focused on:

- scraping and collecting NHANES questionnaire dataset links
- downloading public `.xpt` files from CDC NHANES pages
- automatically generating filenames from NHANES URLs
- converting `.xpt` files into `.csv`
- identifying which NHANES files can be linked together
- determining which public variables are useful for depression-related research

## Research Idea

The main research direction is to explore whether depression symptoms are associated with:

- laboratory biomarkers
- chemical exposure measurements
- inflammatory markers
- metabolic indicators
- nutritional markers
- demographic and lifestyle factors

The depression outcome currently comes from the NHANES PHQ-9 depression screener file, not a formal clinical diagnosis in the more recent public cycles.

## Data Source

Primary source:

- CDC NHANES public datasets

These datasets can often be linked using the participant identifier:

- `SEQN`

This makes it possible to combine, for the same individual:

- questionnaire data
- laboratory data
- chemical exposure data
- body measurements
- demographic variables
- lifestyle variables

## Datasets of Interest

The project is currently centered around combining files such as:

- `DPQ_L` — depression screener
- `DEMO_L` — demographics and survey weights
- `BIOPRO_L` — biochemistry profile
- `CBC_L` — complete blood count
- `HSCRP_L` — inflammation marker
- `VID_L` — vitamin D
- `PBCD_L` — blood metals
- `BMX_L` — body measurements
- `ALQ_L` — alcohol use
- `PAQ_L` — physical activity
- `SMQ_L` — smoking
- `DR1TOT_L` — dietary intake totals

## Current Pipeline

The current workflow looks like this:

1. scrape NHANES dataset pages or construct dataset URLs
2. test possible dataset paths across multiple years
3. download available `.xpt` files
4. save files with automatic descriptive names
5. convert `.xpt` files to `.csv`
6. prepare datasets for merging by `SEQN`
7. build a larger analysis-ready table for research

## Why This Matters

NHANES provides a unique opportunity to study depression-related symptoms together with rich biological and exposure data in a large public health survey.

This project is intended to support downstream work such as:

- exploratory data analysis
- correlation analysis
- regression modeling
- biomarker screening
- feature selection
- hypothesis generation for depression-related research

## Current Limitations

A few important limitations are already known:

- recent NHANES public depression files use a screening questionnaire rather than a confirmed diagnosis
- some NHANES files are restricted and marked as RDC Only
- not every participant has every lab measurement
- merging many files may reduce the final sample size
- NHANES is cross-sectional, so associations should not be interpreted as proof of causation

## Next Steps

Planned next steps include:

- automate downloading across more NHANES cycles
- generate a structured inventory of available datasets
- merge selected public files by `SEQN`
- create a clean depression outcome variable
- inspect missingness and sample overlap
- build an analysis-ready dataset
- start statistical testing and visualization

## Project Status

This project is currently in the data collection and dataset construction phase.