#!/usr/bin/env python3
"""Generate README.md from papers.yaml.

Usage:
    python scripts/build_readme.py          # rewrite README.md
    python scripts/build_readme.py --check  # exit 1 if README.md is out of date
"""
import argparse
import collections
import datetime
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "papers.yaml"
README = ROOT / "README.md"

VENUES = ["NeurIPS", "ICML", "ICLR", "KDD", "WWW", "AAAI", "IJCAI", "CIKM",
          "ICDM", "ICDE", "SIGIR", "WSDM", "ACL", "EMNLP"]

CATEGORIES = [
    ("forecasting", "Price Forecasting & Market Analysis",
     "Price, return and volatility forecasting, market simulation, and event or news analysis."),
    ("trading", "Trading & Portfolio Management",
     "RL and LLM trading agents, high-frequency trading, portfolio management and arbitrage."),
    ("fraud", "Fraud, Scam & Attack Detection",
     "Phishing, scams, rug pulls, money laundering, wash trading, bots and attack transactions."),
    ("onchain", "On-chain Transaction & Graph Analytics",
     "Address clustering, account classification, de-anonymization and transaction graph learning."),
    ("defi", "DeFi, MEV & Market Mechanisms",
     "AMMs and liquidity, MEV and block building, transaction fee mechanisms and token incentives."),
    ("web3", "NFT, DAO & Web3 Ecosystem",
     "NFT markets, DAO governance, memecoins, decentralized identity and naming services."),
    ("smart-contract", "Smart Contract Security & Analysis",
     "Vulnerability detection, program analysis, decompilation, code generation and auditing agents."),
    ("systems", "Blockchain Systems & Infrastructure",
     "Sharding, consensus, transaction execution, storage and query processing, P2P and cross-chain security."),
    ("survey", "Surveys, Tutorials & Workshops",
     "Surveys, tutorials and workshop summaries held at the covered conferences."),
]
CAT_TITLE = {k: t for k, t, _ in CATEGORIES}

TRACK_LABEL = {
    "main": "", "short": "Short", "companion": "Companion", "workshop": "Workshop",
    "D&B": "D&B", "findings": "Findings", "industry": "Industry", "demo": "Demo", "blog": "Blog",
}

RELATED = [
    ("stock-top-papers", "https://github.com/marcuswang6/stock-top-papers",
     "Top-venue papers on stock prediction and quantitative trading."),
    ("Time-Series-Works-Conferences", "https://github.com/lixus7/Time-Series-Works-Conferences",
     "Time-series papers in CS top conferences."),
    ("awesome-ai-in-finance", "https://github.com/georgezouq/awesome-ai-in-finance",
     "LLMs, deep learning strategies and tools for financial markets."),
    ("Awesome_AI4Finance", "https://github.com/AI4Finance-Foundation/Awesome_AI4Finance",
     "AI4Finance tools, frameworks and papers."),
    ("awesome-quant-ai", "https://github.com/leoncuhk/awesome-quant-ai",
     "AI and machine learning resources for quantitative investment."),
]


def anchor(text):
    """GitHub-style heading anchor."""
    a = text.strip().lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")


def venue_label(p):
    track = TRACK_LABEL.get(p.get("track", "main"), p.get("track", ""))
    return f"{p['venue']} {p['year']}" + (f" {track}" if track else "")


def entry(p):
    links = f"[[Paper]({p['paper']})]"
    if p.get("code"):
        links += f" [[Code]({p['code']})]"
    tags = " ".join(f"`{t}`" for t in p.get("tags", []))
    assets = ", ".join(p.get("assets", []))
    star = " ＊" if p.get("general") else ""
    line = f"- ({venue_label(p)}) **{p['title']}**{star} {links}"
    if tags:
        line += f" {tags}"
    if assets:
        line += f" · *{assets}*"
    return line


def sort_key(p):
    venue_rank = VENUES.index(p["venue"]) if p["venue"] in VENUES else len(VENUES)
    return (-p["year"], venue_rank, p.get("track", "main") != "main", p["title"].lower())


def validate(papers):
    errors = []
    seen = set()
    for i, p in enumerate(papers):
        for field in ("title", "venue", "year", "category", "paper"):
            if not p.get(field):
                errors.append(f"entry {i}: missing '{field}'")
        if p.get("venue") not in VENUES:
            errors.append(f"entry {i}: unknown venue {p.get('venue')!r}")
        if p.get("category") not in CAT_TITLE:
            errors.append(f"entry {i}: unknown category {p.get('category')!r}")
        if p.get("track", "main") not in TRACK_LABEL:
            errors.append(f"entry {i}: unknown track {p.get('track')!r}")
        key = re.sub(r"\W+", "", p.get("title", "").lower())
        if key in seen:
            errors.append(f"entry {i}: duplicate title {p.get('title')!r}")
        seen.add(key)
    return errors


def render(papers, updated):
    papers = sorted(papers, key=sort_key)
    n = len(papers)
    years = sorted({p["year"] for p in papers}, reverse=True)
    by_cat = collections.defaultdict(list)
    for p in papers:
        by_cat[p["category"]].append(p)
    datasets = [p for p in papers if p.get("dataset")]
    with_code = sum(1 for p in papers if p.get("code"))

    out = []
    w = out.append
    w('<div align="center">')
    w("")
    w("# Crypto Top Papers")
    w("")
    w("**Cryptocurrency Work Summary in CS Top Conferences "
      "(NeurIPS, ICML, ICLR, KDD, WWW, AAAI, IJCAI, CIKM, ICDM, ICDE, SIGIR, WSDM, ACL, EMNLP)**")
    w("")
    w(f"![Papers](https://img.shields.io/badge/papers-{n}-blue) "
      f"![Venues](https://img.shields.io/badge/venues-{len(VENUES)}-orange) "
      f"![Updated](https://img.shields.io/badge/updated-{updated.replace('-', '--')}-green) "
      "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)")
    w("")
    w("</div>")
    w("")
    w("# About")
    w("")
    w("A curated list of **peer-reviewed** papers on cryptocurrency, blockchain and Web3 published at CS top "
      f"conferences from {min(years)} to {max(years)}. Every entry has been checked against the official "
      "proceedings, the conference website, or an explicit acceptance note from the authors.")
    w("")
    w("- **One entry, one task.** Each paper is listed once under its main research task. "
      "Methods and chains are shown as tags, so you can search the page for `GNN`, `LLM`, `RL`, *Ethereum* and so on.")
    w("- **＊** marks a general financial ML method that uses cryptocurrency data as one of its main experimental datasets.")
    w("- Track labels: *Short*, *Companion*, *Workshop*, *D&B* (NeurIPS Datasets & Benchmarks), *Findings*. "
      "No label means the main track.")
    w(f"- {with_code} of {n} papers currently link to code. Missing papers or code links? "
      "See [Contributing](#contributing). If this list helps your research, consider leaving a ⭐.")
    w("")
    w("# News")
    w("")
    w(f"- **{updated}**: First release with {n} papers from {len(VENUES)} venues ({min(years)}–{max(years)}).")
    w("")
    w("# Table of Contents")
    w("")
    w("- [About](#about)")
    w("- [News](#news)")
    w("- [Venue Statistics](#venue-statistics)")
    w("- [Papers by Task](#papers-by-task)")
    for k, t, _ in CATEGORIES:
        w(f"  - [{t}](#{anchor(t)}) ({len(by_cat.get(k, []))})")
    w("- [Papers by Year](#papers-by-year)")
    for y in years:
        w(f"  - [{y}](#{y})")
    w(f"- [Datasets & Benchmarks](#datasets--benchmarks) ({len(datasets)})")
    w("- [Related Repositories](#related-repositories)")
    w("- [Contributing](#contributing)")
    w("")
    w("# Venue Statistics")
    w("")
    w("| Venue | " + " | ".join(str(y) for y in sorted(years)) + " | Total |")
    w("|:--|" + ":-:|" * (len(years) + 1))
    counts = collections.Counter((p["venue"], p["year"]) for p in papers)
    for v in VENUES:
        row = [counts.get((v, y), 0) for y in sorted(years)]
        w(f"| {v} | " + " | ".join(str(c) if c else "–" for c in row) + f" | {sum(row)} |")
    col = [sum(counts.get((v, y), 0) for v in VENUES) for y in sorted(years)]
    w("| **Total** | " + " | ".join(f"**{c}**" for c in col) + f" | **{n}** |")
    w("")
    w("# Papers by Task")
    w("")
    w("[Back to top](#table-of-contents)")
    for k, t, desc in CATEGORIES:
        items = by_cat.get(k, [])
        w("")
        w(f"## {t}")
        w("")
        w(f"*{desc}*")
        w("")
        for p in items:
            w(entry(p))
    w("")
    w("# Papers by Year")
    w("")
    w("[Back to top](#table-of-contents)")
    for y in years:
        w("")
        w(f"## {y}")
        w("")
        for p in papers:
            if p["year"] == y:
                w(entry(p) + f" — *{CAT_TITLE[p['category']]}*")
    w("")
    w("# Datasets & Benchmarks")
    w("")
    w("[Back to top](#table-of-contents)")
    w("")
    w("Papers that release a dataset or benchmark (also listed under their task above).")
    w("")
    for p in datasets:
        w(entry(p))
    w("")
    w("# Related Repositories")
    w("")
    for name, url, desc in RELATED:
        w(f"- [{name}]({url}): {desc}")
    w("")
    w("# Contributing")
    w("")
    w("All entries live in [`papers.yaml`](papers.yaml); this README is generated by "
      "[`scripts/build_readme.py`](scripts/build_readme.py). To add a paper, append one entry to "
      "`papers.yaml`, run `python scripts/build_readme.py`, and open a pull request. "
      "See [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion criteria and entry format.")
    w("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if README.md is out of date")
    args = ap.parse_args()
    doc = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    papers = doc["papers"]
    errors = validate(papers)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    updated = str(doc.get("updated") or datetime.date.today())
    text = render(papers, updated)
    if args.check:
        current = README.read_text(encoding="utf-8") if README.exists() else ""
        if current != text:
            print("README.md is out of date: run `python scripts/build_readme.py`.")
            sys.exit(1)
        print("README.md is up to date.")
        return
    README.write_text(text, encoding="utf-8")
    print(f"Wrote README.md with {len(papers)} papers.")


if __name__ == "__main__":
    main()
