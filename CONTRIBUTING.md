# Contributing

Thanks for helping keep this list complete and accurate.

## What fits this list

A paper is included when **all** of the following hold:

1. **Venue.** It is published at one of the covered conferences: NeurIPS, ICML, ICLR, KDD, WWW (The Web Conference), AAAI, IJCAI, CIKM, ICDM, ICDE, SIGIR, WSDM, ACL or EMNLP. Main-track papers are preferred; short papers, companion papers, workshop papers, NeurIPS Datasets & Benchmarks papers and ACL/EMNLP Findings are accepted with a track label.
2. **Acceptance is verifiable.** Provide the official proceedings link (DOI, OpenReview, ACL Anthology, PMLR, NeurIPS proceedings) or an explicit acceptance note from the authors (for example an arXiv comment such as "Accepted at ...").
3. **Topic.** Cryptocurrency, blockchain or Web3 is the subject of the paper, or (marked ＊) a general financial ML method uses cryptocurrency data as one of its **main** experimental datasets.

Not included:

- General graph or time-series papers that use Bitcoin-OTC, Elliptic or similar data only as one benchmark among many.
- Papers that use a blockchain only as infrastructure for an unrelated application (federated learning, IoT storage, video provenance, and so on).
- Preprints that have not been accepted at a covered venue.

## How to add a paper

1. Append one entry to [`papers.yaml`](papers.yaml):

   ```yaml
   - title: "CryptoMixer: Fine-grained market information-aware MLP Networks for Individual Cryptocurrency Trading Prediction"
     venue: KDD            # one of the covered venues
     year: 2025
     track: main           # main | short | companion | workshop | D&B | findings | industry | demo | blog
     category: forecasting # see the category list below
     tags: [MLP, Time-Series]
     assets: [Crypto]
     paper: https://doi.org/10.1145/...
     code: https://github.com/...   # optional
     dataset: false        # true if the paper releases a dataset or benchmark
     general: false        # true for ＊ papers
   ```

2. Regenerate the README: `pip install pyyaml && python scripts/build_readme.py`.
3. Open a pull request with one paper (or one closely related batch) per PR, and fill in the template.

## Categories

Each paper goes under the one task it mainly addresses:

| `category` | Section |
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

## Tags

Use existing tags where possible so readers can search the page. Common method tags: `GNN`, `Temporal-Graph`, `Hypergraph`, `Transformer`, `LLM`, `Agent`, `RL`, `Time-Series`, `Generative`, `Diffusion`, `Pre-training`, `Game-Theory`, `Measurement`, `Program-Analysis`, `Sharding`, `Consensus`. Asset tags name the chain or asset class, for example `Bitcoin`, `Ethereum`, `Solana`, `DEX`, `NFT`, `DAO`, `Crypto` (multiple cryptocurrencies).
