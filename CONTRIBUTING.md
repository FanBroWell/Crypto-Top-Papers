# Contributing to Crypto Top Papers

Thanks for taking the time to suggest a paper. This list is **continuously updated**, and it stays complete only with help from the community: new conference proceedings come out all year, and code links appear after publication.

The list is curated rather than exhaustive. The goal is to be a reliable reference for people doing research on cryptocurrency, blockchain and Web3, not a directory of every paper that mentions Bitcoin. A few minutes spent on the criteria below saves time for both of us.

## What we look for

A paper is included when **all three** of the following hold:

- **Covered venue.** It is published at NeurIPS, ICML, ICLR, KDD, WWW (The Web Conference), AAAI, IJCAI, CIKM, ICDM, ICDE, SIGIR, WSDM, ACL or EMNLP. Main-track papers are preferred. Short papers, companion papers, workshop papers, NeurIPS Datasets & Benchmarks papers and ACL/EMNLP Findings are accepted with a track label.
- **Verifiable acceptance.** There is an official link (DOI, OpenReview, ACL Anthology, PMLR, NeurIPS proceedings) or an explicit acceptance note from the authors, such as an arXiv comment saying "Accepted at ...".
- **On topic.** Cryptocurrency, blockchain or Web3 is the subject of the paper. A general financial ML method also fits when cryptocurrency data is one of its **main** experimental datasets; such papers are marked ＊.

Other contributions are just as welcome:

- **Code links** for papers already in the list.
- **Corrections** to a venue, track, link, category or tag.

## What usually doesn't fit

- **Preprints** that have not been accepted at a covered venue. Please come back once the paper is accepted.
- **Generic graph or time-series papers** that use Bitcoin-OTC, Elliptic or similar data only as one benchmark among many.
- **Blockchain as infrastructure** for an unrelated application, such as federated learning, IoT storage or video provenance.
- **Papers from other venues** (for example FC, IEEE ICBC, CCS, IEEE S&P, journals). The list is limited to the 14 conferences above; open an issue if you think a venue should be added.
- **Duplicates.** Please search the README first.

## Submitting your own paper

Authors are welcome to submit their own work. Please **say so in the issue or pull request**. The same criteria apply to everyone.

## How to submit

There are two ways. Pick whichever is easier for you.

**Option 1: open an issue (no setup needed).** Use the [Add a paper](https://github.com/FanBroWell/Crypto-Top-Papers/issues/new?template=add-paper.md) template and fill in the title, venue, year and links. A maintainer will add the entry.

**Option 2: fork and open a pull request.**

1. **Fork** this repository (the **Fork** button at the top right of the GitHub page).
2. **Clone** your fork and create a branch.
3. **Add one entry to [`papers.yaml`](papers.yaml)**, following the format below. The easiest way is to copy an existing entry and edit it.
4. **Regenerate the README** with the script. Do not edit `README.md` by hand: it is generated.
5. **Commit and push** to your fork.
6. **Open a pull request** to the `main` branch of this repository and fill in the template: the paper, the link that proves acceptance, and whether you are an author.

```bash
git clone https://github.com/<your-username>/Crypto-Top-Papers.git
cd Crypto-Top-Papers
git checkout -b add-paper
# edit papers.yaml, then:
pip install pyyaml
python scripts/build_readme.py
git add papers.yaml README.md
git commit -m "Add <paper title> (<venue> <year>)"
git push origin add-paper
```

A few rules keep reviews fast:

- **One paper per pull request**, or a small batch of closely related papers (for example, several papers from the same conference).
- **Use an existing category and existing tags** where possible. Do not create new categories without discussion.
- If you cannot run the script, say so in the pull request and a maintainer will regenerate the README.

## Entry format

```yaml
- title: "CryptoMixer: Fine-grained market information-aware MLP Networks for Individual Cryptocurrency Trading Prediction"
  venue: KDD              # one of the 14 covered conferences
  year: 2025
  track: main             # main | short | companion | workshop | D&B | findings | industry | demo | blog
  category: forecasting   # see the table below
  tags: [MLP, Time-Series]        # methods
  assets: [Crypto]                # chain or asset class
  paper: https://doi.org/10.1145/3711896.3736900   # official link preferred
  code: https://github.com/aqua111000/CryptoMixer  # optional
  # dataset: true         # optional: add if the paper releases a dataset or benchmark
  # general: true         # optional: add for ＊ papers (general method, crypto data as a main dataset)
```

**Categories.** Each paper goes under the one task it mainly addresses.

| `category` | Section in the README |
|:--|:--|
| `forecasting` | Price Forecasting & Market Analysis |
| `trading` | Trading & Portfolio Management |
| `fraud` | Fraud, Scam & Attack Detection |
| `onchain` | On-chain Transaction & Graph Analytics |
| `defi` | DeFi, MEV & Market Mechanisms |
| `web3` | NFT, DAO & Web3 Ecosystem |
| `smart-contract` | Smart Contract Security & Analysis |
| `systems` | Blockchain Systems & Infrastructure |
| `survey` | Surveys, Tutorials & Workshops |

**Tags.** Reuse existing tags so readers can search the page. Common method tags are `GNN`, `Temporal-Graph`, `Hypergraph`, `Transformer`, `LLM`, `Agent`, `RL`, `Time-Series`, `Generative`, `Diffusion`, `Pre-training`, `Game-Theory`, `Measurement`, `Program-Analysis`, `Sharding` and `Consensus`. Asset tags name the chain or asset class, such as `Bitcoin`, `Ethereum`, `Solana`, `DEX`, `NFT`, `DAO` or `Crypto` (several cryptocurrencies). Leave `assets` out when the paper does not name a chain.

## What to expect

Every submission gets a reply. Before merging, a maintainer checks the acceptance link and may adjust the category, tags or track label to keep the list consistent. A decline is not permanent: if a preprint is later accepted at a covered venue, please submit it again.

## Scope reminder

This list covers **cryptocurrency, blockchain and Web3 research at 14 CS top conferences**: market forecasting and trading, fraud and attack detection, on-chain analytics, DeFi and MEV, NFTs and DAOs, smart contracts, and blockchain systems. Tools, trading bots, data APIs and blog posts belong in other lists.

Thanks again. Every correct addition makes the list more useful for the next reader.
