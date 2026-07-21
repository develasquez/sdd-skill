# Specification-Driven Development (SDD) - Core Principles

## The Power Inversion

For decades in software engineering, **code was king**. Specifications served code—they were disposable scaffolding built before coding and abandoned shortly after. As projects evolved, code became the sole source of truth, while documentation decayed into well-intentioned fiction.

**Spec-Driven Development (SDD)** inverts this power dynamic:
> **Specifications don't serve code — code serves specifications.**

The Product Requirements Document (PRD) and technical specifications are not passive guidelines; they are executable blueprints that dictate and generate implementation. Maintaining software means evolving specifications. Debugging means fixing specifications or plans that allowed incorrect code generation. Refactoring means restructuring specifications for clarity.

---

## Core Dogmas of SDD

1. **Specifications as Lingua Franca**:
   Natural language specifications, architectural principles, and domain models are the primary engineering artifacts. Code is an output transformation into a specific language, framework, or runtime.

2. **Intent-Driven Development**:
   Developers express intent, business goals, acceptance scenarios, and constraints. AI coding agents handle the mechanical translation from intent to working software.

3. **Executable Specifications**:
   Specifications must be precise, complete, and unambiguous enough to drive implementation without guesswork. Missing decisions are explicitly flagged with `[NEEDS CLARIFICATION]`.

4. **Zero-Gap Engineering**:
   Traditional gaps between product requirements, architecture plans, task lists, and source code are eliminated by establishing direct lineage and cross-artifact consistency checks.

5. **MVP-First Story Slicing**:
   User journeys are prioritized (P1, P2, P3). User Story 1 (P1) represents an independently testable, minimal viable slice of value. Every subsequent story builds incrementally on top.

6. **Continuous Alignment**:
   If production realities or code refactoring alter system behavior, documentation and specs are brought back into alignment via convergence workflows.
