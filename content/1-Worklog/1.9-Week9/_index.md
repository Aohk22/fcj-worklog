---
title: "Week 9 Worklog"
date: "`r Sys.Date()`"
weight: 1
chapter: false
pre: " <b> 1.9. </b> "
---

### Week 9 Objectives

- Rewrite frontend application using Bun runtime
- Improve user interface for malware analysis reports
- Implement automated report parsing utilities

### Tasks and Achievements

|Task|Start Date|Completion Date|Reference Material|
| --- | --- | --- | --- |
|Migrate frontend to Bun runtime:<br/>- Restructure project dependencies<br/>- Update build scripts and configuration<br/>- Test compatibility with existing APIs<br/>|31-10-2025|01-11-2025|https://bun.sh/<br/>https://bun.sh/docs<br/>|
|Implement UI enhancements:<br/>- Add scrolling for decompiled code section<br/>- Add scrolling for extracted strings section<br/>- Improve report layout and readability<br/>|02-11-2025|03-11-2025||
|Develop automated report parsing utilities:<br/>- Create objectWalk() function for recursive traversal<br/>- Implement headerize() for camelCase to Title Case conversion<br/>- Organize utilities in util.js module<br/>|03-11-2025|05-11-2025|https://github.com/Aohk22/fcj-1-file-analyzer/blob/main/srvc_web/app/util.js|

### Comments

#### Frontend Migration to Bun

Completed a full rewrite of the frontend application using Bun, a modern JavaScript runtime that offers significant performance improvements over traditional Node.js. Bun provides:
- Faster startup times and reduced memory footprint
- Built-in bundler, transpiler, and package manager
- Native TypeScript support without additional configuration
- Improved developer experience with faster hot reload

The migration involved restructuring the project dependencies, updating build scripts, and ensuring compatibility with existing API integrations. The new Bun-based frontend demonstrates noticeably faster load times and improved responsiveness.

#### User Interface Enhancements

Implemented critical UI improvements to enhance the user experience when viewing malware analysis reports:

**Scrolling for Decompiled Code**:
Added scrollable containers for the decompiled code section. Since Ghidra decompilation can generate thousands of lines of pseudocode, displaying everything at once was impractical and caused browser performance issues. The new scrollable view:
- Limits initial viewport to a manageable height
- Maintains code formatting and syntax
- Provides smooth scrolling for large codebases
- Improves page load performance by virtualizing content rendering

**Scrolling for Extracted Strings**:
Similarly implemented scrollable containers for the strings section. Binary files often contain thousands of extracted strings, making them difficult to navigate. The scrollable strings view:
- Organizes strings in a clean, readable format
- Allows users to quickly scan through large string collections
- Maintains search functionality within the scrollable area
- Improves overall report readability

#### Automated Report Parsing Solution

Addressed a significant development pain point: manually parsing large, nested report objects from the analysis API was becoming increasingly tedious and error-prone. As the analysis capabilities expanded, the report structure grew more complex with deeply nested objects containing PE sections, ELF headers, symbol tables, and various metadata.

