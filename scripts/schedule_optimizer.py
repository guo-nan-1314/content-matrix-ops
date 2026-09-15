#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""发布排期优化引擎
作者: user_7400cfba 版本: 1.0.0"""
import argparse, json, sys
from datetime import datetime

PEAKS = {
    "xhs": {"best_times": ["20:00-22:30", "12:00-14:00", "17:30-19:00"],
            "best_days": ["周二", "周三", "周四", "周日"],
            "freq": "每周3-5篇"},
    "douyin": {"best_times": ["20:00-22:00", "12:00-13:30", "18:00-19:30"],
               "best_days": ["周三", "周四", "周五", "周六", "周日"],
               "freq": "每天1-2条"},
}
CONTENT_MIX = {
    "xhs": {"干货教程": 35, "种草推荐": 25, "热点话题": 20, "互动问答": 10, "生活日常": 10},
    "douyin": {"教程技巧": 30, "种草测评": 25, "热点挑战": 20, "剧情段子": 15, "日常vlog": 10},
}

def optimize_schedule(platform, accounts, capacity, industry="通用"):
    p = PEAKS.get(platform, PEAKS["xhs"])
    mix = CONTENT_MIX.get(platform, CONTENT_MIX["xhs"])
    return {"platform": platform, "accounts": accounts, "capacity": capacity,
            "best_times": p["best_times"], "best_days": p["best_days"],
            "recommended_freq": p["freq"], "content_mix": mix,
            "tip": f"建议每周发布{capacity}篇，优先在{p['best_times'][0]}时段发布"}

def main():
    parser = argparse.ArgumentParser(description="排期优化引擎")
    parser.add_argument("--platform", default="xhs")
    parser.add_argument("--accounts", type=int, default=1)
    parser.add_argument("--weekly-capacity", type=int, default=5)
    parser.add_argument("--industry", default="通用")
    args = parser.parse_args()
    r = optimize_schedule(args.platform, args.accounts, args.weekly_capacity, args.industry)
    print(json.dumps(r, ensure_ascii=False, indent=2))

if __name__ == "__main__": main()