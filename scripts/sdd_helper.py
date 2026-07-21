#!/usr/bin/env python3
"""
SDD Helper Utility
Cross-platform Python helper for Spec-Driven Development (SDD) workflows.
Zero external dependencies (uses standard library only).
"""

import sys
import os
import re
import json
import shutil
import argparse
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(SCRIPT_DIR)
TEMPLATES_DIR = os.path.join(SKILL_ROOT, "templates")

def get_next_feature_prefix(specs_dir="specs"):
    os.makedirs(specs_dir, exist_ok=True)
    existing_nums = []
    pattern = re.compile(r"^(\d+)-")
    for item in os.listdir(specs_dir):
        if os.path.isdir(os.path.join(specs_dir, item)):
            match = pattern.match(item)
            if match:
                existing_nums.append(int(match.group(1)))
    next_num = max(existing_nums) + 1 if existing_nums else 1
    return f"{next_num:03d}"

def sanitize_slug(name):
    slug = name.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "feature"

def init_feature(name, specs_dir="specs"):
    prefix = get_next_feature_prefix(specs_dir)
    slug = sanitize_slug(name)
    dir_name = f"{prefix}-{slug}"
    feature_dir = os.path.abspath(os.path.join(specs_dir, dir_name))
    os.makedirs(feature_dir, exist_ok=True)

    spec_file = os.path.join(feature_dir, "spec.md")
    template_file = os.path.join(TEMPLATES_DIR, "spec-template.md")

    if os.path.exists(template_file):
        with open(template_file, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("[FEATURE NAME]", name.title())
        content = content.replace("[###-feature-name]", dir_name)
        content = content.replace("[DATE]", datetime.now().strftime("%Y-%m-%d"))
        content = content.replace("$ARGUMENTS", name)
        with open(spec_file, "w", encoding="utf-8") as f:
            f.write(content)

    result = {
        "status": "success",
        "feature_number": prefix,
        "feature_slug": slug,
        "branch_name": dir_name,
        "feature_dir": feature_dir,
        "spec_file": spec_file
    }
    return result

def setup_plan(feature_dir):
    feature_dir = os.path.abspath(feature_dir)
    spec_file = os.path.join(feature_dir, "spec.md")
    plan_file = os.path.join(feature_dir, "plan.md")
    template_file = os.path.join(TEMPLATES_DIR, "plan-template.md")

    if not os.path.exists(spec_file):
        return {"status": "error", "message": f"spec.md not found in {feature_dir}"}

    dir_name = os.path.basename(feature_dir)
    if os.path.exists(template_file):
        with open(template_file, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("[FEATURE]", dir_name)
        content = content.replace("[###-feature-name]", dir_name)
        content = content.replace("[DATE]", datetime.now().strftime("%Y-%m-%d"))
        with open(plan_file, "w", encoding="utf-8") as f:
            f.write(content)

    return {
        "status": "success",
        "feature_dir": feature_dir,
        "spec_file": spec_file,
        "plan_file": plan_file
    }

def setup_tasks(feature_dir):
    feature_dir = os.path.abspath(feature_dir)
    plan_file = os.path.join(feature_dir, "plan.md")
    tasks_file = os.path.join(feature_dir, "tasks.md")
    template_file = os.path.join(TEMPLATES_DIR, "tasks-template.md")

    if not os.path.exists(plan_file):
        return {"status": "error", "message": f"plan.md not found in {feature_dir}"}

    dir_name = os.path.basename(feature_dir)
    if os.path.exists(template_file):
        with open(template_file, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("[FEATURE NAME]", dir_name)
        content = content.replace("[###-feature-name]", dir_name)
        with open(tasks_file, "w", encoding="utf-8") as f:
            f.write(content)

    return {
        "status": "success",
        "feature_dir": feature_dir,
        "plan_file": plan_file,
        "tasks_file": tasks_file
    }

def check_prerequisites(feature_dir, require_plan=False, require_tasks=False):
    feature_dir = os.path.abspath(feature_dir)
    spec_file = os.path.join(feature_dir, "spec.md")
    plan_file = os.path.join(feature_dir, "plan.md")
    tasks_file = os.path.join(feature_dir, "tasks.md")

    docs = []
    if os.path.exists(spec_file): docs.append("spec.md")
    if os.path.exists(plan_file): docs.append("plan.md")
    if os.path.exists(tasks_file): docs.append("tasks.md")

    missing = []
    if not os.path.exists(spec_file): missing.append("spec.md")
    if require_plan and not os.path.exists(plan_file): missing.append("plan.md")
    if require_tasks and not os.path.exists(tasks_file): missing.append("tasks.md")

    return {
        "status": "error" if missing else "success",
        "feature_dir": feature_dir,
        "available_docs": docs,
        "missing_docs": missing
    }

def main():
    parser = argparse.ArgumentParser(description="SDD Helper Utility")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init-feature
    init_parser = subparsers.add_parser("init-feature")
    init_parser.add_argument("name", help="Feature name or description")
    init_parser.add_argument("--specs-dir", default="specs", help="Base specs directory")

    # setup-plan
    plan_parser = subparsers.add_parser("setup-plan")
    plan_parser.add_argument("feature_dir", help="Path to feature directory")

    # setup-tasks
    tasks_parser = subparsers.add_parser("setup-tasks")
    tasks_parser.add_argument("feature_dir", help="Path to feature directory")

    # check-prerequisites
    check_parser = subparsers.add_parser("check-prerequisites")
    check_parser.add_argument("feature_dir", help="Path to feature directory")
    check_parser.add_argument("--require-plan", action="store_true")
    check_parser.add_argument("--require-tasks", action="store_true")

    args = parser.parse_args()

    if args.command == "init-feature":
        res = init_feature(args.name, args.specs_dir)
    elif args.command == "setup-plan":
        res = setup_plan(args.feature_dir)
    elif args.command == "setup-tasks":
        res = setup_tasks(args.feature_dir)
    elif args.command == "check-prerequisites":
        res = check_prerequisites(args.feature_dir, args.require_plan, args.require_tasks)
    else:
        res = {"status": "error", "message": "Unknown command"}

    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
