---
description: Rules for READMEs, specs, skills, and user-facing text
globs: ["**/*.md", "**/*.mdx"]
alwaysApply: false
---
# Docs rules

- Lead with what the reader can do, then how. First paragraph answers "what is this and why should I care".
- Every instruction is runnable: real commands, real paths, expected output where it matters.
- One idea per sentence. Cut filler ("simply", "just", "robust", "seamless", "leverage").
- Use tables for comparisons and checklists for gates. Use mermaid for flows, not screenshots.
- Specs separate locked decisions from open questions, and list non-goals.
- Skills follow the Agent Skills spec: `name` equals the folder slug, `description` says what it does and when to use it. Run `agent-skill-spec-check`.
- No secrets, internal hostnames, personal contact details, or private project names in anything that might be published. Run the `guardrails/public-safety.md` checklist.
- Dates are absolute (2026-11-02), never "last week".
- Update docs in the same PR as the behavior they describe.
