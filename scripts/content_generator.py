#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""爆款内容生成引擎
作者: user_7400cfba 版本: 1.0.0"""
import argparse, json, random, sys
from datetime import datetime

XHS_TITLES = [
    "🔥 {topic}？{n}个方法帮你搞定",
    "✨ {topic}必看！真的太好用了",
    "📌 后悔没早知道的{topic}技巧",
    "⭐ {n}年经验分享：{topic}",
    "💡 被问爆的{topic}，今天说清楚",
]
DOUYIN_TITLES = [
    "{n}秒学会{topic}！",
    "千万别错过这个{topic}技巧！",
    "{topic}？一个方法搞定！",
    "花了大价钱买的{topic}教训",
    "挑战{topic}！结果没想到...",
]

def generate_xhs(topic, audience, style="种草"):
    titles = [t.replace("{topic}", topic).replace("{n}", str(random.randint(3,10))) for t in random.sample(XHS_TITLES, 5)]
    return {"platform": "小红书", "topic": topic, "audience": audience,
            "titles": titles, "hashtags": [f"#{topic}推荐", f"#{topic}攻略", "#干货分享"],
            "cover": f"3:4竖版，含{topic}关键词"}

def generate_douyin(topic, audience, style="教程"):
    titles = [t.replace("{topic}", topic).replace("{n}", str(random.randint(3,10))) for t in random.sample(DOUYIN_TITLES, 5)]
    return {"platform": "抖音", "topic": topic, "audience": audience,
            "titles": titles, "hashtags": [f"#{topic}教程", "#涨知识", "#fyp"],
            "script": {"hook": f"前3秒：你知道{topic}吗？", "body": "分点列举", "cta": "评论区告诉我"}}

def main():
    parser = argparse.ArgumentParser(description="爆款内容生成")
    parser.add_argument("--type", choices=["xhs", "douyin"], required=True)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--audience", default="通用")
    parser.add_argument("--style", default="种草")
    args = parser.parse_args()
    if args.type == "xhs": r = generate_xhs(args.topic, args.audience, args.style)
    else: r = generate_douyin(args.topic, args.audience, args.style)
    print(json.dumps(r, ensure_ascii=False, indent=2))

if __name__ == "__main__": main()