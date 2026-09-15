#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""数据复盘分析引擎
作者: user_7400cfba 版本: 1.0.0"""
import argparse, json, sys
from datetime import datetime

BENCHMARKS = {
    "xhs": {"click_rate": {"excellent": 0.10, "good": 0.06, "poor": 0.03},
            "interaction_rate": {"excellent": 0.05, "good": 0.03, "poor": 0.015}},
    "douyin": {"completion_rate": {"excellent": 0.40, "good": 0.25, "poor": 0.15},
               "interaction_rate": {"excellent": 0.08, "good": 0.04, "poor": 0.02}},
}
DIAGNOSIS = {
    "xhs": {"low_click": "封面或标题吸引力不足 → 优化封面+标题关键词",
            "low_interaction": "内容质量或互动引导不足 → 增加干货密度+互动引导",
            "low_exposure": "账号权重低或标签不精准 → 确保内容垂直度+SEO优化"},
    "douyin": {"low_completion": "前3秒钩子不够强 → 重写开头+加快节奏",
               "low_interaction": "缺少互动引导 → 设置争议点+引导评论",
               "low_exposure": "未通过初始流量池 → 确保前5条视频高度垂直"},
}

def analyze(platform, impressions=0, clicks=0, likes=0, saves=0, comments=0, shares=0, followers=0):
    bench = BENCHMARKS.get(platform, BENCHMARKS["xhs"])
    diag = DIAGNOSIS.get(platform, DIAGNOSIS["xhs"])
    metrics = {}
    if impressions > 0:
        metrics["click_rate"] = round(clicks / impressions, 4) if clicks else 0
        metrics["interaction_rate"] = round((likes + saves + comments) / impressions, 4)
    result = {"platform": platform, "metrics": metrics, "benchmarks": bench,
              "diagnosis": diag, "summary": f"数据已分析，请参考诊断建议"}
    return result

def main():
    parser = argparse.ArgumentParser(description="数据复盘分析")
    parser.add_argument("--platform", default="xhs")
    parser.add_argument("--impressions", type=float, default=0)
    parser.add_argument("--clicks", type=float, default=0)
    parser.add_argument("--likes", type=float, default=0)
    parser.add_argument("--saves", type=float, default=0)
    parser.add_argument("--comments", type=float, default=0)
    parser.add_argument("--shares", type=float, default=0)
    parser.add_argument("--followers-gained", type=float, default=0)
    args = parser.parse_args()
    r = analyze(args.platform, args.impressions, args.clicks, args.likes,
                args.saves, args.comments, args.shares, args.followers_gained)
    print(json.dumps(r, ensure_ascii=False, indent=2))

if __name__ == "__main__": main()