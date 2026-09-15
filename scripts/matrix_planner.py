#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""账号矩阵规划引擎
作者: user_7400cfba 版本: 1.0.0"""
import argparse, json, sys
from datetime import datetime

INDUSTRIES = {
    "美妆": ["测评号", "教程号", "种草号", "护肤号"],
    "母婴": ["育儿号", "好物号", "辅食号", "孕期号"],
    "美食": ["教程号", "探店号", "零食号", "地域号"],
    "数码": ["测评号", "教程号", "性价比号", "行业号"],
    "通用": ["知识号", "种草号", "教程号", "生活号"],
}

def plan_matrix(industry, accounts, platforms, goal, team_size):
    directions = INDUSTRIES.get(industry, INDUSTRIES["通用"])[:accounts]
    return {
        "industry": industry, "accounts": accounts, "goal": goal,
        "team_size": team_size, "platforms": platforms.split(","),
        "plan": [{"name": f"{d}", "direction": d, "frequency": "3-5篇/周"} for d in directions],
        "phases": ["冷启动期(1-2月)", "成长期(3-6月)", "成熟期(6月+)"],
    }

def main():
    parser = argparse.ArgumentParser(description="矩阵规划引擎")
    sub = parser.add_subparsers(dest="cmd")
    p = sub.add_parser("plan")
    p.add_argument("--industry", default="通用")
    p.add_argument("--accounts", type=int, default=3)
    p.add_argument("--platforms", default="xhs,douyin")
    p.add_argument("--goal", default="brand_exposure")
    p.add_argument("--team-size", type=int, default=2)
    args = parser.parse_args()
    if args.cmd == "plan":
        r = plan_matrix(args.industry, args.accounts, args.platforms, args.goal, args.team_size)
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else: parser.print_help()

if __name__ == "__main__": main()