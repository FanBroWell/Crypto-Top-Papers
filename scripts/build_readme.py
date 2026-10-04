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
REPO = "https://github.com/FanBroWell/Crypto-Top-Papers"
ISSUE_URL = f"{REPO}/issues/new?template=add-paper.md"

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


def render(papers, updated, updates, upcoming):
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
    w("**Cryptocurrency, blockchain and Web3 papers at CS top conferences**")
    w("")
    w(" · ".join(VENUES))
    w("")
    w(f"![Papers](https://img.shields.io/badge/papers-{n}-blue) "
      f"![With Code](https://img.shields.io/badge/with%20code-{with_code}-blueviolet) "
      f"![Updated](https://img.shields.io/badge/updated-{updated.replace('-', '--')}-green) "
      "[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE) "
      "[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)")
    w("")
    w("</div>")
    w("")
    w("# About")
    w("")
    w(f"A curated list of **peer-reviewed** papers on cryptocurrency, blockchain and Web3 from "
      f"{len(VENUES)} CS top conferences ({min(years)}–{max(years)}), with links to each paper and its code.")
    w("")
    w("- **Continuously updated.** New papers are added as each conference publishes its proceedings "
      "(see [Updates](#updates)).")
    w(f"- **Contributions welcome.** Missing a paper or a code link? [Open an issue]({ISSUE_URL}) or a pull "
      "request (see [How to Contribute](#how-to-contribute)).")
    w("- **Easy to scan.** Each paper is listed once under its main task, with method tags such as `GNN`, `LLM` "
      "and `RL` and chain tags such as *Bitcoin* and *Ethereum*. ＊ marks a general financial method that uses "
      "crypto data as a main dataset.")
    w("")
    w("If this list helps your research, please give it a ⭐.")
    w("")
    w("# Updates")
    w("")
    for u in updates:
        w(f"- **{u['date']}**: {u['text']}")
    if upcoming:
        w(f"- **Coming next**: {upcoming}")
    w("")
    w("# Table of Contents")
    w("")
    w("- [About](#about)")
    w("- [Updates](#updates)")
    w("- [Venue Statistics](#venue-statistics)")
    w("- [Papers by Task](#papers-by-task)")
    for k, t, _ in CATEGORIES:
        w(f"  - [{t}](#{anchor(t)}) ({len(by_cat.get(k, []))})")
    w("- [Papers by Year](#papers-by-year)")
    for y in years:
        w(f"  - [{y}](#{y})")
    w(f"- [Datasets & Benchmarks](#datasets--benchmarks) ({len(datasets)})")
    w("- [How to Contribute](#how-to-contribute)")
    w("- [License](#license)")
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
    w("")
    w("Entry format: `(Venue Year Track) Title [Paper] [Code] method tags · chain`. Track labels are *Short*, "
      "*Companion*, *Workshop*, *D&B* (NeurIPS Datasets & Benchmarks) and *Findings*; no label means the main track.")
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
    w("# How to Contribute")
    w("")
    w("This list is kept up to date with the community's help, and contributions are welcome. "
      "Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.")
    w("")
    w("Quick version:")
    w("")
    w("- **What fits**: a peer-reviewed paper at one of the conferences above whose subject is cryptocurrency, "
      "blockchain or Web3 (or a general financial method that uses crypto data as a main dataset, marked ＊).")
    w("- **Proof of acceptance**: include the official link (DOI, OpenReview, ACL Anthology, PMLR) or the "
      "authors' acceptance note.")
    w(f"- **Easiest way**: [open an issue]({ISSUE_URL}) with the title, venue and links, and we will add it.")
    w("- **Pull request**: add one entry to [`papers.yaml`](papers.yaml) and run "
      "`python scripts/build_readme.py`. One paper per PR; do not edit `README.md` by hand.")
    w("- **Your own paper** is welcome: please say so in the issue or PR.")
    w("")
    w("# License")
    w("")
    w("Released under the [Apache License 2.0](LICENSE).")
    w("")
    w('<div align="center">')
    w("")
    w("If you find this list useful, please consider giving it a star. It helps others discover these papers.")
    w("")
    w("</div>")
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
    text = render(papers, updated, doc.get("updates") or [], doc.get("upcoming"))
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
